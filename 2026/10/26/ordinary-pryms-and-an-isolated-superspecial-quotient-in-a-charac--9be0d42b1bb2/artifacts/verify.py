#!/usr/bin/env python3
"""Exact characteristic-seven Cartier coefficient and parameter-stratum checks.

The curve is y^3 = x^5 + a*x^3 + x, with a^2 != 4. Pure Python 3.
The reported matrices contain seventh powers of Cartier entries, which
preserves rank and vanishing over a perfect field.
"""
from collections import defaultdict

P = 7

def multiply(A, B):
    out = defaultdict(int)
    for (i, j), c in A.items():
        for (k, ell), d in B.items():
            out[(i + k, j + ell)] = (out[(i + k, j + ell)] + c*d) % P
    return {key: c for key, c in out.items() if c}

F = {(5, 0): 1, (3, 1): 1, (1, 0): 1}

def power(n):
    g = {(0, 0): 1}
    for _ in range(n):
        g = multiply(g, F)
    return g

def at_x(poly, x_exp):
    return {j: c for (i, j), c in poly.items() if i == x_exp and c}

f2, f4 = power(2), power(4)
assert at_x(f2, 6) == {2: 1, 0: 2}
# In the ordered basis dx/y; dx/y^2,x dx/y^2,x^2 dx/y^2.
# The dx/y block is a^2+2. The second (rank-three) block has entries:
# [4*a,0,1]; [0,a^4+5*a^2+6,0]; [1,0,4*a].
expected = [
    [{1: 4}, {}, {0: 1}],
    [{}, {4: 1, 2: 5, 0: 6}, {}],
    [{0: 1}, {}, {1: 4}],
]
for row in range(3):
    for col in range(3):
        x_exp = 7*(row+1)-1-col
        assert at_x(f4, x_exp) == expected[row][col], (row,col,at_x(f4,x_exp))
print('CARTIER_COEFFICIENTS_OK')

# Evaluate the intrinsic quotient and Prym determinants at all F_49 elements.
# F_49=F_7[u]/(u^2-3), since 3 is a quadratic nonresidue modulo 7.

def add(x, y):
    return ((x[0] + y[0]) % 7, (x[1] + y[1]) % 7)

def mul(x, y):
    return ((x[0]*y[0] + 3*x[1]*y[1]) % 7,
            (x[0]*y[1] + x[1]*y[0]) % 7)

def equals(x, y):
    return x == (y, 0)

def mul_const(x, c):
    return ((c*x[0]) % 7, (c*x[1]) % 7)

ZERO = (0, 0)
ONE = (1, 0)
qrank_hist = {0: 0, 2: 0}
for u in [(i,j) for i in range(7) for j in range(7)]:
    a2 = mul(u, u)
    if equals(a2, 4):
        continue  # singular branch polynomials excluded
    h = add(a2, (2, 0))
    # Complementary (anti-invariant) determinant=2(a^2-4), nonzero.
    d_prym = mul_const(add(a2, (3, 0)), 2)
    assert d_prym != ZERO
    # Quotient Hasse matrix diagonal entries h and h*(a^2-4).
    d_quot = mul(mul(h, h), add(a2, (3, 0)))
    assert (d_quot == ZERO) == (h == ZERO)
    qrank_hist[0 if h == ZERO else 2] += 1

assert qrank_hist == {0: 2, 2: 45}, qrank_hist
print('F49_STRATA_OK:',qrank_hist)

# Geometric smoothness: derivative 5*x^4+3*a*x^2+1 is
# coprime to x*(x^4+a*x^2+1) exactly when a^2 != 4 (char 7).
# Check the finite field base cases by polynomial gcd in F_7[x].
def ptrim(f):
    while f and f[-1] == 0: f.pop()
    return f

def prem(f,g):
    f = ptrim(f[:]);g=ptrim(g[:]); assert g
    while len(f) >= len(g) and f:
        factor = f[-1] * pow(g[-1], -1, 7) % 7
        delta = len(f)-len(g)
        for i,v in enumerate(g): f[i+delta] = (f[i+delta]-factor*v)%7
        ptrim(f)
    return f

def pgcd(a,b):
    while b: a,b=b,prem(a,b)
    return a

for a in range(7):
    f=[0,1,0,a,0,1]
    df=[1,0,3*a%7,0,5]
    is_squarefree=(len(pgcd(f,df))==1)
    assert is_squarefree == (a*a % 7 != 4)
print('SMOOTHNESS_F7_OK')

# Sanity-check rational point enumeration on the smooth projective curve:
# there is one rational point above infinity because gcd(3,5)=1.
for a in (0,1,3,4,5,6):
    n=1
    for x in range(7):
        rhs=(x**5+a*x**3+x)%7
        n += sum(1 for y in range(7) if pow(y,3,7)==rhs)
    print(f'F7_POINTS(a={a}):',n)
print('CHECK_OK')
