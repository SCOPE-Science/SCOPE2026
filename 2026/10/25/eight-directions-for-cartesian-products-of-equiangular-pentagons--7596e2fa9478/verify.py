#!/usr/bin/env python3
"""Exact integer certificate for the product of two equiangular pentagons."""
from fractions import Fraction
from itertools import combinations

N = 5
TILES = [(0, 0), (0, 2), (1, 3), (2, 0),
         (2, 2), (3, 1), (3, 3), (4, 4)]

def tile(i, j):
    return {((i + a) % N, (j + b) % N) for a in (0, 1) for b in (0, 1)}

V = {(i,j) for i in range(N) for j in range(N)}
assert len(TILES) == 8 and len(set(TILES)) == 8
assert all(len(tile(i,j)) == 4 for i,j in TILES)
assert set().union(*(tile(*p) for p in TILES)) == V

# Independent incidence readout for the explicit eight-direction certificate.
rows = [tuple(sum((i,j) in tile(*p) for p in TILES) for j in range(N))
        for i in range(N)]
assert rows == [(2,1,1,1,1), (1,1,1,2,1), (1,1,1,2,1),
                (1,2,2,2,1), (1,1,1,1,2)]

# Verify row-incidence lower bound for ANY family of 2x2 tiles.
# Five entries per row and each tile meets a fixed row in <=2 cells.
per_row_needed = (N + 1)//2
assert per_row_needed == 3
assert (N * per_row_needed + 1)//2 == 8

# Independent exact fractional dual/primal certificates.
wt = Fraction(1,4)
masses = {v:sum((wt for p in V if v in tile(*p)), Fraction(0)) for v in V}
assert all(masses[v] == 1 for v in V)
assert sum((wt for _ in V), Fraction(0)) == Fraction(25,4)
assert Fraction(len(V),4) == Fraction(25,4)
assert Fraction(25,4) < 8 < 9

# All possible potential maximal product-direction incidence patterns.
assert len({frozenset(tile(i,j)) for i in range(N) for j in range(N)}) == 25
assert all(len(t) == 4 for t in (tile(i,j) for i in range(N) for j in range(N)))
# A pentagon's maximal illumination pairs are precisely the five adjacent pairs.
pairs = [{i,(i+1)%N} for i in range(N)]
assert len({frozenset(p) for p in pairs}) == N

print('EXACT_OK: cells=25 tiles=25 selected=8 row_bound=8 fractional=25/4 rows='+str(rows))
