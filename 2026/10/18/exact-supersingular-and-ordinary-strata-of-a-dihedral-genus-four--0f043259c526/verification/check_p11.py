#!/usr/bin/env python3
"""Exact, dependency-free finite-field verification for a genus-four curve family.

Run: python3 verification/check_p11.py
Only integer arithmetic modulo 11 is used; all geometric implications are
proved separately in RESULT.md.
"""
from math import comb

p = 11

# Sparse polynomial in x and t over F_11.
def multiply(f, g):
    h = {}
    for (i, j), u in f.items():
        for (k, ell), v in g.items():
            key = (i + k, j + ell)
            h[key] = (h.get(key, 0) + u*v) % p
    return {m: c for m, c in h.items() if c}

f = {(9, 0): 1, (5, 1): 1, (1, 0): 1}
assert {(10-i, j): c for (i, j), c in f.items()} == f  # x^10 f(1/x)=f(x).
g = {(0, 0): 1}
for _ in range(5):
    g = multiply(g, f)

# Check every entry, including forced zero coefficients, independently.
def coefficient_x(n):
    return {j: c for (i, j), c in g.items() if i == n}

A = {1: 5}
B = {4: 5, 2: 8, 0: 10}
expected = [
    [{}, A, {}, {}],
    [B, {}, {}, {}],
    [{}, {}, {}, B],
    [{}, {}, A, {}],
]
actual = [[coefficient_x(p*(i+1)-(j+1)) for j in range(4)]
          for i in range(4)]
assert actual == expected, (actual, expected)

# Confirm determinant identity det(M) = (5t)^2(5P(t))^2 = 5^4 t^2 P(t)^2.
# P(t) = t^4 - 5t^2 + 2, so 5P(t) = 5t^4 - 3t^2 -1.
P = {4: 1, 2: 6, 0: 2}
assert {n: (5*c) % p for n, c in P.items()} == B

# Quadratic z^2-5z+2 has nonsquare discriminant 17=6 and
# nonsquare norm 2; hence z is nonsquare in F_121 and P is irreducible.
nonzero_squares = {z*z % p for z in range(1, p)}
assert 6 not in nonzero_squares and 2 not in nonzero_squares
assert 2**5 % p == p-1
assert ((2**2 - 5*2 + 2) % p) != 0
assert ((-2)**2)**2 % p == (2**4) % p

# Check that no ordinary F_11 parameter outside 0 is exceptional.
for t in range(p):
    if t in (2, p-2):
        continue  # Singular curves are excluded.
    aval = (5*t) % p
    bval = (5*pow(t, 4, p)-3*pow(t, 2, p)-1) % p
    assert (aval*bval == 0) == (t == 0)
    mat = [[sum(c*pow(t, e, p) for e, c in h.items()) % p for h in row]
           for row in expected]
    prod = [[sum(mat[i][k]*pow(mat[k][j], p, p) for k in range(4)) % p
             for j in range(4)] for i in range(4)]
    if t == 0:
        assert sum(any(z for z in row) for row in mat) == 2
        assert all(all(z == 0 for z in row) for row in prod)
    else:
        assert all(prod[i][(i+2)%4] == 0 for i in range(4))  # no spurious couplings

# Finite-field point count sanity checks for t=0 and t=1.
def npoints(t):
    return 1 + sum(1 if (x**9+t*x**5+x) % p == 0 else
                   2 if pow((x**9+t*x**5+x) % p, (p-1)//2, p)==1 else 0
                   for x in range(p))
assert npoints(0) == 12
assert npoints(1) == 12
print('VERIFY_OK; Cartier coefficients, irreducibility, rational-parameter ranks and point checks')
