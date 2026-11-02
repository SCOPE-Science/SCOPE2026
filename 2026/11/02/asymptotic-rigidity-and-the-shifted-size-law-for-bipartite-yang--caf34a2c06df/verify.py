#!/usr/bin/env python3
"""Standalone small-case conjugation-orbit enumeration and saddle checks.

No external packages. This reproduces the finite examples and tests the
asymptotic saddle used in the accompanying mathematical argument.
"""
from itertools import permutations
from math import factorial, lgamma, log


def compose(a, b):
    return tuple(a[b[i]] for i in range(len(a)))


def inverse(a):
    b = [0] * len(a)
    for i, x in enumerate(a):
        b[x] = i
    return tuple(b)


def orbit_counts(m, kmax):
    group = list(permutations(range(m)))
    idx = {p: i for i, p in enumerate(group)}
    inv = [inverse(g) for g in group]
    total = [0] * (kmax + 1)
    for beta, beta_inv in zip(group, inv):
        c = [idx[compose(compose(beta, h), beta_inv)] for h in group]
        seen = [False] * len(group)
        counts = [0] * (kmax + 1)
        counts[0] = 1
        for v in range(len(group)):
            if seen[v]:
                continue
            j = v
            length = 0
            while not seen[j]:
                seen[j] = True
                j = c[j]
                length += 1
            for k in range(length, kmax + 1):
                counts[k] += counts[k - length]
        for k, count in enumerate(counts):
            total[k] += count
    order = factorial(m)
    assert all(x % order == 0 for x in total)
    return [x // order for x in total]


def partitions(n):
    a = [0] * (n + 1)
    a[0] = 1
    for t in range(1, n + 1):
        for k in range(t, n + 1):
            a[k] += a[k - t]
    return a[n]


def o_by_small_cases(m, k, cache):
    if k == 0 or m <= 1:
        return 1
    if k == 1:
        return partitions(m)
    return cache[m][k]


def finite_examples():
    cache = {m: orbit_counts(m, 8-m) for m in range(2, 7)}
    expected = [1, 2, 3, 7, 17, 57, 305, 4120]
    actual = []
    for n in range(1, 9):
        count = n//2 + 1 + sum(
            o_by_small_cases(m, n-m, cache) - 1 for m in range(2, n+1))
        actual.append(count)
    assert actual == expected, (actual, expected)
    print('EXACT_BIP_N_1_TO_8', actual)
    print('EXACT_ORBIT_CASES', sum(len(x) for x in cache.values()))


def saddle_checks():
    for n in [200, 500, 1000, 4000, 10000]:
        L = log(n)
        vals = [(m*(n-m)*(log(m)-1), m) for m in range(2, n)]
        mx, m = max(vals)
        estimate = n*n/4*(L-log(2)-1) + n*n/(16*L)
        assert abs(mx-estimate) / (n*n) < 0.02
        scaled_shift = (m/n - 0.5)*L
        assert 0.23 < scaled_shift < 0.35
        print('SADDLE',n,m,'scaled_shift',round(scaled_shift,7),
              'normalized_3term_error',round((mx-estimate)/(n*n),8))


if __name__ == '__main__':
    finite_examples()
    saddle_checks()
    print('VERIFY_OK')
