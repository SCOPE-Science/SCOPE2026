#!/usr/bin/env python3
"""Exact integer checks for local positivity on the integral Loday associahedron.

Run: python3 check_associa.py. Requires only the Python standard library.
"""
from collections import Counter
from functools import lru_cache
from math import comb, gcd

LEAF = None

@lru_cache(None)
def trees(n):
    if n == 0:
        return (LEAF,)
    return tuple((a, b) for i in range(n)
                 for a in trees(i) for b in trees(n - 1 - i))

@lru_cache(None)
def leaves(t):
    return 1 if t is LEAF else leaves(t[0]) + leaves(t[1])

@lru_cache(None)
def vertex(t):
    if t is LEAF:
        return ()
    l, r = t
    return vertex(l) + (leaves(l) * leaves(r),) + vertex(r)

@lru_cache(None)
def rotations(t):
    if t is LEAF:
        return frozenset()
    l, r = t
    out = set()
    if l is not LEAF:
        a, b = l
        out.add((a, (b, r)))
    if r is not LEAF:
        b, c = r
        out.add(((l, b), c))
    out.update((x, r) for x in rotations(l))
    out.update((l, x) for x in rotations(r))
    return frozenset(out)

@lru_cache(None)
def rotation_products(t):
    if t is LEAF:
        return ()
    l, r = t
    out = list(rotation_products(l) + rotation_products(r))
    if l is not LEAF:
        out.append(leaves(l[0]) * leaves(r))
    if r is not LEAF:
        out.append(leaves(l) * leaves(r[1]))
    return tuple(out)

def catalan(n):
    return comb(2*n, n) // (n+1)

def forbidden_free_counts(limit):
    g = [1]
    a = [0]
    for n in range(1, limit + 1):
        # A(t) = t(G(t) - A(t)); G(t) = 1 + t(G(t)^2 - 2 A(t)).
        a.append(g[n-1] - a[n-1])
        g.append(sum(g[i]*g[n-1-i] for i in range(n)) - 2*a[n-1])
    return g

def cut_width(n):
    intervals = [(i, j) for i in range(n) for j in range(i, n)]
    def cut_crosses(mask, i, j):
        values = [bool(mask & (1 << k)) for k in range(i, j+1)]
        return any(values) and not all(values)
    return min(sum(cut_crosses(mask, i, j) for i,j in intervals)
               for mask in range(1, (1 << n)-1))

def check():
    expected = [1,1,0,1,2,4,10,23,56,138,344,870]
    g = forbidden_free_counts(len(expected)-1)
    assert g == expected, (g, expected)
    for n in range(2,9):
        ts = trees(n)
        assert len(ts) == catalan(n)
        coords = {vertex(t) for t in ts}
        assert len(coords) == len(ts)
        observed = Counter()
        for t in ts:
            direct_products = sorted(rotation_products(t))
            rts = rotations(t)
            assert len(rts) == n-1
            actual_lengths = sorted(gcd(*(abs(a-b) for a,b in zip(vertex(t), vertex(q))))
                                    for q in rts)
            assert actual_lengths == direct_products, (n, t, actual_lengths, direct_products)
            observed[min(actual_lengths)] += 1
        if n >= 3:
            assert observed == Counter({1: catalan(n)-g[n], 2: g[n]}), (n,observed)
        assert cut_width(n) == n-1
        print(f'n={n}: {catalan(n)} vertices; Seshadri 1: {observed[1]}; Seshadri 2: {observed[2]}; width: {n-1}')
    print('VERIFY_OK')

if __name__ == '__main__':
    check()
