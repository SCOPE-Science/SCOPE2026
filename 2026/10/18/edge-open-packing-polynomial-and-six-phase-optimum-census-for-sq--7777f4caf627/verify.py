#!/usr/bin/env python3
"""Independent finite EOP tests for square-path graph families.

Run with Python 3 standard library: python3 verify.py.
"""
from collections import Counter
from functools import lru_cache
from math import comb


def brute_polynomial(n):
    # Construct actual edges of the path square without referring to tiles.
    edges = [(i, j) for i in range(n) for j in range(i+1, min(i+3, n))]
    bad = []
    for a, (u, v) in enumerate(edges):
        flags = 0
        for b, (w, x) in enumerate(edges):
            if a == b:
                continue
            found = False
            for i in (u, v):
                for j in (w, x):
                    third = (min(i,j), max(i,j))
                    if i != j and abs(i-j) <= 2 and third != (u,v) and third != (w,x):
                        found = True
            if found:
                flags |= 1 << b
        bad.append(flags)

    result = Counter()
    def walk(i, forbidden, chosen):
        if i == len(edges):
            result[chosen] += 1
            return
        walk(i+1, forbidden, chosen)
        if (forbidden >> i) & 1 == 0:
            walk(i+1, forbidden | bad[i], chosen+1)
    walk(0, 0, 0)
    return result, len(edges)


def tile_polynomial(n):
    @lru_cache(None)
    def rec(left):
        if left > n:
            return Counter({0:1})
        out = Counter(rec(left+1))
        for width, edges, multiplicity in ((2,1,1),(3,1,1),(4,2,2),(5,2,1)):
            if left+width-1 <= n:
                for degree, count in rec(left+width+2).items():
                    out[degree+edges] += multiplicity*count
        return out
    return rec(1)


def formula_polynomial(n):
    out = Counter({0:1})
    for singles in range(n+1):
        for doubles in range(n+1):
            blocks = singles+doubles
            if blocks == 0 or 2*singles+4*doubles+2*(blocks-1)>n:
                continue
            for long_singles in range(singles+1):
                for long_doubles in range(doubles+1):
                    unused = n-2*singles-long_singles-4*doubles-long_doubles-2*(blocks-1)
                    if unused < 0:
                        continue
                    count = (comb(blocks, doubles)*comb(singles, long_singles)*
                             comb(doubles, long_doubles)*2**(doubles-long_doubles)*
                             comb(unused+blocks, blocks))
                    out[singles+2*doubles] += count
    return out


def top_formula(n):
    if n == 0 or n == 1:
        return 0, 1
    if n <= 5:
        return (1 if n in (2,3) else 2), {2:1,3:3,4:2,5:5}[n]
    k, r = divmod(n, 6)
    degree = 2*k+(0 if r in (0,1) else 1 if r in (2,3) else 2)
    counts = (
        2**(k-3)*(11*k*k+17*k+8),
        2**(k-4)*(15*k**3+47*k*k+50*k+16),
        (k+1)*2**k,
        3*(k+1)*(k+2)*2**(k-1),
        2**(k+1),
        (3*k+5)*2**k,
    )
    return degree, int(counts[r])


total = 0
for n in range(0, 12):
    brute, n_edges = brute_polynomial(n)
    tiles = tile_polynomial(n)
    formula = formula_polynomial(n)
    assert brute == tiles == formula, (n, brute, tiles, formula)
    degree, count = top_formula(n)
    assert max(brute) == degree and brute[degree] == count
    total += 2**n_edges
    print('n=%d edges=%d maximum=%d maxima=%d all=%d' %
          (n, n_edges, degree, count, sum(brute.values())))

for n in range(12, 51):
    tiles = tile_polynomial(n)
    formula = formula_polynomial(n)
    assert tiles == formula, n
    degree, count = top_formula(n)
    assert max(tiles) == degree and tiles[degree] == count, (n, degree, count)

print('VERIFICATION_OK brute_orders=0..11 transfer_orders=0..50 binary_subsets=%d' % total)
