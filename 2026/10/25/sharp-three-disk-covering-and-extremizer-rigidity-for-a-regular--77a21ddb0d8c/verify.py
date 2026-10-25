"""Exact rational geometry checks for the three-disk covering of a regular hexagon.

The proof of the universal lower bound is in RESULT.md; the rational mesh
checks below are regression tests and do not replace quantified algebra.
"""
from fractions import Fraction as F

# Coordinates (x,y) mean the Euclidean point (x,y*sqrt(3)).
V0 = (F(1), F(0))
V1 = (F(1, 2), F(1, 2))
P = (F(3, 4), F(-1, 4))
Q = (F(0), F(1, 2))
C = (F(3, 8), F(1, 8))
O = (F(0), F(0))


def distance_squared(p, q):
    dx, dy = p[0] - q[0], p[1] - q[1]
    return dx * dx + 3 * dy * dy


assert distance_squared(C, P) == F(9, 16)
assert distance_squared(C, Q) == F(9, 16)
assert distance_squared(C, V0) == F(7, 16)
assert distance_squared(C, V1) == F(7, 16)
assert distance_squared(C, O) == F(3, 16)
assert distance_squared(P, Q) == F(9, 4)


def opposite_contact_separation_squared(a, b):
    """Separation of the two opposite candidate gap-contacts for one disk."""
    return (b + (1 - a) / 2) ** 2 + F(3, 4) * (1 + a) ** 2


# Exact polynomial identity at the threshold a+b=1.
for i in range(101):
    a = F(i, 100)
    assert opposite_contact_separation_squared(a, 1 - a) == (
        F(9, 4) + 3 * (a - F(1, 2)) ** 2
    )

# Strict monotonicity in b for b>=1-a, since b+(1-a)/2 >= 0.
# Finite rational values are checked as supplementary regression tests.
tests = 0
for i in range(41):
    for j in range(41):
        a, b = F(i, 40), F(j, 40)
        if a + b >= 1:
            d2 = opposite_contact_separation_squared(a, b)
            assert d2 >= F(9, 4)
            assert (d2 == F(9, 4)) == (a == b == F(1, 2))
            tests += 1

# Opposite edge-pair is vertically sqrt(3) apart: > 2*(3/4).
assert F(3) > F(9, 4)
print("Exact center/fan checks passed; threshold identity for 101 rationals;")
print(f"{tests} exact rational contact inequality regression checks passed.")
