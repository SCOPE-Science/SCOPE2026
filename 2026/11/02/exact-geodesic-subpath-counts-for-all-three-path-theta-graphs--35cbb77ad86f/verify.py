#!/usr/bin/env python3
"""Independent graph construction and shortest-path count check for the closed theta formula.

Usage: python3 verify.py  (Python standard library only).
"""
from collections import deque
from itertools import combinations_with_replacement
from random import Random


def formula(lengths):
    a, b, c = sorted(lengths)
    if a < 2:
        raise ValueError("Each path must contain at least two edges")
    n = a + b + c - 1
    par = lambda x, y: int((x - y) % 2 == 0)

    def r(t, s):
        return (t - s) // 2 + 1 if t > s and par(t, s) else 0

    k = (c - a + 1) // 2
    q = max(0, k * (k + 1) // 2 - 1) if c > a else 0
    p = int(a == b) * (1 + int(b == c))
    m = b - 1 if a == b else a + par(a, b)
    ell = max(0, (b - a - 1) // 2)
    h = (par(b, c) * m
         + 2 * int(c >= a + 2 and par(c, a)) * ell
         + 2 * int(b >= a + 2 and par(b, a)) * ((c - a) // 2))
    return (n * (n + 1) // 2 + p + r(b, a)
            + (1 + int(a == b)) * r(c, a)
            + int(a == b) * q
            + (a - 1) * (par(a, b) + par(a, c)) + h)


def independent_bfs(lengths):
    """Construct all labelled edges and count shortest paths by repeated BFS.

    This routine does not use the closed formula or its case distinctions.
    """
    n = 2
    adj = [[], []]
    for length in lengths:
        interior = list(range(n, n + length - 1))
        n += length - 1
        adj.extend([] for _ in interior)
        chain = [0] + interior + [1]
        for u, v in zip(chain, chain[1:]):
            adj[u].append(v)
            adj[v].append(u)
    total = n  # each vertex's length-zero path
    for start in range(n):
        distances = [-1] * n
        ways = [0] * n
        distances[start] = 0
        ways[start] = 1
        queue = deque([start])
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if distances[v] < 0:
                    distances[v] = distances[u] + 1
                    queue.append(v)
                if distances[v] == distances[u] + 1:
                    ways[v] += ways[u]
        assert all(d >= 0 for d in distances)
        total += sum(ways[start + 1:])
    return total


def run():
    z = 0
    for triple in combinations_with_replacement(range(2, 14), 3):
        assert formula(triple) == independent_bfs(triple), triple
        z += 1
    print("EXHAUSTIVE_LENGTH_TRIPLES_2_TO_13_OK", z)

    rng = Random(4004)
    for _ in range(200):
        triple = tuple(rng.randint(2, 70) for _ in range(3))
        assert formula(triple) == independent_bfs(triple), triple
    print("INDEPENDENT_RANDOM_WIDE_LENGTH_TRIPLES_OK", 200)

    for t in range(2, 100):
        n = 3 * t - 1
        assert formula((t, t, t)) == n * (n + 1) // 2 + 3 * t - 1
    print("EQUAL_ARM_COROLLARY_OK", 98)

    examples = [((2, 2, 2), 20), ((3, 3, 3), 44),
                ((2, 2, 4), 36), ((2, 8, 8), 176),
                ((3, 3, 9), 125), ((10, 10, 2), 260)]
    for lengths, value in examples:
        assert formula(lengths) == value
    print("INDEPENDENT_EXAMPLES_OK", len(examples))
    print("VERIFY_OK")


if __name__ == "__main__":
    run()
