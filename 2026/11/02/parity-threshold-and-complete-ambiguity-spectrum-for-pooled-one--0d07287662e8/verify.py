#!/usr/bin/env python3
"""Literal-substring verification of sparse pooled read theorem."""
from collections import Counter
from itertools import combinations
from math import comb


def weak_compositions(k, n):
    if n == 1:
        yield (k,)
        return
    for bars in combinations(range(k + n - 1), n - 1):
        boundaries = (-1,) + bars + (k + n - 1,)
        yield tuple(boundaries[i + 1] - boundaries[i] - 1 for i in range(n))


def multiset_signature(x):
    n = len(x)
    # Construct the actual length-(n-1) factors, not the analytic edge-sum model.
    acc = Counter()
    for i, multiplicity in enumerate(x):
        if multiplicity:
            word = '0' * i + '1' + '0' * (n - i - 1)
            acc[word[:-1]] += multiplicity
            acc[word[1:]] += multiplicity
    return tuple(sorted(acc.items()))


def choose(t, r):
    return comb(t, r) if t >= r >= 0 else 0


def expected(n, k):
    total = choose(k + n - 1, n - 1)
    if n % 2:
        return {1: total}
    m = n // 2
    def c(j):
        return choose(j + n - 1, n - 1) if j >= 0 else 0
    return {
        s: c(k - m * (s - 1)) - 2 * c(k - m * s) + c(k - m * (s + 1))
        for s in range(1, k // m + 2)
        if c(k - m * (s - 1)) - 2 * c(k - m * s) + c(k - m * (s + 1))
    }


def verify():
    cases = 0
    sources = 0
    all_obs = 0
    for n in range(2, 11):
        for k in range(0, 7):
            fibers = Counter()
            for x in weak_compositions(k, n):
                fibers[multiset_signature(x)] += 1
                sources += 1
            histogram = Counter(fibers.values())
            predicted = Counter(expected(n, k))
            assert histogram == predicted, (n, k, histogram, predicted)
            assert sum(s * c for s, c in histogram.items()) == choose(k + n - 1, n - 1)
            if n % 2 == 0 and k >= n // 2:
                assert max(fibers.values()) == 1 + k // (n // 2)
            else:
                assert max(fibers.values()) == 1
            cases += 1
            all_obs += len(fibers)
    print('VERIFY_OK', 'parameter_pairs=' + str(cases),
          'source_multisets=' + str(sources),
          'distinct_profiles_accumulated=' + str(all_obs),
          'method=literal_nminus1_factor_multisets')

if __name__ == '__main__':
    verify()
