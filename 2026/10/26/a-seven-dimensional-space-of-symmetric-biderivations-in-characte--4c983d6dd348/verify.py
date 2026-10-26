#!/usr/bin/env python3
"""Reproduce the finite linear-algebra checks for the displayed Lie algebra."""
from itertools import product
from collections import Counter

# Basis indices 0,1,2 stand for e1,e2,e3.
def bracket_basis(i, j):
    if i == j:
        return {}
    return {(0, 1): {2: 1}, (0, 2): {1: 1}, (1, 2): {0: 1}}[tuple(sorted((i, j)))]

def bracket(x, y):
    out = [0, 0, 0]
    for i, xi in enumerate(x):
        for j, yj in enumerate(y):
            if xi and yj:
                for k, c in bracket_basis(i, j).items():
                    out[k] = (out[k] + xi * yj * c) % 2
    return tuple(out)

def bmap(params):
    a, b, d, e, g, h, i = params
    vals = {
        (0, 0): ((a+g)%2, (b+h)%2, (e+i)%2),
        (0, 1): ((b+h)%2, a%2, d%2),
        (0, 2): ((e+i)%2, d%2, g%2),
        (1, 1): (a%2, b%2, e%2),
        (1, 2): (d%2, e%2, h%2),
        (2, 2): (g%2, h%2, i%2),
    }
    def basis_value(i, j):
        if i > j:
            i, j = j, i
        return vals[(i, j)]
    def B(x, y):
        out = [0, 0, 0]
        for i, xi in enumerate(x):
            for j, yj in enumerate(y):
                if xi and yj:
                    value = basis_value(i, j)
                    for k in range(3):
                        out[k] = (out[k] + xi * yj * value[k]) % 2
        return tuple(out)
    return B

basis = [(1,0,0), (0,1,0), (0,0,1)]
zero = (0,0,0)
# Jacobi and alternation on basis triples.
for x, y, z in product(basis, repeat=3):
    j1 = bracket(x, bracket(y, z))
    j2 = bracket(y, bracket(z, x))
    j3 = bracket(z, bracket(x, y))
    assert tuple((j1[k]+j2[k]+j3[k]) % 2 for k in range(3)) == zero
    assert bracket(x, x) == zero
# Perfectness: each basis vector is a bracket.
assert bracket(basis[0], basis[1]) == basis[2]
assert bracket(basis[1], basis[2]) == basis[0]
assert bracket(basis[2], basis[0]) == basis[1]

# Variables are B(e_i,e_j)_k for i <= j and k=0,1,2.
pairs = [(i,j) for i in range(3) for j in range(i,3)]
variables = [(i,j,k) for i,j in pairs for k in range(3)]
index = {v:n for n,v in enumerate(variables)}
def vi(i,j,k):
    if i > j:
        i,j = j,i
    return index[(i,j,k)]

rows = []
for x in range(3):
    for y,z in [(0,1),(0,2),(1,2)]:
        coeffs = [Counter() for _ in range(3)]
        # In characteristic two, D([y,z]) - [D(y),z] - [y,D(z)] is a sum.
        for l,c in bracket_basis(y,z).items():
            for t in range(3):
                coeffs[t][vi(x,l,t)] += c
        for m in range(3):
            for t,c in bracket_basis(m,z).items():
                coeffs[t][vi(x,y,m)] += c
        for m in range(3):
            for t,c in bracket_basis(y,m).items():
                coeffs[t][vi(x,z,m)] += c
        for t in range(3):
            rows.append([coeffs[t][j] % 2 for j in range(len(variables))])

# RREF over F_2.
A = [row[:] for row in rows]
num_rows, num_cols = len(A), len(A[0])
pivots = []
r = 0
for c in range(num_cols):
    pivot = next((rr for rr in range(r, num_rows) if A[rr][c]), None)
    if pivot is None:
        continue
    A[r], A[pivot] = A[pivot], A[r]
    for rr in range(num_rows):
        if rr != r and A[rr][c]:
            A[rr] = [(u+v) % 2 for u,v in zip(A[rr], A[r])]
    pivots.append(c)
    r += 1
    if r == num_rows:
        break
assert len(variables) == 18
assert len(pivots) == 11
assert len(variables) - len(pivots) == 7

# Verify every parameter choice against all basis triples.
for params in product(range(2), repeat=7):
    B = bmap(params)
    for x, y, z in product(basis, repeat=3):
        lhs = B(x, bracket(y, z))
        r1 = bracket(B(x, y), z)
        r2 = bracket(y, B(x, z))
        rhs = tuple((r1[k] + r2[k]) % 2 for k in range(3))
        assert lhs == rhs, (params, x, y, z, lhs, rhs)

print("VERIFY_OK: Jacobi, perfectness, rank=11, nullity=7, all 128 parameterizations pass")
