#!/usr/bin/env python3
"""Exact small-parameter arithmetic checks of the integer Euler-form theorem.

Standard library only. The proof for all n is in RESULT.md; finite tests do
not replace it. No remote services or external mathematical datasets are used.
"""
from itertools import combinations, permutations
from math import gcd

def product(A, B):
    size = len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(size)) for j in range(size)] for i in range(size)]

def power(A, n):
    size = len(A)
    result = [[int(i==j) for j in range(size)] for i in range(size)]
    while n:
        if n & 1:
            result = product(result, A)
        A = product(A, A)
        n //= 2
    return result

def determinant(A):
    n = len(A)
    total = 0
    for p in permutations(range(n)):
        inversions = sum(p[i]>p[j] for i in range(n) for j in range(i+1, n))
        total += (-1 if inversions%2 else 1) * __import__('math').prod(A[i][p[i]] for i in range(n))
    return total

def determinantal_divisors(M):
    n = len(M)
    result = []
    for k in range(1, n+1):
        g = 0
        for rows in combinations(range(n),k):
            for cols in combinations(range(n),k):
                g = gcd(g, determinant([[M[i][j] for j in cols] for i in rows]))
        result.append(g)
    return result

C = [[0,0,0,-1],[1,0,0,2],[0,1,0,-2],[0,0,1,2]]
I = [[int(i==j) for j in range(4)] for i in range(4)]
A = [[power(C,4)[i][j]-I[i][j] for j in range(4)] for i in range(4)]
assert A == [[-2]*4,[2]*4,[-2]*4,[2]*4]
assert product(A,A)==[[0]*4 for _ in range(4)]

for n in range(3,129):
    M = [[power(C,n)[i][j]-I[i][j] for j in range(4)] for i in range(4)]
    d = determinantal_divisors(M)
    if n % 4 == 0:
        expected = [n//2,0,0,0]
    elif n % 2 == 0:
        expected = [1,1,2*n,0]
    else:
        expected = [1,1,n,0]
    assert d == expected, (n,d,expected)

for n in range(3,41):
    H = [[0]*n for _ in range(n)]
    for i in range(n):
        for j,val in ((i,2),((i+1)%n,-2),((i-1)%n,-2),((i+2)%n,1),((i-2)%n,1)):
            H[i][j] += val
    assert all(H[i][j]==H[j][i] for i in range(n) for j in range(n))
    assert all(sum(row)==0 for row in H)
    for v in ([i*i%7 for i in range(n)],[int(i%3==0) for i in range(n)], [i for i in range(n)]):
        quadratic = sum((v[i]-v[(i+1)%n])**2 for i in range(n))*2 - sum((v[i]-v[(i+2)%n])**2 for i in range(n))
        h_value = sum(v[i]*H[i][j]*v[j] for i in range(n) for j in range(n))
        assert quadratic == h_value, (n,v)
print('EXACT_VERIFICATION_OK: companion Smith divisors n=3..128, Hessian identity n=3..40')
