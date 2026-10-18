#!/usr/bin/env python3
"""Exact rational cross-checks for random-quadrat co-detection covariance."""
from fractions import Fraction
from itertools import combinations
from math import comb
import json


def miss(N, occupied, m):
    if not (0 <= m <= N):
        raise ValueError("sample size outside census")
    return Fraction(comb(N - occupied, m), comb(N, m)) if m <= N - occupied else Fraction(0)


def formula(N, r, s, a, m):
    return miss(N, r + s - a, m) - miss(N, r, m) * miss(N, s, m)


def enumeration(N, r, s, a, m):
    A = set(range(r))
    B = set(range(a)) | set(range(r, r + s - a))
    assert len(B) == s and len(A & B) == a and len(A | B) <= N
    hits_A = hits_B = hits_both = 0
    for sample in combinations(range(N), m):
        S = set(sample)
        i = bool(S & A)
        j = bool(S & B)
        hits_A += i
        hits_B += j
        hits_both += i and j
    count = comb(N, m)
    return Fraction(hits_both, count) - Fraction(hits_A * hits_B, count * count)


def sign(x):
    return (x > 0) - (x < 0)


def valid_parameters(N):
    for r in range(1, N):
        for s in range(r, N):
            for a in range(max(0, r + s - N), min(r, s) + 1):
                yield r, s, a


def main():
    direct_checks = 0
    formula_checks = 0
    flipped_by_census = {}
    for N in range(2, 11):
        flips = []
        for r, s, a in valid_parameters(N):
            values = [formula(N, r, s, a, m) for m in range(1, N + 1)]
            nz = [sign(x) for x in values if x]
            assert nz == sorted(nz, reverse=True), (N, r, s, a, nz)
            nonnested = a < min(r, s)
            should_flip = nonnested and (a * N > r * s)
            observed_flip = 1 in nz and -1 in nz
            assert observed_flip == should_flip, (N, r, s, a, nz)
            if observed_flip:
                flips.append([r, s, a])
            for m, v in enumerate(values, 1):
                assert v == enumeration(N, r, s, a, m), (N, r, s, a, m)
                direct_checks += 1
            formula_checks += 1
        flipped_by_census[str(N)] = flips
    assert flipped_by_census['2'] == []
    assert flipped_by_census['3'] == []
    assert flipped_by_census['4'] == []
    assert flipped_by_census['5'] == [[2, 2, 1], [3, 3, 2]]
    family_checks = 0
    for N in range(5, 101):
        seq = [formula(N, 2, 2, 1, m) for m in range(1, N + 1)]
        assert all(v > 0 for v in seq[:N - 3])
        assert seq[N - 3] < 0
        assert seq[N - 2:] == [0, 0]
        for m, val in enumerate(seq, 1):
            x = N - m
            polynomial = Fraction(x * (x - 1) * m * ((N - 2) * x - 2 * (N - 1)),
                                  N * N * (N - 1) * (N - 1) * (N - 2))
            assert polynomial == val
            family_checks += 1
    example_221 = [str(formula(5, 2, 2, 1, m)) for m in range(1, 6)]
    example_332 = [str(formula(5, 3, 3, 2, m)) for m in range(1, 6)]
    result = {
        'scope': 'all pairs of nonempty proper incidence subsets; unordered range sizes; N=2..10',
        'direct_enumeration_covariance_checks': direct_checks,
        'parameter_triples_checked': formula_checks,
        'flip_profiles_census_2_through_5': {str(n): flipped_by_census[str(n)] for n in range(2, 6)},
        'five_site_examples': {'2_2_1': example_221, '3_3_2': example_332},
        'all_N_5_through_100_family_exact_checks': family_checks,
        'status': 'all_passed'
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
