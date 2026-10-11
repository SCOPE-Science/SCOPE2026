#!/usr/bin/env python3
"""Exact rational spot checks for a rank-one numerical-radius comparison."""
from fractions import Fraction as F


def ratio(q, s, rho, c, u):
    """Ratio where s^2=1-q^2 and u^2=1-c^2, with nonnegative inputs."""
    assert q * q + s * s == 1
    assert c * c + u * u == 1
    assert 0 <= q <= 1 and 0 <= c <= 1
    assert rho > 0 and s >= 0 and u >= 0
    eta = abs(rho - 1)
    return 2 * (1 + eta * c) / (rho * (1 + q * c + s * u))


def predicted(q, s, rho):
    eta = abs(rho - 1)
    t = q / (1 + s)
    if eta < t:
        minimum = (1 - eta * eta) / (rho * (1 - q * eta))
    else:
        minimum = 2 / (rho * (1 + s))
    maximum = max(2 / (rho * (1 + s)), 2 * (1 + eta) / (rho * (1 + q)))
    return minimum, maximum


# Complete exact rational witness for a nontrivial interior minimizer.
q, s, rho = F(3, 5), F(4, 5), F(6, 5)
eta = abs(rho - 1)
t = q / (1 + s)
assert eta < t
c = (q * (1 + eta * eta) - 2 * eta) / (1 + eta * eta - 2 * q * eta)
u = s * (1 - eta * eta) / (1 + eta * eta - 2 * q * eta)
assert (c, u) == (F(7, 25), F(24, 25))
assert c * c + u * u == 1
assert ratio(q, s, rho, c, u) == F(10, 11)
assert ratio(q, s, rho, F(0), F(1)) == F(25, 27)
assert ratio(q, s, rho, F(1), F(0)) == F(5, 4)
assert predicted(q, s, rho) == (F(10, 11), F(5, 4))

# At the sharp upper-endpoint crossing, both distinct overlaps maximize.
q, s, rho = F(4, 5), F(3, 5), F(9, 8)
assert abs(rho - 1) == (q - s) / (1 + s)
assert ratio(q, s, rho, F(0), F(1)) == F(10, 9)
assert ratio(q, s, rho, F(1), F(0)) == F(10, 9)
assert predicted(q, s, rho)[1] == F(10, 9)

# The threshold for the lower minimizer includes equality at the left endpoint.
q, s, rho = F(3, 5), F(4, 5), F(4, 3)
assert abs(rho - 1) == q / (1 + s)
assert predicted(q, s, rho)[0] == ratio(q, s, rho, F(0), F(1))

# Equal radius special case and both degenerate choices of q.
for c, u in [(F(0), F(1)), (F(7, 25), F(24, 25)), (F(1), F(0))]:
    assert ratio(F(1), F(0), F(2), c, u) == 1

# All sample statements are exact Fraction inequalities, not floating-point tests.
qs = [(F(0), F(1)), (F(3, 5), F(4, 5)),
      (F(4, 5), F(3, 5)), (F(1), F(0))]
rhos = [F(1, 2), F(1), F(9, 8), F(6, 5), F(4, 3), F(2), F(3)]
cs = [(F(0), F(1)), (F(3, 5), F(4, 5)),
      (F(7, 25), F(24, 25)), (F(5, 13), F(12, 13)), (F(1), F(0))]
for q, s in qs:
    for rho in rhos:
        m, M = predicted(q, s, rho)
        for c, u in cs:
            val = ratio(q, s, rho, c, u)
            assert m <= val <= M, (q, s, rho, c, val, m, M)
        if q < 1 and abs(rho - 1) < q / (1 + s):
            eta = abs(rho - 1)
            d = 1 + eta * eta - 2 * q * eta
            c = (q * (1 + eta * eta) - 2 * eta) / d
            u = s * (1 - eta * eta) / d
            assert 0 < c < 1 and c * c + u * u == 1
            assert ratio(q, s, rho, c, u) == m

print('RANK_ONE_Q_RHO_SHARP_COMPARISON_EXACT_CHECKS_OK')
