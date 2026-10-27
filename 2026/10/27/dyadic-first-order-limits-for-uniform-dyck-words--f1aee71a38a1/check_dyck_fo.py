#!/usr/bin/env python3
"""Exact small-size checks for first-order limiting probabilities of Dyck words.

Finite tests are corroborative; the asymptotic and logical conclusions
require the mathematical argument in RESULT.md.
"""
from collections import Counter
from math import comb


def dyck_words(n):
    def visit(up, down, bits):
        if up == n and down == n:
            yield bits
        if up < n:
            yield from visit(up + 1, down, bits + 'U')
        if down < up:
            yield from visit(up, down + 1, bits + 'D')
    yield from visit(0, 0, '')


def catalan(n):
    return comb(2 * n, n) // (n + 1)


def height(u):
    h = 0
    for z in u:
        h += (1 if z == 'U' else -1)
        if h < 0:
            return None
    return h


def reverse_reflect(v):
    return ''.join('D' if z == 'U' else 'U' for z in v[::-1])


def ballot_count(length, start, finish):
    if length < 0 or start < 0 or finish < 0:
        return 0
    if (length + finish - start) % 2:
        return 0
    x = (length + finish - start) // 2
    y = (length + finish + start + 2) // 2
    return (comb(length, x) if 0 <= x <= length else 0) - (comb(length, y) if 0 <= y <= length else 0)


def nonnegative_prefixes(length):
    return [u for u in map(''.join, __import__('itertools').product('UD', repeat=length)) if height(u) is not None]


checks = 0
paths_checked = 0
for n in range(1, 10):
    words = list(dyck_words(n))
    assert len(words) == catalan(n)
    paths_checked += len(words)
    max_a = min(4, n)
    for a in range(max_a + 1):
        for b in range(max_a + 1):
            if a + b > 2*n:
                continue
            empirical = Counter((w[:a], w[-b:] if b else '') for w in words)
            for u in nonnegative_prefixes(a):
                for reflected in nonnegative_prefixes(b):
                    v = reverse_reflect(reflected)
                    h, h2 = height(u), height(reflected)
                    expected = ballot_count(2*n-a-b, h, h2)
                    assert empirical[(u, v)] == expected, (n, a, b, u, v, empirical[(u,v)], expected)
                    checks += 1

coins_checked = 0
for m in range(2, 8):
    weights = sorted(height(u) + 1 for u in nonnegative_prefixes(2*m))
    assert sum(weights) == (1 << (2*m))
    reach = 1
    for w in weights:
        reach |= reach << w
    assert reach.bit_count() == (1 << (2*m)) + 1
    coins_checked += len(weights)

# Check convergence of fixed two-boundary cylinder probabilities in the
# exact reflection formula against the product Bessel(3) boundary law.
asymptotic_checks = 0
for a in (2, 3, 4):
    for b in (2, 3, 4):
        for u in nonnegative_prefixes(a):
            for reflected in nonnegative_prefixes(b):
                q = ballot_count(10000-a-b, height(u), height(reflected)) / catalan(5000)
                limit = (height(u) + 1) * (height(reflected) + 1) / (2 ** (a+b))
                assert abs(q-limit) < 0.0008, (u, reflected, q, limit)
                asymptotic_checks += 1

print('DYCK_FO_EXACT_OK', paths_checked, checks, coins_checked, asymptotic_checks)
