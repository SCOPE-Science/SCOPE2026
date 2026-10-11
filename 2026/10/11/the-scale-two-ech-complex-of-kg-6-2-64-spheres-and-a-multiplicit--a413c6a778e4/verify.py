#!/usr/bin/env python3
"""Exact finite simplicial and symmetry checks for the Kneser Čech example."""
from itertools import combinations
from collections import Counter, defaultdict, deque
from math import factorial
from functools import lru_cache

V = list(combinations(range(6), 2))
N = len(V)
assert N == 15
I = {e: j for j, e in enumerate(V)}
NB = [sum(1 << j for j, f in enumerate(V) if e == f or set(e).isdisjoint(f)) for e in V]
assert len(set(NB)) == 15 and all(f.bit_count() == 7 for f in NB)
faces = {0}
for f in NB:
    ids = [i for i in range(N) if f >> i & 1]
    for mask in range(1, 1 << len(ids)):
        faces.add(sum(1 << ids[k] for k in range(len(ids)) if mask >> k & 1))
faces.remove(0)
count = Counter(s.bit_count() - 1 for s in faces)
assert [count[i] for i in range(7)] == [15, 105, 455, 525, 315, 105, 15]

active = set(faces)
matching = []
for i in range(N):
    bit = 1 << i
    pair = [(s, s | bit) for s in active if not (s & bit) and (s | bit) in active]
    for a, b in pair:
        assert a in active and b in active and b.bit_count() == a.bit_count() + 1
        active.remove(a); active.remove(b)
    matching += pair
crit = Counter(s.bit_count() - 1 for s in active)
assert len(matching) == 735 and len(active) == 65
assert crit == {0: 1, 2: 64}, crit

# Full directed Hasse poset; matched edges point upwards, all others downwards.
matched = set(matching)
indegree = {s: 0 for s in faces}
out = defaultdict(list)
edges = 0
for t in faces:
    if t.bit_count() < 2:
        continue
    for i in range(N):
        if t >> i & 1:
            s = t ^ (1 << i)
            if (s, t) in matched:
                a, b = s, t
            else:
                a, b = t, s
            out[a].append(b)
            indegree[b] += 1
            edges += 1
q = deque(s for s, d in indegree.items() if d == 0)
visited = 0
while q:
    s = q.popleft()
    visited += 1
    for t in out[s]:
        indegree[t] -= 1
        if indegree[t] == 0: q.append(t)
assert visited == len(faces), (visited, len(faces))

# Independent finite-field chain calculation, not used for integral homotopy conclusion.
classes = [[s for s in faces if s.bit_count() == d + 1] for d in range(7)]
rank = [0]
for d in range(1, 7):
    rows = {s: i for i, s in enumerate(classes[d - 1])}
    pivots = {}
    for t in classes[d]:
        col = 0
        for i in range(N):
            if t >> i & 1:
                col ^= 1 << rows[t ^ (1 << i)]
        while col:
            j = col.bit_length() - 1
            if j in pivots: col ^= pivots[j]
            else:
                pivots[j] = col
                break
    rank.append(len(pivots))
rank.append(0)
betti = [len(classes[d]) - rank[d] - rank[d + 1] for d in range(7)]
assert betti == [1, 0, 64, 0, 0, 0, 0], (rank, betti)

# Full character of S6 on H_2 from the signed simplicial Lefschetz formula.
def partitions(n, maxpart=None):
    if maxpart is None: maxpart = n
    if n == 0:
        yield ()
    for k in range(min(maxpart, n), 0, -1):
        for rest in partitions(n - k, k): yield (k,) + rest

def representative(cycles):
    out = list(range(6))
    pos = 0
    for c in cycles:
        for i in range(c): out[pos + i] = pos + (i + 1) % c
        pos += c
    return out

def trace(cycles):
    p = representative(cycles)
    a = [I[tuple(sorted((p[i], p[j])))] for i,j in V]
    lefschetz = 0
    for s in faces:
        inds = [j for j in range(N) if s >> j & 1]
        move = [a[j] for j in inds]
        if set(inds) != set(move): continue
        inversions = sum(move[i] > move[j] for i in range(len(move)) for j in range(i + 1, len(move)))
        lefschetz += (-1) ** (len(inds) - 1 + inversions)
    return lefschetz - 1

character = {c: trace(c) for c in partitions(6)}
expected = {(6,):0,(5,1):-1,(4,2):0,(4,1,1):0,(3,3):4,(3,2,1):0,
            (3,1,1,1):-2,(2,2,2):0,(2,2,1,1):0,(2,1,1,1,1):0,(1,1,1,1,1,1):64}
assert character == expected, character

# Integer character decomposition by the Murnaghan-Nakayama rim-hook rule.
@lru_cache(None)
def irrep(shape, cycles):
    if not cycles: return int(not shape)
    k = cycles[0]
    total = 0
    for sub in partitions(sum(shape) - k):
        if len(sub) > len(shape) or any(sub[i] > shape[i] for i in range(len(sub))):continue
        cells = {(i,j) for i,row in enumerate(shape) for j in range(row) if j >= (sub[i] if i < len(sub) else 0)}
        if len(cells) != k:continue
        if any({(i,j),(i+1,j),(i,j+1),(i+1,j+1)} <= cells for i,j in cells):continue
        seen = {next(iter(cells))};todo = list(seen)
        while todo:
            i,j = todo.pop()
            for e in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if e in cells and e not in seen:seen.add(e);todo.append(e)
        if len(seen) != len(cells):continue
        total += (-1) ** (len({i for i,j in cells}) - 1) * irrep(sub, cycles[1:])
    return total

multiplicity = {}
for shape in partitions(6):
    numerator = 0
    for cyc, value in character.items():
        centralizer = 1
        for size, multiplicity_size in Counter(cyc).items():
            centralizer *= size ** multiplicity_size * factorial(multiplicity_size)
        numerator += value * irrep(shape, cyc) * (factorial(6) // centralizer)
    assert numerator % factorial(6) == 0
    multiplicity[shape] = numerator // factorial(6)
expected_shapes = {(4,2),(4,1,1),(3,3),(3,2,1),(3,1,1,1),(2,2,2),(2,2,1,1)}
assert all(multiplicity[s] == int(s in expected_shapes) for s in multiplicity),multiplicity
print('VERIFY_OK')
print('faces',len(faces),'f_vector',tuple(count[d] for d in range(7)))
print('matching',len(matching),'critical',dict(crit),'Hasse_incidence',edges,'dag_vertices',visited)
print('mod2_boundary_ranks',rank,'mod2_betti',betti)
print('S6_character',character)
print('S6_irreps',multiplicity)
