#!/usr/bin/env python3
"""Exact rational sharpness certificate for one affine-regular hexagon.

All operations use built-in Python arithmetic; no downloaded data is needed.
The finite enumeration certifies only a six-vertex integer model. The
universal hexagon enclosure formula is an analytic theorem in RESULT.md.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import gcd

V = ((1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1))

def chord_directions():
    result = set()
    for a, b in combinations(V, 2):
        dx, dy = b[0] - a[0], b[1] - a[1]
        g = gcd(abs(dx), abs(dy))
        dx, dy = dx // g, dy // g
        if dx < 0 or (dx == 0 and dy < 0):
            dx, dy = -dx, -dy
        result.add((dx, dy))
    return sorted(result)

def intersect_halfplane(poly, normal, c):
    """Sutherland-Hodgman clipping over the rational field."""
    if not poly:
        return []
    nx, ny = normal
    ans = []
    for a, b in zip(poly, poly[1:] + poly[:1]):
        va = nx * a[0] + ny * a[1] - c
        vb = nx * b[0] + ny * b[1] - c
        if va <= 0:
            ans.append(a)
        if (va < 0 and vb > 0) or (va > 0 and vb < 0):
            t = va / (va - vb)
            ans.append((a[0] + t * (b[0] - a[0]),
                        a[1] + t * (b[1] - a[1])))
    return ans

def area(poly):
    if len(poly) < 3:
        return Q(0)
    return abs(sum(a[0] * b[1] - a[1] * b[0]
                   for a, b in zip(poly, poly[1:] + poly[:1]))) / 2

def main():
    dirs = chord_directions()
    assert len(dirs) == 6, dirs
    normals = sorted({(dy, -dx) for dx, dy in dirs} |
                     {(-dy, dx) for dx, dy in dirs})
    assert len(normals) == 12, normals
    supports = [(nx, ny, max(nx * x + ny * y for x, y in V))
                for nx, ny in normals]
    box = [(Q(-100), Q(-100)), (Q(100), Q(-100)),
           (Q(100), Q(100)), (Q(-100), Q(100))]
    assert area([(Q(x), Q(y)) for x, y in V]) == 3
    candidates = 0
    best = None
    equality_count = 0
    for k in (3, 4):
        for subset in combinations(supports, k):
            polygon = box
            for nx, ny, c in subset:
                polygon = intersect_halfplane(polygon, (nx, ny), Q(c))
            A = area(polygon)
            candidates += 1
            if best is None or A < best:
                best = A
                equality_count = 1
            elif A == best:
                equality_count += 1
    assert candidates == 715
    assert best == Q(4), (best, equality_count)
    assert equality_count > 0
    print('AFFINE_HEXAGON_EXACT_CHORD_BOUND_OK')
    print('directions=6 normals=12 candidate_systems=715 hexagon_area=3 minimum_clipped_area=4')

if __name__ == '__main__':
    main()
