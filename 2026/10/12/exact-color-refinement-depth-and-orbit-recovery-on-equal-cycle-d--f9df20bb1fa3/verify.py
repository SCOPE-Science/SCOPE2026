#!/usr/bin/env python3
from collections import defaultdict

def dumbbell(m, k):
    n = 2*m + k
    adj = [set() for _ in range(n)]
    for i in range(m):
        u, v = i, (i+1) % m
        adj[u].add(v); adj[v].add(u)
    off = m + k
    for i in range(m):
        u, v = off+i, off+(i+1) % m
        adj[u].add(v); adj[v].add(u)
    if k == 0:
        adj[0].add(off); adj[off].add(0)
    else:
        adj[0].add(m); adj[m].add(0)
        for v in range(m, m+k-1):
            adj[v].add(v+1); adj[v+1].add(v)
        adj[m+k-1].add(off); adj[off].add(m+k-1)
    return adj

def partition(colors):
    d = defaultdict(set)
    for v,c in enumerate(colors):
        d[c].add(v)
    return frozenset(frozenset(s) for s in d.values())

def stable_partition_and_depth(adj):
    colors = [0]*len(adj)
    part = partition(colors)
    for r in range(len(adj)+5):
        sigs = [(colors[v], tuple(sorted(colors[w] for w in adj[v])))
                for v in range(len(adj))]
        names = {}
        new = [names.setdefault(s, len(names)) for s in sigs]
        newpart = partition(new)
        if newpart == part:
            return r, part
        colors, part = new, newpart
    raise RuntimeError("no stabilization")

def formula(m,k):
    p = k+1
    if p == m:
        return m//2
    return max(m//2, p//2, min(m,p))

def orbit_partition(m,k):
    off = m+k
    classes = [{0, off}]
    for d in range(1, m//2 + 1):
        s = set()
        for i in range(1,m):
            if min(i,m-i) == d:
                s.add(i)
                s.add(off+i)
        if s:
            classes.append(s)
    for j in range(1,k+1):
        if j <= k+1-j:
            classes.append({m+j-1, m+(k+1-j)-1})
    return frozenset(frozenset(s) for s in classes)

dc = oc = 0
for m in range(3,31):
    for k in range(0,101):
        depth, stable = stable_partition_and_depth(dumbbell(m,k))
        assert depth == formula(m,k), (m,k,depth,formula(m,k))
        dc += 1
        orbit = orbit_partition(m,k)
        assert (stable == orbit) == (k+1 != m), (m,k,stable,orbit)
        oc += 1

print(f"VERIFY_OK depth_checks={dc} orbit_checks={oc} m=3..30 k=0..100")
