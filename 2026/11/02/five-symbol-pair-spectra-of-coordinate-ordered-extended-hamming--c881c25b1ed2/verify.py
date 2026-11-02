#!/usr/bin/env python3
"""Verify the complete symbol-pair spectrum of coordinate-ordered E8 codes."""
from collections import Counter, defaultdict
from itertools import combinations, permutations
from functools import reduce
from operator import xor

N = 8
MASK = (1 << N) - 1

# Construction A: affine planes in F_2^3, represented by xor-zero 4-sets.
planes = [frozenset(s) for s in combinations(range(N), 4) if reduce(xor, s) == 0]
assert len(planes) == 14

# Construction B: all affine Boolean functions on F_2^3.
functions = []
for slope in range(8):
    for intercept in range(2):
        functions.append(tuple(((slope & v).bit_count() & 1) ^ intercept for v in range(N)))
assert len(set(functions)) == 16

def pair_weight(mask):
    return sum(((mask >> i) & 1) | ((mask >> ((i + 1) % N)) & 1)
               for i in range(N))

def encode(word, ordering):
    return sum(word[value] << position for position, value in enumerate(ordering))

def support_masks(ordering):
    index = {point: position for position, point in enumerate(ordering)}
    return frozenset([0, MASK] + [sum(1 << index[x] for x in B) for B in planes])

def affine_masks(ordering):
    return frozenset(encode(f, ordering) for f in functions)

counts = Counter()
representatives = {}
orders_per_code = defaultdict(int)
for p in permutations(range(N)):
    if p[0] != 0:
        continue
    C = support_masks(p)
    assert C == affine_masks(p)
    orders_per_code[C] += 1
    if C in representatives:
        continue
    T = sum(sum(1 << ((i + j) % 8) for j in range(4)) in C for i in range(4))
    Z = (0b01010101 in C)
    profile = tuple(sum(pair_weight(w) == d for w in C) for d in range(9))
    expected = {0:1, 5:2*T, 6:10-4*T+2*int(Z),
                7:4+2*T-4*int(Z), 8:2*int(Z)+1}
    assert all(profile[d] == expected.get(d, 0) for d in range(9))
    assert 0 <= T <= 2
    counts[(T, int(Z), profile)] += 1
    representatives[C] = p
assert len(representatives) == 30
assert set(orders_per_code.values()) == {168}

expected_counts = {(0,0):10, (1,0):12, (1,1):4, (2,0):2, (2,1):2}
assert {(T,Z):n for (T,Z,_),n in counts.items()} == expected_counts
assert sum(n for n in counts.values()) == 30
assert sum(n for (T,Z,_),n in counts.items() if T == 0) == 10
for (T,Z,profile), n in sorted(counts.items()):
    exemplar = min(p for C,p in representatives.items()
                   if sum(sum(1 << ((i+j)%8) for j in range(4)) in C for i in range(4))==T
                   and int(0b01010101 in C)==Z)
    print(f'T={T} Z={Z} codebooks={n} polynomial='+
          '+'.join(f'{a}z^{k}' for k,a in enumerate(profile) if a)+
          ' example='+str(exemplar))
print('VERIFY_OK')
