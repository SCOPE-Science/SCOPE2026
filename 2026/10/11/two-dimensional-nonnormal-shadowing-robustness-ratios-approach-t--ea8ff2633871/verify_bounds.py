"""Finite exact-arithmetic checks for the displayed shadowability bounds.

The analytic proof, not these checks, establishes the infinite-series
and asymptotic statements.
"""
from fractions import Fraction as F


def check(epsilon, coupling):
    assert 0 < epsilon < 1 and coupling > 0
    a = 1 - epsilon
    b = -1 - epsilon
    assert a - b == 2
    # Stable/unstable projectors have matrices
    # [[1, coupling/2], [0, 0]] and [[0, -coupling/2], [0, 1]].
    assert a > 0 and b < -1
    quadratic_coefficient = -4 * (1 - epsilon) * (1 + epsilon)
    assert quadratic_coefficient < 0
    endpoint_plus = epsilon * (2 + epsilon)
    endpoint_minus = epsilon * (2 - epsilon)
    assert endpoint_minus < endpoint_plus
    lower_bound = (2 - epsilon) * coupling / (coupling + 2 - epsilon)
    return lower_bound


value = check(F(1, 4), F(8))
assert value == F(56, 39), value
assert value * value > 2
for epsilon in [F(1, 20), F(1, 4), F(1, 2), F(3, 4)]:
    assert check(epsilon, F(8)) < 2 - epsilon
print("RATIONAL_BOUNDS_OK")
