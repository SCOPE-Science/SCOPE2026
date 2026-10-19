#!/usr/bin/env python3
"""Exact finite checks for descent / inverse-descent covariance and sharp linear correlation."""
from itertools import permutations
from fractions import Fraction as F
from math import factorial


def inverse(matrix):
    n = len(matrix)
    a = [list(matrix[i]) + [F(int(i == j)) for j in range(n)] for i in range(n)]
    for col in range(n):
        pivot = next(i for i in range(col, n) if a[i][col])
        a[col], a[pivot] = a[pivot], a[col]
        div = a[col][col]
        a[col] = [t / div for t in a[col]]
        for i in range(n):
            if i != col:
                mult = a[i][col]
                a[i] = [a[i][j] - mult * a[col][j] for j in range(2 * n)]
    return [row[n:] for row in a]


def check(n):
    m = n - 1
    sums_dd = [[0] * m for _ in range(m)]
    sums_de = [[0] * m for _ in range(m)]
    sums_ee = [[0] * m for _ in range(m)]
    nd = [0] * m
    ne = [0] * m
    total = 0
    for p in permutations(range(n)):
        q = [0] * n
        for i, v in enumerate(p):
            q[v] = i
        d = [int(p[i] > p[i+1]) for i in range(m)]
        e = [int(q[j] > q[j+1]) for j in range(m)]
        total += 1
        for i in range(m):
            nd[i] += d[i]
            ne[i] += e[i]
            for j in range(m):
                sums_dd[i][j] += d[i] * d[j]
                sums_ee[i][j] += e[i] * e[j]
                sums_de[i][j] += d[i] * e[j]
    assert total == factorial(n)
    assert nd == ne == [total // 2] * m
    C = F(1, 2*n*(n-1))
    A = [[F(1,4) if i==j else (F(-1,12) if abs(i-j)==1 else F(0)) for j in range(m)] for i in range(m)]
    tests = 0
    for i in range(m):
        for j in range(m):
            assert F(sums_de[i][j],total)-F(1,4)==C
            assert F(sums_dd[i][j],total)-F(1,4)==A[i][j]
            assert F(sums_ee[i][j],total)-F(1,4)==A[i][j]
            tests += 3
    B = inverse(A)
    w = [sum(B[i], F(0)) for i in range(m)]
    for i in range(m):
        assert sum((A[i][j]*w[j] for j in range(m)), F(0)) == 1
        tests += 1
    rho = C * sum(w)
    expected = {2:F(1),3:F(1),4:F(13,14),5:F(21,25),6:F(34,45),7:F(62,91),8:F(813,1316)}[n]
    assert rho==expected
    tests += 1
    # Centered covariance identities and variational equality for arbitrary small weights.
    test_weights = [ [F(i+1) for i in range(m)], [F((-1)**i) for i in range(m)], [F(1) for _ in range(m)] ]
    for u in test_weights:
        vu = sum((u[i]*A[i][j]*u[j] for i in range(m) for j in range(m)),F(0))
        assert sum(u)**2 <= sum(w)*vu
        assert (C*sum(u)**2)**2 <= (rho**2)*vu**2
        tests += 2
    return tests, rho, w


def main():
    assertions = 0
    for n in range(2,9):
        checks, rho, w = check(n)
        assertions += checks
        print(f'n={n}: {checks} exact identities; canonical correlation={rho}, weights={w}')
    print(f'PASS: {assertions} exact covariance, inversion and optimization identities')

if __name__ == '__main__':
    main()
