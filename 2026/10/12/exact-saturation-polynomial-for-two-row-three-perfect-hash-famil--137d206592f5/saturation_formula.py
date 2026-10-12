#!/usr/bin/env python3
"""Exact labeled two-row, strength-three perfect-hash saturation polynomial.

Uses a labeled-component recurrence, independent of the forbidden-triple
subset enumeration in brute_maximal.cpp. Python standard library only.
"""
from collections import Counter
from functools import lru_cache
from math import comb, factorial
import sys

@lru_cache(None)
def spanning(left, right):
    """Edges -> number of star forests covering all named vertices."""
    if left == right == 0:
        return ((0, 1),)
    if not left or not right:
        return ()
    result = Counter()
    # Component of first left vertex: left-centered star, K_2 included.
    for degree in range(1, right + 1):
        for edges, count in spanning(left - 1, right - degree):
            result[edges + degree] += comb(right, degree) * count
    # First left vertex is a leaf of a right-centered star of degree >= 2.
    for degree in range(2, left + 1):
        for edges, count in spanning(left - degree, right - 1):
            result[edges + degree] += right * comb(left - 1, degree - 1) * count
    return tuple(sorted(result.items()))

@lru_cache(None)
def partitions_without_singletons(n, k):
    """Partitions of n named elements into k blocks, each of size >= 2."""
    if (n, k) == (0, 0):
        return 1
    if n <= 0 or k <= 0:
        return 0
    return (k * partitions_without_singletons(n - 1, k)
            + (n - 1) * partitions_without_singletons(n - 2, k - 1))

def distribution(q):
    assert q >= 3
    result = Counter(dict(spanning(q, q)))
    extra = 2 * sum(factorial(q) // factorial(q-k)
                    * partitions_without_singletons(q, k)
                    for k in range(1, q//2 + 1))
    result[q] += extra
    return dict(sorted(result.items()))

if __name__ == '__main__':
    expect = {
        3: {3: 12, 4: 9},
        4: {4: 104, 5: 144, 6: 16},
        5: {5: 530, 6: 1800, 7: 1000, 8: 25},
        6: {6: 5832, 7: 21600, 8: 36900, 9: 4500, 10: 36},
    }
    print('q,k,number_of_labeled_inclusion_maximal_families')
    for q in range(3, 9):
        data = distribution(q)
        assert data and min(data) == q and max(data) == 2*q-2
        assert all(data[k] > 0 for k in range(q, 2*q-1))
        assert data[2*q-2] == q*q
        if q in expect:
            assert data == expect[q], (q, data)
        for k, count in data.items():
            print(f'{q},{k},{count}')
    print('FORMULA_VERIFIED', file=sys.stderr)
