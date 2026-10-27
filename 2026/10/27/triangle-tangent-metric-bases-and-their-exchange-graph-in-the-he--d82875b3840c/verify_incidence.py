#!/usr/bin/env python3
"""Exhaustive incidence-and-triangle verification for Fano metric bases."""
from itertools import combinations
from collections import Counter, deque
import json

POINTS = range(7)
LINES = tuple(t for t in combinations(range(1, 8), 3) if t[0] ^ t[1] ^ t[2] == 0)
assert len(LINES) == 7


def incident(p, ell):
    return p + 1 in LINES[ell - 7]


def distance(u, v):
    if u == v:
        return 0
    if (u < 7) == (v < 7):
        return 2
    if u < 7:
        return 1 if incident(u, v) else 3
    return 1 if incident(v, u) else 3


def resolves(S):
    return len({tuple(distance(v, s) for s in S) for v in range(14)}) == 14


def triangle_triple(T):
    assert len(T) == 3
    if all(v < 7 for v in T):
        return tuple(v + 1 for v in T) not in LINES
    if all(v >= 7 for v in T):
        return not any(all(incident(p, ell) for ell in T) for p in POINTS)
    return False


def predicted(S):
    if len(S) != 5:
        return False
    P = tuple(v for v in S if v < 7)
    L = tuple(v for v in S if v >= 7)
    if len(P) == 3:
        maj, minority = P, L
    elif len(L) == 3:
        maj, minority = L, P
    else:
        return False
    if not triangle_triple(maj):
        return False
    return sorted(sum(distance(a, b) == 1 for b in minority) for a in maj) == [0, 1, 1] and all(sum(distance(a, b) == 1 for a in maj) == 1 for b in minority)


small_counts = {k: sum(resolves(S) for S in combinations(range(14), k)) for k in range(5)}
assert all(v == 0 for v in small_counts.values())
bases = {S for S in combinations(range(14), 5) if resolves(S)}
assert len(bases) == 168
assert all(predicted(S) == (S in bases) for S in combinations(range(14), 5))

# Independently construct the bases by triangles and their three single-incidence tangents.
constructed = set()
for major_side in (range(7), range(7, 14)):
    minor_side = range(7, 14) if major_side.start == 0 else range(7)
    for triple in combinations(major_side, 3):
        if not triangle_triple(triple):
            continue
        tangents = [v for v in minor_side if sum(distance(v, a) == 1 for a in triple) == 1]
        assert len(tangents) == 3
        for pair in combinations(tangents, 2):
            constructed.add(tuple(sorted(triple + pair)))
assert constructed == bases

# All legal single-vertex replacements among optimal solutions.
near = {b: set() for b in bases}
for b in bases:
    for old in b:
        for new in range(14):
            if new not in b:
                candidate = tuple(sorted((set(b) - {old}) | {new}))
                if candidate in bases:
                    near[b].add(candidate)
assert all(len(n) == 5 for n in near.values())
assert all(b in near[c] for b, N in near.items() for c in N)


def major(S):
    p = tuple(v for v in S if v < 7)
    return p if len(p) == 3 else tuple(v for v in S if v >= 7)

blocks = {}
for b in bases:
    blocks.setdefault(major(b), set()).add(b)
assert len(blocks) == 56
assert all(len(v) == 3 for v in blocks.values())
assert all(len(near[b] & block) == 2 for block in blocks.values() for b in block)
assert all(len(near[b] - blocks[major(b)]) == 3 for b in bases)

profiles = Counter()
for start in bases:
    dist = {start: 0}
    Q = deque([start])
    while Q:
        u = Q.popleft()
        for v in near[u]:
            if v not in dist:
                dist[v] = dist[u] + 1
                Q.append(v)
    assert len(dist) == 168
    counts = Counter(dist.values())
    profiles[tuple(counts[i] for i in range(max(counts) + 1))] += 1
assert profiles == {(1, 5, 18, 49, 71, 24): 168}
edges = sum(len(x) for x in near.values()) // 2
assert edges == 420
triangles = sum(len(near[b] & near[c]) for b, N in near.items() for c in N) // 6
assert triangles == 56
print(json.dumps({'minimum_size': 5, 'smaller_resolving_counts': small_counts,
 'bases': len(bases), 'point_majority': sum(sum(v < 7 for v in b) == 3 for b in bases),
 'line_majority': sum(sum(v >= 7 for v in b) == 3 for b in bases),
 'majority_triangles': len(blocks), 'all_bases_triangle_tangent': True,
 'exchange_vertices': len(bases), 'exchange_edges': edges, 'degree': 5,
 'triangles': triangles, 'distance_profiles': [[list(k), v] for k,v in profiles.items()],
 'radius': 5, 'diameter': 5}, sort_keys=True))
