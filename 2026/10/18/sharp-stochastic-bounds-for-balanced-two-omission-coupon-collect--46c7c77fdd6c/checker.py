"""Exact rational checks for balanced two-omission coupon collection.

Uses only Python's standard library. Analytical proof is in RESULT.md.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import comb


def matching_triangle(n):
    assert n >= 4
    p = {}
    q = F(2, n)
    end = n if n % 2 == 0 else n - 3
    for i in range(0, end, 2):
        p[(i, i + 1)] = q
    if n % 2:
        for a, b in combinations(range(n - 3, n), 2):
            p[(a, b)] = q / 2
    return p


def uniform(n):
    return {edge: F(1, comb(n, 2)) for edge in combinations(range(n), 2)}


def tail(n, p, k):
    q = F(2, n)
    return n * q ** k - sum((v ** k for v in p.values()), F(0))


def fast_tail(n, k):
    q = F(2, n)
    if n % 2 == 0:
        return q ** (k - 1)
    return q ** k * (F(n + 3, 2) - F(3, 2 ** k))


def slow_tail(n, k):
    q, m = F(2, n), comb(n, 2)
    return q ** k * (n - F(m, (n - 1) ** k))


def direct_tail(n, p, k):
    edges = tuple(p)
    total = F(0)
    for seq in product(edges, repeat=k):
        common = set(seq[0])
        weight = F(1)
        for e in seq:
            common.intersection_update(e)
            weight *= p[e]
        if common:
            total += weight
    return total


checks = 0
for n in range(4, 10):
    q = F(2, n)
    m = comb(n, 2)
    fast, slow = matching_triangle(n), uniform(n)
    for p in (fast, slow):
        assert sum(p.values()) == 1
        for vertex in range(n):
            assert sum((p[e] for e in p if vertex in e), F(0)) == q
            checks += 1
        for k in range(1, 8):
            assert fast_tail(n, k) <= tail(n, p, k) <= slow_tail(n, k)
            checks += 1
        for k in (1, 2, 3):
            if n <= 7:
                assert direct_tail(n, p, k) == tail(n, p, k)
                checks += 1
    assert tail(n, fast, 2) == fast_tail(n, 2)
    assert tail(n, slow, 2) == slow_tail(n, 2)
    for a in (F(1, 4), F(1, 3), F(1, 2), F(2, 3), F(3, 4)):
        p = {e: a * fast.get(e, 0) + (1 - a) * slow[e]
             for e in slow}
        assert sum(p.values()) == 1
        for k in range(2, 8):
            assert fast_tail(n, k) < tail(n, p, k) < slow_tail(n, k)
            checks += 1
    # Exact expectations from summing geometric series.
    fast_mean = (1 + F(1, 1 - q)) if n % 2 == 0 else (
        1 + F(n + 3, n - 2) - F(3, n - 1))
    slow_mean = 1 + F(2 * n, n - 2) - F(m, m - 1)
    def mean(p):
        return 1 + n * q / (1 - q) - sum((v / (1 - v) for v in p.values()), F(0))
    assert fast_mean == mean(fast)
    assert slow_mean == mean(slow)
    assert fast_mean < slow_mean
    checks += 3
print(f"PASS: {checks} exact rational checks; complete direct enumeration for n<=7 and k<=3")
