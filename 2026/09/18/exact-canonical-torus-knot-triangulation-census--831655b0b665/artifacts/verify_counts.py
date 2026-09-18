#!/usr/bin/env python3
"""Exact checks for the canonical layered torus-knot census theorem."""
from collections import Counter, defaultdict
from math import gcd


def ell(a: int, b: int) -> int:
    """Subtraction-Euclidean distance from (a,b) to (1,1)."""
    if a <= 0 or b <= 0 or gcd(a, b) != 1:
        raise ValueError((a, b))
    steps = 0
    while (a, b) != (1, 1):
        if a < b:
            b -= a
        elif b < a:
            a -= b
        else:
            raise AssertionError((a, b))
        steps += 1
    return steps


def children(M):
    p, q, r, s = M
    return (
        (p, p + q, r, r + s),
        (p + q, q, r + s, s),
    )


def det(M):
    p, q, r, s = M
    return p * s - q * r


def row_lengths(M):
    p, q, r, s = M
    return ell(p, q), ell(r, s)


def knot(M):
    p, q, r, s = M
    P, Q = p + q, r + s
    assert gcd(P, Q) == 1
    return tuple(sorted((P, Q)))


def enumerate_upto(N: int):
    by_size = Counter()
    by_pair = Counter()
    knots = defaultdict(set)
    for k in range(1, N + 1):
        root = (1, 1, k, k + 1)
        stack = [(root, 0)]
        while stack:
            M, depth = stack.pop()
            a, b = row_lengths(M)
            assert (a, b) == (depth, depth + k)
            n = a + b
            if n > N:
                continue
            assert det(M) == 1 and min(M) > 0
            K = knot(M)
            knots[n].add(K)
            by_pair[(a, b)] += 1
            by_size[n] += 1
            stack.extend((C, depth + 1) for C in children(M))
    return by_size, by_pair, knots


def closed_exact(n: int) -> int:
    return 2 ** ((n + 1) // 2) - 1


def closed_cumulative(N: int) -> int:
    if N % 2 == 0:
        m = N // 2
        return 2 ** (m + 2) - 2 * m - 4
    m = (N + 1) // 2
    return 3 * 2 ** m - 2 * m - 3


if __name__ == "__main__":
    N = 19
    by_size, by_pair, knots = enumerate_upto(N)
    for n in range(1, N + 1):
        assert by_size[n] == closed_exact(n)
        assert len(knots[n]) == closed_exact(n)
        for a in range((n - 1) // 2 + 1):
            b = n - a
            if a < b:
                assert by_pair[(a, b)] == 2 ** a
    cumulative = sum(by_size[n] for n in range(1, N + 1))
    assert cumulative == closed_cumulative(N) == 3049
    assert sum(by_size[n] for n in range(1, 18)) == closed_cumulative(17) == 1515
    print("exact counts n=1..19:", [by_size[n] for n in range(1, N + 1)])
    print("cumulative through 17:", closed_cumulative(17))
    print("cumulative through 19:", cumulative)
