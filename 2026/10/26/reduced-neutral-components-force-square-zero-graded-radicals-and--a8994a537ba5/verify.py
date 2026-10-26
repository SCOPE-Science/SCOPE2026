#!/usr/bin/env python3
"""Exact check of the quadratic-field Z/2 grading on M_2(F_2)."""
from itertools import product

# Matrices are tuples (a,b,c,d) for [[a,b],[c,d]], over F_2.
def add(X, Y):
    return tuple((a ^ b) for a, b in zip(X, Y))

def mul(X, Y):
    a,b,c,d = X
    e,f,g,h = Y
    return ((a*e ^ b*g) & 1, (a*f ^ b*h) & 1,
            (c*e ^ d*g) & 1, (c*f ^ d*h) & 1)

I = (1,0,0,1)
A = (0,1,1,1)       # multiplication by alpha, alpha^2=alpha+1
S = (1,1,0,1)       # Frobenius alpha -> alpha^2
Z = (0,0,0,0)
K = {Z, I, A, add(A, I)}
C1 = {mul(x, S) for x in K}
M = set(product((0,1), repeat=4))
assert len(K) == 4 and len(C1) == 4 and K & C1 == {Z}
D = {add(x, y) for x in K for y in C1}
assert len(D) == 16 and D == M
assert mul(A, A) == add(A, I)
assert mul(S, S) == I
assert mul(S, A) == mul(mul(A, A), S)  # S a = sigma(a) S
# Degree-zero field: every nonzero element has inverse; no nonzero nilpotent.
for x in K - {Z}:
    assert any(mul(x, y) == I and mul(y, x) == I for y in K)
    assert mul(x, x) != Z
# Grading products: 0*0 and 1*1 lie in K; mixed products lie in C1.
for x, y in product(K, repeat=2):
    assert mul(x, y) in K
for x, y in product(C1, repeat=2):
    assert mul(x, y) in K
for x in K:
    for y in C1:
        assert mul(x, y) in C1 and mul(y, x) in C1
print("VERIFY_OK: F4 degree-zero field grading on M2(F2)")
