"""Exact, standard-library certificate for minimum feedback vertex sets of a dodecahedron.
Run with Python 3.10+. No external data or dependencies.
"""
from collections import Counter, deque
from itertools import combinations

V = 20
EDGES = sorted({tuple(sorted(e)) for i in range(10) for e in
                [(i, (i + 1) % 10), (i, i + 10), (10 + i, 10 + (i + 2) % 10)]})
assert len(EDGES) == 30

def acyclic_after_deletion(deleted):
    parent = list(range(V))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for u, v in EDGES:
        if (deleted >> u) & 1 or (deleted >> v) & 1:
            continue
        ru, rv = find(u), find(v)
        if ru == rv:
            return False
        parent[ru] = rv
    return True

# Every FVS has >=6 vertices: removing k cubic vertices deletes at most 3k
# edges, while an acyclic remaining graph has at most 19-k edges.
FVS = sorted(sum(1 << v for v in c) for c in combinations(range(V), 6)
             if acyclic_after_deletion(sum(1 << v for v in c)))
assert len(FVS) == 2520
index = {m: i for i, m in enumerate(FVS)}
adj = []
for m in FVS:
    outside = [v for v in range(V) if not (m >> v) & 1]
    neighbors = set()
    for u in range(V):
        if (m >> u) & 1:
            for v in outside:
                j = index.get(m ^ (1 << u) ^ (1 << v))
                if j is not None:
                    neighbors.add(j)
    adj.append(neighbors)
assert all(i in adj[j] for i, neighborhood in enumerate(adj) for j in neighborhood)
assert sum(map(len, adj)) // 2 == 23940
DEGREE = {12:420, 16:600, 18:360, 21:120, 22:360,
          24:320, 25:240, 26:60, 27:40}
assert dict(Counter(map(len, adj))) == DEGREE

pair_table = Counter()
deviations = Counter()
exceptional = []
ecc = Counter()
for start in range(len(FVS)):
    ds = [-1] * len(FVS)
    ds[start] = 0
    q = deque([start])
    while q:
        i = q.popleft()
        for j in adj[i]:
            if ds[j] == -1:
                ds[j] = ds[i] + 1
                q.append(j)
    assert -1 not in ds
    ecc[max(ds)] += 1
    for j in range(start + 1, len(FVS)):
        intersection = (FVS[start] & FVS[j]).bit_count()
        distance = ds[j]
        pair_table[(intersection, distance)] += 1
        detour = distance - (6-intersection)
        assert 0 <= detour <= 2
        deviations[detour] += 1
        if detour == 2:
            exceptional.append((start, j))
EXPECTED_PAIRS = {(5,1):23940, (4,2):162870, (4,3):4410,
                  (3,3):567820, (3,4):20960, (3,5):60,
                  (2,4):1067430, (2,5):21510, (2,6):120,
                  (1,5):972420, (1,6):1920, (0,6):330480}
assert dict(pair_table) == EXPECTED_PAIRS
assert dict(deviations) == {0:3124960, 1:48800, 2:180}
assert dict(ecc) == {6:2520}
partner_counts = Counter(i for a,b in exceptional for i in (a,b))
assert len(partner_counts) == 360
assert set(partner_counts.values()) == {1}

# Three explicit graph automorphisms generate a group of 120.
GENERATORS = [
(0,1,11,13,15,5,6,16,18,10,9,2,19,3,17,4,7,14,8,12),
(0,9,19,17,15,5,4,14,12,10,1,8,11,7,13,6,3,16,2,18),
(1,0,10,18,16,6,5,15,13,11,2,9,12,8,14,7,4,17,3,19),
]
for gen in GENERATORS:
    assert sorted(gen) == list(range(V))
    assert {tuple(sorted((gen[u],gen[v]))) for u,v in EDGES} == set(EDGES)
identity = tuple(range(V))
group = {identity}
frontier = [identity]
while frontier:
    p = frontier.pop()
    for q in GENERATORS:
        r = tuple(p[q[i]] for i in range(V))
        if r not in group:
            group.add(r)
            frontier.append(r)
assert len(group) == 120

def transform(mask, permutation):
    return sum(1 << permutation[u] for u in range(V) if (mask >> u) & 1)
exceptional_set = set(exceptional)
remaining = set(exceptional)
orbit_sizes = []
while remaining:
    i,j = min(remaining)
    images = set()
    for perm in group:
        a = index[transform(FVS[i], perm)]
        b = index[transform(FVS[j], perm)]
        images.add((min(a,b), max(a,b)))
    assert images <= exceptional_set
    orbit_sizes.append(len(images))
    remaining -= images
assert sorted(orbit_sizes) == [60,60,60]
# Explicit orbital representatives in GP(10,2) vertex numbering.
REPRESENTATIVES = [
    ((0,1,3,5,16,17),(0,1,5,7,13,14)),
    ((0,1,3,7,14,19),(0,1,4,8,12,17)),
    ((0,1,3,8,14,17),(0,1,4,7,12,19)),
]
rep_orbits=[]
for aa,bb in REPRESENTATIVES:
    a=sum(1<<v for v in aa); b=sum(1<<v for v in bb)
    assert a in index and b in index
    orbit=set()
    for perm in group:
        x=index[transform(a,perm)]; y=index[transform(b,perm)]
        orbit.add((min(x,y), max(x,y)))
    assert len(orbit)==60 and orbit<=exceptional_set
    rep_orbits.append(orbit)
assert len(set.union(*rep_orbits))==180
# Every exceptional pair shares exactly one original dodecahedral edge.
for i,j in exceptional:
    shared = FVS[i] & FVS[j]
    assert sum(bool((shared>>u)&1 and (shared>>v)&1) for u,v in EDGES) == 1
# Edge-local refinement: exactly 2 exceptional pairs with triple overlap and 4 with double overlap per original edge.
by_original_edge = Counter()
for i,j in exceptional:
    common = FVS[i] & FVS[j]
    common_edge = next((u,v) for u,v in EDGES if common>>u&1 and common>>v&1)
    by_original_edge[common_edge,common.bit_count()] += 1
assert all(by_original_edge[e,2]==4 and by_original_edge[e,3]==2 for e in EDGES)
print('DIRECT_DODECAHEDRAL_FVS_ALL_PAIRS_AND_ORBITS_PASS')
print('FVS=2520; edges=23940; diameter=radius=6; detours=0:3124960,1:48800,2:180; orbits=60+60+60')
