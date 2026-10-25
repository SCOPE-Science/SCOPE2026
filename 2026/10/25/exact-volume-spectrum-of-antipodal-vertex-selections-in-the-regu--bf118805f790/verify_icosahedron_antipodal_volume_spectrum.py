#!/usr/bin/env python3
"""Exact volume spectrum of antipodal six-vertex selections from a regular icosahedron.

Only the Python standard library is required. Coordinates are in Z[phi], where
phi=(1+sqrt(5))/2 and phi**2=phi+1. The 64 sign selections are enumerated
exhaustively; supporting facets and signed tetrahedral volumes are computed
with exact arithmetic in that quadratic field.
"""
from collections import defaultdict
from itertools import combinations, product
import json

# An element a+b*phi is stored as (a,b), with a,b integers.
ZERO = (0, 0)
ONE = (1, 0)
PHI = (0, 1)

def add(x, y):
    return (x[0] + y[0], x[1] + y[1])

def neg(x):
    return (-x[0], -x[1])

def sub(x, y):
    return add(x, neg(y))

def mul(x, y):
    a, b = x
    c, d = y
    return (a*c + b*d, a*d + b*c + b*d)

def sign(x):
    # 2(a+b*phi) = u+v*sqrt(5), where u=2a+b and v=b.
    a, b = x
    u, v = 2*a + b, b
    if v == 0:
        return (u > 0) - (u < 0)
    if v > 0:
        if u >= 0:
            return 1
        return 1 if 5*v*v > u*u else -1
    if u <= 0:
        return -1
    return 1 if u*u > 5*v*v else -1

def dot(u, v):
    return add(add(mul(u[0], v[0]), mul(u[1], v[1])), mul(u[2], v[2]))

def cross(u, v):
    return [
        sub(mul(u[1], v[2]), mul(u[2], v[1])),
        sub(mul(u[2], v[0]), mul(u[0], v[2])),
        sub(mul(u[0], v[1]), mul(u[1], v[0])),
    ]

def vsub(u, v):
    return [sub(a, b) for a, b in zip(u, v)]

def vscale(u, c):
    return [(c*x[0], c*x[1]) for x in u]

def det(u, v, w):
    return dot(u, cross(v, w))

# One representative from each antipodal pair of the standard icosahedron.
# The full vertex set is {+/- v_i : i=1,...,6}.
REP = [
    [(0, 0), (1, 0), (0, 1)],   # (0, 1, phi)
    [(0, 0), (1, 0), (0, -1)],  # (0, 1, -phi)
    [(1, 0), (0, 1), (0, 0)],   # (1, phi, 0)
    [(1, 0), (0, -1), (0, 0)],  # (1, -phi, 0)
    [(0, 1), (0, 0), (1, 0)],   # (phi, 0, 1)
    [(0, 1), (0, 0), (-1, 0)],  # (phi, 0, -1)
]

def six_times_volume(bits):
    """Return 6*Vol(conv{bits[i]*REP[i]}), exactly as a+b*phi."""
    points = [vscale(REP[i], bits[i]) for i in range(6)]
    # Each facet is stored by its complete set of coplanar vertex indices.
    facets = {}
    for tri in combinations(range(6), 3):
        i, j, k = tri
        normal = cross(vsub(points[j], points[i]), vsub(points[k], points[i]))
        side = {
            ell: sign(dot(normal, vsub(points[ell], points[i])))
            for ell in range(6) if ell not in tri
        }
        values = list(side.values())
        if all(s >= 0 for s in values) and any(s > 0 for s in values):
            face = tuple(sorted(set(tri) | {ell for ell, s in side.items() if s == 0}))
            facets.setdefault(face, vscale(normal, -1))
        elif all(s <= 0 for s in values) and any(s < 0 for s in values):
            face = tuple(sorted(set(tri) | {ell for ell, s in side.items() if s == 0}))
            facets.setdefault(face, normal)

    face_list = list(facets)
    if len(face_list) < 4:
        raise AssertionError("selection is not a full-dimensional polytope")

    total = ZERO
    for face in face_list:
        # In a convex 3-polytope, two facet vertices are adjacent precisely
        # when their pair is the intersection of two distinct facets.
        adjacency = {i: [] for i in face}
        for i, j in combinations(face, 2):
            if any(set(face) & set(other) == {i, j}
                   for other in face_list if other != face):
                adjacency[i].append(j)
                adjacency[j].append(i)
        if any(len(adjacency[i]) != 2 for i in face):
            raise AssertionError("facet boundary is not a cycle")

        start = min(face)
        nxt = min(adjacency[start])
        order = [start, nxt]
        previous, current = start, nxt
        while True:
            following = next(z for z in adjacency[current] if z != previous)
            if following == order[0]:
                break
            order.append(following)
            previous, current = current, following
            if len(order) > len(face):
                raise AssertionError("invalid facet cycle")
        if len(order) != len(face):
            raise AssertionError("facet cycle omits a vertex")

        # Orient the boundary cycle so its normal points outward.
        p0 = points[order[0]]
        n_triangle = cross(vsub(points[order[1]], p0), vsub(points[order[2]], p0))
        if sign(dot(n_triangle, facets[face])) < 0:
            order = [order[0]] + list(reversed(order[1:]))

        # Fan-triangulate the polygonal facet. The signed-volume formula is
        # Vol(P) = (1/6) * sum det(a,b,c) over outward-oriented boundary triangles.
        for j in range(1, len(order) - 1):
            total = add(total, det(points[order[0]], points[order[j]], points[order[j+1]]))

    return neg(total) if sign(total) < 0 else total

def main():
    spectrum = defaultdict(list)
    for bits in product((1, -1), repeat=6):
        value = six_times_volume(bits)
        spectrum[value].append(bits)

    expected = {
        (8, 4): 12,
        (8, 12): 20,
        (8, 16): 20,
        (12, 16): 12,
    }
    actual = {value: len(patterns) for value, patterns in spectrum.items()}
    assert actual == expected, (actual, expected)
    assert sum(actual.values()) == 64

    rows = []
    for (a, b), patterns in sorted(spectrum.items(), key=lambda kv: (kv[0][0], kv[0][1])):
        rows.append({
            "six_times_volume": {"constant": a, "phi_coefficient": b},
            "volume_exact": {"constant_numerator": a, "phi_coefficient_numerator": b, "denominator": 6},
            "multiplicity": len(patterns),
            "representative_signs": "".join("+" if x == 1 else "-" for x in patterns[0]),
        })
    print(json.dumps(rows, indent=2))

if __name__ == "__main__":
    main()
