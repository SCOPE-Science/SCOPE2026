#!/usr/bin/env python3
"""Exact finite checks using the Petersen KG(5,2) permutation model.
Python 3 standard library only. All graphs are labelled and fully enumerated.
"""
from collections import Counter, deque
from itertools import combinations, permutations

V = list(combinations(range(5), 2))
A = tuple(frozenset(j for j in range(10) if not set(V[i]) & set(V[j])) for i in range(10))
assert all(len(x) == 3 for x in A)
E = {(i, j) for i in range(10) for j in A[i] if i < j}
assert len(E) == 15

# All undirected simple cycles, canonicalized by least vertex and orientation.
C = {k: set() for k in range(5, 11)}
for root in range(10):
    def go(path):
        u = path[-1]
        if len(path) >= 5 and root in A[u] and path[1] < u:
            C[len(path)].add(tuple(path))
        if len(path) == 10:
            return
        for w in A[u]:
            if w > root and w not in path:
                go(path + [w])
    for nxt in A[root]:
        if nxt > root:
            go([root, nxt])
assert {k: len(v) for k, v in C.items()} == {5: 12, 6: 10, 7: 0, 8: 15, 9: 20, 10: 0}
for c in C[5]:
    rest = set(range(10)) - set(c)
    assert sum(len(A[v] & rest) for v in rest) == 10
for c in C[6]:
    rest = set(range(10)) - set(c)
    assert sorted(len(A[v] & rest) for v in rest) == [1, 1, 1, 3]
for u, v in E:
    rest = set(range(10)) - {u, v}
    assert sum(set(c) == rest for c in C[8]) == 1

# Petersen 1-factors.
def matchings(uncovered, edges=()):
    if not uncovered:
        yield frozenset(edges)
        return
    u = min(uncovered)
    for v in sorted(A[u] & uncovered):
        yield from matchings(uncovered - {u, v}, edges + ((min(u, v), max(u, v)),))
F = sorted(set(matchings(frozenset(range(10)))))
assert len(F) == 6
assert Counter(e for f in F for e in f) == Counter({e: 2 for e in E})
assert all(len(f & g) == 1 for f, g in combinations(F, 2))

# Perfect matchings of the bipartite double cover are Petersen-supported permutations.
P = []
def fill(i, used, p):
    if i == 10:
        P.append(tuple(p)); return
    for j in sorted(A[i]):
        if not (used >> j) & 1:
            p.append(j)
            fill(i + 1, used | (1 << j), p)
            p.pop()
fill(0, 0, [])
assert len(P) == len(set(P)) == 60

def cycle_type(p):
    seen = set(); sizes = []
    for u in range(len(p)):
        if u not in seen:
            v = u; length = 0
            while v not in seen:
                seen.add(v); length += 1; v = p[v]
            sizes.append(length)
    return tuple(sorted(sizes, reverse=True))

TYPE_I = (2, 2, 2, 2, 2)
TYPE_II = (5, 5)
TYPE_III = (8, 2)
type_of = tuple(cycle_type(p) for p in P)
assert Counter(type_of) == {TYPE_I: 6, TYPE_II: 24, TYPE_III: 30}
assert {p for p in P if cycle_type(p) == TYPE_I} == {
    tuple(next(v for v in edge if v != u) for u in range(10)
          for edge in [next(e for e in f if u in e)]) for f in F
}

# The S_5 automorphisms induce the three whole matching orbits.
idx = {p: i for i, p in enumerate(P)}
for t in [TYPE_I, TYPE_II, TYPE_III]:
    i = type_of.index(t)
    orbit = set()
    for sigma in permutations(range(5)):
        q = tuple(V.index(tuple(sorted((sigma[x], sigma[y])))) for x, y in V)
        qinv = [0] * 10
        for a, b in enumerate(q):
            qinv[b] = a
        pnew = tuple(q[P[i][qinv[x]]] for x in range(10))
        orbit.add(idx[pnew])
    assert orbit == {j for j, tj in enumerate(type_of) if tj == t}

def flip_length(p, q):
    inv = [0] * 10
    for u, v in enumerate(p):
        inv[v] = u
    rel = tuple(inv[q[u]] for u in range(10))
    lens = [v for v in cycle_type(rel) if v > 1]
    return 2 * lens[0] if len(lens) == 1 else 0

G6 = [set() for _ in P]
G8 = [set() for _ in P]
G8only = [set() for _ in P]
for i, j in combinations(range(60), 2):
    k = flip_length(P[i], P[j])
    if k == 6:
        G6[i].add(j); G6[j].add(i)
        G8[i].add(j); G8[j].add(i)
    if k == 8:
        G8only[i].add(j); G8only[j].add(i)
        G8[i].add(j); G8[j].add(i)

def components(G):
    seen = set(); comps = []
    for root in range(len(G)):
        if root in seen:
            continue
        todo = [root]; seen.add(root); comp = []
        while todo:
            u = todo.pop(); comp.append(u)
            for v in G[u] - seen:
                seen.add(v); todo.append(v)
        comps.append(comp)
    return sorted(comps, key=lambda x: -len(x))

assert sum(map(len, G6)) // 2 == 120
assert sorted(map(len, components(G6)), reverse=True) == [54, 1, 1, 1, 1, 1, 1]
assert sum(map(len, G8only)) // 2 == 60
assert sum(map(len, G8)) // 2 == 180
assert len(components(G8)) == 1
for i, typ in enumerate(type_of):
    assert (len(G6[i]), len(G8only[i]), len(G8[i])) == {
        TYPE_I: (0, 10, 10), TYPE_II: (5, 0, 5), TYPE_III: (4, 2, 6)
    }[typ]
    assert all(type_of[j] == TYPE_III for j in G8only[i]) if typ == TYPE_I else True
    if typ == TYPE_II:
        assert all(type_of[j] == TYPE_III for j in G6[i])
    if typ == TYPE_III:
        assert all(type_of[j] == TYPE_II for j in G6[i])
        assert all(type_of[j] == TYPE_I for j in G8only[i])
I = [i for i in range(60) if type_of[i] == TYPE_I]
assert all(len(G8only[i] & G8only[j]) == 2 for i, j in combinations(I, 2))
assert all(sum(u in G8only[x] for u in I) == 2 for x in range(60) if type_of[x] == TYPE_III)

pair_dist = Counter()
spheres = {}
for root in range(60):
    dist = {root: 0}; Q = deque([root])
    while Q:
        u = Q.popleft()
        for v in G8[u]:
            if v not in dist:
                dist[v] = dist[u] + 1; Q.append(v)
    assert len(dist) == 60
    sphere = tuple(Counter(dist.values())[d] for d in range(5))
    assert sphere == {
        TYPE_I: (1, 10, 25, 20, 4),
        TYPE_II: (1, 5, 15, 25, 14),
        TYPE_III: (1, 6, 21, 24, 8),
    }[type_of[root]]
    spheres[root] = sphere
    for v, d in dist.items():
        if v > root:
            pair_dist[d] += 1
assert pair_dist == {1: 180, 2: 570, 3: 720, 4: 300}
print('PETERSEN_PERMUTATION_CYCLE_CLASSIFICATION_PASS')
print('DESARGUES_S5_THREE_ORBITS_AND_HEX_OCTAGON_PASS')
print('SIX_FROZEN_MATCHINGS_DOUBLE_K6_INCIDENCE_PASS')
print('ALL_60_SOURCE_GEODESICS_PASS')
