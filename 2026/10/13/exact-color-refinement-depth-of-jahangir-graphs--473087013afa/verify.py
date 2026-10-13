#!/usr/bin/env python3
from collections import defaultdict

def jahangir(n, m):
    # J_{n,m}: C_{nm} plus a center adjacent to m cycle vertices
    # spaced n edges apart.  Domain: n>=2, m>=3.
    N = n * m
    adj = [set() for _ in range(N + 1)]
    for i in range(N):
        j = (i + 1) % N
        adj[i].add(j)
        adj[j].add(i)
    center = N
    for j in range(m):
        v = j * n
        adj[center].add(v)
        adj[v].add(center)
    return adj

def partition(colors):
    cells = defaultdict(set)
    for v, c in enumerate(colors):
        cells[c].add(v)
    return frozenset(frozenset(s) for s in cells.values())

def stable_partition_and_depth(adj):
    colors = [0] * len(adj)
    old = partition(colors)
    for r in range(len(adj) + 5):
        sigs = [
            (colors[v], tuple(sorted(colors[w] for w in adj[v])))
            for v in range(len(adj))
        ]
        names = {}
        new = [names.setdefault(s, len(names)) for s in sigs]
        newpart = partition(new)
        if newpart == old:
            return r, old
        colors, old = new, newpart
    raise RuntimeError("no stabilization")

def depth_formula(n, m):
    return max(2, n // 2) if m == 3 else n // 2

def predicted_orbits(n, m):
    N = n * m
    cells = [{N}, {j * n for j in range(m)}]
    for d in range(1, n // 2 + 1):
        cell = set()
        for j in range(m):
            a = j * n
            for t in range(1, n):
                if min(t, n - t) == d:
                    cell.add((a + t) % N)
        if cell:
            cells.append(cell)
    return frozenset(frozenset(c) for c in cells)

depth_checks = orbit_checks = 0
for n in range(2, 61):
    for m in range(3, 31):
        depth, stable = stable_partition_and_depth(jahangir(n, m))
        assert depth == depth_formula(n, m), (n, m, depth, depth_formula(n, m))
        assert stable == predicted_orbits(n, m), (n, m)
        depth_checks += 1
        orbit_checks += 1

print(
    f"VERIFY_OK depth_checks={depth_checks} orbit_checks={orbit_checks} "
    f"n=2..60 m=3..30"
)
