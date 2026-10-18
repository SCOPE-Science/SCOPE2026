#!/usr/bin/env python3
"""Exact lattice/face verification for the five-leaf binary symmetric phylogenetic polytope.

Requires Python 3 and sympy. All geometric claims are over an arbitrary algebraically
closed field: lattice computations use exact integers, not floating point geometry.
"""
from itertools import combinations, combinations_with_replacement, product
from collections import Counter
from math import gcd, comb
from functools import reduce
from sympy import Matrix
from sympy.matrices.normalforms import hermite_normal_form

# Edge order: leaf edges 0,...,4; internal edges 5 (A--B), 6 (B--C).
triples = ((0, 1, 5), (2, 5, 6), (3, 4, 6))
verts = [tuple(v) for v in product(range(2), repeat=7)
         if all(sum(v[i] for i in tr) % 2 == 0 for tr in triples)]
assert len(verts) == 16
basis = hermite_normal_form(Matrix([list(v) for v in verts[1:]]).T)
assert abs(basis.det()) == 8
basis_inv = basis.inv()

# The four local tetrahedron inequalities: a+b-c>=0 (3 permutations),
# and 2-a-b-c>=0 at every interior vertex.
facets = []
for tr in triples:
    for m in range(4):
        a = [0]*7
        c = 0
        for j,e in enumerate(tr):
            a[e] = (-1 if j == m else 1) if m < 3 else -1
        if m == 3: c = 2
        evaluation = [sum(a[j]*v[j] for j in range(7))+c for v in verts]
        assert min(evaluation) == 0 and max(evaluation) > 0
        mask = sum(1<<i for i,z in enumerate(evaluation) if z == 0)
        assert sum(z == 0 for z in evaluation) == 12
        zero_verts = [verts[i] for i,z in enumerate(evaluation) if z == 0]
        assert Matrix([[u[j] - zero_verts[0][j] for j in range(7)] for u in zero_verts[1:]]).rank() == 6
        row = [int(z) for z in Matrix([a])*basis]
        g = reduce(gcd,(abs(z) for z in row),0)
        assert g > 0
        ray = tuple(z//g for z in row)
        facets.append((mask,ray))
assert len(set(mask for mask,_ in facets)) == 12

# Every face of the polytope is an intersection of facets. The closure below
# examines all 2^12 subsets without using any numerical polyhedral routines.
whole = (1 << 16)-1
faces = {whole}
for fm,_ in facets:
    faces |= {mask & fm for mask in tuple(faces)}
faces.discard(0)
assert len(faces) == 711

def dim_of(mask):
    v = [verts[i] for i in range(16) if mask & (1 << i)]
    return Matrix([[u[j]-v[0][j] for j in range(7)] for u in v[1:]]).rank()

def minor_gcd(rows, r):
    if r == 0: return 1
    g = 0
    for ix in combinations(range(7),r):
        g = gcd(g,abs(int(Matrix([[row[i] for i in ix] for row in rows]).det())))
    return g

info = {}
for mask in faces:
    dimension = dim_of(mask)
    active = tuple(i for i,(fm,_) in enumerate(facets) if mask & ~fm == 0)
    rays = [facets[i][1] for i in active]
    codim = 7-dimension
    assert Matrix(rays).rank() == codim
    smooth = len(rays) == codim and minor_gcd(rays,codim) == 1
    info[mask] = (dimension,active,smooth)

assert dict(Counter(dim for dim,_,_ in info.values())) == {
    0:16,1:80,2:180,3:216,4:148,5:58,6:12,7:1}
singular = {m for m,(_,_,smooth) in info.items() if not smooth}
maximal = {m for m in singular if not any(m != z and m & ~z == 0 for z in singular)}
assert len(maximal) == 4
assert all(info[m][0] == 4 for m in maximal)

# The four proposed components are the faces where one internal edge is fixed.
# They are all of dimension four; every other nonsmooth cone contains one of
# their 3-dimensional normal cones.
family = {(edge,bit): sum((1<<i) for i,v in enumerate(verts) if v[edge] == bit)
          for edge in (5,6) for bit in (0,1)}
assert set(family.values()) == maximal
assert all(m in faces and info[m][0] == 4 for m in family.values())
assert len(singular) == 16+48+52+24+4
assert all(any(m & ~z == 0 for z in maximal) for m in singular)

# Each generic transverse cone is a saturated four-ray rank-three cone with
# a primitive unit-square circuit, so its affine toric germ is ad-bc=0.
for m in maximal:
    rays = [facets[i][1] for i in info[m][1]]
    assert len(rays) == 4 and Matrix(rays).rank() == 3
    assert minor_gcd(rays[:3],3) == 1 or minor_gcd(rays[1:],3) == 1
    assert any(tuple(rays[a][j]+rays[b][j] for j in range(7)) ==
               tuple(rays[c][j]+rays[d][j] for j in range(7))
               for a,b in combinations(range(4),2)
               for c,d in [tuple(x for x in range(4) if x not in (a,b))])

# For each component: the coordinates split into an independent 0--1 coordinate
# and a tetrahedron of four binary-even vertices. Their primitive difference
# vectors generate the full rank-four lattice of the affine span, so the face
# is a unimodular Delta_1 x Delta_3, not merely a combinatorial product.
for (edge,bit),m in family.items():
    members = [v for i,v in enumerate(verts) if m >> i & 1]
    assert len(members) == 8
    seg = 0 if edge == 5 else 3
    tet = (3,4,6) if edge == 5 else (0,1,5)
    svals = {v[seg] for v in members}
    tvals = {tuple(v[i] for i in tet) for v in members}
    assert svals == {0,1} and len(tvals) == 4
    assert {(v[seg],tuple(v[i] for i in tet)) for v in members} == set(product(svals,tvals))
    base = next(v for v in members if v[seg] == 0 and tuple(v[i] for i in tet) == min(tvals))
    sother = next(v for v in members if v[seg] == 1 and tuple(v[i] for i in tet) == min(tvals))
    tothers = [next(v for v in members if v[seg] == 0 and tuple(v[i] for i in tet) == t)
               for t in sorted(tvals)[1:]]
    dirs = [list(basis_inv*Matrix([w[i]-base[i] for i in range(7)]))
            for w in [sother]+tothers]
    assert Matrix(dirs).rank() == 4 and minor_gcd(dirs,4) == 1

# Opposite faces are disjoint. Distinct internal-edge faces intersect in
# Delta_1 x Delta_1, giving four Segre quadrics with no triple intersections.
assert family[5,0] & family[5,1] == 0
assert family[6,0] & family[6,1] == 0
for b,c in product((0,1),repeat=2):
    m = family[5,b] & family[6,c]
    assert m in faces and info[m][0] == 2 and m.bit_count() == 4
    members = [verts[i] for i in range(16) if m & (1<<i)]
    assert {(v[0],v[3]) for v in members} == set(product((0,1),repeat=2))
    base = next(v for v in members if v[0] == v[3] == 0)
    a = next(v for v in members if v[0] == 1 and v[3] == 0)
    e = next(v for v in members if v[0] == 0 and v[3] == 1)
    z = next(v for v in members if v[0] == v[3] == 1)
    assert all(z[i]-base[i] == a[i]+e[i]-2*base[i] for i in range(7))
    dirs = [list(basis_inv*Matrix([w[i]-base[i] for i in range(7)])) for w in (a,e)]
    assert Matrix(dirs).rank() == 2 and minor_gcd(dirs,2) == 1

# Normality of Segre faces gives the degree-d Hilbert counts. For d>=1,
# inclusion-exclusion has four components and four pairwise intersection squares;
# degree zero contains a single unit monomial, not an empty virtual sum.
for d in range(1,4):
    S = set()
    for mask in maximal:
        members = [verts[i] for i in range(16) if mask & (1<<i)]
        for T in combinations_with_replacement(members,d):
            S.add(tuple(sum(v[j] for v in T) for j in range(7)))
    expected = 4*(d+1)*comb(d+3,3)-4*(d+1)**2
    assert len(S) == expected, (d,len(S),expected)
assert [4*(d+1)*comb(d+3,3)-4*(d+1)**2 for d in (1,2,3)] == [16,84,256]

print('VERIFY_OK')
print('vertices=16 facets=12 faces=711 f_vector=(16,80,180,216,148,58,12,1)')
print('singular_face_counts=(16,48,52,24,4); maximal_singular_components=4')
print('components=4 x Segre(P1 x P3), degree=16, pairwise_meetings=4 x Segre(P1 x P1)')
print('Hilbert_function_d0_to_d3=(1,16,84,256)')
print('Hilbert_series=1+4(1+3t)/(1-t)^5-4(1+t)/(1-t)^3')
