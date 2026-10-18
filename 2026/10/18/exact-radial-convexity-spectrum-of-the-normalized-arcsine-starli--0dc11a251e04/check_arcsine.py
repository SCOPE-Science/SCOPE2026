"""Numerical diagnostics for the sharp radial convexity-order theorem.
These do not replace the analytic inequalities in RESULT.md.
"""
from math import asin, cos, sin, pi, sqrt
from random import Random
from scipy.optimize import brentq
c = 2/pi

def Q(s): return 1-c*asin(s)
def radial(s): return Q(s)-c*s/(Q(s)*sqrt(1-s*s))
def bound(r,s):
    A=sqrt(1-s*s); B=s+(r*r-s*s)/(1-r*r)
    return Q(s)-c*B/(Q(s)*A)

R=brentq(radial,.5,.55,xtol=1e-14)
assert .5<R<.55
for r in [.01,.1,.3,R,.6,.8,.9,.99,.999]:
    assert all(bound(r,r*k/5000) >= radial(r)-1e-9 for k in range(5001))
    assert all(radial(r) <= radial(r*.99999) for _ in range(1))

rng=Random(20261013)
for _ in range(20000):
    r=0.999 * rng.random()
    s=r*rng.random()
    theta=2*pi*rng.random()
    w=s*(cos(theta)+1j*sin(theta))
    k=rng.random(); phase=2*pi*rng.random()
    derivative=w+(r*r-s*s)/(1-r*r)*k*(cos(phase)+1j*sin(phase))
    import cmath
    q=1+c*cmath.asin(w)
    tested=(q+c*derivative/(q*cmath.sqrt(1-w*w))).real
    assert tested >= radial(r)-1e-9,(r,s,tested,radial(r))
print(f'R={R:.15f}; deterministic grid and 20000 complex Dieudonne-admissible cases passed')
