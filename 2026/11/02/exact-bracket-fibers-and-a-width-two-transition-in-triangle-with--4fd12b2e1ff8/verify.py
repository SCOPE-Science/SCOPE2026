#!/usr/bin/env python3
"""Finite-field direct bracket-fiber census for triangle-with-leaves graphs.

Run with Python 3 standard library: python3 verify.py
"""
from itertools import product
from collections import Counter


def multiplication(q, x, y):
    if q == 4:
        # F_4 = F_2[u]/(u^2+u+1); elements encoded as 0,1,u,u+1.
        t = 0
        for i in range(2):
            for j in range(2):
                if (x >> i) & (y >> j) & 1:
                    t ^= (1 << (i + j))
        if t & 8:
            t ^= 14  # u^3=u^2+u=1, so reduce by u*(u^2+u+1).
        if t & 4:
            t ^= 7
        return t
    return (x * y) % q


def subtraction(q, x, y):
    return x ^ y if q == 4 else (x - y) % q


def predicted(q, r, z):
    a, b, c, *d = z
    if a or b:
        return q ** (r+1) * (q*q-1)
    if c and any(d):
        return 0
    if c:
        return q ** (2*r+1) * (q*q-1)
    if any(d):
        return q ** (r+2) * (q*q-1)
    return (q*q-1)*q**(r+2) + (q**3+q*q-q)*q**(2*r)


def check(q, r):
    vertices = list(product(range(q), repeat=2))
    n = 3+r
    m = q*q
    dtable = [[subtraction(q, multiplication(q, a, d), multiplication(q, b, c))
               for c, d in vertices] for a, b in vertices]
    edges = [(0, 1), (0, 2), (1, 2)] + [(0, j) for j in range(3, n)]
    counts = Counter()
    for points in product(range(m), repeat=n):
        z = tuple(dtable[points[i]][points[j]] for i, j in edges)
        counts[z] += 1
    assert sum(counts.values()) == q**(2*n)
    missing=0
    for z in product(range(q), repeat=len(edges)):
        expect=predicted(q,r,z)
        assert counts[z] == expect, (q,r,z,counts[z],expect)
        missing += (expect == 0)
    assert missing == (q-1)*(q**r-1)
    print('OK q=%s r=%s |input|=%s |image|=%s |missing|=%s |zero-fiber|=%s' %
          (q,r,q**(2*n), len(counts),missing,counts[(0,)*len(edges)]))


if __name__ == '__main__':
    cases=[(2,0),(2,1),(2,2),(2,3),(2,4),
           (3,0),(3,1),(3,2),(4,0),(4,1),(4,2),(5,0),(5,1)]
    for q,r in cases:
        check(q,r)
    print('TRIANGLE_LEAF_BRACKET_FIBERS_OK',len(cases))
