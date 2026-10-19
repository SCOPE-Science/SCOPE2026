#!/usr/bin/env python3
"""Exact arithmetic checks for a three-stage Markov-hole classification.
This finite checker supplements, but does not replace, the general proof.
"""
from itertools import product
from math import comb

def multiply(A, B):
    k = len(A)
    return [[sum(A[i][h]*B[h][j] for h in range(k)) for j in range(k)] for i in range(k)]

def matrix(k, a, b):
    return [[1-int(i == a and j == b) for j in range(k)] for i in range(k)]

def trace(A):
    return sum(A[i][i] for i in range(len(A)))

def total(A):
    return sum(map(sum, A))

def checks(k):
    words = list(product(range(k), repeat=2))
    mat = {w: matrix(k, *w) for w in words}
    counter = [0]*4
    for a, b, c in product(words, repeat=3):
        overlaps = [int(a[1] == b[0]), int(b[1] == c[0]),
                    int(c[1] == a[0])]
        r = sum(overlaps)
        counter[r] += 1
        P = multiply(multiply(mat[a], mat[b]), mat[c])
        assert trace(P) == k**3 - 3*k + r - int(r == 3)
        q = multiply(P, P)
        delta = (trace(P)**2-trace(q))//2
        assert delta == (-1)**r * (k-1)**r
        # Exact count of allowed length-four digit strings.
        c1 = k**4-3*k*k+k*(overlaps[0]+overlaps[1])+1-overlaps[0]*overlaps[1]
        assert total(P) == c1
    assert counter == [comb(3, r)*k**3*(k-1)**(3-r) for r in range(4)]
    return counter

for k in range(2, 6):
    print('k=', k, 'classes=', checks(k))
A = {w: matrix(2, *w) for w in product(range(2), repeat=2)}
fast = multiply(multiply(A[0, 0], A[1, 1]), A[0, 1])
slow = multiply(multiply(A[0, 0], A[0, 1]), A[1, 1])
assert fast == [[1,0],[3,1]], fast
assert slow == [[2,1],[3,2]], slow
R = [[1,0],[0,1]]
for m in range(14):
    assert total(R) == 2+3*m
    R = multiply(R, fast)
print('VERIFY_OK')
