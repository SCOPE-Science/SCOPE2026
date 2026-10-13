"""Exact-arithmetic finite sanity checks for reciprocal-Hankel normal form.

The theorem is proved by a formal generating-function identity. These tests
verify instances over integers and rationals, not an infinite quantifier.
Run with: python3 checker.py
"""
from fractions import Fraction
from random import Random

rng = Random(20261008)

def mm(A, B):
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*B)] for row in A]

def transpose(A):
    return [list(col) for col in zip(*A)]

def rank(M):
    A = [[Fraction(x) for x in row] for row in M]
    rows, cols = len(A), len(A[0])
    pivot_row = 0
    for col in range(cols):
        q = next((i for i in range(pivot_row, rows) if A[i][col]), None)
        if q is None:
            continue
        A[pivot_row], A[q] = A[q], A[pivot_row]
        p = A[pivot_row][col]
        A[pivot_row] = [z / p for z in A[pivot_row]]
        for i in range(rows):
            if i != pivot_row and A[i][col]:
                t = A[i][col]
                A[i] = [z-t*v for z,v in zip(A[i],A[pivot_row])]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row

cases = 0
entries = 0
for d in range(4, 15):
    for r in range(2, d//2 + 1):
        for _ in range(17):
            a = [1]+[rng.randint(-5,5) for j in range(d)]
            c = [1]
            for n in range(1,d+1):
                c.append(-sum(a[k]*c[n-k] for k in range(1,n+1)))
            b = [0,0]+[-c[j] for j in range(2,d+1)]
            L = [[c[i-j] if i>=j else 0 for j in range(r+1)] for i in range(r+1)]
            R = [[c[i-j] if i>=j else 0 for j in range(d-r+1)] for i in range(d-r+1)]
            H = [[a[i+j] for j in range(d-r+1)] for i in range(r+1)]
            transformed = mm(mm(L,H),transpose(R))
            block = [[int(i==0 and j==0) if i==0 or j==0 else b[i+j]
                     for j in range(d-r+1)] for i in range(r+1)]
            assert transformed==block, (d,r,a,transformed,block)
            assert rank(H)==1+rank([row[1:] for row in block[1:]])
            # Reciprocal of c recovers all original affine coordinates.
            recovered = [1]
            for n in range(1,d+1):
                recovered.append(-sum(c[k]*recovered[n-k] for k in range(1,n+1)))
            assert recovered==a
            cases+=1
            entries += (r+1)*(d-r+1)
print('PASS: %s exact integral specializations, %s transformed matrix entries, degrees 4..14, ranks 2..floor(d/2), inverse-coordinate reconstruction.' % (cases,entries))
print('Method: direct triangular Hankel matrix multiplication and exact Fraction Gaussian rank; formal generating-function proof is separate.')
