#!/usr/bin/env python3
"""Exact finite consistency tests for the hollow rank-two determinantal classification.

The general proof is the Schur-complement identity in RESULT.md;
finite-field tests here do not certify the general theorem by enumeration.
"""
from itertools import combinations, product
from math import comb
import sympy as sp


def rank_mod_p(rows, p):
    a = [[int(x) % p for x in row] for row in rows]
    m = len(a)
    rank = 0
    for c in range(m):
        pivot = next((r for r in range(rank, m) if a[r][c]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        scale = pow(a[rank][c], -1, p)
        a[rank] = [(v * scale) % p for v in a[rank]]
        for r in range(rank + 1, m):
            if a[r][c]:
                factor = a[r][c]
                a[r] = [(u - factor * v) % p for u, v in zip(a[r], a[rank])]
        rank += 1
        if rank == m:
            return rank
    return rank


def canonical_splits(vertices):
    vertices = tuple(sorted(vertices))
    anchor = vertices[0]
    for mask in range(1 << (len(vertices) - 1)):
        A = frozenset([anchor] + [v for j, v in enumerate(vertices[1:]) if mask & (1 << j)])
        B = frozenset(vertices) - A
        if B:
            yield A, B


def edges(A, B):
    return frozenset(tuple(sorted((i, j))) for i in A for j in B)


def combinatorial_checks():
    for n in range(3, 9):
        verts = frozenset(range(n))
        comps = list(canonical_splits(verts))
        assert len(comps) == 2 ** (n - 1) - 1
        pieces = [(w, A, B) for w in range(n)
                  for A, B in canonical_splits(verts - {w})]
        assert len(pieces) == n * (2 ** (n - 2) - 1)
        assert len({(w, edges(A, B)) for w, A, B in pieces}) == len(pieces)
        comp_supports = [edges(A, B) for A, B in comps]
        for w, A, B in pieces:
            E = edges(A, B)
            assert sum(E <= F for F in comp_supports) == 2
        degree = sum(comb(n - 2, len(A) - 1) for A, B in comps)
        sing_degree = sum(comb(n - 3, len(A) - 1) for w, A, B in pieces)
        assert degree == comb(2 * n - 2, n - 1) // 2
        assert sing_degree * 2 == n * comb(2 * n - 4, n - 2)
        if n <= 7:
            # The generic components of every intersection sit inside one of
            # the stated maximal singular Segre components.
            E_sing = [edges(A, B) for w, A, B in pieces]
            for i, j in combinations(range(len(comps)), 2):
                overlap = comp_supports[i] & comp_supports[j]
                if overlap:
                    assert all(any(e in T for T in E_sing) for e in overlap), (n, i, j)
        print(f'n={n}: components={len(comps)}, degree={degree}, '
              f'singular_components={len(pieces)}, singular_degree={sing_degree}')


def symbolic_pivot_check():
    x, bi, ci, bj, cj, zij = sp.symbols('x bi ci bj cj zij')
    test = sp.Matrix([[0, x, bj], [x, 0, cj], [bi, ci, zij]])
    assert sp.expand(test.det() + x*x*zij - x*(bi*cj+ci*bj)) == 0
    diagonal = sp.Matrix([[0, x, bi], [x, 0, ci], [bi, ci, 0]])
    assert sp.expand(diagonal.det() - 2*x*bi*ci) == 0
    print('symbolic Schur-complement minors verified')


def finite_field_check():
    p = 3
    for n in range(3, 6):
        pairs = list(combinations(range(n), 2))
        matched = 0
        for coords in product(range(p), repeat=len(pairs)):
            if not any(coords):
                continue
            A = [[0] * n for _ in range(n)]
            for (i, j), val in zip(pairs, coords):
                A[i][j] = A[j][i] = val
            r = rank_mod_p(A, p)
            if r > 2:
                continue
            matched += 1
            assert r == 2
            pivot_pair = next((i, j) for i, j in pairs if A[i][j])
            i, j = pivot_pair
            xinv = pow(A[i][j], -1, p)
            left, right = {i}, {j}
            for k in range(n):
                if k in (i, j):
                    continue
                b, c = A[i][k], A[j][k]
                assert b*c % p == 0
                if b:
                    right.add(k)
                else:
                    left.add(k)
            assert all(A[a][b] == 0 for a, b in combinations(left, 2))
            assert all(A[a][b] == 0 for a, b in combinations(right, 2))
            for k, l in combinations(range(n), 2):
                if k in (i, j) or l in (i, j):
                    continue
                assert A[k][l] == ((A[i][k]*A[j][l] + A[j][k]*A[i][l])*xinv) % p
        print(f'GF(3), n={n}: {matched} nonzero rank-two matrices exhaustively classified')


if __name__ == '__main__':
    symbolic_pivot_check()
    combinatorial_checks()
    finite_field_check()
    print('VERIFY_OK')
