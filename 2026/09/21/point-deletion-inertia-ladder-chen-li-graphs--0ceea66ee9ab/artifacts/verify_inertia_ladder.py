#!/usr/bin/env python3
"""Numerically verify the point-deletion inertia ladder for small parameters.

For k >= 5, W_k has point vertices a_i and two-subset vertices b_S.
The graph G_{k,t} is obtained by deleting t point vertices.
This script checks k=5,...,10 and every 0 <= t <= k.
"""
from itertools import combinations
from math import comb
import numpy as np

TOL = 1e-8

def adjacency(k, t):
    kept_points = list(range(t, k))
    subsets = list(combinations(range(k), 2))
    vertices = [("a", i) for i in kept_points] + [("b", s) for s in subsets]
    index = {v: j for j, v in enumerate(vertices)}
    A = np.zeros((len(vertices), len(vertices)), dtype=float)

    def add(u, v):
        i, j = index[u], index[v]
        A[i, j] = A[j, i] = 1.0

    for i, j in combinations(kept_points, 2):
        add(("a", i), ("a", j))

    for s, u in combinations(subsets, 2):
        if set(s).isdisjoint(u):
            add(("b", s), ("b", u))

    for i in kept_points:
        for s in subsets:
            if i in s:
                add(("a", i), ("b", s))

    return A

def inertia(A):
    vals = np.linalg.eigvalsh(A)
    p = int(np.sum(vals > TOL))
    z = int(np.sum(np.abs(vals) <= TOL))
    q = int(np.sum(vals < -TOL))
    return p, z, q, float(np.min(np.abs(vals)))

def connected(A):
    n = len(A)
    seen = {0}
    stack = [0]
    while stack:
        v = stack.pop()
        for u in np.flatnonzero(A[v] > 0.5):
            u = int(u)
            if u not in seen:
                seen.add(u)
                stack.append(u)
    return len(seen) == n

def reduced(A):
    if np.any(A.sum(axis=1) == 0):
        return False
    rows = {tuple(row.astype(int)) for row in A}
    return len(rows) == len(A)

def main():
    checked = 0
    min_gap = float("inf")
    for k in range(5, 11):
        N = comb(k, 2)
        for t in range(k + 1):
            A = adjacency(k, t)
            got = inertia(A)
            expected = (N + 1 - t, 0, k - 1)
            assert got[:3] == expected, (k, t, got, expected)
            assert connected(A), (k, t, "disconnected")
            assert reduced(A), (k, t, "not reduced")
            min_gap = min(min_gap, got[3])
            checked += 1
    print(f"verified {checked} graphs for 5 <= k <= 10 and all 0 <= t <= k")
    print("all inertia triples, connectivity checks, and reducedness checks passed")
    print(f"smallest absolute eigenvalue in this census: {min_gap:.12g}")

if __name__ == "__main__":
    main()
