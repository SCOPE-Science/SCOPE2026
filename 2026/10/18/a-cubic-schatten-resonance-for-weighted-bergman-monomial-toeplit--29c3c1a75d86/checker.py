"""Reproducibility checks for the monomial weighted-Bergman Toeplitz commutator spectrum.
Requires Python 3 and sympy; optional numpy for matrix cross-checks.
Checks are finite exact algebra or finite numerical comparisons, not a replacement for the asymptotic proof.
"""
from fractions import Fraction
from math import sqrt
import random
import sympy as sp

# Define A=alpha+1>0.  R_j(n)=mu_{n+j}/mu_n for integer j and n+j>=0.
def R(n,j,A):
    assert n>=0 and n+j>=0 and A>0
    if j<0: return 1/R(n+j,-j,A)
    out=Fraction(1)
    for t in range(1,j+1): out *= Fraction(n+t,1)/(n+t+A)
    return out

def D(p,q,r,s,n,A):
    k=p-q; ell=r-s; m=k+ell
    assert n>=max(0,-k,-ell,-m, -(ell+p), -(k+r))
    return R(n,r,A)*R(n+ell,p,A)-R(n,p,A)*R(n+k,r,A)

def B(p,q,r,s):
    return -p*p*s+p*q*s-p*s+q*r*r-q*r*s+q*r

rng=random.Random(24017)
count=0
for A in [Fraction(1,2),Fraction(1),Fraction(2),Fraction(10,3)]:
    for _ in range(220):
        p,q,r,s=(rng.randrange(0,8) for _ in range(4))
        if (p==q==0) or (r==s==0): continue
        k=p-q;ell=r-s;m=k+ell
        n=max(1, -k,-ell,-m)+rng.randrange(0,40)
        lhs=D(p,q,r,s,n,A)
        # Compare with direct two products of Bergman matrix weights; squared roots cancel here.
        one=R(n,r,A)*R(n+ell,p,A)
        two=R(n,p,A)*R(n+k,r,A)
        assert lhs==one-two
        det=q*r-p*s
        if det==0 and B(p,q,r,s)==0: assert lhs==0
        count+=1

# Fully symbolic expansion of all three terms in 1/n for arbitrary monomial exponents.
A,p,q,r,s=sp.symbols('A p q r s',real=True)
k=p-q;ell=r-s
f1=-A*p;g1=-A*r
f2=A*(A+1)*p*(p+1)/2;g2=A*(A+1)*r*(r+1)/2
D2=sp.expand(-ell*f1+k*g1)
D3=sp.expand(-2*ell*f2+ell**2*f1-ell*f1*g1+2*k*g2-k**2*g1+k*f1*g1)
assert sp.simplify(D2-A*(q*r-p*s))==0
u,v,a,b=sp.symbols('u v a b',integer=True)
resD3=sp.factor(D3.subs({p:u*a,q:u*b,r:v*a,s:v*b}))
assert sp.simplify(resD3+A*a*b*u*v*(a-b)*(u-v))==0
count+=3

# Exact n^2 and n^3 scaled coefficients, with conservative large-n tolerances.
from decimal import Decimal, localcontext
for par in [(2,1,4,2),(4,2,2,1),(3,1,2,1),(1,0,0,1),(3,2,5,1)]:
    p0,q0,r0,s0=par
    exponent=3 if q0*r0==p0*s0 else 2
    expect=B(*par) if exponent==3 else q0*r0-p0*s0
    for A0 in [Fraction(1,2), Fraction(1), Fraction(2),Fraction(10,3)]:
        n=200000
        m=(p0-q0)+(r0-s0)
        val=D(*par,n,A0)
        with localcontext() as ctx:
            ctx.prec=70
            scaled=((Decimal(val.numerator)/Decimal(val.denominator))*Decimal(n)**exponent /
                    (Decimal(R(n,m,A0).numerator)/Decimal(R(n,m,A0).denominator)).sqrt())
            target=Decimal(A0.numerator)*Decimal(expect)/Decimal(A0.denominator)
            assert abs(scaled-target)<Decimal('0.01'), (par,A0,scaled,target)
        count+=1
# Independent matrix entries computed from weighted monomial moments.
import numpy as np
from math import lgamma, exp
L=40
for alpha in [-0.5,0.0,1.0,2.5]:
    mu=np.array([exp(lgamma(i+1)+lgamma(alpha+2)-lgamma(i+alpha+2)) for i in range(L+20)])
    for par in [(1,0,0,1),(2,1,4,2),(3,1,2,1),(0,3,2,0),(4,2,2,1)]:
        P,Q,Rr,Ss=par
        def Tmatrix(p,q):
            out=np.zeros((L,L))
            for n in range(L):
                target=n+p-q
                if 0<=target<L:
                    out[target,n]=mu[n+p]/sqrt(mu[n]*mu[target])
            return out
        X=Tmatrix(P,Q);Y=Tmatrix(Rr,Ss)
        K=X@Y-Y@X
        k=P-Q;ell=Rr-Ss;m=k+ell
        for n in range(max(0,-k,-ell,-m)+1,20):
            actual=K[n+m,n]
            A0=Fraction(str(alpha+1))
            exact=D(P,Q,Rr,Ss,n,A0)
            R0=R(n,m,A0)
            expected=float(exact)/sqrt(float(R0))
            assert abs(actual-expected)<4e-12,(alpha,par,n,actual,expected)
            count+=1
print('PASS:',count,'exact symbolic/rational, large-n and independent finite-matrix checks.')
