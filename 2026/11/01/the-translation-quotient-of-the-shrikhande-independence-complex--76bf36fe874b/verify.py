#!/usr/bin/env python3
"""Exact orbit-cell and elementary-collapse verification for a finite graph complex.

Run: python3 verify.py
Requires only the Python standard library; reads certificate.json beside this script.
"""
from collections import defaultdict
from itertools import combinations, product
from pathlib import Path
import json

V = [(i, j) for i in range(4) for j in range(4)]
S = {(1, 0), (3, 0), (0, 1), (0, 3), (1, 1), (3, 3)}
TRANS = [tuple(4*((i+a)%4)+((j+b)%4) for i,j in V)
         for a in range(4) for b in range(4)]

def adjacent(x, y):
    a, b = V[x]; c, d = V[y]
    return ((a-c) % 4, (b-d) % 4) in S

def mask(vertices):
    return sum(1 << i for i in vertices)

def translate(s, g):
    return sum(1 << g[i] for i in range(16) if (s >> i) & 1)

def canonical(chain):
    return min(tuple(translate(s,g) for s in chain) for g in TRANS)

faces = []
face_counts = []
for k in range(1, 17):
    current = [mask(c) for c in combinations(range(16), k)
               if all(not adjacent(i, j) for i, j in combinations(c, 2))]
    if not current:
        break
    faces.extend(current)
    face_counts.append(len(current))
assert face_counts == [16,72,96,16], face_counts

orbits = [set() for _ in range(4)]
for s in faces:
    vertices = [i for i in range(16) if (s >> i) & 1]
    k = len(vertices)
    for r in range(1, k + 1):
        for word in product(range(r), repeat=k):
            if set(word) != set(range(r)):
                continue
            subchain = []
            cumulative = 0
            for z in range(r):
                cumulative |= mask(vertices[i] for i in range(k) if word[i] == z)
                subchain.append(cumulative)
            orbits[r-1].add(canonical(tuple(subchain)))
orbits = [sorted(x) for x in orbits]
assert tuple(map(len, orbits)) == (17,62,72,24)
index = [{x:i for i,x in enumerate(lst)} for lst in orbits]

def boundary_cell(c, z):
    return index[len(c)-2][canonical(c[:z] + c[z+1:])]

# Each top-dimensional cell's four codimension-one faces are distinct in orbit.
incidence = defaultdict(list)
for c_id, c in enumerate(orbits[3]):
    fs = [boundary_cell(c, z) for z in range(4)]
    assert len(set(fs)) == 4
    for f_id in fs:
        incidence[f_id].append(c_id)

cert = json.loads(Path(__file__).with_name('certificate.json').read_text(encoding='utf-8'))
pairs = cert['free_face_pairs']
assert len(pairs) == 24 and len(set(tuple(x) for x in pairs)) == 24
remaining3 = set(range(len(orbits[3])))
removed2 = set()
for face_id, cell_id in pairs:
    assert face_id not in removed2 and cell_id in remaining3
    cofaces = [t for t in incidence[face_id] if t in remaining3]
    assert cofaces == [cell_id], (face_id, cell_id, cofaces)
    removed2.add(face_id)
    remaining3.remove(cell_id)
assert not remaining3 and len(removed2) == 24

# Cells are orbits of barycentric flags. All flag vertices have different
# cardinalities, so no nontrivial group element can identify points inside
# the closure of one flag simplex. Thus the quotient is a regular CW complex.
endpoints = []
for c in orbits[1]:
    u = index[0][canonical((c[0],))]
    v = index[0][canonical((c[1],))]
    assert u != v
    endpoints.append((u,v))
assert len(endpoints) == 62

# A spanning tree contracts the 1-skeleton without changing pi_1.
tree = cert['spanning_tree_edges']
assert len(tree) == 16 and len(set(tree)) == 16
parent = list(range(17))
def root(x):
    while parent[x] != x:
        x = parent[x]
    return x
for edge_id in tree:
    u,v = endpoints[edge_id]
    a,b = root(u),root(v)
    assert a != b
    parent[a] = b
assert len({root(u) for u in range(17)}) == 1

# Every remaining edge becomes trivial through a displayed triangular
# 2-cell whose two other edges are already trivial.
known = set(tree)
assert len(cert['triangle_propagation']) == 46
for tri_id, edge_id in cert['triangle_propagation']:
    assert tri_id not in removed2
    c = orbits[2][tri_id]
    boundary_edges = [boundary_cell(c, z) for z in range(3)]
    assert len(set(boundary_edges)) == 3
    unknown = [e for e in boundary_edges if e not in known]
    assert unknown == [edge_id], (tri_id,edge_id,unknown)
    known.add(edge_id)
assert known == set(range(62))

# After 24 regular elementary collapses, Euler characteristic is
# 17 - 62 + 48 = 3. The connected 2-complex is simply connected,
# hence H_2 is Z^2 and it has the homotopy type of S^2 vee S^2.
assert (len(orbits[0]),len(orbits[1]),len(orbits[2])-len(removed2)) == (17,62,48)
assert 17-62+48 == 3
print('ORIGINAL_F_VECTOR 16 72 96 16')
print('ORBIT_FLAG_CELLS 17 62 72 24')
print('REGULAR_FREE_COLLAPSES 24')
print('SPANNING_TREE_EDGES 16')
print('TRIANGULAR_RELATOR_ELIMINATIONS 46')
print('REMAINING_2_COMPLEX 17 62 48')
print('EULER_CHARACTERISTIC 3')
print('PI1_TRIVIAL; HOMOTOPY_TYPE WEDGE_OF_2_TWO_SPHERES')
print('VERIFY_OK')
