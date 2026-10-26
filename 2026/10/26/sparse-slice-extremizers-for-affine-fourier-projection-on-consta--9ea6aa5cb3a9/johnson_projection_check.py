#!/usr/bin/env python3
"""Reproduce exact affine Johnson-slice projection identities.

No third-party dependencies are required for the exact checks; scipy is
optional for separate large-n asymptotic spot checks.
"""
from itertools import combinations
from math import comb, factorial, sqrt, exp
from fractions import Fraction

checks = 0

def verify(ok):
    global checks
    checks += 1
    if not ok:
        raise AssertionError(f'assertion {checks} failed')

def kernel(n,k,j):
    return Fraction(1) + Fraction(n*(n-1), k*(n-k)) * (j - Fraction(k*k,n))

def norm(n,k):
    N=comb(n,k)
    return sum((Fraction(comb(k,j)*comb(n-k,k-j),N) * abs(kernel(n,k,j))
                for j in range(max(0,2*k-n),k+1)),Fraction(0))

def rows(n,k):
    ss=[frozenset(c) for c in combinations(range(n),k)]
    N=len(ss)
    return [[kernel(n,k,len(x & y))/N for y in ss] for x in ss]

for n in range(2,9):
    for k in range(1,n):
        N=comb(n,k)
        R=rows(n,k)
        for row in R:
            verify(sum(row)==1)
            verify(sum(abs(x) for x in row)==norm(n,k))
        verify(sum(R[i][i] for i in range(N))==n)
        for row in R:
            verify(sum(a*a for a in row)==Fraction(n,N))
        for i in range(N):
            for j in range(N):
                verify(R[i][j]==R[j][i])
                verify(sum(R[i][h]*R[h][j] for h in range(N))==R[i][j])
        verify(norm(n,k)==norm(n,n-k))

for n in range(3,121):
    verify(norm(n,1)==1)
    for k in range(1,n//2+1):
        v=norm(n,k)
        verify(Fraction(1) <= v <= n)
        verify(v==norm(n,n-k))
        if k==2: verify(v==Fraction(3*n-7,n-1))

# Direct exact convolution formula agrees with integral row computation for n=5,k=2.
verify(norm(5,2)==Fraction(2))
verify(norm(12,3)>3)
verify(norm(11,3)<3)
print(f'EXACT_VERIFY_OK assertions={checks}')
for n in (20,50,100,300):
    vals=[norm(n,k) for k in range(1,n//2+1)]
    top=max(range(1,n//2+1), key=lambda k:vals[k-1])
    print(f'EXACT_SLICE_MAX n={n} k={top} norm={float(vals[top-1]):.10f}')
# The exact-rational calculations are finite checks only; asymptotic uniqueness is analytic.
