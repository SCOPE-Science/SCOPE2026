#!/usr/bin/env python3
"""Verify the exact domination-polynomial formula for P_3 strong-product C_n.
Requires Python 3 and SymPy. Run: python verify.py
"""
from collections import Counter
from itertools import product
from sympy import Matrix, Poly, Symbol, factor, expand, trace

z = Symbol('z')
x = Symbol('x')
u = z
v = z + 3*z**2 + z**3
weights = (1, u, u, v)
coverage = (0b000, 0b011, 0b110, 0b111)


def transfer(weights):
    mat = [[0]*16 for _ in range(16)]
    for a, b, c in product(range(4), repeat=3):
        if coverage[a] | coverage[b] | coverage[c] == 0b111:
            mat[4*a+b][4*b+c] = weights[b]
    return Matrix(mat)


def brute_domination(n):
    """Directly enumerate subsets and closed neighborhoods in the graph."""
    vertices = list(product(range(3), range(n)))
    neighborhoods = []
    for r,j in vertices:
        mask = 0
        for pos, (s,k) in enumerate(vertices):
            if abs(r-s) <= 1 and (j-k) % n in (0,1,n-1):
                mask |= (1 << pos)
        neighborhoods.append(mask)
    full = (1 << (3*n)) - 1
    bysize = Counter()
    for subset in range(1 << (3*n)):
        cover = 0
        bits = subset
        while bits:
            bit = bits & -bits
            cover |= neighborhoods[bit.bit_length()-1]
            bits -= bit
        if cover == full:
            bysize[subset.bit_count()] += 1
    return sum(count*z**size for size,count in bysize.items())

M = transfer(weights)
C = x**3 + u*x**2 + u**2*x - u**2
Q = (x**6 - (u+v)*x**5 - (u**2+u*v+v)*x**4
     - (u**2*v+u**2+3*u*v+v)*x**3 + u*v*x**2 + u**2*v)
actual = M.charpoly(x).as_expr()
assert expand(actual - x**7*C*Q) == 0, 'symbolic characteristic polynomial mismatch'

for n in range(3,7):
    direct = expand(brute_domination(n))
    predicted = expand(trace(M**n))
    assert direct == predicted, f'domination coefficients differ at n={n}'
    assert direct.subs(z,-1) == (9 if n%4==0 else 1)

signed_M = transfer((1,-1,-1,1))
assert factor(signed_M.charpoly(x).as_expr()) == x**7*(x-1)**3*(x+1)**2*(x**2+1)**2
T = Matrix.eye(16)
for n in range(1,65):
    T = T*signed_M
    observed = int(trace(T))
    expected = 9 if n%4 == 0 else 1
    assert observed == expected, (n, observed, expected)
print('VERIFY_OK: symbolic degree-16 determinant, direct graph enumeration n=3..6, period n=1..64')
