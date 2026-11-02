#!/usr/bin/env python3
"""Exact rational, independent pair-of-edges verifier for unit-edge ladder networks.

No third-party packages, network access, or research framework required.
Run: python verify_ladders.py
"""
from collections import deque
from fractions import Fraction as F

ZERO, ONE, HALF = F(0), F(1), F(1, 2)


def graphs(n, periodic):
    assert n >= 3
    edges = []
    for i in range(n):
        edges.append((('top', i), ('bottom', i)))
    for row in ('top', 'bottom'):
        for i in range(n-1):
            edges.append(((row, i), (row, i+1)))
        if periodic:
            edges.append(((row, n-1), (row, 0)))
    return edges


def vertex_distances(edges):
    adj = {}
    for a, b in edges:
        adj.setdefault(a, set()).add(b)
        adj.setdefault(b, set()).add(a)
    result = {}
    for a in adj:
        d = {a: 0}
        queue = deque([a])
        while queue:
            v = queue.popleft()
            for w in adj[v]:
                if w not in d:
                    d[w] = d[v] + 1
                    queue.append(w)
        assert len(d) == len(adj)
        result[a] = d
    return result


def affine(terms, x, y):
    a, b, c = terms
    return a*x+b*y+c


def clip_polygon(poly, bound):
    """Return points satisfying affine(bound) <= 0, exactly."""
    if not poly:
        return []
    out = []
    for i, p in enumerate(poly):
        q = poly[(i+1) % len(poly)]
        fp, fq = affine(bound, *p), affine(bound, *q)
        if fp <= 0:
            out.append(p)
        if (fp < 0 and fq > 0) or (fp > 0 and fq < 0):
            t = fp/(fp-fq)
            out.append((p[0]+t*(q[0]-p[0]), p[1]+t*(q[1]-p[1])))
        elif fp > 0 and fq == 0:
            out.append(q)
    clean = []
    for p in out:
        if not clean or clean[-1] != p:
            clean.append(p)
    if len(clean) > 1 and clean[0] == clean[-1]:
        clean.pop()
    return clean


def integrate_affine_on_polygon(poly, terms):
    if len(poly) < 3:
        return ZERO, ZERO
    first, second = ZERO, ZERO
    p0 = poly[0]
    for i in range(1, len(poly)-1):
        p1, p2 = poly[i:i+2]
        area = abs((p1[0]-p0[0])*(p2[1]-p0[1])-
                   (p1[1]-p0[1])*(p2[0]-p0[0]))/2
        v0, v1, v2 = (affine(terms, *p) for p in (p0, p1, p2))
        first += area*(v0+v1+v2)/3
        second += area*(v0*v0+v1*v1+v2*v2+v0*v1+v1*v2+v2*v0)/6
    return first, second


def edge_pair_moments(e, f, distances):
    if e == f:
        return F(1, 3), F(1, 6)
    a, b = e
    c, d = f
    # Affine shortest-path candidates for points at x on e, y on f.
    forms = ((ONE, ONE, F(distances[a][c])),
             (ONE, -ONE, F(1+distances[a][d])),
             (-ONE, ONE, F(1+distances[b][c])),
             (-ONE, -ONE, F(2+distances[b][d])))
    total1, total2 = ZERO, ZERO
    for i, form in enumerate(forms):
        poly = [(ZERO, ZERO), (ONE, ZERO), (ONE, ONE), (ZERO, ONE)]
        for j, other in enumerate(forms):
            if i != j:
                poly = clip_polygon(poly, tuple(u-v for u, v in zip(form, other)))
                if len(poly) < 3:
                    break
        m1, m2 = integrate_affine_on_polygon(poly, form)
        total1 += m1
        total2 += m2
    return total1, total2


def predicted(n, periodic):
    n = F(n)
    if not periodic:
        m1 = n*(9*n*n-4*n-4)/(3*(3*n-2)**2)
        m2 = (27*n**4-16*n**3+42*n*n-38*n-12)/(18*(3*n-2)**2)
    elif int(n) % 2 == 0:
        m1 = n/4+F(14,27)+1/(27*n)
        m2 = (9*n**3+28*n*n+48*n+20)/(108*n)
    else:
        m1 = n/4+F(14,27)+1/(108*n)
        m2 = (9*n**3+28*n*n+45*n+16)/(108*n)
    return m1, m2


def exact_test(n, periodic):
    edges = graphs(n, periodic)
    distances = vertex_distances(edges)
    moment1, moment2 = ZERO, ZERO
    for i, e in enumerate(edges):
        for j in range(i, len(edges)):
            a, b = edge_pair_moments(e, edges[j], distances)
            fac = 1 if i == j else 2
            moment1 += fac*a
            moment2 += fac*b
    result = (moment1/len(edges)**2, moment2/len(edges)**2)
    expected = predicted(n, periodic)
    assert result == expected, (n, periodic, result, expected)
    return len(edges)*(len(edges)+1)//2


def main():
    checks = 0
    for n in range(3, 10):
        for periodic in (False, True):
            pairs = exact_test(n, periodic)
            checks += 2*pairs
            print(f"PASS n={n:2d} periodic={periodic} edge_pairs={pairs} exact_moments=2")
    print(f"PASS: {checks} exact rational moment comparisons over 14 metric networks")

if __name__ == '__main__':
    main()
