#!/usr/bin/env python3
"""Finite, exhaustive checks for the Pappus induced-edge-matching complex.

Run: python3 verify_pappus_strong_matching.py
Python standard library only. Every face and every automorphism is enumerated.
"""
from collections import Counter, deque
from itertools import combinations

N = 18
LCF = [5, 7, -7, 7, -7, -5] * 3
EDGES = tuple(sorted({tuple(sorted((i, (i+1) % N))) for i in range(N)} |
                     {tuple(sorted((i, (i+LCF[i]) % N))) for i in range(N)}))
assert len(EDGES) == 27
M = len(EDGES)
ADJ = [0] * N
for a, b in EDGES:
    ADJ[a] |= 1 << b
    ADJ[b] |= 1 << a
assert all(x.bit_count() == 3 for x in ADJ)

# Method A: first construct the distance-two conflict graph on edge indices.
CONFLICT = [0] * M
for i, (a,b) in enumerate(EDGES):
    for j, (c,d) in enumerate(EDGES):
        if i == j:
            continue
        if ((a == c or a == d or b == c or b == d) or
            (ADJ[a] & ((1<<c)|(1<<d))) or
            (ADJ[b] & ((1<<c)|(1<<d)))):
            CONFLICT[i] |= 1 << j
ALL = (1 << M) - 1
ALLOWED = [ALL & ~CONFLICT[j] & ~(1<<j) for j in range(M)]
FACES = []
def recurse(candidates, face):
    FACES.append(face)
    while candidates:
        bit = candidates & -candidates
        candidates ^= bit
        i = bit.bit_length() - 1
        recurse(candidates & ALLOWED[i], face | bit)
recurse(ALL, 0)
FACESET = set(FACES)
assert len(FACESET) == len(FACES)
assert len(FACESET) == 766

# Method B: independently enumerate all k-edge subsets with k<=5 and
# check the induced subgraph on their endpoints is exactly k isolated edges.
def independently_valid(index_tuple):
    endpoints = []
    for i in index_tuple:
        endpoints.extend(EDGES[i])
    if len(set(endpoints)) != 2 * len(index_tuple):
        return False
    return sum((ADJ[u] >> v) & 1 for u,v in combinations(endpoints, 2)) == len(index_tuple)
independent_faces = set()
for k in range(6):
    for selection in combinations(range(M), k):
        if independently_valid(selection):
            independent_faces.add(sum(1<<j for j in selection))
assert independent_faces == FACESET
assert Counter(x.bit_count() for x in FACES) == {0:1,1:27,2:189,3:387,4:135,5:27}
assert all(not independently_valid(x) for x in combinations(range(M), 6))

# A completely specified matching: stagewise first-available toggles in
# ascending edge-index order, leaving empty face UNMATCHED (ordinary complex).
unmatched = set(FACESET)
unmatched.discard(0)
PAIRS = []
for j in range(M):
    bit = 1 << j
    stage = []
    for low in sorted(unmatched):
        if not low & bit and (low | bit) in unmatched:
            stage.append((low, low | bit))
    for low, high in stage:
        if low in unmatched and high in unmatched:
            unmatched.remove(low)
            unmatched.remove(high)
            PAIRS.append((low,high))
# The stagewise matching above has one extra critical vertex compared with
# the reduced matching that also paired the empty simplex with that vertex.
assert len(PAIRS) == 324, len(PAIRS)
assert Counter(x.bit_count() for x in unmatched) == {1:1,3:116}
CRITICAL_VERTEX = next(x for x in unmatched if x.bit_count()==1)

# Directed Hasse graph: normal incidences point high->low; matched incidences
# point low->high. Kahn sort proves no closed gradient path anywhere.
matched_low = {a:b for a,b in PAIRS}
indegree = {f:0 for f in FACESET if f}
out = {f:[] for f in FACESET if f}
incidences = 0
for high in FACESET:
    if not high: continue
    remaining = high
    while remaining:
        bit = remaining & -remaining
        remaining ^= bit
        low = high ^ bit
        if low == 0: continue
        if matched_low.get(low) == high:
            source, target = low, high
        else:
            source, target = high, low
        out[source].append(target)
        indegree[target] += 1
        incidences += 1
q = deque(k for k,d in indegree.items() if d==0)
visited = 0
while q:
    u = q.popleft()
    visited += 1
    for v in out[u]:
        indegree[v] -= 1
        if indegree[v] == 0: q.append(v)
assert visited == len(FACESET) - 1
assert incidences == 2214, incidences

# Every graph automorphism is enumerated by a full constraint-preserving
# backtracking bijection on all 18 vertices (not just a list of generators).
image = [-1] * N
AUTOS = []
visited_search_nodes = 0
def all_autos(used, assigned):
    global visited_search_nodes
    visited_search_nodes += 1
    if assigned == N:
        AUTOS.append(tuple(image))
        return
    options = []
    for u in range(N):
        if image[u] >= 0: continue
        mapped_neighbors = (ADJ[u] & sum(1<<k for k in range(N) if image[k] >= 0)).bit_count()
        candidates = []
        for v in range(N):
            if used & (1<<v): continue
            if all(bool(ADJ[u] & (1<<k)) == bool(ADJ[v] & (1<<image[k]))
                   for k in range(N) if image[k]>=0):
                candidates.append(v)
        if not candidates: return
        options.append((-mapped_neighbors, len(candidates), u, candidates))
    options.sort()
    _,_,u,candidates=options[0]
    for v in candidates:
        image[u] = v
        all_autos(used | (1<<v), assigned+1)
        image[u] = -1
all_autos(0,0)
assert len(AUTOS) == 216 and len(set(AUTOS)) == 216
assert visited_search_nodes == 3529, visited_search_nodes

# Compute signed simplicial Lefschetz traces directly. Because reduced
# homology is entirely in dimension two, this equals the H_2 character.
edge_idx = {edge:j for j,edge in enumerate(EDGES)}
TRACES = Counter()
REFINED = Counter()
IDENTITY = tuple(range(N))
def compose(p,q): return tuple(p[q[i]] for i in range(N))
for p in AUTOS:
    induced = [edge_idx[tuple(sorted((p[a],p[b])))] for a,b in EDGES]
    assert len(set(induced)) == M
    # Augmented empty face has signed contribution -1.
    trace = -1
    for f in FACES:
        if not f: continue
        inds = [j for j in range(M) if f>>j & 1]
        images = [induced[j] for j in inds]
        if set(inds) != set(images):
            continue
        inversions = sum(images[i] > images[j]
                         for i in range(len(images)) for j in range(i+1,len(images)))
        orient_sign = -1 if inversions%2 else 1
        trace += (-1 if len(inds)%2==0 else 1) * orient_sign
    TRACES[trace] += 1
    order = 1
    r = p
    while r != IDENTITY:
        r = compose(r,p); order += 1
    REFINED[(order,trace)] += 1
assert TRACES == {116:1,8:2,5:12,2:12,-10:18,-1:36,0:135}, TRACES
assert sum(v*n for v,n in TRACES.items()) == 0
assert sum(TRACES.values()) == len(AUTOS)
assert REFINED == {
    (1,116):1, (2,-10):18, (2,0):27,
    (3,2):12, (3,5):12, (3,8):2,
    (4,0):18, (6,-1):36, (6,0):54, (12,0):36
}, REFINED
print('VERIFY_OK')
print('graph_vertices=18 graph_edges=27 graph_aut_order=216')
print('face_cardinality_vector=[1,27,189,387,135,27] total_faces=766')
print('matching_pairs=324 critical_vertex=1 critical_triangles=116')
print('Hasse_incidences=2214 topologically_sorted_nonempty_faces=765')
print('aut_search_nodes=3529')
print('trace_multiplicities='+repr(sorted(TRACES.items())))
print('order_trace_multiplicities='+repr(sorted(REFINED.items())))
print('invariant_dimension=0')
