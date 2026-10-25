#!/usr/bin/env python3
"""Independent finite checks for cyclic incidence-poset type spectra.

Implements direct enumerations of lower/upper choices, separately from the
transfer-matrix recurrence and the claimed closed-form mixed-cut count.
"""
from itertools import product


def matmul(A, B):
    n = len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def trace_power(r, n):
    T = [[0]*r for _ in range(r)]
    for i in range(r):
        T[i][0] += 1
        if i+1 < r: T[i][i+1] += 1
        else: T[i][i] += 2
    P = [[int(i == j) for j in range(r)] for i in range(r)]
    for _ in range(n): P = matmul(P,T)
    return sum(P[i][i] for i in range(r))


def direct_counts(r, n, u=1, v=1):
    # The upper neighbor mask of each lower vertex a_i.
    N = [sum(1 << ((i+d)%n) for d in range(r)) for i in range(n)]
    J = 0
    mixed = 0
    for X in range(1 << n):
        # Count ideals by choosing included lower elements X, with only
        # those upper vertices whose full lower neighborhoods are in X.
        # Construct lower-neighbor masks independently of N.
        free_upper = 0
        for j in range(n):
            need = sum(1 << ((j-d)%n) for d in range(r))
            if need & ~X == 0:
                free_upper += 1
        J += 1 << free_upper
        if X:
            common = (1 << n)-1
            for i in range(n):
                if X >> i & 1:
                    common &= N[i]
            mixed += (u ** X.bit_count()) * ((1+v) ** common.bit_count()-1)
    return J, mixed


if __name__ == '__main__':
    checks=0
    for r in range(1,7):
        for n in range(2*r+1, 2*r+4):
            J, B = direct_counts(r,n)
            T = trace_power(r,n)
            assert J == T, (r,n,J,T)
            assert B == n*r*(1 << (r-1)), (r,n,B)
            _, weighted = direct_counts(r,n,2,3)
            expected_weighted = n*(2*((1+3)**r-1) + sum(2**2 * (1+2)**(s-1) * ((1+3)**(r-s)-1) for s in range(1,r)))
            assert weighted == expected_weighted, (r,n,weighted,expected_weighted)
            t = 2*J-1+B
            print(f'r={r} n={n} ideals={J} mixed={B} nonalgebraic_types={t} OK')
            checks += 1
    print(f'PASS: {checks} distinct (r,n) instances, all independent counts and bivariate checks agree')
