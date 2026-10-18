#!/usr/bin/env python3
"""Finite-state and exact-arithmetic checks for the random-tournament cycle identity."""
from fractions import Fraction as F
from itertools import combinations, permutations
from math import comb
from collections import Counter


def cycles(n, mask, edges, index, triples, fours):
    def arrow(i, j):
        if i < j:
            return (mask >> index[(i, j)]) & 1
        return 1 - ((mask >> index[(j, i)]) & 1)
    triangle_state = {}
    for a, b, c in triples:
        triangle_state[a, b, c] = int(arrow(a, b) == arrow(b, c) == arrow(c, a))
    four_state = {}
    for s in fours:
        root = s[0]
        total = 0
        for tail in permutations(s[1:]):
            v = (root,) + tail
            total += int(all(arrow(v[i], v[(i + 1) % 4]) for i in range(4)))
        assert total in (0, 1), ('nonbinary 4-cycle count', n, mask, s, total)
        four_state[s] = total
    return triangle_state, four_state


def enumerate_moments(n):
    edges = list(combinations(range(n), 2))
    index = {e: i for i, e in enumerate(edges)}
    triples = list(combinations(range(n), 3))
    fours = list(combinations(range(n), 4))
    acc = Counter()
    loc = Counter()
    for mask in range(1 << len(edges)):
        t, f = cycles(n, mask, edges, index, triples, fours)
        X = sum(t.values())
        Y = sum(f.values())
        acc['X'] += X
        acc['Y'] += Y
        acc['XX'] += X * X
        acc['YY'] += Y * Y
        acc['XY'] += X * Y
        vals = []
        for s in fours:
            local_X = sum(t[a] for a in combinations(s, 3))
            local_Y = f[s]
            loc[(local_X, local_Y)] += 1
            vals.append(8*local_Y-4*local_X+1)
        if n >= 4:
            assert sum(vals) == 8*Y-4*(n-3)*X+len(fours)
            acc['8R'] += sum(vals)
            acc['64R2'] += sum(vals)**2
            acc['8RX'] += sum(vals)*X
        if n == 6:
            if mask == 0:
                pair_groups = Counter(len(set(s)&set(u)) for s,u in combinations(fours,2))
                assert pair_groups[2] and pair_groups[3]
            for a in range(len(fours)):
                for b in range(a+1,len(fours)):
                    acc[('64pair',len(set(fours[a])&set(fours[b])))] += vals[a]*vals[b]
    size = 1 << len(edges)
    EX, EY = F(acc['X'], size), F(acc['Y'], size)
    varX, varY = F(acc['XX'], size)-EX**2, F(acc['YY'], size)-EY**2
    covXY = F(acc['XY'], size)-EX*EY
    alpha = F(n-3, 2)
    assert EX == F(comb(n, 3), 4)
    assert EY == F(3 * comb(n, 4), 8)
    assert varX == F(3 * comb(n, 3), 16)
    assert covXY == F(3 * comb(n, 4), 8)
    assert varY == F(3 * (4*n-11) * comb(n, 4), 64)
    assert varY - alpha**2 * varX == F(3 * comb(n, 4), 64)
    assert acc['8R'] == 0 and acc['8RX'] == 0
    assert F(acc['64R2'], 64*size) == F(3*comb(n,4),64)
    if n==6:
        for k in (2,3): assert acc[('64pair',k)] == 0
    assert covXY**2 / (varX * varY) == F(4*(n-3), 4*n-11)
    print('n', n, 'orientations', size, 'EX', EX, 'EY', EY, 'varX', varX,
          'varY', varY, 'cov', covXY, 'local-types', dict(sorted(loc.items())))


# Exhaustively validate every local tournament, including the conditional-degeneracy lemma.
n = 4
es = list(combinations(range(n), 2))
index = {e:i for i,e in enumerate(es)}
triangles = list(combinations(range(n), 3))
whole = tuple(range(n))
count = Counter()
for mask in range(64):
    t, f = cycles(4, mask, es, index, triangles, [whole])
    x, y = sum(t.values()), f[whole]
    assert (x, y) in {(0, 0), (1, 0), (2, 1)}
    count[x, y] += 1
assert count == Counter({(0, 0):24, (1, 0):16, (2, 1):24})
for triple in triangles:
    for orientations in range(8):
        vals = []
        triples_edges = [e for e in es if set(e) <= set(triple)]
        for mask in range(64):
            if sum(((mask >> index[e]) & 1) << j for j, e in enumerate(triples_edges)) != orientations:
                continue
            t, f = cycles(4, mask, es, index, triangles, [whole])
            vals.append(F(f[whole]) - F(sum(t.values()), 2) + F(1, 8))
        assert len(vals) == 8
        assert sum(vals) == 0

for n in (4,5,6):
    enumerate_moments(n)
for n in range(4, 101):
    a = F(n-3, 2)
    vx = F(3*comb(n,3),16)
    vr = F(3*comb(n,4),64)
    vy = F(3*(4*n-11)*comb(n,4),64)
    cv = F(3*comb(n,4),8)
    assert a*a*vx + vr == vy and a*vx == cv
    assert cv*cv == vx*vy*F(4*(n-3),4*n-11)
print('All exact checks passed. Computational checks cover only the displayed finite sizes; the general theorem is proved algebraically.')
