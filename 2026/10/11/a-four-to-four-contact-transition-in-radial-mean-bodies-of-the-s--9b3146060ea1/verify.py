#!/usr/bin/env python3
"""Independent arithmetic consistency checks for the square radial-mean phase formula.

The proof for every real parameter is in RESULT.md. This program checks identities
and finite diagnostic cases, rather than certifying an infinite continuum by sampling.
"""
from fractions import Fraction as F
from math import exp, log, sqrt, isclose


def radial(p, q):
    p, q = float(p), float(q)
    factor = sqrt(1.0 + q * q) * 2.0
    if p == 0.0:
        return factor * exp(-1.0 - q / 2.0)
    base = (p + 2.0 - p * q) / ((p + 1.0) * (p + 2.0))
    return factor * exp(log(base) / p)


# Rational Mellin integral identity, valid for real p > -1 by the same algebra.
for p in [F(-9, 10), F(-1, 2), F(-1, 7), F(1, 9), F(1, 2), F(1), F(2), F(7)]:
    for q in [F(0), F(1, 13), F(1, 3), F(2, 5), F(5, 7), F(1)]:
        left = (1 + q) / (p + 1) - 2 * q / (p + 2)
        right = (p + 2 - p * q) / ((p + 1) * (p + 2))
        assert left == right
        # Unnormalized log-radius derivative has a quadratic numerator.
        lhs = q * (p + 2 - p * q) - (1 + q * q)
        rhs = -(q - 1) * ((p + 1) * q - 1)
        assert lhs == rhs

# Rigorous closed-form p=2 values; numerical comparison is diagnostic.
assert isclose(radial(2, 0), 2 / sqrt(3), abs_tol=1e-14)
assert isclose(radial(2, 1), 2 / sqrt(3), abs_tol=1e-14)
assert isclose(radial(2, F(1, 3)), F(10, 9), abs_tol=1e-14)

# Finitely sampled phase/critical checks, not a proof of exhaustive extremizers.
for p in [-0.9, -0.5, 0.0, 0.1, 0.5, 1.0, 1.9, 2.0, 2.1, 4.0, 20.0]:
    values = [radial(p, j / 1000.0) for j in range(1001)]
    q_max = values.index(max(values)) / 1000.0
    q_min = values.index(min(values)) / 1000.0
    if p < 2.0:
        assert q_max == 0.0
    elif p > 2.0:
        assert q_max == 1.0
    else:
        assert isclose(values[0], values[-1], rel_tol=2e-14)
    expected_min = 1.0 if p <= 0.0 else 1.0 / (p + 1.0)
    assert abs(q_min - expected_min) <= 0.00051

print("VERIFY_OK: exact rational moment/factorization identities and finite phase checks")
