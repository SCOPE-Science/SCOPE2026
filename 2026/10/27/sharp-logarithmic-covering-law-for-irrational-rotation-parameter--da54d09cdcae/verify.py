"""Exact-rational consistency checks for two-branch rotation-parameter staircases.

This verifies finite algebraic identities and sample rational plateaux;
finite checks do not prove the universal covering theorem.
"""
from fractions import Fraction as F
from math import gcd, floor, isqrt
import sympy as sp


def phi(s, lam, mu, b, c):
    return (1-lam)*(b+(mu*b-c)*s)/(1+(mu-1)*s)


def sigma_partial(lam, mu, p, q, N):
    return sum((F((k+1)*p,q).__floor__()-F(k*p,q).__floor__()) * lam**k * mu**(k*p//q) for k in range(1,N+1))


def sigma_rational(lam, mu, p, q):
    numerator = sigma_partial(lam, mu, p, q, q)
    return numerator/(1-lam**q*mu**p)


def jump(lam, mu, p, q):
    return (1-lam)*lam**(q-1)*mu**(p-1)/(1-lam**q*mu**p)

checks=0
S,L,M,B,C=sp.symbols('s l m b c')
expr=(1-L)*(B+(M*B-C)*S)/(1+(M-1)*S)
assert sp.simplify(sp.diff(expr,S)-(1-L)*(B-C)/(1+(M-1)*S)**2)==0
checks+=1
for lam,mu,b,c in [(F(1,2),F(3),F(1),F(0)),(F(2,3),F(1,2),F(3,4),F(1,4)),(F(2,3),F(1),F(1),F(0)),(F(1,3),F(2),F(1),F(0))]:
    for q in range(2,33):
        for p in range(1,q):
            if gcd(p,q)!=1 or lam**q*mu**p>=1: continue
            s=sigma_rational(lam,mu,p,q)
            jm=jump(lam,mu,p,q)
            lo,hi=phi(s-jm,lam,mu,b,c),phi(s,lam,mu,b,c)
            assert 0<jm and lo<hi
            checks+=2
            # Independent factorization of the Moebius-fraction plateau width.
            target=(1-lam)*(b-c)*jm/((1+(mu-1)*(s-jm))*(1+(mu-1)*s))
            assert hi-lo==target
            checks+=1
            # Truncation at period multiples agrees with exact geometric tails.
            for periods in (1,2,3):
                approx=sigma_partial(lam,mu,p,q,periods*q)
                expected=s*(1-(lam**q*mu**p)**periods)
                assert approx==expected
                checks+=1
    
# Verify the rational plateau for the genuinely expanding right branch.
lam,mu,b,c=F(1,2),F(3),F(1),F(0)
assert lam*mu>1
sp1=sigma_rational(lam,mu,1,2)
assert sp1==2 and jump(lam,mu,1,2)==1
assert phi(sp1-jump(lam,mu,1,2),lam,mu,b,c)==F(2,3)
assert phi(sp1,lam,mu,b,c)==F(7,10)
checks+=5

# Finite Sturmian approximants have jumps only at rationals of bounded denominator.
from fractions import Fraction
for N in (4,8,13,19):
    boundaries=sorted({F(1,5),F(3,5)} | {F(p,q) for q in range(1,N+2) for p in range(q+1) if F(1,5)<F(p,q)<F(3,5)})
    for left,right in zip(boundaries,boundaries[1:]):
        x=left+(right-left)*F(1,3)
        y=left+(right-left)*F(2,3)
        assert sigma_partial(lam,mu,x.numerator,x.denominator,N)==sigma_partial(lam,mu,y.numerator,y.denominator,N)
        checks+=1
print('PASS', checks, 'exact identity/interval and finite-symbolic checks')
print('expand_right_example_half_rotation_plateau', (F(2,3),F(7,10)))
