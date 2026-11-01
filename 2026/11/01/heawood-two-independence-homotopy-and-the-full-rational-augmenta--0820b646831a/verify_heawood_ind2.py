#!/usr/bin/env python3
"""Exact finite checks for the two-independence complex of the Fano incidence graph.
Run: python3 heawood_ind2_check.py
Only Python's standard library is required.
"""
from collections import Counter, deque
from itertools import permutations
from math import lcm

N = 14
D = (0, 1, 3)
LINES = tuple(frozenset((i+d)%7 for d in D) for i in range(7))
NEIGHBORS = [0] * N
for j, line in enumerate(LINES):
    for i in line:
        NEIGHBORS[i] |= 1 << (7+j)
        NEIGHBORS[7+j] |= 1 << i
assert all(n.bit_count() == 3 for n in NEIGHBORS)
assert len(set(LINES)) == 7
assert len({tuple(sorted((i,j))) for line in LINES for i in line for j in line if i<j}) == 21

# A subset spans only isolated vertices and edges iff every selected vertex
# has at most one selected neighbor, for a simple graph.
FACES = tuple(m for m in range(1, 1<<N)
              if all((NEIGHBORS[v] & m).bit_count() <= 1
                     for v in range(N) if (m>>v)&1))
FACESET = set(FACES)
assert len(FACES) == 2256
FVECTOR = Counter(m.bit_count()-1 for m in FACES)
assert tuple(FVECTOR[i] for i in range(7)) == (14,91,322,651,728,392,58)
FACETS = tuple(m for m in FACES if all((m|1<<v) not in FACESET
                                        for v in range(N) if not (m>>v)&1))
assert Counter(m.bit_count()-1 for m in FACETS) == {5:70,6:58}

# Sequential elementary vertex toggles. The matching is independently
# checked against all cover incidences for global acyclicity below.
remaining = set(FACES)
matched = set()
for vertex in range(N):
    for low in FACES:
        if low not in remaining or (low>>vertex)&1:
            continue
        high = low | (1<<vertex)
        if high in remaining:
            remaining.remove(low)
            remaining.remove(high)
            matched.add((low,high))
assert len(matched) == 1121
assert Counter(m.bit_count()-1 for m in remaining) == {0:1,5:13}

# Complete face-poset cover graph. Direct matched edges upwards, unmatched
# edges downwards. Kahn's algorithm must visit EVERY nonempty simplex.
indegree = {f:0 for f in FACES}
successors = {f:[] for f in FACES}
incidences = 0
for high in FACES:
    low = high
    while low:
        bit = low & -low
        low -= bit
        face = high ^ bit
        if face == 0:
            continue  # empty simplex omitted from this face-poset matching
        incidences += 1
        if (face,high) in matched:
            tail,head = face,high
        else:
            tail,head = high,face
        successors[tail].append(head)
        indegree[head] += 1
q = deque(f for f in FACES if indegree[f]==0)
visited = 0
while q:
    current = q.popleft()
    visited += 1
    for nxt in successors[current]:
        indegree[nxt] -= 1
        if indegree[nxt]==0:
            q.append(nxt)
assert visited == len(FACES), (visited,len(FACES))

# Independent check on the integral homotopy prediction using simplicial
# boundary matrix ranks mod 2: 2-dimensional or higher critical cells cannot
# arise from the elementary discrete-Morse reduction.
def rank_mod2(vectors):
    pivots = {}
    for x in vectors:
        while x:
            i = x.bit_length()-1
            if i not in pivots:
                pivots[i] = x
                break
            x ^= pivots[i]
    return len(pivots)
groups = [[f for f in FACES if f.bit_count()==k+1] for k in range(7)]
ranks = [0]
for degree in range(1,7):
    indexes = {f:i for i,f in enumerate(groups[degree-1])}
    cols = []
    for high in groups[degree]:
        boundary = 0
        for v in range(N):
            if (high>>v)&1:
                boundary ^= 1<<indexes[high^(1<<v)]
        cols.append(boundary)
    ranks.append(rank_mod2(cols))
assert [len(groups[d])-ranks[d]- (ranks[d+1] if d<6 else 0)
        for d in range(7)] == [1,0,0,0,0,13,0]

# Enumerate all seven-point Fano-plane collineations directly from S_7,
# and extend them to incidence-graph automorphisms. Compose with the
# explicit point/line polarity i <-> line(-i), yielding the full 336.
line_lookup = {line:i for i,line in enumerate(LINES)}
collineations=[]
for perm in permutations(range(7)):
    mapped = tuple(line_lookup.get(frozenset(perm[x] for x in line),-1)
                   for line in LINES)
    if -1 not in mapped:
        collineations.append(tuple(perm)+tuple(7+j for j in mapped))
assert len(collineations) == 168
polarity = tuple(7+(-i)%7 for i in range(7)) + tuple((-j)%7 for j in range(7))
def is_automorphism(p):
    return all(sum(1<<p[v] for v in range(N) if (NEIGHBORS[i]>>v)&1)
               == NEIGHBORS[p[i]] for i in range(N))
assert is_automorphism(polarity)
automorphisms = collineations + [tuple(polarity[x] for x in p) for p in collineations]
assert len(set(automorphisms)) == 336
assert all(is_automorphism(p) for p in automorphisms)

# Simplicial Lefschetz: trace(H_5(g)) = 1 - sum_{nonempty invariant sigma}
# (-1)^{dim sigma} sign(g|sigma), since X is a connected wedge of 5-spheres.
def mapped_face(face, p):
    result = 0
    while face:
        bit = face & -face
        face ^= bit
        result |= 1<<p[bit.bit_length()-1]
    return result

def orientation_sign(face, p):
    coords = [p[i] for i in range(N) if (face>>i)&1]
    inversions = sum(coords[i]>coords[j] for i in range(len(coords))
                     for j in range(i+1,len(coords)))
    return 1 if inversions%2==0 else -1

def permutation_order(p):
    seen=set();order=1
    for x in range(N):
        if x in seen:continue
        y=x;k=0
        while y not in seen:
            seen.add(y);y=p[y];k+=1
        order=lcm(order,k)
    return order

classes=Counter()
char_total = 0
char_col_pres = 0
for p in automorphisms:
    lefschetz = sum((-1 if f.bit_count()%2 == 0 else 1) * orientation_sign(f,p)
                    for f in FACES if mapped_face(f,p)==f)
    tr = 1 - lefschetz
    fixed = sum(p[i]==i for i in range(N))
    assert tr == fixed-1, (p,tr,fixed)
    order = permutation_order(p)
    exchange = p[0]>=7
    classes[(order,exchange,fixed,tr)] += 1
    char_total+=tr
    if not exchange:
        char_col_pres+=tr
assert sum(classes.values()) == 336
assert char_total == 0
assert char_col_pres == 168
print('HEAWOOD_IND2_FULL_AUTOMORPHISM_CHARACTER_OK')
print('vertices=14 graph_edges=21 simplices=2256')
print('f_vector=',tuple(FVECTOR[i] for i in range(7)))
print('facets_dimension_counts=',dict(Counter(m.bit_count()-1 for m in FACETS)))
print('morse_pairs=1121 critical_vertex=1 critical_5_cells=13')
print('hasse_incidences=',incidences,'acyclic_faces=',visited)
print('mod2_boundary_ranks=',ranks)
print('full_automorphism_group=336 partition_preserving=168')
print('character_signatures=',sorted((key,count) for key,count in classes.items()))
print('full_invariant_dimension=0 partition_preserving_invariant_dimension=1')
