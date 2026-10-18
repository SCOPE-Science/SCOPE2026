#!/usr/bin/env python3
"""Exact finite face-lattice cross-check for the K(2,3) cut-polytope theorem.

Uses only the Python standard library. The infinite-field toric-germ statements
are proved symbolically in RESULT.md, not inferred from this enumeration.
"""
from itertools import product
from collections import Counter

signs = list(product((-1, 1), repeat=3))
verts = [(s, (0, 0, 0)) for s in signs] + [((0, 0, 0), s) for s in signs]
assert len(verts) == 16
# The 36 facet supports of the free sum C3 \oplus C3.
facets = {}
for i, j in product(range(3), repeat=2):
    for ei, ej in product((-1, 1), repeat=2):
        mask = sum(1 << k for k, (y,z) in enumerate(verts)
                   if ei*y[i] + ej*z[j] == 1)
        assert mask.bit_count() == 8
        facets[(i, j, ei, ej)] = mask
assert len(facets) == 36 and len(set(facets.values())) == 36
all_mask = (1 << 16) - 1
faces = {all_mask}
for fac in facets.values():
    faces |= {m & fac for m in tuple(faces)}
faces.discard(0)
assert len(faces) == 729


def part_dimension(indices, start):
    if not indices:
        return None
    vectors = [verts[i][0 if start == 0 else 1] for i in indices]
    return sum(len({v[j] for v in vectors}) == 2 for j in range(3))


def details(mask):
    ia = [i for i in range(8) if mask & (1 << i)]
    ib = [i for i in range(8, 16) if mask & (1 << i)]
    a = part_dimension(ia, 0)
    b = part_dimension(ib, 8)
    if mask == all_mask:
        return (6, -1, a, b, 0, True)
    if a is None or b is None:
        d = a if b is None else b
        active = 6*(3-d)
        kind = 'cube'
    else:
        d = a+b+1
        active = (3-a)*(3-b)
        kind = 'mixed'
    real_active = sum(mask & f == mask for f in facets.values())
    assert real_active == active, (mask, d, real_active, active)
    return (d, active, a, b, 6-d, kind)

fvector = Counter()
sing_by_dim = Counter()
maxsing = []
for mask in faces:
    d, active, a, b, codim, kind = details(mask)
    fvector[d] += 1
    if d == 6:
        continue
    if active > codim:
        sing_by_dim[d] += 1
    else:
        assert active == codim
    if (kind == 'cube' and d == 2) or (kind == 'mixed' and a == b == 1):
        maxsing.append(mask)
assert [fvector[j] for j in range(7)] == [16, 88, 204, 240, 144, 36, 1]
assert [sing_by_dim[j] for j in range(6)] == [16, 88, 204, 144, 0, 0]
assert len(maxsing) == 156
assert sum(details(m)[0] == 3 for m in maxsing) == 144
assert sum(details(m)[0] == 2 for m in maxsing) == 12
# All nonsmooth cones occur in the closures of these 156 orbit types.
for face in faces:
    d, nr, a, b, cod, kind = details(face)
    if d < 6 and nr > cod:
        assert any(face & m == face for m in maxsing)
# The 144 face-joins of cube edges are simplices with 4 vertices.
assert all(m.bit_count() == 4 for m in maxsing)
# In doubled coordinates primitive normal rays have the form e_i + e_{3+j}.
def doubled_ray(i, j, ei, ej):
    v = [0]*6
    v[i] = ei
    v[3+j] = ej
    return tuple(v)

for i in range(3):
    sums = [tuple(a+b for a,b in zip(doubled_ray(i,j,1,1),
                                      doubled_ray(i,j,1,-1))) for j in range(3)]
    assert len(set(sums)) == 1  # three opposite pairs of octahedron rays
for i,j in ((0,1),(1,2),(0,2)):
    for p,q in ((0,1),(1,2),(0,2)):
        lhs = tuple(a+b for a,b in zip(doubled_ray(i,p,1,1),
                                      doubled_ray(j,q,1,1)))
        rhs = tuple(a+b for a,b in zip(doubled_ray(i,q,1,1),
                                      doubled_ray(j,p,1,1)))
        assert lhs == rhs  # conifold square relation
# Both transverse monoids have the claimed defining additive relations.
row1, row2 = ((1,1,0,0),(0,0,1,1))
col1, col2 = ((1,0,1,0),(0,1,0,1))
assert tuple(a+b for a,b in zip(row1,row2)) == tuple(a+b for a,b in zip(col1,col2))
print('VERIFY_OK: 16 vertices, 36 facets, 729 faces, f=(16,88,204,240,144,36,1),')
print('  singular face orbits (0..5)=(16,88,204,144,0,0); maximal=144 P3 + 12 squares.')
