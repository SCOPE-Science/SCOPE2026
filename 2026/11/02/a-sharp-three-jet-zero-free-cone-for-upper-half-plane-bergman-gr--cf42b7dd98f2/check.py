#!/usr/bin/env python3
"""Exact elementary checks for the three-jet Bergman Gram kernel.

All exact assertions use Python integers and fractions. Floating-point root
samples are ancillary; the uniform all-real-parameter proof is in RESULT.md.
"""
from fractions import Fraction as F
from math import factorial, sqrt
import cmath

# For K=-1/(pi*u^2), each derivative pair contributes
# -(1/pi) * (-1)^j * (j+k+1)! / u^(j+k+2).
# Recover coefficients of -pi*u^6*B in monomials a^j b^k.
# a_0=1, a_1=a, a_2=b.
keys = [(0, 0), (1, 0), (0, 1)]
from collections import defaultdict
P = defaultdict(int)  # (power of u, power of a, power of b) -> integer
for j, (aj, bj) in enumerate(keys):
    for k, (ak, bk) in enumerate(keys):
        P[(4-j-k, aj+ak, bj+bk)] += (-1)**j * factorial(j+k+1)
P = {monomial: coeff for monomial, coeff in P.items() if coeff}
expected = {
    (4, 0, 0): 1,
    (2, 0, 1): 12,
    (2, 2, 0): -6,
    (0, 0, 2): 120,
}
assert P == expected, (P, expected)

# Discriminant identity for y^2+(12b-6a^2)y+120b^2.
for a in [F(0), F(1), F(-2), F(3, 7)]:
    for b in [F(-4), F(-1, 2), F(0), F(1, 10), F(3)]:
        D = (12*b-6*a*a)**2 - 4*120*b*b
        assert D == 12*(3*a**4-12*a*a*b-28*b*b)
        # The real-coefficient polynomial is the exact kernel numerator.
        assert sum(coeff * (F(2)**power_u) * a**power_a * b**power_b
                   for (power_u, power_a, power_b), coeff in P.items()) == (
                       F(2)**4+(12*b-6*a*a)*F(2)**2+120*b*b)

# Boundary constants: 28c^2+12c-3=0; one negative, one positive.
cminus = -(3+sqrt(30))/14
cplus = (sqrt(30)-3)/14
assert cminus < 0 < cplus < F(1, 2)
for c in (cminus, cplus):
    assert abs(28*c*c+12*c-3) < 1e-13

# Test four numerators per representative; count exactly the upper roots.
for a,b,expected_upper in [
    (1, -1, 2), (1, -0.5, 0), (1, 0, 0), (1, 0.1, 0),
    (1, 0.25, 2), (0, 0, 0), (0, 0.1, 2), (-2, -1, 0)
]:
    delta = (12*b-6*a*a)**2-480*b*b
    y1=(6*a*a-12*b+cmath.sqrt(delta))/2
    y2=(6*a*a-12*b-cmath.sqrt(delta))/2
    roots=[cmath.sqrt(y1),-cmath.sqrt(y1),cmath.sqrt(y2),-cmath.sqrt(y2)]
    assert sum(z.imag>1e-9 for z in roots)==expected_upper, (a,b,roots)
    for u in roots:
        assert abs(u**4+(12*b-6*a*a)*u*u+120*b*b)<1e-8

print('THREE_JET_CERTIFICATE_OK: exact coefficient/discriminant identities and ancillary samples')
