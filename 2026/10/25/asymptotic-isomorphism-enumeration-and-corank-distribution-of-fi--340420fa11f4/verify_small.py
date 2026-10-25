#!/usr/bin/env python3
"""Exact small-prime-field tests for evolution-algebra isomorphism orbit bounds.

Usage: python verify_small.py
Only prime fields F_2 and F_3 are used; theorem allows all prime powers.
"""
from itertools import product, permutations
from math import factorial


def invmat(mat, p):
    n = len(mat)
    a = [[x % p for x in row] + [int(i == j) for j in range(n)]
         for i, row in enumerate(mat)]
    for j in range(n):
        t = next((i for i in range(j, n) if a[i][j]), None)
        if t is None:
            return None
        a[t], a[j] = a[j], a[t]
        v = pow(a[j][j], -1, p)
        a[j] = [(z * v) % p for z in a[j]]
        for i in range(n):
            if i != j:
                v = a[i][j]
                a[i] = [(a[i][k] - v * a[j][k]) % p for k in range(2 * n)]
    return [row[n:] for row in a]


def all_gl(n, p):
    for tup in product(range(p), repeat=n*n):
        mat = [tup[i*n:(i+1)*n] for i in range(n)]
        inv = invmat(mat, p)
        if inv is not None:
            yield mat, inv


def transformed(M, P, Pinv, p):
    n = len(M)
    B = []
    for a in range(n):
        for b in range(a):
            v = [sum(P[i][a]*P[i][b]*M[i][j]
                     for i in range(n)) % p for j in range(n)]
            if any(v):
                return None
        v = [sum(P[i][a]*P[i][a]*M[i][j]
                 for i in range(n)) % p for j in range(n)]
        B += [tuple(sum(Pinv[j][k]*v[k] for k in range(n)) % p
                    for j in range(n))]
    return tuple(x for row in B for x in row)


def property_2li(M, p):
    n = len(M)
    rows = [tuple(row) for row in M]
    if any(not any(row) for row in rows):
        return False
    for i in range(n):
        for j in range(i):
            if any(tuple((c*x) % p for x in rows[i]) == rows[j]
                   for c in range(1, p)):
                return False
    return True


def experiment(n, p):
    elements = tuple(product(range(p), repeat=n*n))
    element_ids = {t: i for i,t in enumerate(elements)}
    parent = list(range(len(elements)))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(x,y):
        rx, ry = find(x), find(y)
        parent[rx] = ry
    changes = list(all_gl(n,p))
    monomial_changes = []
    for P,Pinv in changes:
        if all(sum(int(P[i][j] != 0) for i in range(n)) == 1 for j in range(n)):
            monomial_changes.append((P,Pinv))
    assert len(monomial_changes) == factorial(n)*(p-1)**n
    good_count = 0
    for mid, tup in enumerate(elements):
        M = [tup[i*n:(i+1)*n] for i in range(n)]
        if property_2li(M,p):
            good_count += 1
        for P,Pinv in changes:
            t = transformed(M,P,Pinv,p)
            if t is not None:
                union(mid, element_ids[t])
    iso_classes = len({find(i) for i in range(len(elements))})
    # Independent monomial orbit calculation (no dependence on enumeration order).
    parent = list(range(len(elements)))
    for mid, tup in enumerate(elements):
        M = [tup[i*n:(i+1)*n] for i in range(n)]
        for P,Pinv in monomial_changes:
            t = transformed(M,P,Pinv,p)
            assert t is not None
            union(mid, element_ids[t])
    mono_classes = len({find(i) for i in range(len(elements))})
    # Good monomial orbits give a lower bound on true isomorphism classes.
    good_orbits = {find(i) for i,t in enumerate(elements)
                   if property_2li([t[j*n:(j+1)*n] for j in range(n)],p)}
    assert len(good_orbits) <= iso_classes <= mono_classes
    print(f"q={p} n={n} matrices={p**(n*n)} 2LI={good_count} "
          f"monomial_orbits={mono_classes} true_isomorphism_classes={iso_classes} "
          f"2LI_orbits={len(good_orbits)}")

if __name__ == '__main__':
    import sys
    cases = [(2,2),(2,3)] + ([(3,2)] if '--extended' in sys.argv else [])
    for n,p in cases:
        experiment(n,p)
    print('VERIFY_OK')
