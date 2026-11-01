#!/usr/bin/env python3
"""Independent incidence-geometric certificate for Heawood locating-dominating reconfiguration.

Points are nonzero three-bit vectors, lines are nonzero normals, and
incidence is the vanishing of the binary dot product.  All 168 invertible
binary linear maps and incidence duality generate 336 permutations.
Shortest paths are checked from every symmetry-orbit representative.
"""
from collections import Counter, defaultdict
from itertools import combinations

POINTS = range(1,8)
VERTICES = range(14)

# Vertex indices 0..6 are point vectors 1..7; 7..13 are line normals 1..7.
def parity(a): return a.bit_count() & 1
adj = [set() for _ in VERTICES]
for p in POINTS:
    for l in POINTS:
        if parity(p & l) == 0:
            adj[p-1].add(l+6)
            adj[l+6].add(p-1)
assert sum(map(len,adj)) == 42
assert all(len(x)==3 for x in adj)

def feasible(combo):
    chosen = set(combo)
    signatures = [frozenset(adj[v] & chosen) for v in VERTICES if v not in chosen]
    return all(signatures) and len(set(signatures)) == len(signatures)

# Independent enumeration: finite set combinations rather than masks.
for k in range(6):
    assert not any(feasible(t) for t in combinations(VERTICES,k))
states = {frozenset(c) for c in combinations(VERTICES,6) if feasible(c)}
assert len(states)==448

# Linear maps determined by the images of the three independent unit vectors.
def independent(a,b,c):
    return len({0,a,b,c,a^b,a^c,b^c,a^b^c})==8

def linear_image(x, basis):
    return (basis[0] if x&1 else 0) ^ (basis[1] if x&2 else 0) ^ (basis[2] if x&4 else 0)

maps = []
for a in POINTS:
  for b in POINTS:
   for c in POINTS:
    if not independent(a,b,c): continue
    basis=(a,b,c)
    pointmap={p:linear_image(p,basis) for p in POINTS}
    linemap={}
    for l in POINTS:
        image_points={pointmap[p] for p in POINTS if parity(p & l)==0}
        matches=[z for z in POINTS if {p for p in POINTS if parity(p & z)==0} == image_points]
        assert len(matches)==1
        linemap[l]=matches[0]
    perm=tuple([pointmap[p]-1 for p in POINTS]+[linemap[l]+6 for l in POINTS])
    assert set(perm)==set(VERTICES)
    assert all((v in adj[u])==(perm[v] in adj[perm[u]]) for u in VERTICES for v in VERTICES)
    maps.append(perm)
assert len(set(maps)) == 168
# Incidence duality p <-> line p preserves all edges.
duality=tuple([v+7 if v<7 else v-7 for v in VERTICES])
permutations=set(maps)
permutations.update(tuple(duality[perm[v]] for v in VERTICES) for perm in maps)
assert len(permutations)==336
assert all((v in adj[u])==(perm[v] in adj[perm[u]]) for perm in permutations for u in VERTICES for v in VERTICES)

def transform(s,perm): return frozenset(perm[v] for v in s)
remaining=set(states)
orbits=[]
while remaining:
    s=min(remaining,key=lambda t:tuple(sorted(t)))
    orbit={transform(s,perm) for perm in permutations}
    assert orbit <= states
    remaining -= orbit
    orbits.append((s,orbit))
assert sorted(len(o) for _,o in orbits)==[28,84,168,168]

neighbors={}
for s in states:
    neighbors[s] = {frozenset((s-{u})|{v}) for u in s for v in set(VERTICES)-s if frozenset((s-{u})|{v}) in states}
assert sum(len(v) for v in neighbors.values())//2 ==3192

# This local signature describes the four orbit types without depending on
# a labeling of the Fano plane.
def signature(s):
    p = sum(v<7 for v in s)
    local = tuple(sorted(len(adj[v] & s) for v in s))
    if local == (0,0,1,1,1,1):
        return '2K2+2K1,points={}'.format(p)
    if local == (1,1,1,1,1,1):
        return '3K2,points={}'.format(p)
    if local == (0,0,1,1,2,2):
        return 'P4+2K1,points={}'.format(p)
    raise AssertionError((p,local))

orbit_summary=[]
weighted_dist=Counter()
weighted_extra=Counter()
weighted_exception_lengths=Counter()
for representative,orbit in orbits:
    source=representative
    d={source:0}
    queue=[source]
    for u in queue:
        for v in neighbors[u]:
            if v not in d:
                d[v]=d[u]+1
                queue.append(v)
    assert len(d)==448 and max(d.values())==6
    # Every member of an orbit has the same distance distribution.
    distances=Counter(d.values())
    assert len({len(neighbors[t]) for t in orbit})==1
    assert len({tuple(sorted(len(adj[v]&t) for v in t)) for t in orbit})==1
    for target,dd in d.items():
        lower=6-len(source & target)
        extra=dd-lower
        assert extra in {0,1}
        weighted_dist[dd] += len(orbit)
        weighted_extra[extra] += len(orbit)
        if extra:weighted_exception_lengths[lower]+=len(orbit)
    type_label=sorted({signature(t) for t in orbit})
    orbit_summary.append((len(orbit),len(neighbors[source]),distances,type_label))

# Ordered-pair totals divided by two give unordered pairs; 448 diagonal
# pairs (all with distance zero) are removed before division.
assert weighted_dist[0]==448
weighted_dist[0]-=448
assert all(n%2==0 for n in weighted_dist.values())
assert all(n%2==0 for n in weighted_exception_lengths.values())
assert {d:n//2 for d,n in weighted_dist.items() if d} == {1:3192,2:15204,3:32508,4:32298,5:14868,6:2058}
assert {d:n//2 for d,n in weighted_exception_lengths.items()} == {2:1008,3:1428,4:504}
assert weighted_extra[1]//2 == 2940
assert weighted_extra[0] == 2*97188 + 448
assert sorted((o,d) for o,d,_,_ in orbit_summary)==[(28,6),(84,22),(168,12),(168,14)]
print('FANO_GL3_SYMMETRY_CERTIFICATE_PASS')
for sz,degree,dists,types in sorted(orbit_summary):
    print('orbit size',sz,'degree',degree,'distances',tuple(dists[k] for k in range(7)),'type',types)
print('pairs', sorted((d,n//2) for d,n in weighted_dist.items() if d))
print('extra-move pairs',weighted_extra[1]//2)
