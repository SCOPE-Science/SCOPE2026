#!/usr/bin/env python3
from fractions import Fraction as F
from decimal import Decimal, getcontext

# Polynomial coefficients are low-to-high throughout this checker.
def trim(p):
    p=list(p)
    while len(p)>1 and p[-1]==0:
        p.pop()
    return p

def pder(p):
    return trim([F(i)*p[i] for i in range(1,len(p))] or [F(0)])

def pdivmod(p,q):
    p=trim(p); q=trim(q)
    if q==[0]: raise ZeroDivisionError
    r=p[:]
    if len(r)<len(q): return [F(0)],r
    out=[F(0)]*(len(r)-len(q)+1)
    while len(r)>=len(q) and r!=[0]:
        k=len(r)-len(q); c=r[-1]/q[-1]
        out[k]=c
        for j,v in enumerate(q): r[j+k]-=c*v
        r=trim(r)
    return trim(out),trim(r)

def psturm(p):
    s=[trim(p),pder(p)]
    while s[-1] != [0]:
        _,r=pdivmod(s[-2],s[-1])
        if r==[0]: break
        s.append(trim([-x for x in r]))
    return s

def peval(p,x):
    y=F(0)
    for c in reversed(p): y=y*x+c
    return y

def sgn(x): return 1 if x>0 else (-1 if x<0 else 0)

def variations(vals):
    ss=[sgn(v) for v in vals if v!=0]
    return sum(ss[i]!=ss[i-1] for i in range(1,len(ss)))

def var_at(sturm,x): return variations([peval(p,x) for p in sturm])

def var_inf(sturm,positive=True):
    vals=[]
    for p in sturm:
        lead=p[-1]
        if positive:
            vals.append(lead)
        else:
            vals.append(lead*((-1)**(len(p)-1)))
    return variations(vals)

def roots_between(p,left,right):
    s=psturm(p)
    return var_at(s,left)-var_at(s,right)

def pos_neg_counts(p):
    s=psturm(p)
    v0=var_at(s,F(0))
    pos=v0-var_inf(s,True)
    neg=var_inf(s,False)-v0
    return pos,neg

def det_frac(M):
    A=[row[:] for row in M]; n=len(A); d=F(1)
    for i in range(n):
        pivot=next((r for r in range(i,n) if A[r][i]),None)
        if pivot is None: return F(0)
        if pivot!=i:
            A[i],A[pivot]=A[pivot],A[i]; d=-d
        pv=A[i][i]; d*=pv
        for r in range(i+1,n):
            if A[r][i]==0: continue
            f=A[r][i]/pv
            for c in range(i,n): A[r][c]-=f*A[i][c]
    return d

def resultant_high(f,g):
    # Sylvester determinant for coefficients supplied high-to-low.
    m=len(f)-1; n=len(g)-1; N=m+n
    M=[]
    for i in range(n):
        row=[F(0)]*N
        for j,c in enumerate(f): row[i+j]=c
        M.append(row)
    for i in range(m):
        row=[F(0)]*N
        for j,c in enumerate(g): row[i+j]=c
        M.append(row)
    return det_frac(M)

def qpoly(av):
    av=F(av)
    # lambda^4 + lambda^3 + (3-a/10)lambda^2 + (a+21/10)lambda - a/10
    return [ -av/F(10), av+F(21,10), F(3)-av/F(10), F(1), F(1) ]

def discriminant_q(av):
    low=qpoly(av)
    high=list(reversed(low))
    der_high=[F(4)*high[0],F(3)*high[1],F(2)*high[2],high[3]]
    # degree four: (-1)^(4*3/2)=+1 and leading coefficient=1
    return resultant_high(high,der_high)

def Pval(x):
    x=F(x)
    return (F(192)*x**5-F(1380360)*x**4-F(11138818)*x**3
            -F(29595555)*x**2-F(44649090)*x-F(24931935))

# The printed characteristic polynomial at an outer equilibrium after setting
# y11=1 and y12=1/10 and replacing the inner slope b by the outer slope a.
for av in [F(-10),F(-8),F(-6),F(-4),F(-2),F(-1),F(0)]:
    assert discriminant_q(av)==Pval(av)/F(50000)

P=[F(-24931935),F(-44649090),F(-29595555),F(-11138818),F(-1380360),F(192)]
Ps=psturm(P)
assert roots_between(P,F(-10),F(-1))==2
alpha_L,alpha_R=F(-487197,100000),F(-487196,100000)
beta_L,beta_R=F(-100903,100000),F(-100902,100000)
assert roots_between(P,alpha_L,alpha_R)==1
assert roots_between(P,beta_L,beta_R)==1
# Both roots are simple.
def pgcd(p,q):
    p,q=trim(p),trim(q)
    while q!=[0]:
        _,r=pdivmod(p,q); p,q=q,r
    if p[-1]!=1: p=[x/p[-1] for x in p]
    return trim(p)
assert pgcd(P,pder(P))==[F(1)]

# Routh-Hurwitz quantities for q_a.
def D2(av): return (F(9)-F(11)*av)/F(10)
def D3(av): return -(F(110)*av*av+F(131)*av-F(189))/F(100)
def A4(av): return -F(av)/F(10)
def sign_changes(seq): return variations(seq)
def routh_unstable(av):
    av=F(av)
    return sign_changes([F(1),F(1),D2(av),D3(av)/D2(av),A4(av)])

# The only negative Routh crossing in [-10,-1] is the negative root of
# 110 a^2 + 131 a - 189 = 0.
H=[F(-189),F(131),F(110)]
aH_L,aH_R=F(-2036,1000),F(-2035,1000)
assert roots_between(H,aH_L,aH_R)==1
assert roots_between(H,F(-10),F(-1))==1
assert D2(F(-10))>0 and D2(F(-1))>0 and A4(F(-10))>0 and A4(F(-1))>0

# Representative exact Sturm/Routh classifications on the four open regions.
expected={
    F(-10):(2,0,2), # positive real, negative real, unstable dimension
    F(-4):(0,0,2),
    F(-2):(0,0,0),
    F(-1):(0,2,0),
}
for av,(ep,en,eu) in expected.items():
    pp,pn=pos_neg_counts(qpoly(av))
    assert (pp,pn,routh_unstable(av))==(ep,en,eu)

# Exact Hopf frequency: omega^2=A3=a_H+21/10.
# a_H=(-131-sqrt(100321))/220, so omega^2=(331-sqrt(100321))/220>0.
assert 331*331>100321

# Produce rigorous decimal enclosures by exact bisection for the two P roots.
def bisect_root(fun,L,R,iters=100):
    L=F(L); R=F(R); fL=fun(L); fR=fun(R)
    assert fL*fR<0
    for _ in range(iters):
        M=(L+R)/2; fM=fun(M)
        if fM==0: return M,M
        if fL*fM<0: R=M; fR=fM
        else: L=M; fL=fM
    return L,R
getcontext().prec=40
def dec(fr): return Decimal(fr.numerator)/Decimal(fr.denominator)
aL,aR=bisect_root(Pval,alpha_L,alpha_R)
bL,bR=bisect_root(Pval,beta_L,beta_R)
sq=Decimal(100321).sqrt()
aHdec=(-Decimal(131)-sq)/Decimal(220)
omega2=(Decimal(331)-sq)/Decimal(220)
print('alpha_interval=',dec(aL),dec(aR))
print('a_H=',aHdec)
print('beta_interval=',dec(bL),dec(bR))
print('omega_H=',omega2.sqrt())
print('sample_classification=',{str(k):v for k,v in expected.items()})
print('VERIFY_OK')
