#!/usr/bin/env python3
"""Exact arithmetic checks for a four-dimensional numerical-radius counterexample."""
from fractions import Fraction as Q
from math import comb

e = Q(1, 10000)
N = 4
I = [[Q(i == j) for j in range(N)] for i in range(N)]
S = [[Q(j == i + 1) for j in range(N)] for i in range(N)]

def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(N))
             for j in range(N)] for i in range(N)]

def powmat(A, k):
    Z = I
    for _ in range(k):
        Z = matmul(Z, A)
    return Z

def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(N)] for i in range(N)]

def scale(A, c):
    return [[c * A[i][j] for j in range(N)] for i in range(N)]

T = add(S, scale(I, e))
assert all(x == 0 for row in powmat(S, 4) for x in row)
B = [[Q(0) for _ in range(N)] for _ in range(N)]
for j in range(4):
    B = add(B, scale(powmat(S, j), Q(comb(4, j)) * e**(4-j)))
assert powmat(T, 4) == B
fourth_power_norm_upper = 4*e + 6*e**2 + 4*e**3 + e**4
assert fourth_power_norm_upper < 5*e
assert 5*e == Q(1, 2000)
assert Q(1, 2000) < Q(3, 20)**4
series_bound = Q(3,4)*(1+e) + Q(1,4)*Q(3,20)
assert series_bound == Q(31503,40000)
assert series_bound < Q(4,5)
assert Q(5) > Q(11,5)**2  # Gives cos(pi/5)=(1+sqrt(5))/4 > 4/5.
assert all(T[i][i] == e for i in range(N)) # determinant is e^4 (triangular).
print('PASS: exact matrix powers, infinite-series upper certificate and strict gap')
