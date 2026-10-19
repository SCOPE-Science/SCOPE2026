#!/usr/bin/env python3
"""Exact finite checks of the two-sum convolution of a modular inverse graph."""
from collections import Counter


def check(p):
    n = p * p
    units = tuple(u for u in range(n) if u % p)
    inverse = {u: pow(u, -1, n) for u in units}
    representations = Counter(
        ((u + v) % n, (inverse[u] + inverse[v]) % n)
        for u in units for v in units
    )
    histogram = Counter(representations.values())
    histogram[0] = n * n - len(representations)
    expected = {
        2: p * p * (p - 1) * (p - 3) // 2,
        p: p * (p - 1),
        2 * p: (p - 1) ** 2 // 2,
        p * (p - 1): 1,
    }
    expected[0] = n * n - sum(expected.values())
    assert histogram == Counter(expected), (p, histogram, expected)
    assert sum(m * count for m, count in histogram.items()) == len(units) ** 2
    assert len(representations) == n * n - histogram[0]
    energy = sum(m * m * count for m, count in histogram.items())
    assert energy == 3 * p * p * (p - 1) * (2 * p - 3)
    print(f"p={p}; fibers={dict(sorted(histogram.items()))}; sumset={len(representations)}; energy={energy}; PASS")


if __name__ == '__main__':
    for prime in (5, 7, 11, 13, 19):
        check(prime)
    print('All five exact exhaustive tests passed.')
