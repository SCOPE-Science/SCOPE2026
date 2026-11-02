#!/usr/bin/env python3
"""Exact finite regression tests for cycle--fixed-point TP2; no external modules.
The all-size theorem follows from a separate symbolic proof, not this test.
"""
from math import comb, factorial
from fractions import Fraction
from itertools import permutations
from collections import Counter

MAX_N = 160
D = [[0] * (MAX_N + 2) for _ in range(MAX_N + 2)]
D[0][0] = 1
assertions = 0

def check(statement, label):
    global assertions
    assertions += 1
    if not statement:
        raise AssertionError(label)

def d(n, k):
    if n < 0 or k < 0 or n > MAX_N or k > MAX_N:
        return 0
    return D[n][k]

for n in range(2, MAX_N + 1):
    for j in range(1, n // 2 + 1):
        D[n][j] = (n - 1) * (d(n - 1, j) + d(n - 2, j - 1))

for n in range(2, MAX_N + 1):
    for j in range(0, n + 1):
        lc = d(n, j)**2 - d(n, j - 1) * d(n, j + 1)
        check(lc >= 0, f'log concavity n={n} j={j}')
        aa = d(n-1, j-1) * d(n, j) - d(n-1, j) * d(n, j-1)
        bb = d(n, j) * d(n-1, j) - d(n, j+1) * d(n-1, j-1)
        check(aa >= 0, f'A n={n} j={j}')
        check(bb >= 0, f'B n={n} j={j}')
        if n >= 3:
            prev_b = d(n-1,j-1)*d(n-2,j-1)-d(n-1,j)*d(n-2,j-2)
            prev_a = d(n-2,j-1)*d(n-1,j)-d(n-2,j)*d(n-1,j-1)
            prev_lc = d(n-1,j)**2-d(n-1,j-1)*d(n-1,j+1)
            check(aa == (n-1) * prev_b, f'A identity n={n} j={j}')
            check(bb == (n-1) * (prev_lc + prev_a), f'B identity n={n} j={j}')

def w(n,k,f):
    return comb(n,f)*d(n-f,k-f) if 0 <= f <= n else 0

for n in range(2,28):
    for k in range(1,n+1):
        for f in range(n+1):
            check(w(n,k,f) >= 0, f'nonnegative n={n} k={k} f={f}')
    for k in range(1,n+1):
        for ell in range(k+1,n+1):
            for f in range(n):
                for g in range(f+1,n+1):
                    minor = w(n,k,f)*w(n,ell,g)-w(n,k,g)*w(n,ell,f)
                    check(minor >= 0, f'TP2 n={n} k={k} ell={ell} f={f} g={g}')
                    if w(n,k,g)*w(n,ell,f)>0:
                        check(minor>0, f'strict overlap TP2 n={n}, {k},{ell},{f},{g}')
    check(sum(w(n,k,f) for k in range(n+1) for f in range(n+1))==factorial(n),f'total n={n}')

for n in range(2,9):
    observed=Counter()
    for perm in permutations(range(n)):
        seen=[False]*n
        k=0
        for i in range(n):
            if not seen[i]:
                k+=1
                j=i
                while not seen[j]:
                    seen[j]=True
                    j=perm[j]
        f=sum(perm[i]==i for i in range(n))
        observed[(k,f)]+=1
    for k in range(1,n+1):
        for f in range(n+1):
            check(observed[(k,f)] == w(n,k,f),f'exhaustive n={n} k={k} f={f}')

# In Ewens(theta), the weighting theta**k cancels within K=k and
# multiplies any TP2 minor by theta**(k+ell), so the theorem persists.
for n in range(2,26):
    s=factorial(n)
    check(Fraction(sum(f*k*w(n,k,f) for k in range(1,n+1) for f in range(n+1)),s)-Fraction(sum(f*w(n,k,f) for k in range(1,n+1) for f in range(n+1)),s)*Fraction(sum(k*w(n,k,f) for k in range(1,n+1) for f in range(n+1)),s)==Fraction(n-1,n),f'covariance n={n}')

print(f'PASS: {assertions} exact assertions; exhaustive permutations to n=8; all 2x2 joint minors to n=27; recurrence inequalities to n=160.')
