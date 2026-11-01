#!/usr/bin/env python3
"""Exact finite checks for the sharp bounded-degree Crank--Nicolson positivity theorem.

Python 3 standard library only. Finite tests supplement the mathematical proof.
"""
from fractions import Fraction as F
from collections import deque


def bound(delta):
    return F(2 * delta - 1, 2 * delta * (delta - 1))


def invert(matrix):
    n = len(matrix)
    aug = [[F(v) for v in matrix[i]] + [F(i == j) for j in range(n)] for i in range(n)]
    for j in range(n):
        pivot = next((k for k in range(j, n) if aug[k][j]), None)
        if pivot is None:
            raise AssertionError("singular matrix")
        aug[j], aug[pivot] = aug[pivot], aug[j]
        b = aug[j][j]
        aug[j] = [x / b for x in aug[j]]
        for i in range(n):
            if i == j:
                continue
            b = aug[i][j]
            if b:
                aug[i] = [a - b * c for a, c in zip(aug[i], aug[j])]
    return [line[n:] for line in aug]


def connected(n, edges):
    nei = [[] for _ in range(n)]
    for u, v in edges:
        nei[u].append(v)
        nei[v].append(u)
    seen, queue = {0}, deque([0])
    while queue:
        for v in nei[queue.popleft()]:
            if v not in seen:
                seen.add(v)
                queue.append(v)
    return len(seen) == n


def endpoint(n, edges, s):
    lap = [[F(0) for _ in range(n)] for _ in range(n)]
    for u, v in edges:
        lap[u][u] += 1
        lap[v][v] += 1
        lap[u][v] -= 1
        lap[v][u] -= 1
    a = [[(F(i == j) + s * lap[i][j]) for j in range(n)] for i in range(n)]
    res = invert(a)
    return [[2 * res[i][j] - F(i == j) for j in range(n)] for i in range(n)]


def finite_tree(delta, radius):
    edges = []
    frontier = [0]
    count = 1
    for h in range(radius):
        next_frontier = []
        for u in frontier:
            for _ in range(delta if h == 0 else delta - 1):
                v = count
                count += 1
                edges.append((u, v))
                next_frontier.append(v)
        frontier = next_frontier
    return count, edges


def main():
    for d in range(2, 11):
        s = bound(d)
        z = 1 + s * d
        t = (d * s - 1) / (d * s * s)
        assert t > 0
        assert (d - 1) * s * s * t * t - z * t + 1 == 0
        assert 2 * (d - 1) * s * s * t < z  # smaller (physical) cavity root
        assert 1 / (z - d * s * s * t) == F(1, 2)
    print("EXACT TREE-GREEN IDENTITIES: 9 degrees")

    total = 0
    for n in range(2, 6):
        pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
        for mask in range(1 << len(pairs)):
            edges = [p for j, p in enumerate(pairs) if (mask >> j) & 1]
            if not connected(n, edges):
                continue
            d = max(sum(1 for u, v in edges if i in (u, v)) for i in range(n))
            s = bound(max(2, d))
            cn = endpoint(n, edges, s)
            assert all(v >= 0 for row in cn for v in row)
            total += 1
    print(f"EXHAUSTIVE LABELLED CONNECTED GRAPHS n=2..5: {total} passed")

    for d in (2, 3, 4):
        n, edges = finite_tree(d, 2)
        c_at = endpoint(n, edges, bound(d))
        assert all(v >= 0 for row in c_at for v in row)
        c_after = endpoint(n, edges, F(11, 10) * bound(d))
        assert c_after[0][0] < 0
        print(f"TREE BALL SHARPNESS: degree {d}, radius 2, nodes {n}, center={c_after[0][0]}")
    print("VERIFY_OK")

if __name__ == '__main__':
    main()
