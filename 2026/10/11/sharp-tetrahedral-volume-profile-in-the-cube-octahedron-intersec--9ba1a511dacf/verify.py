#!/usr/bin/env python3
"""Exact determinant/Bernstein certificate for tetrahedra in cube-octahedron intersections.
Python 3 standard library only; no external files required.
"""
from itertools import permutations, product, combinations
from fractions import Fraction
from math import comb


def vertex_set(branch):
    # Affine coordinates (constant, coefficient of t or u).
    seed = ((1, 0), (0, 1), (0, 0)) if branch == 1 else ((1, 0), (1, 0), (0, 1))
    return sorted({tuple((sign[i]*a, sign[i]*b) for i, (a, b) in enumerate(perm))
                   for perm in set(permutations(seed))
                   for sign in product((-1, 1), repeat=3)})


def add(p, q, sign=1):
    return tuple(p[i] + sign*q[i] for i in range(4))


def times(p, q):
    return tuple(sum(p[j]*q[i-j] for j in range(i+1)) for i in range(4))


def det4(verts):
    a, b, c, d = verts
    edges = [[(v[j][0] - a[j][0], v[j][1] - a[j][1], 0, 0) for j in range(3)]
             for v in (b, c, d)]
    out = (0, 0, 0, 0)
    for perm in permutations(range(3)):
        sign = (-1)**sum(perm[i] > perm[j] for i in range(3) for j in range(i+1, 3))
        term = times(times(edges[0][perm[0]], edges[1][perm[1]]), edges[2][perm[2]])
        out = add(out, term, sign)
    return out


def bernstein_nonnegative_on(poly, left, right):
    # Transform f(left + (right-left)*s) into the degree-three Bernstein basis.
    ordinary = [sum(Fraction(poly[j])*comb(j, k)*left**(j-k)*(right-left)**k
                    for j in range(k, 4)) for k in range(4)]
    bernstein = [sum(ordinary[k]*Fraction(comb(i, k), comb(3, k))
                     for k in range(i+1)) for i in range(4)]
    return all(b >= 0 for b in bernstein), bernstein


def formatted_vertex(v):
    return '(' + ', '.join(str(a) if b == 0 else (str(b) + '*parameter' if a == 0 else f'{a}+{b}*parameter')
                           for a, b in v) + ')'


def main():
    totals = 0
    for branch in (1, 2):
        vertices = vertex_set(branch)
        assert len(vertices) == 24
        regimes = ([(Fraction(0), Fraction(1, 2), (2, 2, 4, 0)),
                    (Fraction(1, 2), Fraction(1), (0, 8, 0, 0))]
                   if branch == 1 else
                   [(Fraction(0), Fraction(1), (8, 0, 8, 0))])
        witnesses = [None] * len(regimes)
        counter = 0
        distinct = set()
        for inds in combinations(range(24), 4):
            p = det4([vertices[i] for i in inds])
            distinct.add(p)
            counter += 1
            for j, (lo, hi, bound) in enumerate(regimes):
                for sig in (-1, 1):
                    difference = add(bound, p, sig)
                    ok, coefficients = bernstein_nonnegative_on(difference, lo, hi)
                    if not ok:
                        raise AssertionError(('Invalid universal upper bound', branch, inds, p, lo, hi, sig, coefficients))
                if witnesses[j] is None and (p == bound or p == tuple(-v for v in bound)):
                    witnesses[j] = inds
        assert counter == comb(24, 4) == 10626
        assert all(w is not None for w in witnesses)
        totals += counter*len(regimes)*2
        print('branch', branch, 'vertices',len(vertices),'quadruples', counter,
              'distinct_determinants',len(distinct))
        for j, witness in enumerate(witnesses):
            print(' interval',j,'witness=',[formatted_vertex(vertices[i]) for i in witness],
                  'det=',det4([vertices[i] for i in witness]))
    print('VERIFY_OK Bernstein_polynomial_inequalities=',totals)

if __name__ == '__main__':
    main()
