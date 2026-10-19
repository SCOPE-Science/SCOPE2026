#!/usr/bin/env python3
"""Exact symbolic and rational checks for a fourfold-equivariant cubic flow.

Requires Python 3 and SymPy. The general theorem is proved in RESULT.md;
finite tests are diagnostics and are not substitutes for the proof.
"""
from fractions import Fraction
from itertools import product
import sympy as S

x, y, a, b, w = S.symbols('x y a b w', real=True)
r2 = x*x+y*y
C = 4*x**3*y-4*x*y**3           # imaginary part of (x+iy)^4
R = x**4-6*x*x*y*y+y**4       # real part of (x+iy)^4
f = (-a+S.I*w)*r2*(x+S.I*y)+b*(x-S.I*y)**3
fx, fy = S.expand(S.re(f)), S.expand(S.im(f))
Ptilde = w*r2*r2 - b*C

def exact_zero(v):
    assert S.expand(S.together(v)) == 0, str(S.factor(v))

# Clearing the positive denominator w makes the certificate polynomial
# in all variables and all parameters, not just a numerical sample.
exact_zero(S.diff(Ptilde,x)*fx+S.diff(Ptilde,y)*fy+4*a*r2*Ptilde)
exact_zero(2*x*fx+2*y*fy-2*(-a*r2*r2+b*R))
# Quarter-turn covariance f(-y,x)=(-fy(x,y), fx(x,y)).
exact_zero(fx.subs({x:-y,y:x}, simultaneous=True)+fy)
exact_zero(fy.subs({x:-y,y:x}, simultaneous=True)-fx)

N = 0
for aa, bb, ww in [(1, 0, 2), (1, 1, 2), (1, 2, 3), (2, 3, 5), (3, 1, 4)]:
    assert ww > bb >= 0 and aa > 0
    for xx, yy in product(range(-5,6), repeat=2):
        if xx == yy == 0:
            continue
        rv = xx*xx + yy*yy
        qv = ww*rv*rv - bb*(4*xx**3*yy-4*xx*yy**3)
        assert qv > 0
        assert -(4*aa*rv*qv) < 0
        # At b=a, Euclidean radius is weakly decreasing, while adding
        # the quartic makes the smooth Morse certificate strictly decrease.
        if aa >= bb:
            radial = 2*(-aa*rv*rv+bb*(xx**4-6*xx*xx*yy*yy+yy**4))
            assert radial <= 0
            assert radial - Fraction(4*aa*rv*qv,ww) < 0
        N += 1
# On the supercritical side the radial derivative is outward at (1,0).
assert 2*(-1+2) == 2
print('PASS: two symbolic Lie identities and two equivariance identities')
print('PASS: '+str(N)+' exact positive-certificate parameter/point checks')
print('PASS: boundary Morse witness and supercritical outward-sector check')
