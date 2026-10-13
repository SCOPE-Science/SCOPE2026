#!/usr/bin/env python3
from fractions import Fraction as F

# Polynomials are coefficient lists in ascending powers.
def trim(p):
    p=list(p)
    while len(p)>1 and p[-1]==0: p.pop()
    return p

def add(a,b):
    n=max(len(a),len(b)); c=[F(0)]*n
    for i in range(n): c[i]=(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
    return trim(c)

def sub(a,b): return add(a,[-x for x in b])
def mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return trim(c)
def deriv(a): return trim([F(i)*a[i] for i in range(1,len(a))] or [F(0)])
def divrem(a,b):
    a=trim(a); b=trim(b)
    if b==[0]: raise ZeroDivisionError
    q=[F(0)]*max(1,len(a)-len(b)+1)
    while len(a)>=len(b) and a!=[0]:
        k=len(a)-len(b); c=a[-1]/b[-1]; q[k]+=c
        a=sub(a,[F(0)]*k+[c*y for y in b])
    return trim(q),trim(a)
def sturm(p):
    s=[trim(p),deriv(p)]
    while s[-1]!=[0]:
        _,r=divrem(s[-2],s[-1])
        if r==[0]: break
        s.append([-x for x in r])
    return s
def evalp(p,x):
    y=F(0)
    for c in reversed(p): y=y*x+c
    return y
def sgn(x): return (x>0)-(x<0)
def variations(signs):
    a=[z for z in signs if z]
    return sum(a[i]!=a[i-1] for i in range(1,len(a)))
def root_count_interval(p,a,b):
    S=sturm(p)
    va=variations([sgn(evalp(q,a)) for q in S])
    vb=variations([sgn(evalp(q,b)) for q in S])
    return va-vb
def positive_root_count(p):
    S=sturm(p)
    v0=variations([sgn(q[0]) for q in S])
    vi=variations([sgn(q[-1]) for q in S])
    return v0-vi

def zeta(t):
    # x^0,...,x^6
    return [F(8), -(12*t-8), 6*t*t-4*t+8,
            -(t**3+2*t*t+4*t), t**3+6*t-2,
            -(3*t*t-3*t+2), 2*t-1]
def eta_num(t): return [F(2),-t,t,F(-1)]

def det_bareiss(A):
    A=[list(map(F,row)) for row in A]; n=len(A); sign=1; prev=F(1)
    for k in range(n-1):
        if A[k][k]==0:
            j=next(j for j in range(k+1,n) if A[j][k]!=0)
            A[k],A[j]=A[j],A[k]; sign=-sign
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                A[i][j]=(A[i][j]*pivot-A[i][k]*A[k][j])/prev
        prev=pivot
        for i in range(k+1,n): A[i][k]=F(0)
        for j in range(k+1,n): A[k][j]=A[k][j]
    return F(sign)*A[-1][-1]

def resultant(f,g):
    f=trim(f); g=trim(g); m=len(f)-1; n=len(g)-1
    # descending coefficients for Sylvester matrix
    fd=list(reversed(f)); gd=list(reversed(g)); N=m+n
    M=[]
    for i in range(n): M.append([F(0)]*i+fd+[F(0)]*(N-i-len(fd)))
    for i in range(m): M.append([F(0)]*i+gd+[F(0)]*(N-i-len(gd)))
    return det_bareiss(M)

def discrim(f):
    n=len(f)-1
    return F((-1)**(n*(n-1)//2))*resultant(f,deriv(f))/f[-1]

def qcrit(t): return t*t-9*t+19

def R(w): return w**5-47*w**4+697*w**3-4384*w**2+10816*w-9728

def p10(t): return R((t-2)**2)

def rhs_disc(t): return 4096*qcrit(t)*(t*t+t-1)*p10(t)

# Exact discriminant identity: both sides have degree <=33 in t; 34 exact samples suffice.
for n in range(-10,24):
    tt=F(n)
    assert discrim(zeta(tt)) == rhs_disc(tt)

# Exact resultant identity with the positivity numerator: degree <=27; 34 samples suffice.
for n in range(-10,24):
    tt=F(n)
    assert resultant(zeta(tt),eta_num(tt)) == 64

# Exact polynomial identities at x=1.
for n in range(-5,8):
    tt=F(n); z=zeta(tt); dz=deriv(z)
    assert evalp(z,F(1)) == qcrit(tt)
    assert evalp(dz,F(1)) == tt*qcrit(tt)

# R has exactly one positive root by Sturm, and the bracket isolates tau_*.
Rpoly=[F(-9728),F(10816),F(-4384),F(697),F(-47),F(1)]
assert positive_root_count(Rpoly)==1
lo=F(711925832,10**8); hi=F(711925833,10**8)
assert p10(lo)<0<p10(hi)

# Positive-root counts in the four open parameter cells.
expected={F(3):0,F(4):2,F(6):4,F(8):6}
for tt,c in expected.items(): assert positive_root_count(zeta(tt))==c

# At tau=8 isolate all six roots and independently verify eta>0 there.
intervals=[
 (F(2585,10000),F(2586,10000)),
 (F(3595,10000),F(3596,10000)),
 (F(3946,10000),F(3947,10000)),
 (F(7591,10000),F(7592,10000)),
 (F(28565,10000),F(28566,10000)),
 (F(67049,10000),F(67050,10000)),
]
for a,b in intervals:
    assert root_count_interval(zeta(F(8)),a,b)==1
    # eta numerator has no zero in the root isolating interval and is positive at its midpoint.
    assert root_count_interval(eta_num(F(8)),a,b)==0
    assert evalp(eta_num(F(8)),(a+b)/2)>0

print('VERIFY_OK discriminant_samples=34 resultant_samples=34 sturm_cells=0,2,4,6 tau_star_bracket=[7.11925832,7.11925833] tau8_eta=positive')
