#!/usr/bin/env python3
"""Independent finite checks for two-level poset Ungar games (standard library only)."""
from functools import lru_cache
from math import isqrt


def mex(values):
    x = 0
    while x in values:
        x += 1
    return x


def triangle(k):
    return k * (k + 1) // 2


def closed_two_levels(a, b):
    assert a >= 0 and b >= 0
    t = triangle(b)
    if a <= t:
        return 2 * a + b
    return t + ((a - t - 1) % (b + 1))


def closed_star(n):
    assert n >= 1
    k = (isqrt(8 * n + 1) - 1) // 2
    while triangle(k + 1) <= n:
        k += 1
    while triangle(k) > n:
        k -= 1
    return 2 * n - k + 1


@lru_cache(None)
def direct_two_levels(a, b):
    successors = set()
    for i in range(a + 1):
        for j in range(b + 1):
            if i + j:
                successors.add(direct_two_levels(a - i, b + i - j))
    return mex(successors)


@lru_cache(None)
def direct_central(a, b):
    succ = {direct_two_levels(a - i, b + i) for i in range(a + 1)}
    succ.update(direct_central(a - i, b + i) for i in range(1, a + 1))
    return mex(succ)


def graph_incidence_star(n):
    # Original labeled objects: center 0, leaves 1..n, edges n+1..2n.
    # Each edge-element is BELOW both endpoint-elements.
    count = 2 * n + 1
    upper = [0] * count
    for i in range(1, n + 1):
        e = n + i
        upper[e] = (1 << 0) | (1 << i)
    @lru_cache(None)
    def recurse(mask):
        if not mask:
            return 0
        maxima = 0
        for v in range(count):
            if (mask >> v) & 1 and not (upper[v] & mask):
                maxima |= 1 << v
        assert maxima
        sub = maxima
        values = set()
        while sub:
            values.add(recurse(mask ^ sub))
            sub = (sub - 1) & maxima
        return mex(values)
    return recurse((1 << count) - 1), recurse.cache_info().currsize


def run():
    num = 0
    for a in range(31):
        for b in range(31):
            x = direct_two_levels(a, b)
            y = closed_two_levels(a, b)
            assert x == y, (a, b, x, y)
            num += 1
    print('TWO_LEVEL_POSITIONS_OK', num)
    for a in range(30):
        for b in range(1, 15):
            assert direct_central(a, b) == a, (a, b)
    print('CENTER_RESIDUALS_OK', 30 * 14)
    for n in range(1, 28):
        assert direct_central(n, 0) == closed_star(n), (n, direct_central(n,0), closed_star(n))
    print('STAR_REDUCED_RECURSION_OK', 27)
    for n in range(1, 9):
        brute, states = graph_incidence_star(n)
        assert brute == closed_star(n), (n, brute, closed_star(n))
        print('ORIGINAL_GRAPH_OK', n, brute, states)
    print('VERIFY_OK')

if __name__ == '__main__':
    run()
