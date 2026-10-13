"""Numerical diagnostics for the smooth copula construction.

The analytic proof establishes the theorem for all parameters and points.
These diagnostics test normalizations and representative values only.
Requires scipy and mpmath.
"""
from math import exp, sqrt
from scipy.integrate import quad
import mpmath as mp

DELTA = 2.0**(-14)

def raw_h(z):
    return exp(-1.0/(z*(1-z))) if 0 < z < 1 else 0.0

I, i_err = quad(raw_h, 0, 1, epsabs=1e-14)
H = exp(-4.0)/I
assert 0 < H < 8.0, H

def h(z):
    return raw_h(z)/I

def eta(z):
    return exp(-1.0/z) if z > 0.0 else 0.0

def chi(u):
    if u <= DELTA/2:
        return 1.0
    if u >= DELTA:
        return 0.0
    z = 2*u/DELTA - 1
    return eta(1-z)/(eta(1-z)+eta(z))

def eps(u):
    return exp(-1.0/(u*u)) if u > 0 else 0.0

def a(u,v):
    return (1-eps(u))*h(v/sqrt(u))/sqrt(u) + eps(u)

def m(v):
    # Substitute z=v/sqrt(u) to resolve boundary layers at tiny v.
    lower = v/sqrt(DELTA)
    if lower >= 1:
        major = 0.0
    else:
        major, err = quad(
            lambda z: 2*v*chi((v/z)**2)*(1-eps((v/z)**2))*h(z)/(z*z),
            lower, 1, epsabs=1e-10, limit=300)
    small, _ = quad(lambda u: chi(u)*eps(u),0,DELTA)
    return major + small

J = 1-3*DELTA/4
cs, _ = quad(chi, 0, DELTA, points=[DELTA/2], epsabs=1e-12)
assert abs(cs-3*DELTA/4)<1e-9, (cs,DELTA)
assert 2*H*sqrt(DELTA)+DELTA < 0.25

for v in [0.000001, 0.0001, 0.001, 0.005, 0.01, 0.2, 0.8]:
    mv = m(v)
    gv = (1-mv)/J
    assert 0 <= mv < .25 and gv > 0
    print('v=',v,'m=',mv,'g=',gv)

for u in [DELTA/4, 3*DELTA/4, 0.1, 0.7]:
    part, _ = quad(lambda v: a(u,v), 0, 1,
                    epsabs=1e-9, limit=200)
    assert abs(part-1)<2e-6, (u,part)

# Exact curve formula: C_*(t,sqrt(t)) = t - (1-sqrt(t))*integral_0^t exp(-1/u^2)du.
# Compare by multiprecision with the entire Clayton family at selected parameters.
mp.mp.dps = 90
for theta in (mp.mpf('0.25'),mp.mpf('1'),mp.mpf('2'),mp.mpf('4'),mp.mpf('10')):
    t = mp.mpf('0.000001')
    if theta > 4:
        t = mp.mpf('1e-8')
    curve_error_upper = t * mp.exp(-1/t**2)
    z = t**(theta/2)-t**theta
    clayton_deficit = t*(-mp.expm1(-mp.log1p(z)/theta))
    assert clayton_deficit > curve_error_upper
    print('theta=',str(theta),'t=',str(t),'Clayton deficit/t=',mp.nstr(clayton_deficit/t,14))
print('Numerical diagnostics passed; analytic argument handles continuum assertions.')
