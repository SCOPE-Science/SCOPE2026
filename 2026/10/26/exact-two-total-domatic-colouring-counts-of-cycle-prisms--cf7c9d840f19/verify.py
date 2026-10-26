#!/usr/bin/env python3
"""Exact checks for the cycle-prism two-total-domatic enumeration."""
from collections import Counter
from hashlib import sha256

STATES = tuple((p, c) for p in range(4) for c in range(4))

def top(s): return s >> 1

def bottom(s): return s & 1

def admissible(p, c, q):
    return len({top(p), bottom(c), top(q)}) == 2 and len({bottom(p), top(c), bottom(q)}) == 2

M = [[int(c == d and admissible(p, c, q)) for d, q in STATES] for p, c in STATES]
N = len(M)

def multiply(A, B):
    # Entirely integer arithmetic.
    m = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(m)) for j in range(m)] for i in range(m)]

def trace(A): return sum(A[i][i] for i in range(len(A)))

def identity(n): return [[int(i == j) for j in range(n)] for i in range(n)]

def charpoly_coeffs(A):
    # Exact Faddeev-LeVerrier: det(tI-A) = t^n + c1*t^(n-1)+...+cn.
    n = len(A)
    B = identity(n)
    coeffs = [1]
    for k in range(1, n+1):
        B = multiply(A, B)
        assert (-trace(B)) % k == 0
        c = -trace(B) // k
        coeffs.append(c)
        for i in range(n): B[i][i] += c
    assert all(z == 0 for row in B for z in row)  # Cayley-Hamilton
    return coeffs

def poly_product(factors):
    p=[1]
    for f in factors:
        q=[0]*(len(p)+len(f)-1)
        for i,a in enumerate(p):
            for j,b in enumerate(f): q[i+j] += a*b
        p=q
    return p

factors = ([1,-1],[1,-1],[1,1],[1,1],
           [1,-3,1],[1,1,1],
           [1,-1,2,1,1],[1,1,2,-1,1])
coefficients = charpoly_coeffs(M)
assert coefficients == poly_product(factors), (coefficients,poly_product(factors))


def lucas(n):
    a, b=2,1
    for _ in range(n): a,b=b,a+b
    return a

def closed_form(n):
    assert n >= 3
    r=n%6
    if r==0: return lucas(2*n)+6+4*lucas(n)
    if r in (2,4): return lucas(2*n)+3-2*lucas(n)
    if r==3: return lucas(2*n)+2
    return lucas(2*n)-1

def exhaustive(n):
    # Separate direct enumeration of 2^(2n) named colorings.
    answer=0
    for mask in range(1 << (2*n)):
        def color(i,side): return (mask >> (2*(i%n)+side))&1
        good=True
        for i in range(n):
            if len({color(i-1,0), color(i+1,0), color(i,1)}) != 2:
                good=False; break
            if len({color(i-1,1), color(i+1,1), color(i,0)}) != 2:
                good=False; break
        if good: answer+=1
    return answer

assert N==16
P=identity(N)
for n in range(1,31):
    P=multiply(P,M)
    if n>=3:
        obtained=trace(P)
        expected=closed_form(n)
        assert obtained==expected,(n,obtained,expected)
        if n<=9:
            enumerated=exhaustive(n)
            assert enumerated==expected,(n,enumerated,expected)
        assert obtained>0 and obtained%2==0

print('CHARPOLY_OK:', coefficients)
print('BRUTE_FORCE_OK (n=3,...,9):', ', '.join(f'{n}:{exhaustive(n)}' for n in range(3,10)))
print('TRACE_FORMULA_OK: all 3<=n<=30')
print('ORDERED_TO_UNORDERED_FREE_SWAP_OK: A_n/2')
print('VERIFY_OK')
