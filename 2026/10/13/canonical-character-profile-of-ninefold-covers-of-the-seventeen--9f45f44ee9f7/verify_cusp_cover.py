#!/usr/bin/env python3
"""Exact finite character and numerical consistency checks for a 17-cusp quintic cover.

These checks concern the code combinatorics and Chern/Lefschetz formulas;
the existence of the algebraic cover is proved separately.
"""
from collections import Counter
from itertools import product

F = range(3)
u = [1] * 12 + [0] * 5
v = [1,1] + [2] * 5 + [0] * 5 + [1] * 5
assert len(u) == len(v) == 17
weight = lambda w: sum(x != 0 for x in w)
words = {(a,b):[(a*x+b*y)%3 for x,y in zip(u,v)] for a,b in product(F,repeat=2)}
assert len({tuple(w) for w in words.values()}) == 9
assert Counter(weight(w) for w in words.values()) == {12:6,15:2,0:1}
assert sum(bool(x) and bool(y) for x,y in zip(u,v)) == 7
assert sum(bool(x) or bool(y) for x,y in zip(u,v)) == 17

# Every coordinate is a nonzero row vector defining an inertia line in F_3^2.
line = lambda a,b: min((a%3,b%3),((2*a)%3,(2*b)%3))
blocks = Counter(line(a,b) for a,b in zip(u,v))
assert sorted(blocks.values()) == [2,5,5,5]

# Four order-3 subgroups, with 3 fixed points per cusp in the corresponding block.
fixed = sorted((3*n for n in blocks.values()))
assert fixed == [6,15,15,15]
assert all(n%3 == 0 for n in fixed)

# Local cusp A_2 exceptional chain has Euler characteristic 3.
e_resolution = 12*5-5
n_cusp = 17
e_smooth_base = e_resolution - 3*n_cusp
cover_degree = 9
e_cover = cover_degree*e_smooth_base + 3*n_cusp
k_square = cover_degree*5
assert (e_resolution,e_smooth_base,e_cover,k_square) == (55,4,87,45)
assert (e_cover+k_square) % 12 == 0
chi = (e_cover+k_square)//12
assert chi == 11

# Pair inverse group elements in holomorphic Lefschetz; each fixed point gives 1/3.
# Virtual Euler representation: multiplicity for characters with kernel H.
local_L = sorted((n for n in blocks.values()))  # 2,5,5,5
assert local_L == [2,5,5,5]
trivial_euler = (chi+2*sum(local_L))//9
assert (chi+2*sum(local_L)) % 9 == 0
assert trivial_euler == 5
nontrivial_euler = []
for L in local_L:
    n = chi + 2*L -(sum(local_L)-L)
    assert n%9 == 0
    nontrivial_euler.extend([n//9]*2)
assert Counter(nontrivial_euler) == {1:6,0:2}
# Irregularity vanishes by Tan's cyclic-quotient classification;
# hence H^0(K_X) = four invariant sections + 6 one-dimensional eigenspaces.
assert 4 + sum(nontrivial_euler) == 10
assert 1 - 0 + 10 == chi
print('CUSP_NINEFOLD_CHARACTER_AND_CHERN_CHECK_OK')
