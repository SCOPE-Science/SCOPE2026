#!/usr/bin/env python3
"""Self-contained scientific consistency checks for the stated Bessel exit-time law.
Run: python verification.py; requires sympy and mpmath.
"""
from fractions import Fraction
import sympy as sp
import mpmath as mp

# Exact Rayleigh/Kishore cumulant recursion, derived independently of Gamma matching.
a = sp.symbols('a', positive=True)
sigma = {1: 1 / (4*a)}
for n in range(2, 5):
    sigma[n] = sp.factor(sum(sigma[m]*sigma[n-m] for m in range(1,n))/(a+n-1))
k1=2*sigma[1]
k2=4*sigma[2]
k3=2*8*sigma[3]
assert sp.simplify(k1-1/(2*a)) == 0
assert sp.simplify(k2-1/(4*a*a*(a+1))) == 0
assert sp.simplify(k3-1/(2*a**3*(a+1)*(a+2))) == 0
std=sp.sqrt(k2)
third_t=sp.simplify(k3/std**3)
third_g=2/sp.sqrt(a+1)
assert sp.simplify(third_t-4*sp.sqrt(a+1)/(a+2)) == 0
assert sp.simplify((third_g-third_t)/6 + a/(3*(a+2)*sp.sqrt(a+1)))==0
assert sp.simplify(sp.limit(sp.sqrt(a)*a/(3*(a+2)*sp.sqrt(a+1)),a,sp.oo)-sp.Rational(1,3))==0
z=sp.symbols('z', real=True)
h=(z*z-1)*sp.exp(-z*z/2)/sp.sqrt(2*sp.pi)
assert sp.simplify(sp.diff(h,z)+z*(z*z-3)*sp.exp(-z*z/2)/sp.sqrt(2*sp.pi))==0
assert sp.simplify(sp.Abs(h.subs(z,sp.sqrt(3)))/sp.Abs(h.subs(z,0))) < 1

mp.mp.dps=45
for k in (4,8,20,40):
    nu=mp.mpf(k-1)
    j=mp.besseljzero(nu,1)
    assert j*j >= mp.mpf(k*k)/2
    jj=mp.besseljzero(nu,min(k,4))
    assert jj*jj <= (4*mp.pi**2+4)*k*k

# Independent inversion of Laplace transform and closed Gamma CDF at center.
expected = -1/(3*mp.sqrt(2*mp.pi))
previous = None
for k in (20, 40, 80, 160):
    a0=mp.mpf(k)
    mean=1/(2*a0)
    laplace=lambda s:1/(s*mp.hyper([],[a0],s/2))
    prob_t=mp.invertlaplace(laplace,mean,method='dehoog',degree=55)
    prob_g=mp.gammainc(a0+1,0,a0+1)/mp.gamma(a0+1)
    signed=mp.sqrt(a0)*(prob_g-prob_t)
    assert signed<0
    # finite-index deviation is consistent in sign and approaches predicted limit
    assert abs(signed-expected)<mp.mpf('0.04')
    if previous is not None:
        assert abs(signed-expected) < abs(previous-expected)
    previous=signed
    print(f'a={k:>3d}, sqrt(a)*(F_G(mu)-F_T(mu))={mp.nstr(signed,16)}')
print('limiting signed coefficient at center:',mp.nstr(expected,16))
print('all exact and numerical assertions passed')
