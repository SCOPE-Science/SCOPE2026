#!/usr/bin/env python3
"""Exact verification of the 12-element counterexample in RESULT.md."""

from itertools import combinations, product

X = (0, 1)
E = (0, 1)
C0 = (0, 0)
C1 = (1, 1)

def compose(r, t):
    # Right action convention: x (r t) = (x r) t.
    return tuple(t[r[i]] for i in X)

# S = {identity, constant 0}; R = {identity, constant 0, constant 1}.
S = (E, C0)
R = (E, C0, C1)

def wreath_multiply(u, v):
    a, r = u
    b, t = v
    base = tuple(compose(a[i], b[r[i]]) for i in X)
    return base, compose(r, t)

W = tuple((a, r) for a in product(S, repeat=2) for r in R)
identity = ((E, E), E)

def closure(gens):
    C = {identity}
    C.update(gens)
    changed = True
    while changed:
        changed = False
        current = tuple(C)
        for u in current:
            for v in current:
                z = wreath_multiply(u, v)
                if z not in C:
                    C.add(z)
                    changed = True
    return C

minimum = None
witness = None
candidates = tuple(w for w in W if w != identity)
for k in range(len(candidates) + 1):
    for gens in combinations(candidates, k):
        if len(closure(gens)) == len(W):
            minimum = k
            witness = gens
            break
    if minimum is not None:
        break

assert len(W) == 12
assert minimum == 4
# In the notation of RESULT.md, rank(R:G)=2, rank(S:H)=1, and G has 2 orbits.
assert 2 + 2 * 1 == minimum
assert 2 + 1 == 3 < minimum

print("wreath_size =", len(W))
print("exact_relative_rank =", minimum)
print("source_lemma_bound =", 3)
print("correct_orbit_formula =", 4)
