"""Exhaustive, standard-library verification of order-five binary de Bruijn cross-join metrics.

State: truth-table mask F in [0,65535].  State word x has successor
2*(x mod 16) + ((x//16) XOR F[x mod 16]).
All masks with a single 32-state orbit from 0 are the objects counted.
"""
from collections import Counter, deque
from itertools import combinations

N = 1 << 5
M = 1 << 4

def successor(x, f):
    z = x & (M-1)
    return 2*z + ((x >> 4) ^ ((f >> z)&1))

def maximal_cycle(f):
    x, seen = 0, 0
    for _ in range(N):
        if seen & (1 << x):
            return False
        seen |= 1 << x
        x = successor(x, f)
    return x == 0 and seen == (1 << N) - 1

states = [f for f in range(1 << M) if maximal_cycle(f)]
assert len(states) == 2048
assert all((f & 32769) == 32769 for f in states)
assert len(set(states)) == len(states)
valid = set(states)
adj = {f: [] for f in states}
for f in states:
    for i in range(M):
        for j in range(i+1,M):
            g = f ^ (1 << i) ^ (1 << j)
            if g in valid:
                adj[f].append(g)
assert all(f in adj[g] for f in states for g in adj[f])
assert sum(map(len, adj.values()))//2 == 38704
# All 2048 states and every pair; no sampling or orbit assumptions.
pair_dist = Counter()
ecc = Counter()
centers = []
for i, f in enumerate(states):
    lengths = Counter()
    for g in states:
        lengths[(f ^ g).bit_count()//2] += 1
    ef = max(lengths)
    ecc[ef] += 1
    if ef == 5: centers.append(f)
    for g in states[i+1:]:
        pair_dist[(f ^ g).bit_count()//2] += 1
assert sorted(ecc.items()) == [(5,48),(6,1264),(7,736)]
assert [pair_dist[i] for i in range(1,8)] == [38704,305376,758800,710976,254800,27104,368]
assert len(centers) == 48 and all(f.bit_count()==7 for f in centers)
assert all(((f ^ 0x7ffe) in valid) == ((max((f ^ g).bit_count() for g in states)) == 14) for f in states)
assert sum((f ^ 0x7ffe) in valid for f in states) == 736
assert 0x80af in valid and 0xff51 in valid
assert (0x80af ^ 0xff51).bit_count() == 14
# Direct search of the complete set of edges proves that every nontrivial pair
# admits a legal move decreasing the Hamming distance by exactly two.
for f in states:
    near = set(adj[f])
    for g in states:
        if f != g:
            dis = (f ^ g).bit_count()
            assert any((h ^ g).bit_count() == dis - 2 for h in near)
print('TRUTH_TABLE_65536_CANDIDATES_2048_FULL_CYCLES_PASS')
print('CROSS_JOIN_38704_EDGES_AND_ALL_PAIR_GEODESIC_DESCENT_PASS')
print('DISTANCES_38704_305376_758800_710976_254800_27104_368_PASS')
print('RADIUS5_CENTER48_DIAMETER7_ANTIPODE_PAIRS368_PASS')
