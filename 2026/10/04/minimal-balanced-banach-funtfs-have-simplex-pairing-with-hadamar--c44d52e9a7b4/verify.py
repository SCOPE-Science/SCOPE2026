#!/usr/bin/env python3
from fractions import Fraction

def sylvester(order):
    H = [[1]]
    while len(H) < order:
        m = len(H)
        H = [row + row for row in H] + [row + [-x for x in row] for row in H]
    return H

def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]

def transpose(A):
    return [list(col) for col in zip(*A)]

cases = 0
for r in range(2, 9):
    N = 2**r
    n = N - 1
    H = sylvester(N)
    assert H[0] == [1]*N
    # Hadamard identity.
    HHt = matmul(H, transpose(H))
    for i in range(N):
        for j in range(N):
            assert HHt[i][j] == (N if i == j else 0)

    S = H[1:]                 # n x N sign matrix
    cols = transpose(S)       # N vectors s_j in R^n

    # Balance.
    assert all(sum(S[i][j] for j in range(N)) == 0 for i in range(n))

    # Unit norms and diagonal pairings for x_j=s_j/n, f_j=s_j.
    for s in cols:
        assert sum(abs(v) for v in s) == n
        assert max(abs(v) for v in s) == 1
        assert Fraction(sum(v*v for v in s), n) == 1

    # Pairing matrix: 1 on the diagonal, -1/n off diagonal.
    for i, si in enumerate(cols):
        for j, sj in enumerate(cols):
            val = Fraction(sum(a*b for a,b in zip(si,sj)), n)
            assert val == (Fraction(1,1) if i == j else Fraction(-1,n))

    # Frame operator (1/n) S S^T = (N/n) I.
    SSt = matmul(S, transpose(S))
    for i in range(n):
        for j in range(n):
            lhs = Fraction(SSt[i][j], n)
            rhs = Fraction(N, n) if i == j else Fraction(0,1)
            assert lhs == rhs
    cases += 1

print(f"VERIFY_OK sylvester_cases={cases} r_range=2..8")
