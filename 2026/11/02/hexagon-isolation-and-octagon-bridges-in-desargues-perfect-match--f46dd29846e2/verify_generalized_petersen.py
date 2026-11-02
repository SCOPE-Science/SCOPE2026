#!/usr/bin/env python3
"""Independent Desargues GP(10,3) perfect-matching and flip enumerator.
Python 3 standard library only. The edge-mask algorithm does not use
permutation-relative cycles to decide legal flips.
"""
from collections import Counter, deque
from itertools import combinations

n = 10
edges = set()
for i in range(n):
    for a, b in ((i, (i+1) % n), (i, i+n), (i+n, n+(i+3) % n)):
        edges.add(tuple(sorted((a, b))))
E = sorted(edges)
assert len(E) == 30
nbr = [set() for _ in range(20)]
inc = [[] for _ in range(20)]
for k, (a, b) in enumerate(E):
    nbr[a].add(b); nbr[b].add(a)
    inc[a].append((b, k)); inc[b].append((a, k))
assert all(len(x) == 3 for x in nbr)

# A concrete 20-vertex isomorphism to the incidence graph of KG(5,2).
# The first ten target vertices represent the first bipartite layer,
# and target vertices 10..19 the second layer with the same 2-subset names.
map_gp_to_double = (0, 17, 6, 11, 9, 10, 7, 16, 1, 19, 18, 3, 12, 5, 14, 8, 13, 2, 15, 4)
assert sorted(map_gp_to_double) == list(range(20))
labels = list(combinations(range(5), 2))
for i, j in combinations(range(20), 2):
    a, b = map_gp_to_double[i], map_gp_to_double[j]
    target_edge = ((a < 10) != (b < 10)) and (
        not set(labels[a % 10]).intersection(labels[b % 10]))
    assert ((min(i,j),max(i,j)) in edges) == target_edge

full = (1 << 20) - 1
PM = []
def match(uncovered, emask):
    if not uncovered:
        PM.append(emask); return
    low = uncovered & -uncovered
    a = low.bit_length() - 1
    for b, k in inc[a]:
        if uncovered & (1 << b):
            match(uncovered ^ (1 << a) ^ (1 << b), emask | (1 << k))
match(full, 0)
assert len(PM) == len(set(PM)) == 60
assert all(p.bit_count() == 10 for p in PM)

# Independent inclusion-exclusion permanent of the double-cover biadjacency
# matrix (Ryser's formula; no matching recursion or graph search needed).
labels = list(combinations(range(5), 2))
B = [[int(not set(a).intersection(b)) for b in labels] for a in labels]
perm_ryser = 0
for mask in range(1 << 10):
    term = 1
    for row in B:
        term *= sum(row[j] for j in range(10) if mask & (1 << j))
    perm_ryser += (-1)**(10 - mask.bit_count()) * term
assert perm_ryser == len(PM) == 60

def single_alternating_cycle_length(a, b):
    # Symmetric difference of two matchings: direct degree and connectivity check.
    dif = a ^ b
    if not dif: return 0
    used = [k for k in range(30) if (dif >> k) & 1]
    if len(used) not in (6, 8, 10, 12, 14, 16, 18, 20): return 0
    sub = {}
    for k in used:
        u, v = E[k]
        sub.setdefault(u, set()).add(v)
        sub.setdefault(v, set()).add(u)
    if any(len(N) != 2 for N in sub.values()): return 0
    start = min(sub)
    visited = {start}; stack = [start]
    while stack:
        u = stack.pop()
        for v in sub[u]:
            if v not in visited:
                visited.add(v); stack.append(v)
    return len(used) if len(visited) == len(sub) else 0

adj6 = [set() for _ in PM]
adj8 = [set() for _ in PM]
adj8only = [set() for _ in PM]
cycle_counts = Counter()
for i, j in combinations(range(len(PM)), 2):
    k = single_alternating_cycle_length(PM[i], PM[j])
    if k: cycle_counts[k] += 1
    if k == 6:
        adj6[i].add(j); adj6[j].add(i)
        adj8[i].add(j); adj8[j].add(i)
    elif k == 8:
        adj8only[i].add(j); adj8only[j].add(i)
        adj8[i].add(j); adj8[j].add(i)
assert cycle_counts == {6:120, 8:60, 10:324, 12:120, 14:240, 16:120, 18:180, 20:24}

# Independently derive cycle types via the explicit graph isomorphism.
def perm_from_matching(mask):
    p = [None] * 10
    for k, (u, v) in enumerate(E):
        if not (mask >> k) & 1: continue
        u, v = map_gp_to_double[u], map_gp_to_double[v]
        if u >= 10: u, v = v, u
        assert u < 10 <= v
        assert p[u] is None
        p[u] = v - 10
    assert sorted(p) == list(range(10))
    return tuple(p)

def decomp(p):
    visited = set(); out = []
    for start in range(10):
        if start in visited: continue
        x = start; length = 0
        while x not in visited:
            visited.add(x); length += 1; x = p[x]
        out.append(length)
    return tuple(sorted(out, reverse=True))

T = [decomp(perm_from_matching(x)) for x in PM]
small = (2, 2, 2, 2, 2)
pent = (5, 5)
octag = (8, 2)
assert Counter(T) == {small:6, pent:24, octag:30}
for i in range(60):
    t = T[i]
    assert (len(adj6[i]), len(adj8only[i]), len(adj8[i])) == {
        small:(0,10,10), pent:(5,0,5), octag:(4,2,6)}[t]
    assert {T[j] for j in adj6[i]} == ({octag} if t == pent else {pent} if t == octag else set())
    assert {T[j] for j in adj8only[i]} == ({octag} if t == small else {small} if t == octag else set())

# Perform all-source BFS with a fresh connectivity/radius implementation.
def distances(graph, start):
    d = [-1] * len(graph)
    d[start] = 0
    fifo = deque([start])
    while fifo:
        x = fifo.popleft()
        for y in graph[x]:
            if d[y] == -1:
                d[y] = d[x] + 1
                fifo.append(y)
    return d

sizes6 = Counter()
seen = set()
for i in range(60):
    if i in seen: continue
    comp = [j for j, d in enumerate(distances(adj6, i)) if d >= 0]
    seen.update(comp); sizes6[len(comp)] += 1
assert sizes6 == {54:1,1:6}
assert len(set.union(*(adj8[i] | {i} for i in range(60)))) == 60
assert all(-1 not in distances(adj8, i) for i in range(60))
D = Counter()
for i in range(60):
    dist = distances(adj8, i)
    assert max(dist) == 4
    prof = tuple(dist.count(d) for d in range(5))
    assert prof == {
        small:(1,10,25,20,4), pent:(1,5,15,25,14),
        octag:(1,6,21,24,8)}[T[i]]
    for j in range(i+1,60): D[dist[j]] += 1
assert D == {1:180,2:570,3:720,4:300}
Z = [i for i in range(60) if T[i] == small]
assert sorted(len(adj8only[a]&adj8only[b]) for a,b in combinations(Z,2)) == [2]*15
print('GENERALIZED_PETERSEN_30_EDGE_EXHAUSTION_PASS')
print('EXACT_RYSER_PERMANENT_60_PASS')
print('INDEPENDENT_KNESER_DOUBLE_ISOMORPHISM_PASS')
print('MATCHING_CYCLE_FLIP_COMPONENTS_AND_K6_PASS')
print('ALL_PAIRS_DISTANCE_AND_ECCENTRICITY_PASS')
