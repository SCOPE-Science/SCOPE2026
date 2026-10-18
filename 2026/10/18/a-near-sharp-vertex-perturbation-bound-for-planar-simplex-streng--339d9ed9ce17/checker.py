"""Exact-algebra verification of the one-vertex triangle-strength bound.

Requires Python 3 and SymPy. Run: python checker.py
All positivity tests below use rational coefficients, not numerical sampling.
"""
from math import comb
import sympy as s

u, v, t, z = s.symbols('u v t z', real=True)
w = z / (1 + z)
strength = (u - 1) * (1 - v**2) / (2 * (u + 1)**2)

du = s.diff(strength, u)
dv = s.diff(strength, v)
grad_squared = s.factor(
    du**2 * 4 * (u**2 - 1) / (u**2 - v**2)
    + dv**2 * 4 * (1 - v**2) / (u**2 - v**2)
)
expected = (
    (u - 1) * (1 - v**2)
    * ((u - 3)**2 * (1 - v**2) + 4 * (u**2 - 1) * v**2)
    / ((u + 1)**5 * (u**2 - v**2))
)
assert s.simplify(grad_squared - expected) == 0

P = s.Poly(s.cancel((
    9 * (u + 1)**5 * (u**2 - w)
    - 1024 * (u - 1) * (1 - w)
    * ((u - 3)**2 * (1 - w) + 4 * (u**2 - 1) * w)
).subs(u, 1 + t) * (1 + z)**2).expand(), z)
P0 = (9 * t**7 + 108 * t**6 + 549 * t**5 + 1530 * t**4
      + 1496 * t**3 + 6544 * t**2 - 2800 * t + 288)
P1 = ((t + 2) * (18 * t**6 + 180 * t**5 + 729 * t**4
       + 1512 * t**3 - 2440 * t**2 + 864 * t + 144))
P2 = 9 * t * (t + 2)**6
assert P.degree() == 2
assert all(s.expand(P.nth(k) - q) == 0 for k, q in enumerate([P0, P1, P2]))


def bernstein_coefficients(poly, a, b):
    """Exact Bernstein coefficients after affine remap of [a,b] to [0,1]."""
    f = s.Poly(poly, t)
    degree = f.degree()
    remapped = s.Poly(s.expand(poly.subs(t, a + (b-a)*t)), t)
    return [sum(remapped.nth(j)*s.Rational(comb(i, j), comb(degree, j))
                for j in range(i+1)) for i in range(degree+1)]

for poly in [P0, P1]:
    # Positivity for all t>=1/2 by positive shifted power coefficients.
    shifted = s.Poly(s.expand(poly.subs(t, t+s.Rational(1, 2))), t)
    assert all(shifted.nth(j) > 0 for j in range(shifted.degree()+1))
    # Positivity on 0<=t<=1/2 by rational Bernstein certificates.
    vals = [coefficient
            for i in range(8)
            for coefficient in bernstein_coefficients(
                poly, s.Rational(i,16), s.Rational(i+1,16))]
    assert len(vals) == 64
    assert min(vals) > 0

assert s.factor(P2) == 9*t*(t+2)**6
assert s.Poly(P2, t).degree() == 7

# Exact lower witness: base endpoints (0,0),(1,0), apex (1/2,1/3).
y = s.symbols('y', real=True, positive=True)
p = (1 + 2*s.sqrt(s.Rational(1,4) + y**2))/2
sigma = y**2/(4*p**3)
low = s.simplify(s.radsimp(s.diff(sigma,y).subs(y,s.Rational(1,3))))
expected_low = s.Rational(567,4) - s.Rational(2043,52)*s.sqrt(13)
assert s.simplify(low-expected_low) == 0
assert s.N(low,35) > 0
assert s.N(low,35) < s.Rational(3,32)
assert s.N((s.Rational(3,32)-low)/s.Rational(3,32),30) < s.Rational(1,250)
print('PASS: derivative identity, exact polynomial, rational positivity, witness')
print('one-vertex coefficient in [%s, %s]' % (str(low), '3/32'))
