#!/usr/bin/env python3
"""Exact block identities and finite diagnostics for rank-two quotient commutators.
This finite checker is not a proof of infinite-dimensional asymptotics.
"""
from fractions import Fraction
from math import sqrt


def block(d, l, overlap_sq):
    a = Fraction(d - 1, l + d - 1)
    b = Fraction(d - 1, l + d)
    q = Fraction(1) - overlap_sq
    trace = a - b
    discriminant_sq = trace * trace + 4 * a * b * q
    # Exact identities for the trace, determinant and Hilbert--Schmidt energy.
    assert discriminant_sq - trace * trace == 4 * a * b * q
    assert a * a + b * b - 2 * a * b * overlap_sq == trace * trace + 2 * a * b * q
    if q == 0:
        assert trace == Fraction(d - 1, (l + d - 1) * (l + d))
    root = sqrt(float(discriminant_sq))
    r_plus = (float(trace) + root) / 2
    r_minus = (float(trace) - root) / 2
    assert r_plus >= -1e-13 and r_minus <= 1e-13
    assert abs(r_plus * r_minus + float(a * b * q)) <= 1e-12
    return r_plus, -r_minus


def kth_singular(d, m, overlap_sq, k, horizon):
    vals = []
    for l in range(horizon):
        vals.extend(block(d, l, overlap_sq))
    vals = sorted(vals * m, reverse=True)
    assert k <= len(vals)
    return vals[k - 1]


def main():
    for d in (2, 3, 5):
        for alpha2 in (Fraction(0), Fraction(1, 4), Fraction(9, 16), Fraction(1)):
            for l in (0, 1, 2, 5, 23, 197):
                block(d, l, alpha2)
            for m in (1, 3):
                n = 4000
                mu = kth_singular(d, m, alpha2, n, 10000)
                predicted = 2 * m * (d - 1) * sqrt(1 - float(alpha2))
                assert abs(n * mu - predicted) < max(0.045, 0.012 * predicted), (
                    d, m, alpha2, n * mu, predicted
                )
        # Exact finite telescoping identity in the trace-class endpoint.
        for L in (0, 1, 7, 128):
            partial = sum(
                (Fraction(d - 1, (l + d - 1) * (l + d)) for l in range(L + 1)),
                Fraction(0)
            )
            assert partial == 1 - Fraction(d - 1, L + d)
    print('QUOTIENT_ENDPOINT_BLOCK_CHECK_OK')


if __name__ == '__main__':
    main()
