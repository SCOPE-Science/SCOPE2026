#!/usr/bin/env python3
"""Exact-rational independent edge-pair diameter checks for weighted complete networks."""
from fractions import Fraction as Q
from itertools import combinations


def edge_length(e, lam):
    return lam if e == (0, 1) else Q(1)


def vertex_dist(a, b, lam):
    if a == b:
        return Q(0)
    return min(lam, Q(2)) if {a, b} == {0, 1} else Q(1)


def intersection(l1, l2):
    a, b, c = l1
    d, e, f = l2
    det = a * e - b * d
    if not det:
        return None
    return ((c * e - b * f) / det, (a * f - c * d) / det)


def max_between_edges(e, f, lam):
    le, lf = edge_length(e, lam), edge_length(f, lam)
    funcs = []
    for i, a in enumerate(e):
        for j, b in enumerate(f):
            s, t = (Q(1) if i == 0 else Q(-1)), (Q(1) if j == 0 else Q(-1))
            c = (Q(0) if i == 0 else le) + (Q(0) if j == 0 else lf) + vertex_dist(a, b, lam)
            funcs.append((s, t, c))
    lines = [(Q(1), Q(0), Q(0)), (Q(1), Q(0), le),
             (Q(0), Q(1), Q(0)), (Q(0), Q(1), lf)]
    for i, j in combinations(range(4), 2):
        a, b, c = funcs[i]
        d, h, k = funcs[j]
        if (a, b) != (d, h):
            lines.append((a-d, b-h, k-c))
    candidates = []
    for l1, l2 in combinations(lines, 2):
        xy = intersection(l1, l2)
        if xy is None:
            continue
        x, y = xy
        if 0 <= x <= le and 0 <= y <= lf:
            candidates.append(min(a*x+b*y+c for a, b, c in funcs))
    assert candidates
    return max(candidates)


def diam_exact(n, lam):
    edges = list(combinations(range(n), 2))
    top = Q(0)
    for e in edges:
        le = edge_length(e, lam)
        same = min(le, (le + 2) / 2) if e == (0, 1) else Q(1)
        top = max(top, same)
    for e, f in combinations(edges, 2):
        top = max(top, max_between_edges(e, f, lam))
    return top


def run():
    checked = 0
    for n in (3, 4, 5, 6):
        for lam in (Q(1, 7), Q(1, 4), Q(3, 4), Q(1), Q(5, 4), Q(3), Q(11)):
            exact = diam_exact(n, lam)
            expected = (lam+2)/2 if n == 3 else ((lam+3)/2 if n == 4 else max(Q(2), (lam+3)/2))
            assert exact == expected, (n, lam, exact, expected)
            checked += 1
    for n in range(3, 43):
        m = n * (n-1) // 2
        for lam in (Q(1, 100), Q(1, 5), Q(1, 2), Q(4, 5), Q(1), Q(6, 5), Q(2), Q(17)):
            D = (lam+2)/2 if n == 3 else ((lam+3)/2 if n == 4 else max(Q(2), (lam+3)/2))
            r = D / (m-1+lam)
            if n == 3:
                assert r == Q(1,2)
            elif n >= 5:
                assert r >= Q(2,m)
                assert (r == Q(2,m)) == (lam == 1)
            else:
                assert (r < Q(1,3)) == (lam < 1)
    print('PASS: {} exact-rational continuous diameter configurations; 320 normalized comparisons'.format(checked))

if __name__ == '__main__':
    run()
