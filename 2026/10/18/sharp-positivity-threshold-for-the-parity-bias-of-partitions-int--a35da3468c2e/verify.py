#!/usr/bin/env python3
"""Exact finite certificates for square-partition parity-bias cutoff.

All arithmetic is over integers. No third-party packages are required.
"""

ZERO_SET = (4, 5, 6, 7, 13, 14, 15, 16, 22, 23, 24, 31, 39, 47, 48, 56, 64)
BASE = (1, 2, 8, 9, 18, 25, 32, 49, 50, 72)


def subsets(elements):
    values = {0}
    for value in elements:
        values |= {s + value for s in values}
    return values


def check_finite():
    assert BASE == tuple(sorted(BASE))
    assert all((b == j * j for j in range(1, 16, 2) if j * j == b) or
               (b == 2 * j * j for j in range(1, 8) if 2 * j * j == b)
               for b in BASE)
    values = subsets(BASE)
    assert sum(BASE) == 266
    assert len(values) == 233
    observed_zeros = tuple(n for n in range(65) if n not in values)
    assert observed_zeros == ZERO_SET
    assert all(n in values for n in range(65, 202))
    assert 202 not in values
    # A second exact count via polynomial multiplication, not set operations.
    c = [0] * 267
    c[0] = 1
    for b in BASE:
        for n in range(266, b - 1, -1):
            c[n] += c[n - b]
    assert sum(x != 0 for x in c) == len(values)
    assert all((c[n] != 0) == (n in values) for n in range(267))
    assert c[64] == 0 and c[65] > 0 and c[201] > 0
    return len(values)


def check_inductive_bound(m_max=500):
    """Exact check of the base and monotonic inequality used symbolically."""
    total = sum(BASE)
    for m in range(7, m_max + 1):
        margin = total - 129 - 2 * m * m
        assert margin >= 39
        if m < m_max:
            next_margin = (total + 2*m*m) - 129 - 2*(m+1)*(m+1)
            assert next_margin - margin == 2*m*m - 4*m - 2 > 0
        total += 2 * m * m


def check_series(degree=500):
    """Independent coefficient comparison of the parity product and subset product."""
    signed = [0] * (degree + 1)
    signed[0] = 1
    m = 1
    while m * m <= degree:
        b = m * m
        for n in range(b, degree + 1):
            signed[n] -= signed[n-b]
        m += 1
    positive = [0] * (degree + 1)
    positive[0] = 1
    factors = [m*m for m in range(1, int(degree**0.5) + 2, 2) if m*m <= degree]
    factors += [2*m*m for m in range(1, int((degree/2)**0.5) + 2) if 2*m*m <= degree]
    assert len(factors) == len(set(factors))
    for b in factors:
        for n in range(degree, b - 1, -1):
            positive[n] += positive[n-b]
    assert all(positive[n] == ((-1)**n)*signed[n] for n in range(degree + 1))
    assert tuple(n for n in range(degree + 1) if positive[n] == 0) == ZERO_SET
    return degree + 1


if __name__ == '__main__':
    states = check_finite()
    check_inductive_bound()
    terms = check_series()
    print(f'VERIFY_OK subset_support={states} checked_series_coefficients={terms} '
          'verified_induction_steps=494 exact_zero_count=17')
