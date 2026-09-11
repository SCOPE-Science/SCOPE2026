#!/usr/bin/env python3
"""Verifier: 20-tuple -> equivariant Latin? pair orthogonal?"""
import sys, json

def cell_orbit(r, c):
    return (r // 5, c // 5, ((c % 5) - (r % 5)) % 5)

orbits = [(er, ec, d) for er in (0, 1) for ec in (0, 1) for d in range(5)]
oidx = {o: i for i, o in enumerate(orbits)}
NO = 20
cells_of = [[] for _ in range(NO)]
for r in range(10):
    for c in range(10):
        cells_of[oidx[cell_orbit(r, c)]].append((r, c))

def sym_of(val, r):
    s, b = divmod(val, 5)
    return s * 5 + (b + r % 5) % 5

def grid(X):
    G = [[0]*10 for _ in range(10)]
    for i in range(NO):
        for (r, c) in cells_of[i]:
            G[r][c] = sym_of(X[i], r)
    return G

def is_latin(X):
    G = grid(X)
    for r in range(10):
        if sorted(G[r]) != list(range(10)):
            return False, ("row", r)
    for c in range(10):
        if sorted(G[r][c] for r in range(10)) != list(range(10)):
            return False, ("col", c)
    return True, ("ok",)

def pair_class(a, b):
    return (a // 5, b // 5, ((a % 5) - (b % 5)) % 5)

def orthogonal(X, Y):
    G, H = grid(X), grid(Y)
    seen = set()
    for r in range(10):
        for c in range(10):
            p = (G[r][c], H[r][c])
            if p in seen:
                return False
            seen.add(p)
    return True

if __name__ == "__main__":
    X = [0, 2, 1, 5, 7, 3, 6, 4, 9, 8, 2, 4, 6, 8, 5, 1, 0, 9, 3, 7]
    print("L1 latin:", is_latin(X))
    # identical squares must NOT be orthogonal
    print("self-orth (expect False):", orthogonal(X, X))
    # reversed-symbol square: Y[i] = 9-X[i]? check latin + orth quickly on random
    import random
    random.seed(1)
    Y = [(9 - v) for v in X]
    print("mirror latin:", is_latin(Y), "orth:", orthogonal(X, Y))
