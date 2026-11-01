#!/usr/bin/env python3
"""Independent finite enumeration of fixed-interval and initial-image ranks.
Run: python3 verify_weak_path_attractor.py
Uses only Python's standard library.
"""
from collections import Counter
from itertools import product
from math import comb


def maps(n):
    if n == 1:
        yield (1,)
        return
    for bits in product((0, 1), repeat=n - 1):
        increments = [0]
        for bit in bits:
            increments.append(increments[-1] + bit)
        for start in range(1, n - increments[-1] + 1):
            yield tuple(start + t for t in increments)


def stable_map(f):
    n = len(f)
    current = tuple(range(1, n + 1))
    for _ in range(n):
        current = tuple(f[v - 1] for v in current)
    # This check is independent of the claimed clamp form.
    assert tuple(f[v - 1] for v in current) == current
    return current


def binom_poly(n):
    return [comb(n, k) for k in range(n + 1)]


def analytic_joint(n):
    out = Counter()
    for a in range(1, n + 1):
        for b in range(a, n + 1):
            r = b - a + 1
            left_free = max(0, a - 2)
            right_free = max(0, n - b - 1)
            # Forced ones exactly on the interior of [a,b].
            for additional, count in enumerate(binom_poly(left_free + right_free)):
                out[(a, b, r + additional)] += count
    return out


def verify():
    for n in range(1, 14):
        counts = Counter()
        ranks = Counter()
        for f in maps(n):
            e = stable_map(f)
            fixed = tuple(i for i, value in enumerate(f, 1) if value == i)
            assert fixed
            assert fixed == tuple(range(fixed[0], fixed[-1] + 1))
            a, b = fixed[0], fixed[-1]
            assert e == tuple(max(a, min(b, i)) for i in range(1, n + 1))
            image_rank = len(set(f))
            counts[(a, b, image_rank)] += 1
            ranks[(image_rank, b - a + 1)] += 1
        expected = analytic_joint(n)
        assert counts == expected, (n, counts - expected, expected - counts)
        assert sum(counts.values()) == ((n + 1) * 2 ** (n - 2) if n >= 2 else 1)
        for r in range(1, n + 1):
            observed = sum(val for (a, b, k), val in counts.items() if b - a + 1 == r)
            predicted = 1 if r == n else (n - r + 3) * 2 ** (n - r - 2)
            assert observed == predicted, (n, r, observed, predicted)
        if n in (4, 5, 6, 8, 10, 13):
            hist = [sum(val for (a, b, k), val in counts.items() if b - a + 1 == r)
                    for r in range(1, n + 1)]
            print('n=', n, 'total=', sum(counts.values()), 'stable_rank_counts=', hist)
    print('VERIFY_OK exhaustive independent map/iterate/enumerator comparison n=1..13')


if __name__ == '__main__':
    verify()
