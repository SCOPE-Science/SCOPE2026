#!/usr/bin/env python3
"""Exact finite algebra checks for adjacency quantum walks on two-fold blowups of triangle-and-leaf cones.

The unbounded spectral and Diophantine arguments are supplied in RESULT.md;
finite checks are corroboration, not a substitute for those arguments.
"""
from fractions import Fraction
from math import comb


def graph(s):
    """Vertex order: apex, edge endpoint 1, edge endpoint 2, s leaves."""
    n = s + 3
    a = [[0] * n for _ in range(n)]
    for j in range(1, n):
        a[0][j] = a[j][0] = 1
    a[1][2] = a[2][1] = 1
    return a


def multiply(a, b):
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n)) for j in range(n)]
            for i in range(n)]


def charpoly_from_traces(a):
    """Newton identities: descending coefficients, exact rational arithmetic."""
    n = len(a)
    power = [[int(i == j) for j in range(n)] for i in range(n)]
    traces = [0]
    for k in range(1, n + 1):
        power = multiply(power, a)
        traces.append(sum(power[i][i] for i in range(n)))
    p = [Fraction(1)]
    for k in range(1, n + 1):
        coeff = -sum(p[k - j] * traces[j] for j in range(1, k + 1)) / k
        assert coeff.denominator == 1
        p.append(coeff)
    return [int(c) for c in p]


def poly_mul(a, b):
    """Descending coefficient multiplication."""
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] += ai * bj
    return out


def predicted(s):
    p = [1, -1, -(s + 2), s]
    p = poly_mul([1, 1], p)
    return p + [0] * (s - 1)


def rational_rank(a):
    m = [[Fraction(v) for v in row] for row in a]
    n = len(m)
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, n) if m[i][c]), None)
        if pivot is None:
            continue
        m[r], m[pivot] = m[pivot], m[r]
        v = m[r][c]
        m[r] = [x / v for x in m[r]]
        for i in range(n):
            if i != r and m[i][c]:
                v = m[i][c]
                m[i] = [u - v * w for u, w in zip(m[i], m[r])]
        r += 1
    return r


def cubic(s, r):
    return r**3 - r**2 - (s + 2)*r + s


def verify():
    count = 0
    for s in range(1, 21):
        a = graph(s)
        assert charpoly_from_traces(a) == predicted(s), s
        # The nullspace is exactly the zero-sum leaf space for s>1.
        assert len(a) - rational_rank(a) == s - 1, s
        assert cubic(s, 0) == s and cubic(s, 1) == -2
        assert cubic(s, -1) == 2 * s
        count += 1
    roots = []
    for s in range(1, 2001):
        # An integer root of the monic cubic must be an integer,
        # and (r-1) divides 2 by the identity below.
        for r in (-1, 0, 2, 3):
            assert cubic(s, r) == (r - 1) * (r*r - s - 2) - 2
            if cubic(s, r) == 0:
                roots.append((s, r))
    assert roots == [(6, 3)], roots
    assert poly_mul([1, -3], [1, 2, -2]) == [1, -1, -8, 6]
    # For f_6 roots (3,-1+sqrt(3),-1-sqrt(3)), relations
    # plus optional eigenvalue -1: b=c and d=3*a-2*b.
    relations = 0
    for a in range(-20, 21):
        for b in range(-20, 21):
            c = b
            d = 3*a - 2*b
            assert (a + b + c + d) % 2 == 0
            # For the cubic alone, d=0 and 3*a=2*b.
            if d == 0:
                assert (a + b + c) % 2 == 0
            relations += 1
    print(f'VERIFY_OK exact_graph_charpolys={count} exact_nullities={count} '
          f'integer_root_scope=2000 exceptional_roots={roots} '
          f'exceptional_integer_relations={relations}')


if __name__ == '__main__':
    verify()
