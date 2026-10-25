#!/usr/bin/env python3
"""Independent exact checks of the connected-hexagon convex-hull runner-up law.

All geometric computations use integer coordinates for corners scaled by three.
No external packages are required. Finite checks supplement the analytic proof.
"""
from collections import Counter
from itertools import product

NEIGHBORS = ((1, 0), (0, 1), (1, -1), (-1, 0), (0, -1), (-1, 1))
CORNERS3 = ((1, 1), (-1, -1), (-1, 2), (1, -2), (2, -1), (-2, 1))


def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def convex_hull(points):
    points = sorted(set(points))
    if len(points) < 3:
        return points
    lo, hi = [], []
    for p in points:
        while len(lo) > 1 and cross(lo[-2], lo[-1], p) <= 0:
            lo.pop()
        lo.append(p)
    for p in reversed(points):
        while len(hi) > 1 and cross(hi[-2], hi[-1], p) <= 0:
            hi.pop()
        hi.append(p)
    return lo[:-1] + hi[:-1]


def six_area_from_corners(centers):
    corners = [(3*q+x, 3*r+y) for q, r in centers for x, y in CORNERS3]
    boundary = convex_hull(corners)
    determinant_twice = sum(
        boundary[j][0]*boundary[(j+1) % len(boundary)][1]
        - boundary[j][1]*boundary[(j+1) % len(boundary)][0]
        for j in range(len(boundary))
    )
    assert determinant_twice % 3 == 0
    return determinant_twice // 3


def normalize(centers):
    minx = min(x for x, _ in centers)
    miny = min(y for _, y in centers)
    return tuple(sorted((x-minx, y-miny) for x, y in centers))


def maximal_six_area(n):
    return (3*n*n + 14*n + 2)//3


def witness(n):
    k, r = divmod(n, 3)
    if r == 0: a, b, c = k-1, k+1, k-1
    elif r == 1: a, b, c = k, k+1, k-1
    else: a, b, c = k, k, k+1
    assert a >= 0 and b >= 0 and c >= 0
    points = {(0, j) for j in range(a+1)}
    points.update((i, a) for i in range(1, b+1))
    points.update((b+t, a-t) for t in range(1, c+1))
    assert len(points) == n
    return points, (a,b,c)


def test_witnesses():
    for n in range(3, 150):
        points, (a, b, c) = witness(n)
        computed = six_area_from_corners(points)
        expected = maximal_six_area(n) - (2 if n%3 == 2 else 1)
        formula = 3*(a*b+b*c+c*a)+6+6*(n-1)+2*b
        assert computed == formula == expected, (n,computed,formula,expected)
    print('PASS: 147 exact lattice-corner witness evaluations (n=3..149)')


def test_spanning_tree_arithmetic():
    for n in range(3, 110):
        s = n-1
        optimum = maximal_six_area(n)
        for a in range(s+1):
            for b in range(s-a+1):
                c = s-a-b
                m = max(a,b,c)
                L = 3*(a*b+b*c+c*a)+6+6*s+2*m
                assert L <= optimum, (n,a,b,c,L,optimum)
                if n%3 == 2:
                    assert L == optimum or L <= optimum-3, (n,a,b,c,L)
    print('PASS: all spanning-tree count triples for n=3..109')


def test_all_polyhexes():
    shapes = {((0, 0),)}
    for n in range(1, 10):
        spectrum = Counter(six_area_from_corners(shape) for shape in shapes)
        if n >= 3:
            top = sorted(spectrum, reverse=True)[:2]
            expected = [maximal_six_area(n), maximal_six_area(n)-(2 if n%3==2 else 1)]
            assert top == expected, (n, top, expected)
            print(f'PASS: exhaustive n={n}, fixed polyhexes={len(shapes)}, 6*top2={top}')
        if n == 9:
            break
        next_shapes = set()
        for shape in shapes:
            S = set(shape)
            for q, r in shape:
                for dx, dy in NEIGHBORS:
                    p = (q+dx,r+dy)
                    if p not in S:
                        next_shapes.add(normalize(S | {p}))
        shapes = next_shapes


if __name__ == '__main__':
    test_witnesses()
    test_spanning_tree_arithmetic()
    test_all_polyhexes()
    print('All checks passed; finite enumeration is not a proof for arbitrary n.')
