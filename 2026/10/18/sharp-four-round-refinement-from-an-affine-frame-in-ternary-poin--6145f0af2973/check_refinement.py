#!/usr/bin/env python3
"""Direct exhaustive verification of marked ternary affine point-hyperplane graphs.

This is a finite sanity check, not a proof for unbounded dimension.
Run: python check_refinement.py
"""
from collections import Counter
from itertools import product


def graph(d):
    points = list(product(range(3), repeat=d))
    normals = []
    for a in points[1:]:
        first = next(i for i, x in enumerate(a) if x)
        if a[first] == 1:
            normals.append(a)
    planes = [(a, b) for a in normals for b in range(3)]
    n = len(points)
    neighbors = [[] for _ in range(n + len(planes))]
    for j, (a, b) in enumerate(planes, n):
        for i, x in enumerate(points):
            if sum(u*v for u, v in zip(a, x)) % 3 == b:
                neighbors[i].append(j)
                neighbors[j].append(i)
    return points, planes, neighbors


def refine(nbr, marked_indices, num_points):
    mark_colors = {x: i + 2 for i, x in enumerate(marked_indices)}
    colors = [mark_colors.get(i, 0) for i in range(num_points)] + [1] * (len(nbr) - num_points)
    layers = []
    for round_number in range(8):
        count = Counter(colors)
        num_unique = sum(v == 1 for v in count.values())
        pcount = len(set(colors[:num_points]))
        hcount = len(set(colors[num_points:]))
        layers.append((round_number, pcount, hcount, num_unique))
        if num_unique == len(nbr):
            break
        sig = [(colors[i], tuple(sorted(Counter(colors[j] for j in nb).items()))) for i, nb in enumerate(nbr)]
        order = {s: k for k, s in enumerate(sorted(set(sig)))}
        nxt = [order[s] for s in sig]
        if len(set(nxt)) == len(set(colors)):
            break
        colors = nxt
    return layers, colors


def check(d):
    points, planes, nbr = graph(d)
    basis = [(0,) * d] + [tuple(int(j == i) for j in range(d)) for i in range(d)]
    marks = [points.index(x) for x in basis]
    layers, colors = refine(nbr, marks, len(points))
    assert layers[-1][0] == 4, (d, layers)
    assert layers[1][1] == d + 2, (d, layers)  # d+1 singleton marks plus one unmarked point class
    assert layers[1][2] == 2 ** (d + 1) - 1, (d, layers)
    assert layers[3][1] == layers[2][1], (d, layers)
    assert layers[3][2] == len(planes), (d, layers)
    assert layers[-1][1] == len(points), (d, layers)
    assert layers[-1][2] == len(planes), (d, layers)
    def pos(*ls):
        return points.index(tuple(ls) + (0,) * (d - len(ls)))
    assert colors[pos(1, 1)] != colors[pos(1, 2)]  # separated by final round
    # Recompute round 2 to verify the explicit non-discrete triple.
    cc = [{marks[k]: k + 2 for k in range(len(marks))}.get(i, 0) for i in range(len(points))] + [1]*len(planes)
    for _ in range(2):
        ss = [(cc[i], tuple(sorted(Counter(cc[j] for j in nb).items()))) for i, nb in enumerate(nbr)]
        rr = {s:k for k, s in enumerate(sorted(set(ss)))}
        cc = [rr[s] for s in ss]
    assert len({cc[pos(1,1)], cc[pos(1,2)], cc[pos(2,1)]}) == 1
    print(f"dimension={d} points={len(points)} hyperplanes={len(planes)} vertices={len(nbr)} rounds=4 layers={layers}")


if __name__ == '__main__':
    for d in range(2, 7):
        check(d)
    print('PASS direct ternary incidence-graph refinement')
