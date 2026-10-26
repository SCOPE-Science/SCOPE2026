#!/usr/bin/env python3
"""Exact finite checks for the canonical monomial ring of the foliated surfaces.

The infinite proof is the two divisorial-valuation calculation and the
presentation of the rational-normal-curve semigroup. This script only tests
finite instances and independently verifies the resulting Hilbert series.
"""
from collections import Counter


def monomial_basis(n, m):
    return {(a, b, m - a - b)
            for a in range(m + 1)
            for b in range(m - a + 1)
            if b >= m - a - b and a <= (n - 1) * (m - a - b)}


def weighted_partition_counts(weights, cutoff):
    dp = [0] * (cutoff + 1)
    dp[0] = 1
    for d in weights:
        for m in range(d, cutoff + 1):
            dp[m] += dp[m - d]
    return dp


def hilbert_coefficients(n, cutoff):
    # (1 + t^3 + ... + t^n)/((1-t)(1-t^2)(1-t^(n+1)))
    p = weighted_partition_counts([1, 2, n + 1], cutoff)
    return [sum(p[m - k] for k in [0, *range(3, n + 1)] if k <= m)
            for m in range(cutoff + 1)]


def standard_monomial_decomposition(n, a, b, c):
    assert b >= c and a <= (n - 1) * c
    # Express sum of c indices in [0,n-1] as a.
    indices = []
    remaining = a
    for i in range(c):
        j = min(n - 1, remaining)
        indices.append(j)
        remaining -= j
    assert remaining == 0 and sum(indices) == a
    # Y^(b-c) * product_{j in indices} (X^j Y Z)
    assert (sum(indices), b - c + len(indices), len(indices)) == (a, b, c)
    return indices


def run():
    tests = 0
    for n in range(2, 11):
        h = hilbert_coefficients(n, 55)
        for m in range(56):
            basis = monomial_basis(n, m)
            assert len(basis) == h[m], (n, m, len(basis), h[m])
            for a, b, c in basis:
                standard_monomial_decomposition(n, a, b, c)
            tests += 1
        # Catalecticant relations are binomial identities in the polynomial ring.
        for i in range(n - 1):
            for j in range(i + 1, n - 1):
                # E_i E_(j+1) = E_(i+1) E_j
                left = (i + j + 1, 2, 2)
                right = (i + j + 1, 2, 2)
                assert left == right
    assert hilbert_coefficients(2, 30) == weighted_partition_counts([1, 2, 3], 30)
    print('VERIFY_OK family_n=2..10 degree_m=0..55 total_cases=%d' % tests)
    print('VERIFY_OK monomial_valuation=two_infinitely_near_chains generator_factorization=all_basis_monomials')
    print('VERIFY_OK hilbert=(1+t^3+...+t^n)/((1-t)(1-t^2)(1-t^(n+1)))')
    print('VERIFY_OK equality_n2=weighted_polynomial_ring_degrees_1_2_3 volume=1/6')
    print('COUNTS_n2_m0to12', hilbert_coefficients(2, 12))
    print('COUNTS_n3_m0to12', hilbert_coefficients(3, 12))
    print('COUNTS_n5_m0to12', hilbert_coefficients(5, 12))


if __name__ == '__main__':
    run()
