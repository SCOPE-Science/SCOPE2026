#!/usr/bin/env python3
"""Independent reproducibility checks for truncated-tetrahedron central sections.

Only the Python standard library is required. All combinatorial chamber
calculations use exact integers and fractions. Spherical areas use the
stable closed formula for spherical triangle solid angle.
"""
from fractions import Fraction
from itertools import combinations
from collections import Counter
from math import acos, atan2, isclose, pi, sqrt
from random import Random


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1],
            a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])


def subtract(a, b):
    return tuple(x-y for x, y in zip(a, b))


def oriented_facets(vertices):
    """Enumerate each supporting plane by triples, using integer arithmetic."""
    facets = set()
    for a, b, c in combinations(range(len(vertices)), 3):
        v = vertices[a]
        normal = cross(subtract(vertices[b], v), subtract(vertices[c], v))
        if normal == (0, 0, 0):
            continue
        values = [dot(normal, subtract(x, v)) for x in vertices]
        if min(values) < 0 < max(values):
            continue
        facet = tuple(i for i, z in enumerate(values) if z == 0)
        facets.add(facet)
    return sorted(facets)


def edges_from_facets(vertices, facets):
    return sorted((i, j) for i, j in combinations(range(len(vertices)), 2)
                  if sum(i in f and j in f for f in facets) >= 2)


def twice_area_polygon(poly):
    return sum(p[0]*q[1]-q[0]*p[1]
               for p, q in zip(poly, poly[1:]+poly[:1]))


def clip(poly, line):
    """Clip (y,z) rational polygon by line[0]+line[1]*y+line[2]*z >= 0."""
    if not poly:
        return []
    output = []
    for p, q in zip(poly, poly[1:] + poly[:1]):
        fp = line[0] + line[1]*p[0] + line[2]*p[1]
        fq = line[0] + line[1]*q[0] + line[2]*q[1]
        if fp >= 0:
            output.append(p)
        if (fp < 0 < fq) or (fq < 0 < fp):
            t = fp/(fp-fq)
            output.append((p[0]+t*(q[0]-p[0]),
                           p[1]+t*(q[1]-p[1])))
    dedup = []
    for x in output:
        if x not in dedup:
            dedup.append(x)
    if len(dedup) < 3 or twice_area_polygon(dedup) <= 0:
        return []
    return dedup


def spherical_triangle(p, q, r):
    """Area of spherical triangle in hemisphere, rays (1,y,z)."""
    a = (1., float(p[0]), float(p[1]))
    b = (1., float(q[0]), float(q[1]))
    c = (1., float(r[0]), float(r[1]))
    numerator = abs(dot(a, cross(b, c)))
    na, nb, nc = (sqrt(dot(v, v)) for v in (a, b, c))
    denominator = (na*nb*nc + dot(a,b)*nc + dot(b,c)*na + dot(c,a)*nb)
    return 2*atan2(numerator, denominator)


def spherical_polygon(poly):
    return sum(spherical_triangle(poly[0], poly[j], poly[j+1])
               for j in range(1, len(poly)-1))


def n_sides(vertices, edges, y, z):
    vals = [w[0] + w[1]*y + w[2]*z for w in vertices]
    assert all(v != 0 for v in vals)
    return sum((vals[i] > 0) != (vals[j] > 0) for i, j in edges)


def main():
    original = [(1,1,1), (1,-1,-1), (-1,1,-1), (-1,-1,1)]
    vertices = [tuple(2*a[k]+b[k] for k in range(3))
                for i, a in enumerate(original)
                for j, b in enumerate(original) if i != j]
    assert len(vertices) == 12 and len(set(vertices)) == 12
    assert {dot(w,w) for w in vertices} == {11}
    assert tuple(sum(w[k] for w in vertices) for k in range(3)) == (0,0,0)
    facets = oriented_facets(vertices)
    assert len(facets) == 8
    assert sorted(map(len, facets)) == [3]*4 + [6]*4
    edges = edges_from_facets(vertices, facets)
    assert len(edges) == 18
    assert {dot(subtract(vertices[i], vertices[j]),
                subtract(vertices[i], vertices[j])) for i,j in edges} == {8}
    assert all(sum(i in e for e in edges) == 3 for i in range(12))
    print('Exact polyhedron: 12 vertices, 18 equal edges, 4 triangles, 4 hexagons.')

    F = Fraction
    chamber = [(F(0),F(0)),(F(1),F(0)),(F(1),F(1))]
    lines = sorted({tuple(w if w[0] > 0 else tuple(-c for c in w))
                    for w in vertices})
    assert len(lines) == 12
    regions = [chamber]
    splitters = []
    for line in lines:
        updated = []
        for poly in regions:
            pos = clip(poly, line)
            neg = clip(poly, tuple(-c for c in line))
            if pos and neg:
                splitters.append(line)
            if pos:
                updated.append(pos)
            if neg:
                updated.append(neg)
        regions = updated
    # Only four of the 12 vertex-hyperplanes intersect the open chamber.
    assert set(splitters) == {(1,-3,-1),(1,-3,1),
                              (1,-1,-3),(1,1,-3)}
    assert len(regions) == 6
    expected = {
        (4, (F(0),F(0)), (F(1,3),F(0)), (F(1,4),F(1,4))),
        (5, (F(1,3),F(0)), (F(2,5),F(1,5)), (F(1,4),F(1,4))),
        (6, (F(1,3),F(0)), (F(1),F(0)), (F(2,5),F(1,5))),
        (4, (F(2,5),F(1,5)), (F(1,2),F(1,2)), (F(1,4),F(1,4))),
        (5, (F(1),F(0)), (F(1),F(2,3)), (F(1,2),F(1,2)), (F(2,5),F(1,5))),
        (6, (F(1),F(2,3)), (F(1),F(1)), (F(1,2),F(1,2)))
    }
    found = set()
    count_area = Counter()
    for poly in regions:
        cy = sum(v[0] for v in poly) / len(poly)
        cz = sum(v[1] for v in poly) / len(poly)
        n = n_sides(vertices, edges, cy, cz)
        found.add((n, *poly))
        count_area[n] += spherical_polygon(poly)
    assert found == expected, 'Exact rational chamber enumeration differs.'
    assert set(count_area) == {4,5,6}
    assert isclose(sum(count_area.values()), pi/12, rel_tol=0, abs_tol=4e-14)
    probabilities = {n: 12*a/pi for n,a in sorted(count_area.items())}
    assert isclose(sum(probabilities.values()), 1, rel_tol=0, abs_tol=4e-14)
    # An independent integral-geometric expectation counts intersected edges.
    expected_mean = 18*acos(F(7,11))/pi
    inferred_mean = sum(n*probabilities[n] for n in (4,5,6))
    assert isclose(inferred_mean, expected_mean, rel_tol=0, abs_tol=5e-14)
    for n,p in probabilities.items():
        print('Exact spherical-area evaluation: sides=%d, probability=%.15f' % (n,p))
    print('Mean sides from spherical areas=%.15f; from 18 edge angles=%.15f.' %
          (inferred_mean, expected_mean))

    # Independent isotropic-normal experiment; NEVER treated as exhaustive.
    rng = Random(19262026)
    samples = 35000
    histogram = Counter()
    for _ in range(samples):
        u = (rng.gauss(0,1), rng.gauss(0,1), rng.gauss(0,1))
        vals = [dot(w, u) for w in vertices]
        n = sum((vals[i]>0) != (vals[j]>0) for i,j in edges)
        histogram[n] += 1
    assert set(histogram) == {4,5,6}
    assert all(abs(histogram[n]/samples - probabilities[n]) < 0.015
               for n in probabilities)
    print('Independent isotropic Monte Carlo (%d orientations): %s.' %
          (samples, {n: round(histogram[n]/samples, 6) for n in (4,5,6)}))
    print('PASS: exact combinatorics, all 6 spherical chambers, normalization,')
    print('independent mean identity, and finite numerical consistency.')

if __name__ == '__main__':
    main()
