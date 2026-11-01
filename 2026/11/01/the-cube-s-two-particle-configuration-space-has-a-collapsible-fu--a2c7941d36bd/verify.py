#!/usr/bin/env python3
"""Exact certificate checker for a cube-graph two-configuration symmetry quotient.
Public mathematical computation; Python 3 standard library only.
"""
import itertools
import json
from pathlib import Path

V = tuple(range(8))
E = tuple((a, b) for a in V for b in V if a < b and (a ^ b).bit_count() == 1)
ei = {e: i for i, e in enumerate(E)}
C0 = tuple(itertools.combinations(V, 2))
C1 = tuple((v, i) for v in V for i, (a, b) in enumerate(E) if v not in (a, b))
C2 = tuple((i, j) for i, (a, b) in enumerate(E) for j, (c, d) in enumerate(E)
           if i < j and set((a, b)).isdisjoint((c, d)))
i0, i1, i2 = ({x: k for k, x in enumerate(S)} for S in (C0, C1, C2))
assert len(E) == 12 and (len(C0), len(C1), len(C2)) == (28, 72, 42)

# Cubical face poset; each tuple is a chain of pairs (cell dimension, cell index).
S0 = tuple(((d, i),) for d, cells in enumerate((C0, C1, C2)) for i in range(len(cells)))
S10 = tuple(((0, i0[tuple(sorted((v, w)))]), (1, j))
            for j, (v, e) in enumerate(C1) for w in E[e])
S21 = tuple(((1, i1[(v, e)]), (2, j))
            for j, (i, k) in enumerate(C2)
            for v, e in ((E[i][0], k), (E[i][1], k), (E[k][0], i), (E[k][1], i)))
S20 = tuple(((0, i0[tuple(sorted((v, w)))]), (2, j))
            for j, (i, k) in enumerate(C2) for v in E[i] for w in E[k])
S012 = tuple(((0, i0[tuple(sorted((v, w)))]), (1, i1[(v, e)]), (2, j))
             for j, (i, k) in enumerate(C2)
             for v, e in ((E[i][0], k), (E[i][1], k), (E[k][0], i), (E[k][1], i))
             for w in E[e])
SS = (S0, S10 + S21 + S20, S012)
assert tuple(map(len, SS)) == (142, 480, 336)
for group in SS:
    assert len(set(group)) == len(group)

# The 48 full graph automorphisms, each a signed permutation of three coordinates.
G = []
for perm in itertools.permutations(range(3)):
    for flip in range(8):
        gv = tuple(sum(((((v >> i) & 1) ^ ((flip >> perm[i]) & 1)) << perm[i])
                       for i in range(3)) for v in V)
        gm0 = tuple(i0[tuple(sorted((gv[a], gv[b])))] for a, b in C0)
        gm1 = tuple(i1[(gv[v], ei[tuple(sorted((gv[E[e][0]], gv[E[e][1]])))])]
                    for v, e in C1)
        gm2 = tuple(i2[tuple(sorted((ei[tuple(sorted((gv[E[i][0]], gv[E[i][1]])))],
                                       ei[tuple(sorted((gv[E[j][0]], gv[E[j][1]])))])))]
                    for i, j in C2)
        G.append((gm0, gm1, gm2))
assert len(G) == 48 and len({g[0] for g in G}) == 48
assert all(len(set(g[k])) == len((C0, C1, C2)[k]) for g in G for k in range(3))

def transform(g, simplex):
    return tuple((d, g[d][j]) for d, j in simplex)

orbits = []
for dim, simplices in enumerate(SS):
    allcells = set(simplices)
    assert all(transform(g, s) in allcells for g in G for s in simplices)
    canon = {s: min(transform(g, s) for g in G) for s in simplices}
    reps = tuple(sorted(set(canon.values())))
    orbit_id = {rep: j for j, rep in enumerate(reps)}
    orbits.append((canon, reps, orbit_id))
assert tuple(len(x[1]) for x in orbits) == (8, 15, 8)

edge_ends = []
for s in orbits[1][1]:
    edge_ends.append(tuple(orbits[0][2][orbits[0][0][(v,)]] for v in s))
triangle_edges = []
for s in orbits[2][1]:
    triangle_edges.append(tuple(orbits[1][2][orbits[1][0][s[:k] + s[k+1:]]]
                                for k in range(3)))

cert = json.loads((Path(__file__).with_name('certificate.json')).read_text('utf-8'))
assert cert['original_cubical_counts'] == [28, 72, 42]
assert cert['original_barycentric_counts'] == [142, 480, 336]
assert cert['quotient_counts'] == [8, 15, 8]
assert cert['quotient_vertex_representatives'] == [[list(v) for v in rep] for rep in orbits[0][1]]
assert cert['quotient_edge_endpoints'] == [list(e) for e in edge_ends]
assert cert['quotient_triangle_edges'] == [list(t) for t in triangle_edges]

# Check actual elementary collapses, requiring a free codimension-one face.
active_v, active_e, active_t = set(range(8)), set(range(15)), set(range(8))
for step in cert['collapses']:
    dim, high, low = step
    if dim == 2:
        assert high in active_t and low in active_e and low in triangle_edges[high]
        assert sum(low in triangle_edges[t] for t in active_t) == 1
        active_t.remove(high)
        active_e.remove(low)
    elif dim == 1:
        assert not active_t and high in active_e and low in active_v
        assert low in edge_ends[high]
        assert sum(low in edge_ends[e] for e in active_e) == 1
        active_e.remove(high)
        active_v.remove(low)
    else:
        raise AssertionError('Invalid collapse dimension')
assert len(cert['collapses']) == 15
assert len(active_t) == len(active_e) == 0 and len(active_v) == 1
assert next(iter(active_v)) == cert['remaining_vertex']
print('CUBE_CONFIG_QUOTIENT_VERIFY_OK')
print('group=48 original_cubical=28,72,42 barycentric=142,480,336 quotient=8,15,8')
print('elementary_collapses=15 remaining_vertex=' + str(cert['remaining_vertex']))
