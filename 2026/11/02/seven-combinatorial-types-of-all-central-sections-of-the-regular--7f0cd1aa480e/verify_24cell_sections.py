"""Exact integer checker for a stratified central-section classification.

Run: python3 verify_24cell_sections.py
Uses only the Python standard library. No numerical tolerance.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations, product

DIM = 4
roots = set()
for i, j in combinations(range(DIM), 2):
    for a, b in product((-1, 1), repeat=2):
        v = [0] * DIM
        v[i], v[j] = a, b
        roots.add(tuple(v))
R = sorted(roots)
assert len(R) == 24
index = {v: i for i, v in enumerate(R)}

def dot(x, y):
    return sum(a * b for a, b in zip(x, y))

edges = {(i, j) for i, j in combinations(range(len(R)), 2)
         if dot(R[i], R[j]) == 1}
assert len(edges) == 96
facets = []
for i in range(DIM):
    for eps in (-1, 1):
        facets.append(frozenset(j for j, v in enumerate(R) if eps * v[i] == 1))
for eps in product((-1, 1), repeat=DIM):
    facets.append(frozenset(j for j, v in enumerate(R) if dot(eps, v) == 2))
assert len(facets) == 24 and len(set(facets)) == 24
assert all(len(f) == 6 for f in facets)

ridges = set()
for f in facets:
    for tri in combinations(sorted(f), 3):
        if all((min(i, j), max(i, j)) in edges for i, j in combinations(tri, 2)):
            ridges.add(frozenset(tri))
assert len(ridges) == 96
assert all(sum(t <= f for f in facets) == 2 for t in ridges)

# Four standard simple roots: the central index is 1; 0,2,3 are outer.
A = ((1, -1, 0, 0), (0, 1, -1, 0),
     (0, 0, 1, -1), (0, 0, 1, 1))
assert dot(A[1], A[0]) == dot(A[1], A[2]) == dot(A[1], A[3]) == -1
assert dot(A[0], A[2]) == dot(A[0], A[3]) == dot(A[2], A[3]) == 0

# Check the reflection generators preserve the root set.
for alpha in A:
    assert {tuple(v[k] - dot(v, alpha) * alpha[k] for k in range(DIM))
            for v in R} == roots

# Check the diagram's S3 triality acts by actual automorphisms of the roots.
def coefficients(v):
    x, y, z, w = v
    assert (x+y+z-w) % 2 == 0 and (x+y+z+w) % 2 == 0
    return x, x+y, (x+y+z-w)//2, (x+y+z+w)//2

for tail in permutations((0, 2, 3)):
    perm = [0, 1, 2, 3]
    for i, j in zip((0, 2, 3), tail):
        perm[i] = j
    mapped = []
    for v in R:
        c = coefficients(v)
        mapped.append(tuple(sum(c[i]*A[perm[i]][k] for i in range(4))
                            for k in range(4)))
    assert set(mapped) == roots


def section_profile(normal):
    sign = [dot(normal, r) for r in R]
    zero = {i for i, value in enumerate(sign) if value == 0}
    crossing = {(i, j) for i, j in edges if sign[i] * sign[j] < 0}
    polygon_sizes = []
    for facet in facets:
        fs = [sign[i] for i in facet]
        if min(fs) < 0 < max(fs):
            sides = len(facet & zero) + sum(i in facet and j in facet
                                            for i, j in crossing)
            polygon_sizes.append(sides)
    # A triangular ridge can itself be a 2-face of the 3D section.
    polygon_sizes.extend(3 for tri in ridges if tri <= zero)
    vcount = len(zero) + len(crossing)
    facecount = len(polygon_sizes)
    edgecount = vcount + facecount - 2  # Euler's formula for a convex 3-polytope
    assert sum(polygon_sizes) == 2 * edgecount
    return (vcount, edgecount, facecount), tuple(sorted(Counter(polygon_sizes).items()))

expected = {
    (0, 1): ((12, 24, 14), ((3, 8), (4, 6))),
    (0, 2): ((18, 30, 14), ((4, 12), (6, 2))),
    (0, 3): ((26, 42, 18), ((4, 12), (6, 6))),
    (1, 0): ((14, 24, 12), ((4, 12),)),
    (1, 1): ((20, 32, 14), ((4, 6), (5, 8))),
    (1, 2): ((26, 40, 16), ((4, 4), (5, 8), (6, 4))),
    (1, 3): ((32, 48, 18), ((4, 6), (6, 12))),
}
classes = defaultdict(set)
for s in product((0, 1), repeat=4):
    if not any(s):
        continue
    a, b, c, d = s
    # u satisfying dot(u, alpha_i)=2*s_i, all arithmetic exact.
    u = (2*a+2*b+c+d, 2*b+c+d, c+d, d-c)
    assert tuple(dot(u, alpha) for alpha in A) == tuple(2*x for x in s)
    key = (b, a+c+d)
    signature = section_profile(u)
    assert signature == expected[key], (s, u, signature, expected[key])
    classes[key].add(s)
assert len(classes) == 7
assert sorted(map(len, classes.values())) == [1, 1, 1, 3, 3, 3, 3]
assert len({v for v in expected.values()}) == 7
for key, signature in sorted(expected.items()):
    print('central_simple_positive_count=%d outer_simple_positive_count=%d '\
          'f=%s polygons=%s chamber_faces=%d' %
          (key[0], key[1], signature[0], signature[1], len(classes[key])))
print('VERIFY_OK: 24 roots, 96 edges, 96 ridges, 24 octahedral facets, '
      '6 triality automorphisms, 15 chamber faces, 7 sectional classes.')
