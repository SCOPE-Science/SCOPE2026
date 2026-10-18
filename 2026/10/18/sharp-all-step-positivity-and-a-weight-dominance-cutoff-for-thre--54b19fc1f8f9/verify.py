#!/usr/bin/env python3
"""Reproduce exact arithmetic checks for the three-site [2/2] Pade step.
Run with Python >=3.9 and no third-party packages.
"""
from fractions import Fraction as F
from itertools import product


def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def inverse(A):
    T = [list(A[i]) + [F(int(i == j)) for j in range(3)] for i in range(3)]
    for j in range(3):
        pivot = next(i for i in range(j, 3) if T[i][j] != 0)
        T[j], T[pivot] = T[pivot], T[j]
        q = T[j][j]
        T[j] = [v / q for v in T[j]]
        for i in range(3):
            if i != j:
                q = T[i][j]
                T[i] = [T[i][k] - q * T[j][k] for k in range(6)]
    return [row[3:] for row in T]


def compute(a, b, c, h):
    L = [[a + c, -a, -c], [-a, a + b, -b], [-c, -b, b + c]]
    L2 = mm(L, L)
    D = [[F(int(i == j)) + h * L[i][j] / 2 + h*h*L2[i][j]/12 for j in range(3)] for i in range(3)]
    N = [[F(int(i == j)) - h * L[i][j] / 2 + h*h*L2[i][j]/12 for j in range(3)] for i in range(3)]
    return mm(N, inverse(D))


def predictor(a, b, c, h):
    s = a + b + c
    t = a*b + b*c + c*a
    Delta = 48 + 48*s*h + (16*s*s + 12*t)*h*h + 12*s*t*h**3 + 3*t*t*h**4
    def edge(x, y, z):
        return 4*h*(12*x + 6*t*h - t*(x-2*(y+z))*h*h)/Delta
    return {(0, 1): edge(a, b, c), (0, 2): edge(c, a, b), (1, 2): edge(b, a, c)}


def check():
    count = 0
    weights = (F(0), F(1, 4), F(1), F(2), F(3), F(5), F(10))
    times = (F(0), F(1, 20), F(1, 2), F(1), F(3), F(10), F(100))
    for a, b, c in product(weights, repeat=3):
        t = a*b + b*c + c*a
        if t == 0:
            continue   # graph must be connected
        for h in times:
            M = compute(a, b, c, h)
            E = predictor(a, b, c, h)
            for (i, j), v in E.items():
                assert M[i][j] == v, (a,b,c,h,i,j)
                assert M[i][j] == M[j][i]
                count += 2
            for i in range(3):
                assert sum(M[i]) == 1
                assert M[i][i] > 0
                count += 2
            dominance = max(a, b, c) > 2*(a+b+c-max(a,b,c))
            if not dominance:
                assert all(M[i][j] >= 0 for i in range(3) for j in range(3))
                count += 1
            if h > 0:
                signs = {ij: (M[ij[0]][ij[1]] < 0) for ij in E}
                assert sum(signs.values()) <= 1
                count += 1
    # A strict finite horizon example and an exactly-balanced boundary.
    assert compute(F(5), F(1), F(1), F(10))[0][1] < 0
    assert compute(F(4), F(1), F(1), F(1000))[0][1] > 0
    print('VERIFY_OK', count+2, 'exact rational checks')


if __name__ == '__main__':
    check()
