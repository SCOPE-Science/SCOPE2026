#!/usr/bin/env python3
"""Independent direct-dynamics checks of the finite-ring Rule 184 delay law.

Standard library only. `python3 verify.py` runs the default exhaustive checks.
This is a finite test, not a replacement for the all-parameter proof.
"""
from collections import Counter
from itertools import combinations, product
from math import comb


def workload_histogram(k, h):
    """Rooted gap enumerator from the cyclic nonnegative workload theorem."""
    assert k >= 1 and h >= 0
    out = Counter()
    for w in product(range(k), repeat=k):
        if min(w) != 0 or any(w[i] > w[(i + 1) % k] + 1 for i in range(k)):
            continue
        z = w.count(0)
        out[sum(w)] += comb(h + z - 1, z - 1)
    return out


def update_rule184(x, n):
    """Direct site-by-site parallel-update implementation."""
    y = 0
    for i in range(n):
        if (x >> i) & 1:
            j = (i + 1) % n
            y |= 1 << (i if (x >> j) & 1 else j)
    return y


def stopped(x, n):
    """Number of cars blocked at the current update, counted directly."""
    return sum(((x >> i) & 1) * ((x >> ((i + 1) % n)) & 1) for i in range(n))


def direct_delay(x, n, k):
    total = 0
    for _ in range(k):
        b = stopped(x, n)
        if b == 0:
            return total
        total += b
        x = update_rule184(x, n)
    raise AssertionError('No free-flow state reached by k updates')


def direct_histogram(n, k):
    out = Counter()
    for occupied in combinations(range(n), k):
        x = sum(1 << i for i in occupied)
        out[direct_delay(x, n, k)] += 1
    return out


def expected_histogram(n, k):
    h = n - 2 * k
    root = workload_histogram(k, h)
    assert all(n * v % k == 0 for v in root.values())
    return Counter({d: n * v // k for d, v in root.items()})


def gap_delay(occupied, n):
    """Independent car-gap/prefix-minimum formula for an initial configuration."""
    k = len(occupied)
    g = [(occupied[(i + 1) % k] + (n if i + 1 == k else 0)
          - occupied[i] - 1) for i in range(k)]
    total = 0
    for i in range(k):
        b = 0
        w = 0
        for j in range(k - 1):
            b += 1 - g[(i + j) % k]
            w = max(w, b)
        total += w
    return total


def test():
    cases = 0
    for k in range(1, 7):
        for h in range(5):
            n = 2 * k + h
            direct = direct_histogram(n, k)
            symbolic = expected_histogram(n, k)
            assert direct == symbolic, (k, h, direct, symbolic)
            assert sum(direct.values()) == comb(n, k)
            assert max(direct) == comb(k, 2)
            assert direct[comb(k, 2)] == n
            assert direct[0] * k == n * comb(n - k - 1, k - 1)
            for positions in combinations(range(n), k):
                x = sum(1 << i for i in positions)
                assert gap_delay(positions, n) == direct_delay(x, n, k)
            cases += 1
    # Extend to k=7 without relying on any samples or numerical approximation.
    for h in (0, 1):
        k = 7
        n = 2 * k + h
        direct = direct_histogram(n, k)
        symbolic = expected_histogram(n, k)
        assert direct == symbolic
        assert direct[comb(k, 2)] == n
        cases += 1
    print(f'VERIFY_OK: {cases} exact (k,h) cases; direct Rule-184 dynamics, '
          'gap-prefix formula, rooted-workload enumerator, and sharp extrema')


if __name__ == '__main__':
    test()
