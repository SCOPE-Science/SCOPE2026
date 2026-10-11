"""Exact-arithmetic checks for a sharp harmonic-convolution local-univalence radius.
Run: python3 check_radius.py. Python standard library only.
"""
from fractions import Fraction as F
from math import comb

# A polynomial is its ascending list of coefficients.
def add(p,q):
    n=max(len(p),len(q)); return [(p[k] if k<len(p) else 0)+(q[k] if k<len(q) else 0) for k in range(n)]
def neg(p):return [-t for t in p]
def sub(p,q):return add(p,neg(q))
def mul(p,q):
    o=[0]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):o[i+j]+=a*b
    return o
def scale(p,c):return [c*x for x in p]
def ev(p,x):
    y=0
    for c in p[::-1]: y=y*x+c
    return y
def eq(p,q):
    n=max(len(p),len(q));return all((p[i] if i<len(p) else 0)==(q[i] if i<len(q) else 0) for i in range(n))
def pow2(p):return mul(p,p)

# Original normalized ellipse mapping's two geometric coefficient tails.
a=F(-10,11);b=F(1,44)
A=F(-9890884608,9139543205)
B=F(-251761689,562995861428)
C=F(41190732,12795360487)
D=F(1373955264,9139543205)
rates=[a*a,a*b,b*b]
Q=[pow2([1,-u]) for u in rates]
Den=mul(mul(Q[0],Q[1]),Q[2])
terms=[]
for j,u in enumerate(rates):
    other=[1]
    for k in range(3):
        if k!=j:other=mul(other,Q[k])
    terms.append(mul([0,2,-u],other))
pnum=add(Den,add(add(scale(terms[0],A*A),scale(terms[1],2*A*B)),scale(terms[2],B*B)))
qnum=add(add(scale(terms[0],D*D),scale(terms[1],2*D*C)),scale(terms[2],C*C))

# Independently reproduce the rational simplification of p' +/- q'.
P4=[-360263217096475,-231722242336904,96137381658603,-94137557624,24297200]
P6=[-701902078885331749352905757780,-546666175276725488438747500196,
196525575821143049386765307327,6563513204097494574954697684,
64433804996566834468116815,-76570023016489888285400,20269382049144670000]
K=F(3748096,24606462475)
L=F(3748096,818606249961404385845)
polyminus=mul(pow2([-1936,1]),pow2([-121,100]))
polyplus=mul(polyminus,pow2([242,5]))
assert eq(mul(sub(pnum,qnum),polyminus),scale(mul(P4,Den),-K)), 'incorrect minus rational identity'
assert eq(mul(add(pnum,qnum),polyplus),scale(mul(P6,Den),-L)), 'incorrect plus rational identity'

# The first Jacobian zero on the negative real axis: bracket and uniqueness.
lo=F(961916078016035,10**15)
hi=F(961916078016036,10**15)
assert 0<lo<hi<1
assert ev(P6,-lo)<0<ev(P6,-hi)
# Derivative of P6(-r) is positive for all 0<=r<=1:
# discard its other nonnegative terms and bound its one negative term.
assert -P6[1]-3*P6[3]>0
assert ev(P6,0)<0<ev(P6,-1)

# Certify P4 has no zero in |z|<=1 by Cayley and Hurwitz quartic.
# w=(1+z)/(1-z), i.e., z=(w-1)/(w+1). Outside disk --> Re(w)<0.
# Q(w)=-(w+1)^4 P4((w-1)/(w+1)) has coefficients q[0:5].
def shifted_cayley(p,n):
    one=[1,1]; other=[-1,1]; out=[0]
    for k,c in enumerate(p):
        term=[1]
        for _ in range(k):term=mul(term,other)
        for _ in range(n-k):term=mul(term,one)
        out=add(out,scale(term,-c))
    return out
h=shifted_cayley(P4,4)
assert h==[32309431246144,977796756016140,2353853920112856,1904309175133260,495942191035200]
assert all(c>0 for c in h)
assert h[3]*h[2]>h[4]*h[1]
assert h[3]*h[2]*h[1]>h[4]*h[1]**2+h[3]**2*h[0]
# Routh-Hurwitz: Q has all roots strictly in Re(w)<0, so P4 zero-free on closed unit disk.

# The following trigonometric certificate proves Re[(p'+q')/(p'-q')]>0
# on the circle |z|=r* except the negative real contact point.
W=mul(P4,pow2([242,5]))
U=P6
assert len(U)==len(W)==7

def poly_r_add(p,q):
    d=dict(p)
    for k,v in q.items():d[k]=d.get(k,0)+v
    return {k:v for k,v in d.items() if v!=0}
def poly_r_scale(p,c):return {k:c*v for k,v in p.items() if c*v!=0}
def poly_r_eval(p,x):return sum(c*x**k for k,c in p.items())
def cheb(n):
    if n==0:return [1]
    if n==1:return [0,1]
    p=[1];q=[0,1]
    for j in range(2,n+1):
        r=sub(scale([0]+q,2),p);p,q=q,r
    return q

# T(r,x)=Re(P6(r exp(it))*conj(W(r exp(it)))), x=cos(t).
# T(r,x)=sum_{i=0}^6 t_i(r) x^i.
tcoeff=[{} for _ in range(7)]
for k in range(7):
    tcoeff[0]=poly_r_add(tcoeff[0],{2*k:U[k]*W[k]})
for j in range(1,7):
    cj=cheb(j)
    for k in range(7-j):
        val=U[k+j]*W[k]+U[k]*W[k+j]
        for i,ck in enumerate(cj):
            if ck:tcoeff[i]=poly_r_add(tcoeff[i],{2*k+j:val*ck})

# H(r,x)=(T(r,x)-T(r,-1))/(x+1), polynomial degree 5 in x.
hcoeff=[{} for _ in range(6)]
for i in range(1,7):
    for k in range(i):
        hcoeff[k]=poly_r_add(hcoeff[k],poly_r_scale(tcoeff[i],(-1)**(i-1-k)))

# Put x=2t-1 with t in [0,1]; convert degree-5 power basis to Bernstein basis.
gcoeff=[{} for _ in range(6)]
for k in range(6):
    for j in range(k+1):
        gcoeff[j]=poly_r_add(gcoeff[j],poly_r_scale(hcoeff[k],comb(k,j)*2**j*(-1)**(k-j)))
bern=[]
for j in range(6):
    bj={}
    for k in range(j+1):
        bj=poly_r_add(bj,poly_r_scale(gcoeff[k],F(comb(j,k),comb(5,k))))
    bern.append(bj)

# For r in [lo,hi], |r^k-lo^k| <= k*(hi-lo), since hi<1.
# This gives rigorous uniform strict positivity of all six Bernstein coefficients.
margin=[]
for j,bj in enumerate(bern):
    derivative_l1=sum(k*abs(v) for k,v in bj.items())
    safe=poly_r_eval(bj,lo)-(hi-lo)*derivative_l1
    assert safe>0, ('Bernstein coefficient',j)
    margin.append(float(safe/F(10**49)))

# At r*, the T polynomial has T(r*,-1)=P6(-r*)W(-r*)=0.
# Positive Bernstein coefficients yield H(r*,x)>0 on [-1,1].
# Thus T(r*,x)=(x+1)H(r*,x)>=0, equality iff x=-1.
# The analytic quotient (p'+q')/(p'-q') has nonnegative boundary real
# part, positive except at z=-r*. Harmonic minimum principle gives strict
# positive real part inside |z|<r*. Jacobian is positive there.
# At z=-r*, p'+q'=0, p'-q' !=0 so Jacobian is zero; Lewy's theorem
# excludes local univalence on every strictly larger centered disk.
print('PASS: all polynomial identities, root bounds, Hurwitz test, and six Bernstein certificates')
print('root bracket:',float(lo),float(hi))
print('positive lower Bernstein margins / 10^49:',margin)
