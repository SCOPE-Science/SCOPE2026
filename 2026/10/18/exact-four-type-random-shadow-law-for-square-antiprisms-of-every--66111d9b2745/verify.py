#!/usr/bin/env python3
"""Independent numerical checks of exact square-antiprism shadow laws.

Uses only the Python standard library. The analytic proof is separate;
finite tests do not establish its quantified conclusions.
"""
import math
import random
from collections import Counter

PI = math.pi
SQ2 = math.sqrt(2)


def gamma(h):
    return (1 - 1 / SQ2) / (2 * h)


def antiprism(h):
    return [(math.cos(j * PI / 2), math.sin(j * PI / 2), h)
            for j in range(4)] + [
            (math.cos(PI / 4 + j * PI / 2), math.sin(PI / 4 + j * PI / 2), -h)
            for j in range(4)]


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0])


def normalise(v):
    r = math.sqrt(dot(v, v))
    return tuple(x / r for x in v)


def projected_vertex_count(vertices, normal):
    """Compute a planar convex hull directly, without facet visibility tests."""
    n = normalise(normal)
    helper = (0., 0., 1.) if abs(n[2]) < 0.9 else (0., 1., 0.)
    along = dot(n, helper)
    e = normalise(tuple(helper[i] - along * n[i] for i in range(3)))
    f = cross(n, e)
    pts = sorted((dot(v, e), dot(v, f)) for v in vertices)

    def turn(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    lower = []
    for point in pts:
        while len(lower) >= 2 and turn(lower[-2], lower[-1], point) <= 1e-12:
            lower.pop()
        lower.append(point)
    upper = []
    for point in reversed(pts):
        while len(upper) >= 2 and turn(upper[-2], upper[-1], point) <= 1e-12:
            upper.pop()
        upper.append(point)
    return len(lower) + len(upper) - 2


def indicator_count(u, h):
    """Exact sign-chamber combinatorics, independently of polygon hull code."""
    x, y = sorted((abs(u[0]), abs(u[1])), reverse=True)
    z = abs(u[2])
    g = gamma(h)
    A = (x + y < SQ2 * g * z)
    B = (x - y < SQ2 * g * z)
    C = (x < g * z)
    D = (y < g * z)
    return 6 + int(A) + int(C) - abs(int(B) - int(D))


def probabilities(h):
    g = gamma(h)
    q = 1. / math.sqrt(1. + g * g)
    J = lambda a: math.asin(q * math.sin(a))
    j, k, ell, m = [J(a) for a in (PI / 8, PI / 4, 3 * PI / 8, PI / 2)]
    p8 = 1. - 8. * j / PI
    p7 = 8. * (2 * j - k) / PI
    p5 = 8. * (2 * ell - k - m) / PI
    p6 = 1. - p5 - p7 - p8
    return {5: p5, 6: p6, 7: p7, 8: p8}


def dihedral_mean(h):
    g = gamma(h)
    a = math.acos(g / math.sqrt(1 + g*g))
    b = math.acos((1 / SQ2 - g*g) / (1 + g*g))
    return 8 * (a + b) / PI


def numeric_integral(h, steps=4000):
    """Spherical quadrature independently integrating the radial chamber lengths."""
    g = gamma(h)
    R = lambda ang: g / math.cos(ang)
    F = lambda r: 1. - 1. / math.sqrt(1. + r*r)
    accum = [0., 0., 0.]
    dtheta = (PI / 4) / steps
    for j in range(steps + 1):
        theta = j * dtheta
        rC = R(theta)
        rA = R(theta - PI / 4)
        rB = R(theta + PI / 4)
        rD = math.inf if j == 0 else g / math.sin(theta)
        f8 = min(F(rC), F(rA))
        f7 = abs(F(rC) - F(rA))
        f5 = abs(F(rB) - F(rD)) if rD != math.inf else 1. - F(rB)
        weight = 1 if j in (0, steps) else (4 if j % 2 else 2)
        for n, val in enumerate((f5, f7, f8)):
            accum[n] += weight * val
    p5, p7, p8 = [4 / PI * x * dtheta / 3 for x in accum]
    return {5: p5, 6: 1 - p5 - p7 - p8, 7: p7, 8: p8}


def facet_checks(h):
    verts = antiprism(h)
    g = gamma(h)
    normals = [(a, b, SQ2 * g) for a in (-1, 1) for b in (-1, 1)]
    normals += [(a, 0, -g) for a in (-1, 1)]
    normals += [(0, b, -g) for b in (-1, 1)]
    normals += [(0, 0, 1), (0, 0, -1)]
    eqs = [1 + SQ2 * g * h] * 4 + [1 - g * h] * 4 + [h] * 2
    incidence = []
    for normal, constant in zip(normals, eqs):
        ds = [dot(v, normal) - constant for v in verts]
        assert max(ds) < 3e-13, (h, normal, max(ds))
        matched = frozenset(i for i, d in enumerate(ds) if abs(d) < 3e-13)
        assert len(matched) in (3, 4)
        incidence.append(matched)
    assert sum(len(s) == 3 for s in incidence) == 8
    assert sum(len(s) == 4 for s in incidence) == 2
    edges = {}
    for f, I in enumerate(incidence):
        for gface in range(f+1, len(incidence)):
            J = incidence[gface]
            overlap = I & J
            if len(overlap) == 2:
                edges[tuple(sorted(overlap))] = (f, gface)
    assert len(edges) == 16, (h, edges)
    return normals, edges


def main():
    rnd = random.Random(20261017)
    total_hulls = 0
    for h in (0.2, 2**(-3/4), 1.5, 4.):
        verts = antiprism(h)
        normals, edges = facet_checks(h)
        exact = probabilities(h)
        quadrature = numeric_integral(h)
        assert all(0 < p < 1 for p in exact.values())
        assert abs(sum(exact.values()) - 1.) < 1e-12
        assert max(abs(exact[n] - quadrature[n]) for n in range(5,9)) < 2e-9
        mean1 = sum(n * p for n, p in exact.items())
        assert abs(mean1 - dihedral_mean(h)) < 1e-11
        counts = Counter()
        for i in range(18000):
            u = normalise(tuple(rnd.gauss(0, 1) for _ in range(3)))
            n = projected_vertex_count(verts, u)
            expected_n = indicator_count(u, h)
            assert n == expected_n, (h, u, n, expected_n)
            # Separately count sign changes on adjacent facets.
            signs = [dot(a, u) > 0 for a in normals]
            horizon = sum(signs[a] != signs[b] for a, b in edges.values())
            assert n == horizon, (h, u, n, horizon)
            counts[n] += 1
            total_hulls += 1
        assert set(counts).issubset({5,6,7,8})
        assert max(abs(counts[n] / 18000. - exact[n]) for n in exact) < 0.018
        print(f'h={h:.12g} p5={exact[5]:.12f} p6={exact[6]:.12f} '
              f'p7={exact[7]:.12f} p8={exact[8]:.12f} '
              f'samples={dict(sorted(counts.items()))}')
    print(f'SQUARE_ANTIPRISM_SHADOW_OK projected_hulls={total_hulls} '
          'facet_horizon=16 edges per shape and exact spherical quadratures=4')


if __name__ == '__main__':
    main()
