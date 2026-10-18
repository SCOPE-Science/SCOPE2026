#!/usr/bin/env python3
"""Exact circular-factor incidence and optimal-attractor census for Chacon C_1,...,C_4."""
from itertools import combinations

def word(k):
    s = 'a'
    for _ in range(k):
        s = s + s + 'b' + s
    return s

def coverages(s):
    n = len(s)
    doubled = s + s
    result = {}
    all_positions = (1 << n) - 1
    for length in range(1, n + 1):
        for start in range(n):
            factor = doubled[start:start + length]
            interval = ((1 << length) - 1) << start
            covered = (interval & all_positions) | (interval >> n)
            result[factor] = result.get(factor, 0) | covered
    return result

def accepts(chosen, masks):
    positions = sum(1 << index for index in chosen)
    return all(positions & covered for covered in masks)

expected = [(4,13,3,0),(13,124,3,0),(40,1159,1,0),(121,10582,0,546)]
for k in range(1,5):
    s = word(k)
    covers = coverages(s)
    masks = tuple(set(covers.values()))
    pair_total = sum(accepts(p, masks) for p in combinations(range(len(s)), 2))
    triple_total = (sum(accepts(t, masks) for t in combinations(range(len(s)), 3))
                    if k == 4 else 0)
    outcome = (len(s), len(covers), pair_total, triple_total)
    assert outcome == expected[k-1], (k, outcome)
    if k == 4:
        obstruction = ('baabaaababaabab','aaabaaababaabaa',
                       'aaabaaababaabab','baabaaababaabaa','aaabab')
        occurrences = tuple(tuple(i for i in range(len(s))
                            if (s+s)[i:i+len(f)] == f) for f in obstruction)
        assert occurrences == ((66,), (39,120), (12,52,93),
                               (26,80,107), (3,16,30,43,56,70,84,97,111))
        assert all(not accepts(p, (covers[f] for f in obstruction))
                   for p in combinations(range(len(s)), 2))
        assert accepts((0,16,80), masks)
        # The all-length census is exact, with lengths from 1 to |C_4| inclusive.
        print('obstruction_occs', occurrences)
        print('witness_positions', (0,16,80))
    print('C_%d length=%d distinct_factors=%d attracting_pairs=%d attracting_triples=%d'
          % (k,len(s),len(covers),pair_total,triple_total))
print('VERIFY_OK')
