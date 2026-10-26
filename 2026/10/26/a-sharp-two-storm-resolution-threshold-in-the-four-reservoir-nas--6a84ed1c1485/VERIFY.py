"""Reproduce the exact four-reservoir double-impulse threshold calculations.

Only Python's standard library is required. Finite numerical checks illustrate,
but do not replace, the polynomial and monotonicity proof in RESULT.md.
"""
from decimal import Decimal, getcontext
from math import exp
import random

getcontext().prec = 50
D = Decimal

def G(s):
    e = s.exp()
    return 4*(3-s)*e + s**4 - 12*s**2 + 24 + 4*(s+3)/e

def bisection():
    a, b = D('2'), D('3')
    assert G(a)>0 and G(b)<0
    for _ in range(220):
        m = (a+b)/2
        if G(m)>0: a=m
        else: b=m
    return (a+b)/2

scrit = bisection()
print('critical_dimensionless_separation=',format(scrit,'f'))
assert D('2.9588081482') < scrit < D('2.9588081483')

def cubic_coeff(s):
    e=exp(s)
    return (-(1+e),3*(1+e-s),3*s*(2-s),s*s*(3-s))

def discriminant(s):
    e=exp(s)
    return -27*e*s*s*(4*(3-s)*e*e+(s**4-12*s*s+24)*e+4*(s+3))

def dp(s,u):
    a,b,c,d=cubic_coeff(s)
    return ((a*u+b)*u+c)*u+d

def derivative_direct(s,u):
    t=s+u
    return (t*t*(3-t)*exp(-t)+u*u*(3-u)*exp(-u))/6

# Independent substitution check for the factored derivative and cubic.
random.seed(2378)
for _ in range(1500):
    s=random.uniform(0.03,7)
    u=random.uniform(0.01,10)
    err=abs(derivative_direct(s,u)-exp(-s-u)*dp(s,u)/6)
    assert err < 1e-10*(1+abs(derivative_direct(s,u)))

# Cubic discriminant's sign convention is verified via the standard identity.
for _ in range(1500):
    s=random.uniform(.01,6)
    a,b,c,d=cubic_coeff(s)
    direct=b*b*c*c-4*a*c**3-4*b**3*d-27*a*a*d*d+18*a*b*c*d
    factored=discriminant(s)
    assert abs(direct-factored)<1e-8*(1+abs(direct)+abs(factored))

# The threshold cleanly separates the one-peak and two-peak regimes.
for s in (2.0,2.4,2.9,2.95,2.96,2.97,2.98,2.999):
    sign=discriminant(s)
    assert (sign>0)==(s>float(scrit))

# Root-count certificate for sample separations: count signs on a dense mesh,
# not presented as a substitute for the analytic infinite-domain proof.
for s, expected in ((2.90,1),(2.97,3),(2.98,3),(3.5,2)):
    us=[(3+s)*i/10000 for i in range(10001)]
    signs=[dp(s,u) for u in us]
    changes=sum(x*y<0 for x,y in zip(signs,signs[1:]))
    assert changes==expected,(s,changes,expected)
print('1500 identity checks; 1500 discriminant checks; 4 mode-count checks PASSED')
