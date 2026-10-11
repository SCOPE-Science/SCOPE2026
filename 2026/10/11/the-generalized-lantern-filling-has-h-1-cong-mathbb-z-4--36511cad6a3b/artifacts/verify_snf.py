#!/usr/bin/env python3
"""Exact minor certificate for the generalized-lantern vanishing-cycle matrix."""
from itertools import combinations
from math import gcd

V = [
    [0,0,1,1,1,0],
    [1,1,0,0,1,0],
    [1,0,1,0,0,1],
    [0,1,0,1,0,1],
    [0,1,1,0,0,0],
]

def det_bareiss(a):
    a = [row[:] for row in a]
    n = len(a)
    if n == 0:
        return 1
    sign = 1
    prev = 1
    for k in range(n - 1):
        pivot = next((r for r in range(k, n) if a[r][k] != 0), None)
        if pivot is None:
            return 0
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            sign *= -1
        p = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                a[i][j] = (a[i][j] * p - a[i][k] * a[k][j]) // prev
        prev = p
        for i in range(k + 1, n):
            a[i][k] = 0
    return sign * a[-1][-1]

def minor(rows, cols):
    return det_bareiss([[V[i][j] for j in cols] for i in rows])

deltas = []
for k in range(1, 6):
    g = 0
    for rs in combinations(range(5), k):
        for cs in combinations(range(6), k):
            g = gcd(g, abs(minor(rs, cs)))
    deltas.append(g)

assert deltas == [1,1,1,1,4]
invariants = [deltas[0]] + [deltas[i] // deltas[i-1] for i in range(1,5)]
assert invariants == [1,1,1,1,4]

ker = [-1,0,0,-1,1,1]
assert [sum(V[i][j]*ker[j] for j in range(6)) for i in range(5)] == [0]*5

u = [1,1,1,1,0]
vtu = [sum(V[i][j]*u[i] for i in range(5)) for j in range(6)]
assert vtu == [2]*6

print("VERIFY_OK rank=5 determinantal_divisors=1,1,1,1,4 "
      "kernel=(-1,0,0,-1,1,1) VTu=(2,2,2,2,2,2)")
