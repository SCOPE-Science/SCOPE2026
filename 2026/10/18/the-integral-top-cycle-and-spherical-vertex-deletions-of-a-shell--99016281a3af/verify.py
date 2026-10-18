#!/usr/bin/env python3
"""Exact, dependency-free verification of a top-dimensional cycle and local topology
in the independence complex of the circulant graph C16(1,4,8).
Run in the directory containing deletion_collapse.json and link_spheres.json.
"""
import collections
import itertools
import json
from pathlib import Path

N = 16
STEPS = {1, 4, 8}

def adjacent(a, b):
    return min((a - b) % N, (b - a) % N) in STEPS

faces_by_dim = {}
for k in range(1, 5):
    faces_by_dim[k-1] = [t for t in itertools.combinations(range(N), k)
                          if all(not adjacent(a, b) for a, b in itertools.combinations(t, 2))]
assert [len(faces_by_dim[i]) for i in range(4)] == [16, 80, 144, 80]
faces = set().union(*map(set, faces_by_dim.values()))
triangles = faces_by_dim[2]
tetrahedra = faces_by_dim[3]

# The four dihedral orbits carry canonical signs induced by ordered orientations.
seeds = [(0, 2, 5, 7), (0, 2, 5, 11), (0, 2, 7, 9), (0, 3, 6, 9)]
weights = [1, -1, 2, 1]

def ordered_sign(seq):
    return -1 if sum(a > b for i, a in enumerate(seq)
                     for b in seq[i+1:]) % 2 else 1

def transform(t, eps, k):
    im = [(eps*x+k) % N for x in t]
    return tuple(sorted(im)), ordered_sign(im)

cycle = {}
orbit_sizes = []
for seed, weight in zip(seeds, weights):
    orb = {}
    for eps in (1, -1):
        for k in range(N):
            face, sign = transform(seed, eps, k)
            assert face in tetrahedra
            coefficient = weight*sign
            if face in orb:
                assert orb[face] == coefficient, 'orientation-reversing stabilizer'
            orb[face] = coefficient
    assert not cycle.keys() & orb.keys()
    cycle.update(orb)
    orbit_sizes.append(len(orb))
assert orbit_sizes == [16, 32, 16, 16]
assert set(cycle) == set(tetrahedra)
assert collections.Counter(map(abs, cycle.values())) == {1: 64, 2: 16}
assert sum(map(abs, cycle.values())) == 96

# Check the integral simplicial boundary, not just its reduction modulo 2.
boundary = collections.Counter()
for facet, coeff in cycle.items():
    for j in range(4):
        boundary[facet[:j] + facet[j+1:]] += coeff*(-1)**j
assert all(value == 0 for value in boundary.values())

# A 79-dimensional image modulo 2 and the explicit nonzero kernel vector
# imply rank 79 over Q.  The gcd-one integral vector spans the Z-kernel.
index = {tet: j for j, tet in enumerate(tetrahedra)}
rows = [0] * len(triangles)
tindex = {tri: i for i, tri in enumerate(triangles)}
for tet, col in index.items():
    for j in range(4):
        rows[tindex[tet[:j]+tet[j+1:]]] ^= 1 << col
pivots = {}
for row in rows:
    while row:
        pivot = row.bit_length()-1
        if pivot in pivots:
            row ^= pivots[pivot]
        else:
            pivots[pivot] = row
            break
assert len(pivots) == 79
assert sum(abs(c) % 2 for c in cycle.values()) == 64
for eps, k in ((1, 1), (-1, 0)):
    mapped = {}
    for facet, coeff in cycle.items():
        target, sign = transform(facet, eps, k)
        mapped[target] = coeff*sign
    assert mapped == cycle

# Verify all 106 elementary simplicial collapses of a one-vertex deletion.
with open(Path(__file__).with_name('deletion_collapse.json'), encoding='utf-8') as fh:
    cert = json.load(fh)
assert cert['deleted_vertex'] == 0 and cert['graph'] == 'C16(1,4,8)'
remaining = {f for f in faces if 0 not in f}
assert collections.Counter(map(len, remaining)) == {1:15, 2:70, 3:117, 4:60}
assert len(cert['pairs']) == 106
for raw_sigma, raw_tau in cert['pairs']:
    sigma, tau = tuple(raw_sigma), tuple(raw_tau)
    assert sigma in remaining and tau in remaining
    assert len(sigma)+1 == len(tau) and set(sigma) < set(tau)
    supersets = [f for f in remaining if set(sigma) < set(f)]
    assert supersets == [tau], f'not a free face: {sigma}, {supersets}'
    remaining.remove(sigma)
    remaining.remove(tau)
assert collections.Counter(map(len, remaining)) == {1:10, 2:24, 3:16}

def assert_triangulated_sphere(triangle_collection):
    tris = set(map(tuple, triangle_collection))
    vertices = {x for tri in tris for x in tri}
    edges = {e for tri in tris for e in itertools.combinations(tri, 2)}
    edge_degrees = collections.Counter(e for t in tris for e in itertools.combinations(t, 2))
    assert all(v == 2 for v in edge_degrees.values())
    for vertex in vertices:
        graph = collections.defaultdict(set)
        for tri in tris:
            if vertex not in tri:
                continue
            a, b = [x for x in tri if x != vertex]
            graph[a].add(b)
            graph[b].add(a)
        assert all(len(neighbors) == 2 for neighbors in graph.values())
        seen = {next(iter(graph))}
        stack = list(seen)
        while stack:
            for nxt in graph[stack.pop()]:
                if nxt not in seen:
                    seen.add(nxt)
                    stack.append(nxt)
        assert seen == set(graph)
    # Verify the entire surface is connected, not merely all local links.
    graph1 = collections.defaultdict(set)
    for a, b in edges:
        graph1[a].add(b); graph1[b].add(a)
    seen1={next(iter(vertices))}; queue=list(seen1)
    while queue:
        for nxt in graph1[queue.pop()]:
            if nxt not in seen1:
                seen1.add(nxt);queue.append(nxt)
    assert seen1 == vertices
    assert len(vertices) - len(edges) + len(tris) == 2
    return (len(vertices), len(edges), len(tris))

assert assert_triangulated_sphere(f for f in remaining if len(f)==3) == (10, 24, 16)

# Construct the link as the independence complex on the non-neighbors of zero.
link_vertices = {v for v in range(N) if v != 0 and not adjacent(0, v)}
link = {f for f in faces if set(f) <= link_vertices}
assert collections.Counter(map(len, link)) == {1:10, 2:27, 3:20}
with open(Path(__file__).with_name('link_spheres.json'), encoding='utf-8') as fh:
    sphere_cert = json.load(fh)
assert sphere_cert['deleted_vertex'] == 0
A = {tuple(t) for t in sphere_cert['sphere_A_triangles']}
B = {tuple(t) for t in sphere_cert['sphere_B_triangles']}
assert A | B == {t for t in link if len(t) == 3}
assert assert_triangulated_sphere(A) == (10, 24, 16)
assert assert_triangulated_sphere(B) == (6, 12, 8)

def downclosure(tris):
    return {t for f in tris for k in (1,2,3) for t in itertools.combinations(f,k)}
assert downclosure(A) | downclosure(B) == link
intersection = downclosure(A) & downclosure(B)
assert collections.Counter(map(len, intersection)) == {1:6,2:9,3:4}
# A simplicial 2-disk: collapse all its faces to one vertex.
D = set(intersection)
while len(D) > 1:
    move = None
    for tau in sorted(D, key=lambda f: (-len(f), f)):
        if len(tau) < 2:
            continue
        for j in range(len(tau)):
            sigma = tau[:j] + tau[j+1:]
            if sigma in D and not any(set(sigma)<set(f) and f != tau for f in D):
                move=(sigma,tau)
                break
        if move:
            break
    assert move is not None, 'the intersection did not collapse'
    D.difference_update(move)
assert len(D)==1 and len(next(iter(D)))==1

# Rotations act transitively on the sixteen vertices, preserving all data.
print('VERIFY_OK C16_1_4_8 F_VECTOR_16_80_144_80')
print('BOUNDARY_RANK_MOD2_79 INTEGRAL_CYCLE_PRIMITIVE UNIQUE')
print('FACET_ORBITS_16_32_16_16 COEFFICIENTS_64_UNITS_16_DOUBLES L1_96')
print('DIHEDRAL_INVARIANT ALL_VERTICES_AND_FACETS_ESSENTIAL')
print('DELETION_106_COLLAPSE_PAIRS TO_SPHERE_10_24_16')
print('LINK_WEDGE_TWO_SPHERES INTERSECTION_FOUR_TRIANGLE_DISK')
