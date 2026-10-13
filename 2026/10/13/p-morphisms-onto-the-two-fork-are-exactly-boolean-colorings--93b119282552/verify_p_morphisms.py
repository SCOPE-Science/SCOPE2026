#!/usr/bin/env python3
"""Finite sanity checks for p-morphisms A_n -> A_1.

A_n is represented by tuples in {0,1,2}^n, with 0 meaning undefined.
The order is extension of partial functions.
"""
from itertools import product

def A(n):
    return list(product((0, 1, 2), repeat=n))

def leq(x, y):
    return all(a == 0 or a == b for a, b in zip(x, y))

def is_pmorphism(src, tgt, f):
    # monotonicity
    for i, x in enumerate(src):
        for j, y in enumerate(src):
            if leq(x, y) and not leq(tgt[f[i]], tgt[f[j]]):
                return False
    # back condition
    for i, x in enumerate(src):
        fx = tgt[f[i]]
        for u_idx, u in enumerate(tgt):
            if leq(fx, u):
                if not any(leq(x, y) and f[j] == u_idx for j, y in enumerate(src)):
                    return False
    return True

def formula_map(n, coloring):
    src = A(n)
    maxima = list(product((1, 2), repeat=n))
    color = dict(zip(maxima, coloring))
    out = []
    for x in src:
        extensions = [z for z in maxima if leq(x, z)]
        vals = {color[z] for z in extensions}
        out.append(1 if vals == {1} else 2 if vals == {2} else 0)
    return tuple(out)

def exhaustive_pmorphisms(n):
    src, tgt = A(n), A(1)
    found = set()
    for f in product(range(len(tgt)), repeat=len(src)):
        if is_pmorphism(src, tgt, f):
            found.add(tuple(f))
    return found

for n in (1, 2):
    brute = exhaustive_pmorphisms(n)
    maxima = list(product((1, 2), repeat=n))
    constructed = {
        formula_map(n, coloring)
        for coloring in product((1, 2), repeat=len(maxima))
    }
    assert brute == constructed
    surj = sum(len(set(f)) == 3 for f in brute)
    expected_total = 2 ** (2 ** n)
    expected_surj = expected_total - 2
    assert len(brute) == expected_total
    assert surj == expected_surj
    print(f"n={n}: total={len(brute)}, surjective={surj}")

print("all finite sanity checks passed")
