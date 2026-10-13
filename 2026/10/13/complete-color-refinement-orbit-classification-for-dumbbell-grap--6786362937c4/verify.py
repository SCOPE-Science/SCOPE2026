#!/usr/bin/env python3
from collections import defaultdict

def dumbbell(p, k, q):
    n = p + q + k
    adj = [set() for _ in range(n)]
    def add(u, v):
        adj[u].add(v); adj[v].add(u)
    for i in range(p):
        add(i, (i + 1) % p)
    off = p + k
    for i in range(q):
        add(off + i, off + (i + 1) % q)
    if k == 0:
        add(0, off)
    else:
        add(0, p)
        for x in range(p, p + k - 1):
            add(x, x + 1)
        add(p + k - 1, off)
    return adj

def partition(colors):
    cells = defaultdict(set)
    for v, c in enumerate(colors):
        cells[c].add(v)
    return frozenset(frozenset(s) for s in cells.values())

def stable_partition(adj):
    colors = [0] * len(adj)
    old = partition(colors)
    for _ in range(len(adj) + 5):
        sig = [(colors[v], tuple(sorted(colors[w] for w in adj[v])))
               for v in range(len(adj))]
        names = {}
        new = [names.setdefault(s, len(names)) for s in sig]
        newpart = partition(new)
        if newpart == old:
            return old
        colors, old = new, newpart
    raise RuntimeError("no stabilization")

def endpoint_split_round(adj, u, v):
    colors = [0] * len(adj)
    for r in range(1, len(adj) + 5):
        sig = [(colors[x], tuple(sorted(colors[y] for y in adj[x])))
               for x in range(len(adj))]
        names = {}
        colors = [names.setdefault(s, len(names)) for s in sig]
        if colors[u] != colors[v]:
            return r
    return None

def orbit_partition(p, k, q):
    off = p + k
    cells = []
    if p != q:
        cells.extend([{0}, {off}])
        for d in range(1, p // 2 + 1):
            s = {i for i in range(1, p) if min(i, p - i) == d}
            if s: cells.append(s)
        for j in range(k):
            cells.append({p + j})
        for d in range(1, q // 2 + 1):
            s = {off + i for i in range(1, q) if min(i, q - i) == d}
            if s: cells.append(s)
    else:
        cells.append({0, off})
        for d in range(1, p // 2 + 1):
            s = {i for i in range(1, p) if min(i, p - i) == d}
            s |= {off + i for i in range(1, p) if min(i, p - i) == d}
            if s: cells.append(s)
        for j in range(k):
            j2 = k - 1 - j
            if j <= j2:
                cells.append({p + j, p + j2})
    return frozenset(frozenset(s) for s in cells)

def balanced_stable_partition(m):
    k = m - 1
    off = m + k
    cells = [{0, off}]
    for d in range(1, m // 2 + 1):
        s = {i for i in range(1, m) if min(i, m - i) == d}
        s |= {off + i for i in range(1, m) if min(i, m - i) == d}
        for j in range(k):
            left = j + 1
            right = m - left
            if min(left, right) == d:
                s.add(m + j)
        cells.append(s)
    return frozenset(frozenset(s) for s in cells)

orbit_checks = split_checks = balanced_checks = 0
for p in range(3, 19):
    for q in range(3, 19):
        for k in range(0, 51):
            adj = dumbbell(p, k, q)
            stable = stable_partition(adj)
            orbit = orbit_partition(p, k, q)
            predicted_refinable = not (p == q == k + 1)
            assert (stable == orbit) == predicted_refinable, (p, k, q)
            orbit_checks += 1
            if p != q:
                off = p + k
                assert endpoint_split_round(adj, 0, off) == min(p, q) + 1
                split_checks += 1

for m in range(3, 19):
    stable = stable_partition(dumbbell(m, m - 1, m))
    assert stable == balanced_stable_partition(m)
    balanced_checks += 1

print(
    f"VERIFY_OK orbit_checks={orbit_checks} split_checks={split_checks} "
    f"balanced_partition_checks={balanced_checks} p,q=3..18 k=0..50"
)
