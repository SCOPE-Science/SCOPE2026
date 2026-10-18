#!/usr/bin/env python3
"""Exact, independent finite checks of the odd-cycle-chain inertia theorem.

Run with Python 3.9+; requires only the standard library. This enumerates
finite instances; the theorem for all lengths rests on the symbolic proof.
"""
from fractions import Fraction as F
from itertools import product
from collections import Counter


def build(lengths, distances):
    """Cycles in a block path; distances choose the next exit in each new block."""
    v = lengths[0]
    edges = [(i, (i + 1) % v) for i in range(v)]
    exit_vertex = 0
    # Each new cycle has vertex 0 identified with the preceding exit.
    for j, ell in enumerate(lengths[1:]):
        cyc = [exit_vertex] + list(range(v, v + ell - 1))
        v += ell - 1
        edges.extend((cyc[i], cyc[(i + 1) % ell]) for i in range(ell))
        if j < len(lengths) - 2:
            d = distances[j]
            assert 1 <= d < ell
            exit_vertex = cyc[d]
    assert len(edges) == sum(lengths)
    return v, edges


def shifted_q(n, edges):
    a = [[0] * n for _ in range(n)]
    for i, j in edges:
        a[i][i] += 1
        a[j][j] += 1
        a[i][j] += 1
        a[j][i] += 1
    for i in range(n):
        a[i][i] -= 2
    return a


def line_adj(edges):
    m = len(edges)
    a = [[0] * m for _ in range(m)]
    for i, (u, v) in enumerate(edges):
        for j in range(i):
            x, y = edges[j]
            if u == x or u == y or v == x or v == y:
                a[i][j] = a[j][i] = 1
    return a


def inertia(matrix):
    """Exact rational symmetric congruence, with 1x1 and 2x2 pivot blocks."""
    a = [[F(x) for x in row] for row in matrix]
    plus = minus = zero = 0
    while a:
        n = len(a)
        diag = next((i for i in range(n) if a[i][i]), None)
        if diag is not None:
            others = [i for i in range(n) if i != diag]
            p = a[diag][diag]
            plus += p > 0
            minus += p < 0
            a = [[a[i][j] - a[i][diag] * a[diag][j] / p
                  for j in others] for i in others]
            continue
        pair = next(((i, j) for i in range(n) for j in range(i + 1, n)
                     if a[i][j]), None)
        if pair is None:
            zero += n
            break
        i, j = pair
        p = a[i][j]
        others = [k for k in range(n) if k != i and k != j]
        plus += 1
        minus += 1
        a = [[a[x][y] - (a[x][i]*a[j][y] + a[x][j]*a[i][y]) / p
              for y in others] for x in others]
    return (plus, zero, minus)


def det(matrix):
    """Fraction-free Bareiss determinant, with exact row exchanges."""
    a = [row[:] for row in matrix]
    n = len(a)
    if n == 0:
        return 1
    sign, prev = 1, 1
    for k in range(n-1):
        if a[k][k] == 0:
            r = next((r for r in range(k+1,n) if a[r][k]), None)
            if r is None:
                return 0
            a[k], a[r] = a[r], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator = a[i][j]*pivot-a[i][k]*a[k][j]
                assert numerator % prev == 0
                a[i][j] = numerator // prev
        for i in range(k+1,n):
            a[i][k] = 0
        prev = pivot
    return sign*a[-1][-1]


def check(lengths, distances):
    n, edges = build(lengths, distances)
    t = len(lengths)
    q = sum(x % 4 == 1 for x in lengths)
    H = (n-1)//2
    predicted = (H+1, 0, H+t-1) if q else (H, 0, H+t)
    predicted_det = ((-1)**(q-1)*2**(t-1)*(4*q-2)) if q else 2**t
    M = shifted_q(n, edges)
    L = line_adj(edges)
    got_q = inertia(M)
    got_line = inertia(L)
    expect_q = (H+1,0,H) if q else (H,0,H+1)
    assert got_q == expect_q, (lengths, distances, got_q, expect_q)
    assert got_line == predicted, (lengths, distances, got_line, predicted)
    got_det = det(L)
    assert got_det == predicted_det, (lengths, distances, got_det, predicted_det)
    return len(edges)


def main():
    cases, max_vertices, max_edges = 0, 0, 0
    hist = Counter()
    for t in range(1, 6):
        choices = [3, 5, 7, 9] if t <= 3 else [3, 5]
        for ls in product(choices, repeat=t):
            # A size-bounded exhaustive sweep, including 9-cycles for t<=3.
            if sum(ls) > 23:
                continue
            options = [range(1, ls[j]) for j in range(1,t-1)]
            for ds in product(*options):
                edges = check(ls, ds)
                cases += 1
                hist[t] += 1
                max_vertices = max(max_vertices, 1 + sum(x-1 for x in ls))
                max_edges = max(max_edges, edges)
    # A branching counterexample: three pendant pentagons joined at
    # successive vertices 0,1,2 of a central pentagon.
    E=[(i,(i+1)%5) for i in range(5)]
    v=5
    for root in (0,1,2):
        cyc=[root]+list(range(v,v+4))
        v+=4
        E.extend((cyc[i],cyc[(i+1)%5]) for i in range(5))
    branch = inertia(line_adj(E))
    assert branch == (10,0,10), branch
    assert det(line_adj(E)) == 400
    print('PASS exact rational odd-cycle-chain tests:', cases)
    print('Cases by block count:', dict(sorted(hist.items())))
    print('Maximum tested vertices:', max_vertices, 'maximum edges:', max_edges)
    print('PASS branching example: inertia (10,0,10), determinant 400')
    print('All checks exact; finite checks do not establish the infinite theorem.')

if __name__ == '__main__':
    main()
