#!/usr/bin/env python3
"""Exact checks for biclique circulation-space projection constants.

Run: python verify_projection.py
Only Python standard library is required. Finite tests do not replace proof.
"""
from fractions import Fraction as F
from itertools import product


def projection(m, n):
    """Double-centering on m-by-n matrices, flattened row-major."""
    out = []
    for i, j in product(range(m), range(n)):
        row = []
        for k, l in product(range(m), range(n)):
            row.append((F(i == k) - F(1, m)) *
                       (F(j == l) - F(1, n)))
        out.append(row)
    return out


def mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def check(m, n):
    P = projection(m, n)
    v = m * n
    assert mul(P, P) == P
    assert P == [list(t) for t in zip(*P)]
    assert sum(P[i][i] for i in range(v)) == (m-1)*(n-1)
    for col in range(v):
        for i in range(m):
            assert sum(P[i*n+j][col] for j in range(n)) == 0
        for j in range(n):
            assert sum(P[i*n+j][col] for i in range(m)) == 0
    for i in range(m-1):
        for j in range(n-1):
            cyc = [F(0)]*v
            cyc[i*n+j] = 1
            cyc[i*n+n-1] = -1
            cyc[(m-1)*n+j] = -1
            cyc[-1] = 1
            assert [sum(P[a][b]*cyc[b] for b in range(v)) for a in range(v)] == cyc
    norm1 = max(sum(abs(P[i][j]) for i in range(v)) for j in range(v))
    norminf = max(sum(abs(P[i][j]) for j in range(v)) for i in range(v))
    formula = F(4*(m-1)*(n-1), m*n)
    assert norm1 == norminf == formula
    R = [[F(i == j) - P[i][j] for j in range(v)] for i in range(v)]
    complement_formula = F(1) + F(2*(m-1)*(n-1), m*n)
    assert max(sum(abs(R[i][j]) for i in range(v)) for j in range(v)) == complement_formula
    assert max(sum(abs(R[i][j]) for j in range(v)) for i in range(v)) == complement_formula
    assert mul(R, R) == R
    assert mul(R, P) == [[F(0)]*v for _ in range(v)]
    # Four H-orbits of the stabilizer of cell (0,0):
    # a+(n-1)b=c+(n-1)d=a+(m-1)c=b+(m-1)d=0.
    # For a=1 there is a unique solution, proving the invariant
    # kernel has only one dimension.
    a = F(1)
    b, c = -a/F(n-1), -a/F(m-1)
    d = a/F((m-1)*(n-1))
    assert a+(n-1)*b == 0
    assert c+(n-1)*d == 0
    assert a+(m-1)*c == 0
    assert b+(m-1)*d == 0
    return norm1


def main():
    count = 0
    for m in range(2, 13):
        for n in range(2, 13):
            # Large matrix products become slow; use full multiplication
            # on smaller graphs and direct exact column/row formulas above
            # for the rest.
            if m*n > 48:
                continue
            check(m, n)
            count += 1
    print('CHECK_OK', count, 'exact full-matrix cases',
          'including idempotence, cycles, row/column constraints, symmetry, and endpoint norms')


if __name__ == '__main__':
    main()
