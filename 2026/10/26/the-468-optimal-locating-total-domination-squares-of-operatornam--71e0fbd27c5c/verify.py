#!/usr/bin/env python3
"""Exhaustive check of locating-total domination on PG(2,3)'s incidence graph.

No third-party packages. Run: python3 verify.py
"""
from collections import Counter, deque
from itertools import combinations, product

Q = 3

def normalize(x):
    a = next(t for t in x if t)
    return tuple((t * (1 if a == 1 else 2)) % Q for t in x)

vectors = sorted({normalize(x) for x in product(range(Q), repeat=3)
                  if any(x)})
assert len(vectors) == 13
points = range(13)
lines = range(13)
point_lines = [0] * 13
line_points = [0] * 13
for p, v in enumerate(vectors):
    for l, w in enumerate(vectors):
        if sum(v[i] * w[i] for i in range(3)) % Q == 0:
            point_lines[p] |= 1 << l
            line_points[l] |= 1 << p
assert all(x.bit_count() == 4 for x in point_lines + line_points)
assert all((line_points[i] & line_points[j]).bit_count() == 1
           for i in lines for j in lines if i < j)

def masks(k):
    return [sum(1 << x for x in c) for c in combinations(range(13), k)]

def blocking(A):
    return all(A & P for P in line_points)

def covering(B):
    return all(B & P for P in point_lines)

def valid(A, B):
    if not blocking(A) or not covering(B):
        return False
    sig = [point_lines[p] & B for p in points if not A >> p & 1]
    if len(sig) != len(set(sig)):
        return False
    sig = [line_points[l] & A for l in lines if not B >> l & 1]
    return len(sig) == len(set(sig))

point_blocks = {k: list(filter(blocking, masks(k))) for k in range(4, 7)}
line_covers = {k: list(filter(covering, masks(k))) for k in range(4, 7)}
assert len(point_blocks[4]) == len(line_covers[4]) == 13
assert len(point_blocks[5]) == len(line_covers[5]) == 117
solutions = set()
profile = Counter()
for a in range(4, 7):
    for b in range(4, 7):
        if a + b > 10:
            continue
        for A in point_blocks[a]:
            for B in line_covers[b]:
                if valid(A, B):
                    solutions.add((A, B))
                    profile[(a, b)] += 1
assert profile == {(5, 5): 1872}, profile
print('OPTIMUM_OK min_size=10 states=1872 split=5+5')

# Parametric construction; joins of two projective points/lines are unique.
def unique_line(p, q):
    ls = point_lines[p] & point_lines[q]
    assert ls.bit_count() == 1
    return ls.bit_length() - 1

parametric = set()
indexed = {}
for L in lines:
    for q in points:
        if line_points[L] >> q & 1:
            continue
        pencil = point_lines[q]
        for x in points:
            if not (line_points[L] >> x & 1):
                continue
            qx = unique_line(q, x)
            ps = [p for p in points if line_points[qx] >> p & 1
                  and p != q and p != x]
            ts = [t for t in lines if point_lines[x] >> t & 1
                  and t != L and t != qx]
            assert len(ps) == len(ts) == 2
            states = set()
            for p in ps:
                for t in ts:
                    A = line_points[L] | (1 << p)
                    B = pencil | (1 << t)
                    assert valid(A, B)
                    states.add((A, B))
                    parametric.add((A, B))
            assert len(states) == 4
            indexed[(L, q, x)] = states
assert parametric == solutions
assert len(indexed) == 13 * 9 * 4 == 468
print('CLASSIFICATION_OK parameters=468 blocks_of_four')

# Token-jumping exchange: exactly one removed and one inserted vertex.
state_set = solutions
edges = set()
adj = {s: set() for s in solutions}
for A, B in solutions:
    for side in range(2):
        selected = A if side == 0 else B
        for u in range(13):
            if selected >> u & 1:
                for v in range(13):
                    if not (selected >> v & 1):
                        moved = selected ^ (1 << u) ^ (1 << v)
                        nxt = (moved, B) if side == 0 else (A, moved)
                        if nxt in state_set:
                            adj[A, B].add(nxt)
                            edges.add(tuple(sorted(((A, B), nxt))))
assert all(len(neighbors) == 2 for neighbors in adj.values())
components = set()
seen = set()
for s in solutions:
    if s in seen:
        continue
    queue = [s]
    seen.add(s)
    for v in queue:
        for w in adj[v]:
            if w not in seen:
                seen.add(w)
                queue.append(w)
    components.add(frozenset(queue))
assert components == {frozenset(s) for s in indexed.values()}
assert len(components) == 468 and len(edges) == 1872
print('EXCHANGE_OK graph=468*C4 vertices=1872 edges=1872 degree=2')
print('ALL_VERIFY_OK')
