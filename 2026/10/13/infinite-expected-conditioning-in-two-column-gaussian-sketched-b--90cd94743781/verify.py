"""Independent arithmetic checks for the two-column Gaussian-sketch biorthogonalization formulas.
Run with Python 3 and the standard library only: python verify.py
Analytic integrability and probability positivity remain proof obligations, not simulation claims.
"""
from fractions import Fraction as F
from itertools import product
from math import gamma, exp, sqrt, pi, isclose
import random

def dot(x,y): return sum((u*v for u,v in zip(x,y)),F(0))
def sub(x,y,t): return tuple(u-t*v for u,v in zip(x,y))
def fzero(s,c):
    return s*gamma(s-1)/(2**(s-1)*gamma(s/2)**2)*(1-c*c)**((s-2)/2)
def gammapdf(t,k,theta):
    return (t**(k-1))*exp(-t/theta)/(gamma(k)*theta**k)
def integral_fzero(s,c,N=12000):
    k=s/2; a=(1+c)/s; b=(1-c)/s
    upper=36.
    def f(t): return gammapdf(t,k,a)*gammapdf(t,k,b)
    h=upper/N
    return h/3*(f(0)+f(upper)+4*sum(f((2*j-1)*h) for j in range(1,N//2+1))+2*sum(f(2*j*h) for j in range(1,N//2)))

for s in (2,3,4,6,8):
    for c in (-.8,-.25,0.,.37,.9):
        exact=fzero(s,c); numeric=integral_fzero(s,c)
        assert isclose(exact,numeric,rel_tol=.004,abs_tol=.002),(s,c,exact,numeric)
    if s==2:
        for c in (-.99,-.5,0.,.5,.99): assert isclose(fzero(s,c),1.,abs_tol=1e-13)

rng=random.Random(342026)
checks=0
for s in (2,3,5,9):
    for _ in range(250):
        aa=tuple(F(rng.randint(-7,7),rng.randint(1,6)) for i in range(s))
        bb=tuple(F(rng.randint(-7,7),rng.randint(1,6)) for i in range(s))
        cc=tuple(F(rng.randint(-7,7),rng.randint(1,6)) for i in range(s))
        z=dot(aa,bb)
        if z==0: continue
        h=dot(bb,cc); k=dot(aa,cc); v=dot(cc,cc)
        q=sub(cc,aa,h/z)
        p=sub(cc,bb,k/z)
        d=dot(q,p)
        assert d==v-h*k/z
        if d==0: continue
        assert dot(q,bb)==0 and dot(p,aa)==0
        # Columns of the original-space Q have an exact triangular-coordinate description:
        # q1=e1/sqrt(|z|), q2=(e3-h*e1/z)/sqrt(|d|).
        # Squared column norms, squared determinant, and squared condition lower bound.
        trace=1/abs(z)+(h/z)**2/abs(d)+1/abs(d)
        detgram=1/(abs(z)*abs(d))
        tr=float(trace); de=float(detgram)
        discriminant=max(0.,tr*tr-4*de)
        maxeig=(tr+sqrt(discriminant))/2
        kappasq=maxeig*maxeig/de
        assert kappasq+1e-8 >= float(abs(d)/abs(z)),(s,kappasq,float(abs(d)/abs(z)))
        checks+=1
for j in range(2,50):
    z=F(1,2**j)
    a=(F(1),F(0)); b=(z,F(1)); c=(F(1),F(1))
    d=dot(c,c)-dot(a,c)*dot(b,c)/dot(a,b)
    assert d==(z-1)/z
    assert abs(d)/abs(z) >= 2**(2*j-1)
print('VERIFY_OK:',checks,'exact Schur-complement and triangular-Gram tests;',25,'density quadratures; 48 near-breakdown witnesses')
