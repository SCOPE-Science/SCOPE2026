#!/usr/bin/env python3
"""Exact finite verification for the strong Morse complex of the unfilled triangular prism.

Requires Python 3.9 or later; no third-party packages. All loops have explicit finite
bounds. The same complex is reconstructed from total orders and from symmetry orbits.
"""
from collections import Counter, defaultdict, deque
from itertools import permutations, combinations

V = tuple(range(6))
E = frozenset(tuple(sorted(e)) for e in
              [(0,1),(1,2),(2,0),(3,4),(4,5),(5,3),(0,3),(1,4),(2,5)])
assert len(E) == 9
arcs = tuple(sorted((u,v) for a,b in E for u,v in [(a,b),(b,a)]))
assert len(arcs) == 18
ix = {a:i for i,a in enumerate(arcs)}

def bitset(items):
    return sum(1 << i for i in items)

def submasks(mask):
    sub = mask
    while True:
        yield sub
        if sub == 0:
            return
        sub = (sub-1) & mask

def directed_mask(arclist):
    return bitset(ix[a] for a in arclist)

# The induced link of a vertex in a one-dimensional graph is discrete; it is
# a simplicial cone precisely when it consists of one earlier neighbor.
matchings = set()
for order in permutations(V):
    earlier = set()
    selected = []
    for v in order:
        neighbors = [u for u in earlier if tuple(sorted((u,v))) in E]
        if len(neighbors) == 1:
            selected.append((v,neighbors[0]))
        earlier.add(v)
    matchings.add(directed_mask(selected))
assert len(matchings) == 85
facets = {m for m in matchings if not any(m != n and (m & n) == m for n in matchings)}
assert len(facets) == 36
faces = {x for m in facets for x in submasks(m)}
assert len(faces) == 109
by_dim = {i:sorted(m for m in faces if m.bit_count() == i+1) for i in range(3)}
assert tuple(len(by_dim[i]) for i in range(3)) == (18,66,24)
assert Counter(x.bit_count() for x in facets) == {2:12, 3:24}
assert all(x.bit_count() <= 3 for x in faces)

# Independently generate every facet as an orbit of one of three representatives
# under the full prism automorphism group S_3 x C_2.
rep_data = [
    (directed_mask([(1,2),(3,0)]), 12),
    (directed_mask([(0,3),(2,0),(3,4)]), 12),
    (directed_mask([(1,4),(2,1),(3,4)]), 12),
]
group = []
for layer_swap in (0,1):
    for p in permutations(range(3)):
        onv = tuple(p[i % 3] + 3 * ((i // 3) ^ layer_swap) for i in V)
        onarc = tuple(ix[(onv[u],onv[v])] for u,v in arcs)
        assert len(set(onarc)) == 18
        group.append((p,layer_swap,onarc))
assert len(group) == 12

def image(mask, onarc):
    return bitset(onarc[i] for i in range(18) if (mask >> i) & 1)

orbits = []
for rep,sz in rep_data:
    orbit = {image(rep,g[2]) for g in group}
    assert len(orbit) == sz
    orbits.append(orbit)
assert not (orbits[0] & orbits[1] or orbits[0] & orbits[2] or orbits[1] & orbits[2])
assert set().union(*orbits) == facets
for _,_,onarc in group:
    assert all(image(m,onarc) in faces for m in faces)

# Every two-simplex possesses an edge contained in no other two-simplex.
triangles = by_dim[2]
edges = set(by_dim[1])
incidence = defaultdict(list)
for tri in triangles:
    for i in range(18):
        if (tri >> i) & 1:
            incidence[tri ^ (1 << i)].append(tri)
free_map = {}
for tri in triangles:
    free = sorted(e for e in incidence if tri in incidence[e] and len(incidence[e]) == 1)
    assert free
    free_map[tri] = free[0]
assert len(set(free_map.values())) == 24
# Verify the full elementary-collapse sequence, including free-face condition.
current = set(faces)
for tri in triangles:
    edge = free_map[tri]
    assert tri in current and edge in current
    assert [f for f in current if f != edge and (edge & f) == edge] == [tri]
    current.remove(tri)
    current.remove(edge)
assert len(current) == 61
assert all(x.bit_count() <= 2 for x in current)
assert {x for x in current if x.bit_count() == 1} == set(by_dim[0])
spine_edges = [x for x in current if x.bit_count() == 2]
assert len(spine_edges) == 42
neighbors = defaultdict(set)
for e in spine_edges:
    a,b = [i for i in range(18) if (e >> i) & 1]
    neighbors[a].add(b)
    neighbors[b].add(a)
seen = {0}
queue = deque([0])
while queue:
    for j in neighbors[queue.popleft()]:
        if j not in seen:
            seen.add(j)
            queue.append(j)
assert len(seen) == 18
assert 42 - 18 + 1 == 25

# Equivariant alternating Lefschetz formula computes the H_1 character from
# signed chain-fixed-simplex traces, without selecting an equivariant collapse.
def permutation_sign(values):
    inversions = sum(values[i] > values[j] for i in range(len(values))
                     for j in range(i+1,len(values)))
    return 1 if inversions % 2 == 0 else -1

def ch_chain(faces_of_dimension,onarc):
    total = 0
    for face in faces_of_dimension:
        mapped = [onarc[i] for i in range(18) if (face >> i) & 1]
        if set(mapped) == {i for i in range(18) if (face >> i) & 1}:
            total += permutation_sign(mapped)
    return total

class_traces = {}
for p,s,onarc in group:
    kind = ('id' if p == (0,1,2) else
            'transposition' if sum(p[i] != i for i in range(3)) == 2 else
            'three_cycle')
    c = tuple(ch_chain(by_dim[d],onarc) for d in range(3))
    h1 = 1-c[0]+c[1]-c[2]
    sign_p = permutation_sign(p)
    predicted = (24 if kind == 'id' and s == 0 else 0) + sign_p
    assert h1 == predicted
    key = (kind,s)
    if key in class_traces:
        assert class_traces[key] == (c,h1)
    class_traces[key] = (c,h1)
assert class_traces == {
    ('id',0):((18,66,24),25),
    ('transposition',0):((2,0,0),-1),
    ('three_cycle',0):((0,0,0),1),
    ('id',1):((0,0,0),1),
    ('transposition',1):((0,-2,0),-1),
    ('three_cycle',1):((0,0,0),1),
}
print('VERIFY_OK orders=720 matches=85 facets=36 face_counts=(18,66,24)')
print('VERIFY_OK free_edge_collapses=24 spine=(18,42) rank_H1=25')
print('VERIFY_OK equivariant_character=two_regular_plus_S3_sign')
