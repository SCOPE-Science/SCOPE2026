#!/usr/bin/env python3
"""Exact Q(sqrt(5)) enumeration for central regular-icosahedron sections.

Run with Python >= 3.9. Standard library only. A chamber is represented by
its six signs against representative antipodal vertex axes. No floating-point
computation enters the exhaustive chamber/edge/angle classification.
"""
from itertools import combinations
from collections import Counter
import math

ZERO = (0, 0)
TWO = (2, 0)
GOLDEN_DOUBLE = (1, 1)  # 1 + sqrt(5)


def plus(x, y):
    return (x[0] + y[0], x[1] + y[1])


def negative(x):
    return (-x[0], -x[1])


def minus(x, y):
    return plus(x, negative(y))


def times(x, y):
    return (x[0] * y[0] + 5 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def exact_sign(x):
    """Sign of a+b*sqrt(5), for integers a,b, using integer arithmetic."""
    a, b = x
    if a == 0 and b == 0:
        return 0
    if a >= 0 and b >= 0:
        return 1
    if a <= 0 and b <= 0:
        return -1
    if a*a > 5*b*b:
        return 1 if a > 0 else -1
    if a*a < 5*b*b:
        return 1 if b > 0 else -1
    raise AssertionError("sqrt(5) is irrational")


def dot(u, v):
    s = ZERO
    for x, y in zip(u, v):
        s = plus(s, times(x, y))
    return s


def cross(u, v):
    return tuple(minus(times(u[(k+1)%3], v[(k+2)%3]),
                       times(u[(k+2)%3], v[(k+1)%3])) for k in range(3))


def negvec(u):
    return tuple(negative(x) for x in u)


def chamber_vertices(axes, signs):
    """All corners of a closed spherical sign chamber, as (i,j,orientation).

    Every spherical corner lies at a crossing of two great circles. Here there
    are no three concurrent circles, so testing the 30 oriented pair-crossings
    is complete. Distinct listed corners are automatically extreme vertices.
    """
    output = []
    for i, j in combinations(range(len(axes)), 2):
        p = cross(axes[i], axes[j])
        for direction in (-1, 1):
            found = [direction*exact_sign(dot(a, p)) for a in axes]
            if all(v == 0 or v == signs[k] for k, v in enumerate(found)):
                output.append((i, j, direction))
    return output


def main():
    # Doubled vertex coordinates relative to the edge-length-2 model.
    w = [
        (ZERO, TWO, GOLDEN_DOUBLE),
        (ZERO, TWO, negative(GOLDEN_DOUBLE)),
        (TWO, GOLDEN_DOUBLE, ZERO),
        (TWO, negative(GOLDEN_DOUBLE), ZERO),
        (GOLDEN_DOUBLE, ZERO, TWO),
        (GOLDEN_DOUBLE, ZERO, negative(TWO)),
    ]
    vertices = w + [negvec(x) for x in w]
    squared_radius = dot(w[0], w[0])
    assert all(dot(x, x) == squared_radius for x in vertices)
    pairs = list(combinations(range(6), 2))
    assert all(exact_sign(dot(w[i], w[j])) in (-1, 1) for i, j in pairs)
    assert all(exact_sign(dot(w[k], cross(w[i], w[j]))) != 0
               for i, j, k in combinations(range(6), 3))

    # Every non-antipodal pair has the same absolute cosine 1/sqrt(5).
    for i, j in pairs:
        q = dot(w[i], w[j])
        assert times((5, 0), times(q, q)) == times(squared_radius, squared_radius)

    # For regular icosahedron vertices, edges are precisely positive-dot pairs.
    edges = [(i, j) for i, j in combinations(range(12), 2)
             if exact_sign(dot(vertices[i], vertices[j])) > 0]
    assert len(edges) == 30
    assert all(sum(1 for i, j in edges if i == v or j == v) == 5
               for v in range(12))

    counts = Counter()
    triangular_masks, pentagonal_masks = [], []
    for mask in range(64):
        s = [1 if (mask >> k) & 1 else -1 for k in range(6)]
        corners = chamber_vertices(w, s)
        if not corners:
            continue
        # A generic normal in this chamber assigns signs s to w and -s to -w.
        vertex_signs = s + [-v for v in s]
        crossed = sum(vertex_signs[i] != vertex_signs[j] for i, j in edges)
        # Interior angle at corner (i,j) is
        # arccos(-s_i*s_j*sign(<w_i,w_j>)/sqrt(5)).
        angle_cos_signs = [-s[i]*s[j]*exact_sign(dot(w[i], w[j]))
                           for i, j, direction in corners]
        counts[(len(corners), crossed)] += 1
        if len(corners) == 3:
            assert crossed == 12 and set(angle_cos_signs) == {1}
            triangular_masks.append(mask)
        elif len(corners) == 5:
            assert crossed == 10 and set(angle_cos_signs) == {-1}
            pentagonal_masks.append(mask)
        else:
            raise AssertionError((mask, corners, crossed))

    assert counts == {(3, 12): 20, (5, 10): 12}
    assert triangular_masks == [0, 3, 5, 6, 9, 10, 17, 23, 24, 29,
                                34, 39, 40, 46, 53, 54, 57, 58, 60, 63]
    assert pentagonal_masks == [1, 2, 7, 8, 21, 25,
                                 38, 42, 55, 56, 61, 62]
    # Six great circles in general position yield exactly 6^2-6+2=32 faces.
    assert sum(counts.values()) == 32
    assert sum(k*n for (k, _), n in counts.items()) == 120

    theta = math.acos(1 / math.sqrt(5))
    triangle_area = 3*theta - math.pi
    pentagon_area = 2*math.pi - 5*theta
    p12_via_area = 20*triangle_area/(4*math.pi)
    p12_via_crofton = 15*theta/math.pi - 5
    assert triangle_area > 0 and pentagon_area > 0
    assert abs(20*triangle_area + 12*pentagon_area - 4*math.pi) < 1e-12
    assert abs(p12_via_area - p12_via_crofton) < 1e-12
    expectation = 30*theta/math.pi
    assert abs(expectation - (10+2*p12_via_area)) < 1e-12
    assert 0 < p12_via_area < 1

    print("EXACT_CHAMBER_ENUMERATION_OK")
    print("32 chambers: 20 triangular/dodecagon; 12 pentagonal/decagon")
    print("triangular_masks:", triangular_masks)
    print("pentagonal_masks:", pentagonal_masks)
    print("p12 = 15*acos(1/sqrt(5))/pi - 5 = %.15f" % p12_via_area)
    print("p10 = 6 - 15*acos(1/sqrt(5))/pi = %.15f" % (1-p12_via_area))
    print("expected vertices = 30*acos(1/sqrt(5))/pi = %.15f" % expectation)


if __name__ == "__main__":
    main()
