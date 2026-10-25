#!/usr/bin/env python3
"""Standalone exact certificate for the integral homology of the 5-by-5 king complex.

Python standard library only. All cells, matching pairs, signed eliminations, and
independent mod-two boundary ranks are recomputed; no stored matrices are trusted.
"""
from collections import Counter, deque
import heapq
import random

SIZE = 5
V = SIZE * SIZE
adj = []
for a in range(V):
    r, c = divmod(a, SIZE)
    adj.append(sum(1 << b for b in range(V)
                   if b != a and max(abs(r-b//SIZE), abs(c-b%SIZE)) <= 1))

# Nonempty independent sets, with vertices identified by the bit positions
# 5r+c. The DFS visits each subset exactly once in increasing bit order.
faces = []
def enumerate_faces(selected, allowed):
    while allowed:
        bit = allowed & -allowed
        allowed -= bit
        cell = bit.bit_length()-1
        new = selected | bit
        faces.append(new)
        enumerate_faces(new, allowed & ~adj[cell])
enumerate_faces(0, (1 << V)-1)
assert len(faces) == len(set(faces))
index = {f:i for i,f in enumerate(faces)}
N = len(faces)
dimension = [f.bit_count()-1 for f in faces]
counts = Counter(dimension)
assert N == 6426
assert [counts[d] for d in range(9)] == [25,228,964,1987,1974,978,242,27,1]

# Exact oriented incidence matrix ∂, via the natural increasing vertex order.
subfaces = [[] for _ in faces]
signed = [{} for _ in faces]
for j,f in enumerate(faces):
    x = f
    place = 0
    while x:
        bit = x & -x
        x -= bit
        lower = f ^ bit
        if lower:
            i = index[lower]
            subfaces[j].append(i)
            signed[j][i] = (-1)**place
        place += 1
parents = [[] for _ in faces]
for j,lowers in enumerate(subfaces):
    for i in lowers:
        parents[i].append(j)

# An explicit greedy facet/free-facet Morse matching. Only a maximal
# surviving face can be declared critical; a matched lower face must have
# a unique surviving codimension-one coface which is maximal. Thus every
# step is checkable without homological assumptions.
rng = random.Random(1)
tiebreak = [rng.random() for _ in faces]
alive = [True] * N
upper_count = [len(parents[i]) for i in range(N)]
maximals = {i for i in range(N) if upper_count[i] == 0}
free_facets = []

def add_free_candidate(j):
    if alive[j] and upper_count[j] == 0 and any(
            alive[i] and upper_count[i] == 1 for i in subfaces[j]):
        heapq.heappush(free_facets, (dimension[j], tiebreak[j], j))

for j in maximals:
    add_free_candidate(j)

def discard_face(j):
    assert alive[j]
    alive[j] = False
    maximals.discard(j)
    for i in subfaces[j]:
        upper_count[i] -= 1
        assert upper_count[i] >= 0
        if upper_count[i] == 0:
            maximals.add(i)
            add_free_candidate(i)
        elif upper_count[i] == 1:
            for p in parents[i]:
                if alive[p] and upper_count[p] == 0:
                    add_free_candidate(p)

pairs = []
critical = []
while maximals:
    pair = None
    while free_facets:
        _, _, j = heapq.heappop(free_facets)
        if not alive[j] or upper_count[j] != 0:
            continue
        free = [i for i in subfaces[j] if alive[i] and upper_count[i] == 1]
        if free:
            i = min(free, key=lambda a: tiebreak[a])
            pair = (i,j)
            break
    if pair is None:
        j = min(maximals, key=lambda a: (dimension[a],tiebreak[a]))
        critical.append(j)
        discard_face(j)
    else:
        i,j = pair
        assert dimension[j] == dimension[i]+1
        assert upper_count[i] == 1 and upper_count[j] == 0
        pairs.append(pair)
        discard_face(j)
        discard_face(i)
assert not any(alive)
assert len(pairs) == 3173
assert Counter(dimension[j] for j in critical) == {0:1,3:45,4:32,5:2}
assert len(critical) + 2*len(pairs) == N

# Independently check acyclicity by topological sorting of the entire
# face-poset Hasse diagram: paired edges point UP, all others point DOWN.
matched = set(pairs)
successors = [[] for _ in faces]
indegree = [0] * N
for j,lowers in enumerate(subfaces):
    for i in lowers:
        src,dst = (i,j) if (i,j) in matched else (j,i)
        successors[src].append(dst)
        indegree[dst] += 1
q = deque(i for i,d in enumerate(indegree) if d==0)
visited = 0
while q:
    j = q.popleft()
    visited += 1
    for t in successors[j]:
        indegree[t] -= 1
        if indegree[t] == 0:
            q.append(t)
assert visited == N

# Exact integral chain contraction by unit pivots. For (f,g) with
# [∂g:f]=s=+/-1, replace ∂h by ∂h - ([∂h:f]/s) ∂g for every other
# same-dimensional column h, then discard rows f,g and columns f,g.
# The resulting columns are precisely the integral Morse differential.
boundary = [dict(x) for x in signed]
row_columns = [set() for _ in faces]
for j, col in enumerate(boundary):
    for i in col:
        row_columns[i].add(j)
removed = set()
for i,j in pairs:
    assert i not in removed and j not in removed
    pivot = boundary[j].get(i,0)
    assert abs(pivot) == 1
    upper_boundary = boundary[j].copy()
    for h in tuple(row_columns[i]):
        if h == j:
            continue
        amount = boundary[h][i] // pivot
        for row, coeff in upper_boundary.items():
            old = boundary[h].get(row,0)
            new = old - amount*coeff
            if old and new==0:
                del boundary[h][row]
                row_columns[row].remove(h)
            elif new:
                boundary[h][row] = new
                row_columns[row].add(h)
    for h in tuple(row_columns[j]):
        del boundary[h][j]
        row_columns[j].remove(h)
    for removed_col in (i,j):
        for row in tuple(boundary[removed_col]):
            row_columns[row].remove(removed_col)
        boundary[removed_col].clear()
    removed.update((i,j))
assert set(range(N))-removed == set(critical)
assert all(not boundary[j] for j in critical)

# Separate rank computation from the original signed boundary, modulo 2.
# It agrees with the integral Morse counts and independently checks all
# nine face dimensions.
by_dim = {d:[] for d in range(9)}
for j,d in enumerate(dimension):
    by_dim[d].append(j)
ranks = {0:0}
for d in range(1,9):
    to_row = {j:k for k,j in enumerate(by_dim[d-1])}
    pivots = {}
    for j in by_dim[d]:
        bits = 0
        for i in subfaces[j]:
            bits ^= (1<<to_row[i])
        while bits:
            highest = bits.bit_length()-1
            if highest in pivots:
                bits ^= pivots[highest]
            else:
                pivots[highest] = bits
                break
    ranks[d] = len(pivots)
assert [ranks[d] for d in range(9)] == [0,24,204,760,1182,760,216,26,1]
betti = {}
for d in range(9):
    betti[d] = len(by_dim[d]) - ranks[d] - ranks.get(d+1,0)-(d==0)
assert betti == {0:0,1:0,2:0,3:45,4:32,5:2,6:0,7:0,8:0}
print('FACES_NONEMPTY',N,'FACE_VECTOR',tuple(counts[d] for d in range(9)))
print('MATCHED_PAIRS',len(pairs),'CRITICAL',dict(sorted(Counter(dimension[j] for j in critical).items())))
print('HASSE_ACYCLIC',visited,'MORSE_INTEGRAL_NONZERO_ENTRIES',sum(len(boundary[j]) for j in critical))
print('MOD2_BOUNDARY_RANKS',tuple(ranks[d] for d in range(9)))
print('INTEGRAL_REDUCED_BETTI',(0,0,0,45,32,2,0,0,0),'TORSION_NONE')
print('TWO_CONNECTED_YES','HOMOTOPY_IN_DEGREES_5_PLUS_NOT_ASSERTED')
print('VERIFY_OK_KING5_INTEGRAL_HOMOLOGY')
