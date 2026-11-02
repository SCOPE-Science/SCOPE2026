#!/usr/bin/env python3
"""Exact finite diagnostic for inverse fibers of a four-quadrant planar map.

Requires Python 3 standard library only. No numerical tolerance or external input.
The mathematical real-parameter proof is in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product


def cross(p, q):
    return p[0]*q[1] - p[1]*q[0]


def points(a, c, X, Y):
    rays = ((F(1), F(1)), (a, c), (F(1), F(-1)), (-a, c))
    sources = ((1, 0), (0, 1), (-1, 0), (0, -1))
    z = (X, Y)
    p = set()
    for j in range(4):
        u, v = rays[j], rays[(j+1) % 4]
        determinant = cross(u, v)
        if not determinant:
            raise ValueError("requires nondegenerate parameters")
        s = cross(z, v)/determinant
        t = cross(u, z)/determinant
        if s >= 0 and t >= 0:
            p.add((s*sources[j][0] + t*sources[(j+1) % 4][0],
                   s*sources[j][1] + t*sources[(j+1) % 4][1]))
    return p


def predicted(a, c, X, Y):
    if abs(a) > abs(c):
        return 1
    b, t = abs(a), abs(c)
    if c > 0:
        support = X+Y > 0 and t*X+b*Y > 0
        four = Y-X > 0 and t*X-b*Y > 0
    else:
        support = X-Y > 0 and t*X-b*Y > 0
        four = X+Y < 0 and t*X+b*Y > 0
    return 4 if four else (2 if support else 0)


def regular(a, c, X, Y):
    rays = ((F(1), F(1)), (a, c), (F(1), F(-1)), (-a, c))
    return (X, Y) != (0, 0) and all(cross(r, (X, Y)) != 0 for r in rays)


def verify():
    regular_count = 0
    for aa, cc in product(range(-6, 7), repeat=2):
        if abs(aa) == abs(cc):
            continue
        a, c = F(aa), F(cc)
        for xx, yy in product(range(-8, 9), repeat=2):
            X, Y = F(xx), F(yy)
            if not regular(a, c, X, Y):
                continue
            actual = len(points(a, c, X, Y))
            goal = predicted(a, c, X, Y)
            assert actual == goal, (aa, cc, xx, yy, actual, goal)
            regular_count += 1

    boundary_count = 0
    for aa, cc in product(range(-4, 5), repeat=2):
        if abs(aa) >= abs(cc):
            continue
        a, c = F(aa), F(cc)
        b, t = abs(a), abs(c)
        if c > 0:
            samples = [((0, 0), 1), ((1, -1), 1), ((-b, t), 1 if b else 2),
                       ((1, 1), 3), ((b, t), 3 if b else 2)]
        else:
            samples = [((0, 0), 1), ((-b, -t), 1 if b else 2), ((1, 1), 1),
                       ((b, -t), 3 if b else 2), ((1, -1), 3)]
        for (X, Y), goal in samples:
            actual = len(points(a, c, F(X), F(Y)))
            assert actual == goal, (aa, cc, X, Y, actual, goal)
            boundary_count += 1
    print("PASS", regular_count, "regular rational-fiber comparisons")
    print("PASS", boundary_count, "boundary and apex rational-fiber comparisons")


if __name__ == "__main__":
    verify()
