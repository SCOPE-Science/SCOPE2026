#!/usr/bin/env python3
"""Exact finite incidence certificate and spherical-angle checks for central sections.

Pure Python 3; no external dependencies.  The analytic spherical area identity
is established in RESULT.md, not assumed to follow from numerical checks.
"""
from itertools import permutations, product, combinations
from fractions import Fraction
from math import atan2, sqrt, pi


def dot(u, v):
    return sum(x*y for x, y in zip(u, v))


def det3(u, v, w):
    return (u[0]*(v[1]*w[2]-v[2]*w[1])
            -u[1]*(v[0]*w[2]-v[2]*w[0])
            +u[2]*(v[0]*w[1]-v[1]*w[0]))


def normal_norm(u):
    return sqrt(dot(u, u))


VERTICES = tuple(sorted({tuple(x*s for x, s in zip(p, signs))
                         for p in set(permutations((0, 1, 2)))
                         for signs in product((-1, 1), repeat=3)}))
FACETS = tuple((tuple(sign if i == k else 0 for i in range(3)), 2)
               for k in range(3) for sign in (-1, 1)) + tuple(
    (eps, 3) for eps in product((-1, 1), repeat=3))


def shared_edge(i, j):
    u, v = VERTICES[i], VERTICES[j]
    active = [normal for normal, offset in FACETS
              if dot(normal, u) == dot(normal, v) == offset]
    return any(dot(x, x)*dot(y, y) != dot(x, y)**2
               for x in active for y in active)


EDGES = tuple((i, j) for i in range(len(VERTICES))
              for j in range(i + 1, len(VERTICES)) if shared_edge(i, j))


def number_of_sides(n):
    signs = [dot(v, n) for v in VERTICES]
    if any(x == 0 for x in signs):
        raise ValueError('a section hits a vertex')
    return sum(signs[i]*signs[j] < 0 for i, j in EDGES)


def predicted(n):
    a, b, c = sorted(map(abs, n), reverse=True)
    if not a > b > c > 0 or a == 2*b or a == 2*c or b == 2*c:
        raise ValueError('normal is on a chamber wall')
    return 6 + 2*((a > 2*c) + (a > 2*b) - (b > 2*c))


def omega(u, v, w):
    numerator = abs(det3(u, v, w))
    denominator = (normal_norm(u)*normal_norm(v)*normal_norm(w)
                   + dot(u, v)*normal_norm(w)
                   + dot(v, w)*normal_norm(u)
                   + dot(w, u)*normal_norm(v))
    assert numerator and denominator > 0
    return 2 * atan2(numerator, denominator)


def run():
    checks = 0
    assert len(VERTICES) == 24
    assert len(FACETS) == 14
    assert len(EDGES) == 36
    checks += 3
    # Enumerate ALL facet-triple intersections by exact Cramer's rule.
    # The resulting feasible vertices must be exactly the 24 listed points.
    reconstructed = set()
    for triple in combinations(FACETS, 3):
        rows = [list(normal) for normal, offset in triple]
        rhs = [offset for normal, offset in triple]
        determinant = det3(*rows)
        if determinant == 0:
            checks += 1
            continue
        coordinates = []
        for column in range(3):
            modified = [r[:] for r in rows]
            for i in range(3):
                modified[i][column] = rhs[i]
            coordinates.append(Fraction(det3(*modified), determinant))
        point = tuple(coordinates)
        if all(dot(n, point) <= d for n,d in FACETS):
            reconstructed.add(point)
        checks += 1
    assert reconstructed == set(VERTICES)
    checks += 1
    for u in VERTICES:
        assert all(dot(n, u) <= d for n, d in FACETS)
        checks += len(FACETS)
    degree = [0]*24
    for i, j in EDGES:
        degree[i] += 1
        degree[j] += 1
        assert sum((a-b)**2 for a,b in zip(VERTICES[i], VERTICES[j])) == 2
        checks += 1
    assert degree == [3]*24
    checks += 1
    # Five exact rational representatives for five angular regions.
    representatives = ((13, 11, 8, 6), (18, 12, 8, 8),
                       (30, 12, 8, 10), (18, 11, 4, 6),
                       (30, 11, 4, 8))
    for a,b,c,sides in representatives:
        assert number_of_sides((a,b,c)) == sides == predicted((a,b,c))
        checks += 1
    # Stress-test the exact universal chamber identity on integral normals.
    accepted = 0
    for a in range(3, 29):
        for b in range(2, a):
            for c in range(1, b):
                if a == 2*b or a == 2*c or b == 2*c:
                    continue
                n = (a,b,c)
                assert number_of_sides(n) == predicted(n)
                checks += 1
                accepted += 1
    assert accepted > 2000
    # Orthant and coordinate-permutation symmetry certificate.
    for a,b,c,sides in representatives:
        for p in set(permutations((a,b,c))):
            for sign in product((-1,1), repeat=3):
                n=tuple(x*e for x,e in zip(p,sign))
                assert number_of_sides(n) == sides
                checks += 1
    A=(1,1,1); B=(2,2,1); C=(2,1,1); D=(4,2,1)
    E=(1,1,0); F=(2,1,0); G=(1,0,0)
    region_areas = (omega(A,B,C), omega(C,B,D), omega(C,D,G),
                    omega(B,E,F)+omega(B,F,D), omega(G,D,F))
    assert abs(sum(region_areas)-pi/12)<1.e-13
    checks += 1
    probabilities=(12/pi*(region_areas[0]+region_areas[3]),
                   12/pi*(region_areas[1]+region_areas[4]),
                   12/pi*region_areas[2])
    assert all(0<p<1 for p in probabilities)
    assert abs(sum(probabilities)-1) < 1.e-13
    checks += 2
    assert abs(probabilities[0]-0.4984506899177035)<1e-13
    assert abs(probabilities[1]-0.31610885558019075)<1e-13
    assert abs(probabilities[2]-0.18544045450210572)<1e-13
    checks += 3
    print(f'PASS {checks} checks; {accepted} strictly ordered integral normals')
    print('probabilities for 6, 8, 10 sides:', *(f'{p:.15f}' for p in probabilities))
    print('five fundamental spherical areas:', *(f'{a:.15f}' for a in region_areas))


if __name__ == '__main__':
    run()
