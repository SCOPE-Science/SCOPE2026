#!/usr/bin/env python3
"""Independent finite checks of six-point translate-packing spectra.

Only Python standard-library modules are required.  The universal
classification is proved mathematically in the accompanying result.
"""
from collections import Counter
from itertools import combinations
from math import comb

CASES = [
    (3, (0, 1, 2, 3, 4, 5), Counter({1: 8})),
    (4, (0, 1, 2, 3, 4, 8), Counter({2: 24})),
    (4, (0, 1, 2, 4, 8, 15), Counter({1: 16})),
    (5, (0, 1, 2, 4, 8, 16), Counter({2: 16, 4: 120})),
]

def difference_set(A):
    return {x ^ y for x in A for y in A}

def all_maximal_packings(dim, A):
    """Enumerate maximal pairwise-compatible B as maximal cliques."""
    n = 1 << dim
    forbidden = difference_set(A)
    neighbors = [sum(1 << w for w in range(n)
                     if v != w and (v ^ w) not in forbidden)
                 for v in range(n)]
    found = []
    def visit(R, P, X):
        if not P and not X:
            found.append(tuple(i for i in range(n) if (R >> i) & 1))
            return
        # Deterministic pivot speeds up the 32-vertex case.
        union = P | X
        if union:
            pivots = [i for i in range(n) if (union >> i) & 1]
            pivot = max(pivots, key=lambda u: (P & neighbors[u]).bit_count())
            todo = P & ~neighbors[pivot]
        else:
            todo = P
        while todo:
            bit = todo & -todo
            v = bit.bit_length()-1
            visit(R | bit, P & neighbors[v], X & neighbors[v])
            P &= ~bit
            X |= bit
            todo &= ~bit
    visit(0, (1 << n) - 1, 0)
    assert len(found) == len(set(found))
    for B in found:
        assert all((u ^ v) not in forbidden for u, v in combinations(B, 2))
        assert all(any((v ^ w) in forbidden for w in B)
                   for v in range(n) if v not in B)
    return Counter(map(len, found))

for dim, A, desired in CASES:
    actual = all_maximal_packings(dim, A)
    assert actual == desired, (A, actual, desired)
    print('CANONICAL', dim, A, dict(sorted(actual.items())))

# A second independent enumeration checks the five-cube case by direct
# combinations, not by maximal-clique recursion.
A = CASES[-1][1]
forbidden = difference_set(A)
direct = Counter()
for size in (1, 2, 3, 4):
    for B in combinations(range(32), size):
        if any((u ^ v) in forbidden for u, v in combinations(B, 2)):
            continue
        if all(any((v ^ w) in forbidden for w in B)
               for v in range(32) if v not in B):
            direct[size] += 1
assert direct == Counter({2:16, 4:120}), direct
print('INDEPENDENT_COMBINATIONS', dict(sorted(direct.items())))

# All 6-subsets in the 5-cube modulo translations to put 0 in the subset.
def rank(S):
    basis = {}
    for x in S:
        while x:
            highest = x.bit_length() - 1
            if highest in basis:
                x ^= basis[highest]
            else:
                basis[highest] = x
                break
    return len(basis)

counts = Counter()
for T in combinations(range(1, 32), 5):
    A = (0,) + T
    s = rank(T)
    if s == 3:
        k = 'rank3'
    elif s == 5:
        k = 'rank5'
    elif s == 4:
        para = any(a ^ b ^ c ^ d == 0 for a,b,c,d in combinations(A,4))
        k = 'rank4_parallelogram' if para else 'rank4_six_circuit'
    else:
        raise AssertionError((A,s))
    counts[k] += 1
expected = {'rank3':3255, 'rank4_parallelogram':78120,
            'rank4_six_circuit':5208, 'rank5':83328}
assert counts == expected, counts
assert sum(counts.values()) == comb(31, 5)
full = {name: num*32//6 for name,num in counts.items()}
assert full == {'rank3':17360, 'rank4_parallelogram':416640,
                'rank4_six_circuit':27776, 'rank5':444416}
assert sum(full.values()) == comb(32,6)
print('CENSUS_NORMALIZED', dict(sorted(counts.items())))
print('CENSUS_ALL_SIX_SUBSETS', dict(sorted(full.items())))
print('VERIFY_OK')
