#!/usr/bin/env python3
"""Exact finite certificate for ternary length-six restricted-overlap optimum."""
from itertools import product
from collections import Counter, defaultdict

S = range(3)
pairs = tuple(product(S, repeat=2))
triples = tuple(product(S, repeat=3))
assert len(pairs) == 9 and len(triples) == 27

# Every disjoint ordered-pair classification A,B is a map into {unused,A,B}.
# This is a complete 3^9 exhaustive finite check, not stochastic sampling.
max_global = 0
max_by_total = defaultdict(int)
best_count = 0
hist = Counter()
for labels in product(range(3), repeat=9):
    A = {pairs[i] for i in range(9) if labels[i] == 1}
    B = {pairs[i] for i in range(9) if labels[i] == 2}
    assert not A.intersection(B)
    a, b = len(A), len(B)
    common = sum(((u,v) in A and (v,w) in B) for u,v,w in triples)
    assert 0 <= common <= min(3*a,3*b)
    # x prefixes available = 3a, y suffixes available = 3b;
    # exactly 'common' triple words are in both candidate sets.
    # Assign j of these to the prefix side, the other common-j to suffix.
    best = max((3*a-common+j)*(3*b-j) for j in range(common+1))
    hist[best] += 1
    max_by_total[a+b] = max(max_by_total[a+b], best)
    if best > max_global:
        max_global = best
        best_count = 1
    elif best == max_global:
        best_count += 1
assert sum(hist.values()) == 3**9 == 19683
assert max_global == 132 and best_count == 6
assert [max_by_total[k] for k in range(10)] == [0,0,9,18,36,54,81,108,121,132]

# Explicit extremizer, with symbol 0 distinguished:
# length-3 prefixes have first and last consecutive pairs containing 0.
# length-3 suffixes have both last two symbols nonzero.
P = {u for u in triples if 0 in u[:2] and 0 in u[1:]}
T = {u for u in triples if u[1] != 0 and u[2] != 0}
assert len(P)==11 and len(T)==12
assert not P.intersection(T)
assert not {u[:2] for u in P}.intersection({u[-2:] for u in T})

# Entire family at both boundary length n=6 and a longer n=7.
for n in (6,7):
    words = {p+mid+t for p in P for mid in product(S,repeat=n-6) for t in T}
    assert len(words) == 132 * 3**(n-6)
    for k in (2,3):
        assert not {u[:k] for u in words}.intersection({v[-k:] for v in words})

# Independent bitmask-based optimization over all disjoint A,B pair masks.
# This rechecks the global optimum without reusing ternary label-tuples.
mask_max = 0
for A_mask in range(512):
    rem = 511 ^ A_mask
    B_mask = rem
    while True:
        a, b = A_mask.bit_count(), B_mask.bit_count()
        shared = 0
        for i in range(3):
            for j in range(3):
                if A_mask & (1 << (3*i+j)):
                    for k in range(3):
                        if B_mask & (1 << (3*j+k)):
                            shared += 1
        val = max((3*a-shared+t)*(3*b-t) for t in range(shared+1))
        mask_max=max(mask_max,val)
        if B_mask==0:break
        B_mask=(B_mask-1)&rem
assert mask_max==132
print('LABEL_ASSIGNMENTS=19683')
print('UPPER_ENVELOPE_BY_ACTIVE_PAIRS='+','.join(str(max_by_total[k]) for k in range(10)))
print('MAXIMUM=132; MAXIMIZING_ASSIGNMENTS=6')
print('LOWER_PREFIX_TRIPLES=11; LOWER_SUFFIX_TRIPLES=12')
print('VERIFY_OK')
