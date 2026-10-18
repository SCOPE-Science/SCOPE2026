"""Exact arithmetic checks for the outer ellipsoid of orthogonal-disk hulls.

The continuous theorem is proved analytically in RESULT.md. These tests
check the polynomial identities and rational specializations, not novelty
or independent validation.
"""
from fractions import Fraction as F
from math import sqrt


def rational_instance(u):
    assert F(-1, 2) <= u < 0
    t = 3 * u - 1 / u
    a2 = 3 * (u - t / 2) ** 2
    b2 = F(3, 2) * (1 - u * u)
    assert t >= 0 and a2 >= b2 > 0
    assert (u - t / 2) ** 2 / a2 == F(1, 3)
    assert (1 - u * u) / b2 == F(2, 3)
    assert (u - t / 2) / a2 == u / b2
    delta = 1 / b2 - 1 / a2
    # Global containment identity for rational v on the generating circle.
    for i in range(-20, 21):
        v = F(i, 20)
        q = (v - t / 2) ** 2 / a2 + (1 - v * v) / b2
        assert 1 - q == delta * (v - u) ** 2
        assert q <= 1
    return t, a2, b2


pairs = set()
for numerator in range(1, 22):
    for denominator in range(2 * numerator, 2 * numerator + 83):
        pairs.add(F(-numerator, denominator))
for u in sorted(pairs):
    rational_instance(u)

# The normalized four contacts have the Gram matrix of a regular tetrahedron:
# diagonal 1, off-diagonal -1/3, and covariance identity I/3.
x2, y2 = F(1, 3), F(2, 3)
assert x2 + y2 == 1
assert x2 - y2 == -F(1, 3)
assert -x2 == -F(1, 3)
assert y2 / 2 == F(1, 3)

# A few independent floating-point checks at arbitrary real separations.
checks = 0
for t in [0, 1e-6, 0.03, 0.3, 0.5, 1, 2, 4, 17, 100, 10000]:
    root = sqrt(t*t + 12)
    u = -2 / (t + root)
    a2 = (2 * t + root)**2 / 12
    b2 = 1.5 * (1-u*u)
    assert a2 >= b2 > 0
    for j in range(200):
        v = -1 + 2*j/199
        q = (v-t/2)**2/a2 + (1-v*v)/b2
        assert q <= 1 + 2e-10
        checks += 1
print(f'VERIFY_OK exact_rational_parameters={len(pairs)} exact_circle_parameters_per_case=41 float_circle_checks={checks} tetrahedral_frame=exact')
