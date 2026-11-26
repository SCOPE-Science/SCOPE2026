"""Small exact-rational checks of the signed Cesàro trace defect."""
from fractions import Fraction as Q
from itertools import product
from math import comb

checked = 0
for n in range(1, 8):
    C = [[Q(1, i+1) if j <= i else 0 for j in range(n)] for i in range(n)]
    B = [[sum(a*b for a, b in zip(C[i], C[j])) for j in range(n)] for i in range(n)]
    assert all(B[i][j] == Q(1, max(i, j)+1) for i, j in product(range(n), repeat=2))
    H = sum(Q(1, i) for i in range(1, n+1))
    A = [[int(i == j) for j in range(n)] for i in range(n)]
    for k in range(1, 9):
        A = [[sum(A[i][t]*B[t][j] for t in range(n)) for j in range(n)] for i in range(n)]
        trace = sum(A[i][i] for i in range(n))
        if k == 1:
            assert trace == H
        else:
            c = comb(2*k-2, k-1)
            assert 0 < c*H-trace <= k*c
            if k == 2:
                assert c*H-trace == sum(Q(1, j*j) for j in range(1, n+1))
            checked += 1
print(f"PASS: {checked} signed exact-rational trace-defect checks plus trace identities")
