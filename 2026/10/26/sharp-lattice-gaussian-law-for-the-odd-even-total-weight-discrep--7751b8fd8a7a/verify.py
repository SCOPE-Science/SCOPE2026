#!/usr/bin/env python3
"""Finite, self-contained checks for the exact coefficient identity and its Gaussian asymptotic."""
from __future__ import annotations
import math
from functools import lru_cache


def partition_counts(limit):
    p = [0] * (limit + 1)
    q = [0] * (limit + 1)
    p[0] = q[0] = 1
    for part in range(1, limit + 1):
        for total in range(part, limit + 1):
            p[total] += p[total - part]
        if part % 2:
            for total in range(part, limit + 1):
                q[total] += q[total - part]
    return p, q


@lru_cache(maxsize=None)
def small_partitions(n, ceiling):
    if n == 0:
        return ((),)
    out = []
    for first in range(min(n, ceiling), 0, -1):
        for tail in small_partitions(n - first, first):
            out.append((first,) + tail)
    return tuple(out)


def count_exact(n, d, p, q):
    if (n - d) % 4 or (n + d) % 2:
        return 0
    a, b = (n + d) // 2, (n - d) // 4
    if a < 0 or b < 0:
        return 0
    return q[a] * p[b]


def predicted_probability(n, d):
    return (2 / (6 ** 0.25) / n ** 0.75) * math.exp(
        -math.pi * d * d / (4 * math.sqrt(6) * n ** 1.5)
    )


def run():
    p, q = partition_counts(2000)
    assert p[:7] == [1, 1, 2, 3, 5, 7, 11]
    assert q[:7] == [1, 1, 1, 2, 2, 3, 4]
    for n in range(0, 17):
        expected = {}
        for parts in small_partitions(n, n):
            d = sum(v if v % 2 else -v for v in parts)
            expected[d] = expected.get(d, 0) + 1
        assert len(small_partitions(n, n)) == p[n]
        for d in range(-n - 2, n + 3):
            assert expected.get(d, 0) == count_exact(n, d, p, q), (n, d)
    for n in [17, 32, 64, 127, 250, 400, 800, 1200, 2000]:
        exact_total = sum(count_exact(n, d, p, q) for d in range(-n, n + 1))
        assert exact_total == p[n], n
    for n in [400, 800, 1200, 2000]:
        for d in [0, 4 * round(n ** 0.75 / 4)]:
            empirical = count_exact(n, d, p, q) / p[n]
            prediction = predicted_probability(n, d)
            assert abs(empirical / prediction - 1) < 0.17, (n, d)
    assert count_exact(400, 0, p, q) == q[200] * p[100]
    assert count_exact(402, 0, p, q) == 0
    print('VERIFY_OK')


if __name__ == '__main__':
    run()
