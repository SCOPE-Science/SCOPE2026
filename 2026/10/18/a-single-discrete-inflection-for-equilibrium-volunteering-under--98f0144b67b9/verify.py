#!/usr/bin/env python3
"""Reproduce exact and numerical identities for a finite-group volunteering model."""
from fractions import Fraction
import mpmath as mp
import sympy as sp

mp.mp.dps = 80

def volunteers(n, lam):
    assert n >= 2 and lam > 0
    return -n*mp.expm1(-lam/(n-1))

def curvature(n, lam):
    assert n >= 3 and lam > 0
    return volunteers(n+1, lam)-2*volunteers(n, lam)+volunteers(n-1, lam)

def polynomial_sign(n, lam):
    z = mp.exp(-lam/(n*(n-1)*(n-2)))
    return -(n+1)+2*n*z**(n-2)-(n-1)*z**(2*n-2)

def threshold(n):
    lo=mp.mpf(2)*(n-2)/(n-1)
    hi=mp.mpf(2)*n/(n+1)
    assert polynomial_sign(n,lo) > 0
    assert polynomial_sign(n,hi) < 0
    for _ in range(230):
        mid=(lo+hi)/2
        if polynomial_sign(n,mid)>0:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2

# The equality of two player payoffs yields the mixed equilibrium formula.
for n in range(2,90):
    for lam in (mp.mpf('0.12'),mp.mpf('0.8'),mp.mpf('1.4'),mp.mpf('2.5')):
        benefit=mp.exp(lam)
        prob=-mp.expm1(-lam/(n-1))
        volunteer_payoff=benefit-1
        abstain_payoff=benefit*(1-(1-prob)**(n-1))
        assert abs(volunteer_payoff-abstain_payoff) < mp.mpf('1e-67')
print('Equilibrium indifference: 352 high-precision comparisons passed')

# Check the exponential-polynomial identity and the unique-root sign orientation.
last=mp.mpf(0)
for n in range(3,161):
    theta=threshold(n)
    assert last < theta < 2
    last=theta
    assert mp.mpf(2)*(n-2)/(n-1) < theta < mp.mpf(2)*n/(n+1)
    for lam in (theta/5,theta/2,theta*mp.mpf('.99'),theta*mp.mpf('1.01'),theta+mp.mpf('.5'),mp.mpf(4)):
        d=curvature(n,lam)
        p=polynomial_sign(n,lam)
        z=mp.exp(-lam/(n*(n-1)*(n-2)))
        scale=z**((n-1)*(n-2))
        assert abs(d-scale*p) < mp.mpf('1e-66')
        assert (d>0)==(lam<theta)
print('Curvature and threshold ladder: 158 roots, 948 identities/signs passed')

# Mean-preserving spread of n=3 to equally frequent n=2 and n=4.
for s,expected in [(Fraction(6,5),Fraction(575,46656)),
                   (Fraction(5,4),Fraction(-96,15625))]:
    v=lambda n: Fraction(n)*(1-s**(-6//(n-1)))
    assert (v(2)+v(4))/2-v(3)==expected
print('Exact rational spread comparisons passed')

# Two independent algebraic checks of the scaled asymptotic coefficient.
h,c=sp.symbols('h c')
lam=2-2*h+c*h**3
n=1/h
v=lambda shift:(n+shift)*(1-sp.exp(-lam/(n+shift-1)))
d=sp.series(v(1)-2*v(0)+v(-1),h,0,7).removeO()
assert sp.simplify(d-h**6*(-2*c-sp.Rational(8,3)))==0
print('Asymptotic expansion verified: D_n = (-2c-8/3)/n^6 + O(n^-7)')
print('PASS')
