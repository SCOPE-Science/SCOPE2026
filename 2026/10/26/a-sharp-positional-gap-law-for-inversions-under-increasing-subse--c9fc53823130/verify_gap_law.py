#!/usr/bin/env python3
"""Exact checks of inversion expectations under prescribed increasing positions.
No external dependencies. Uses independent permutation enumeration and gap algebra.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial
import json


def inv_count(p):
    return sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))


def gap_excess(s):
    return sum(
        j * (len(s) - j) * (s[j] - s[j - 1] - 1) for j in range(1, len(s))
    )


def predicted(n, s):
    k = len(s)
    return Fraction(n * (n - 1), 4) - Fraction(k * (k - 1), 4) - Fraction(gap_excess(s), k + 1)


def mixture_predicted(n, k):
    return Fraction(n * (n - 1), 4) - Fraction(k * (k - 1) * (2*n + k + 3), 12*(k + 1))


def brute(n):
    all_s = {k: list(combinations(range(1, n + 1), k)) for k in range(2, n + 1)}
    weights = {k: defaultdict(lambda: [0, 0]) for k in all_s}
    overall_sum_i = 0
    overall_sum_z = {k: 0 for k in all_s}
    overall_sum_iz = {k: 0 for k in all_s}
    for p in permutations(range(1, n + 1)):
        i = inv_count(p)
        overall_sum_i += i
        for k, sets in all_s.items():
            for s in sets:
                if all(p[s[a]-1] < p[s[a+1]-1] for a in range(k-1)):
                    cell = weights[k][s]
                    cell[0] += 1
                    cell[1] += i
                    overall_sum_z[k] += 1
                    overall_sum_iz[k] += i
    N = factorial(n)
    for k, sets in all_s.items():
        assert len(sets) == comb(n, k)
        assert all(weights[k][s][0] == N // factorial(k) for s in sets)
        assert all(Fraction(*reversed(weights[k][s])) == predicted(n, s) for s in sets)
        assert min(gap_excess(s) for s in sets) == 0
        assert max(gap_excess(s) for s in sets) == (k*k//4)*(n-k)
        mean_mixture = Fraction(overall_sum_iz[k], overall_sum_z[k])
        assert mean_mixture == mixture_predicted(n, k)
        assert Fraction(sum(gap_excess(s) for s in sets), len(sets)) == Fraction((n-k)*k*(k-1), 6)
        expected_z = Fraction(comb(n, k), factorial(k))
        assert Fraction(overall_sum_z[k], N) == expected_z
        covariance = Fraction(overall_sum_iz[k], N) - Fraction(overall_sum_i, N) * expected_z
        predicted_covariance = -expected_z * Fraction(k*(k-1)*(2*n+k+3), 12*(k+1))
        assert covariance == predicted_covariance
    return {"n": n, "permutations": N, "fixed_position_conditions": sum(map(len, all_s.values())), "status":"PASS"}


if __name__ == "__main__":
    outcomes = [brute(n) for n in range(2, 8)]
    assert predicted(8, (2, 3, 4, 5)) == Fraction(11)
    assert predicted(8, (1, 2, 7, 8)) == Fraction(39, 5)
    assert mixture_predicted(8, 4) == Fraction(47, 5)
    print(json.dumps({"check":"exact enumeration and independent gap formula", "cases":outcomes,
                      "n8_k4_examples":{"contiguous":"11","split":"39/5","uniform_mark_mixture":"47/5"},"status":"PASS"}))
