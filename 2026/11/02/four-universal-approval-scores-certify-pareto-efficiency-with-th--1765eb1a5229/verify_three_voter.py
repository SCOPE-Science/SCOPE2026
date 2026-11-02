#!/usr/bin/env python3
"""Exact finite checks for three-voter committee Pareto certificates.

Independent enumerator: it compares every feasible cardinality-k utility
vector with all other integral vectors, then independently compares four
fixed weighted-approval maximizers. Finite enumeration supplements the
unbounded-candidate proof in RESULT.md; it cannot establish that proof.
"""
from itertools import product
from random import Random

WEIGHTS = ((1,1,1),(2,1,1),(1,2,1),(1,1,2))
TYPES = tuple(tuple((mask >> i) & 1 for i in range(3)) for mask in range(8))

def check_profile(capacity):
    vectors_by_k = {}
    for selected in product(*(range(c+1) for c in capacity)):
        size = sum(selected)
        values = tuple(sum(selected[t]*TYPES[t][j] for t in range(8)) for j in range(3))
        vectors_by_k.setdefault(size,set()).add(values)
    checked = 0
    for size, vectors in vectors_by_k.items():
        vals = tuple(vectors)
        max_scores = tuple(max(sum(x*y for x,y in zip(w,v)) for v in vals) for w in WEIGHTS)
        for v in vals:
            efficient = not any((u != v and all(x>=y for x,y in zip(u,v))) for u in vals)
            certified = any(sum(x*y for x,y in zip(w,v)) == m for w,m in zip(WEIGHTS,max_scores))
            assert efficient == certified, (capacity,size,v,efficient,certified)
            checked += 1
    return checked

def run():
    profiles=0; vector_checks=0
    # Every multiset of candidate approval types with at most two candidates
    # per type: 3^8 distinct capacity vectors, including empty profiles.
    for c in product(range(3),repeat=8):
        profiles += 1
        vector_checks += check_profile(c)
    # Random higher multiplicities, with exact enumeration within each draw.
    rng=Random(20261031)
    for _ in range(400):
        c=tuple(rng.randrange(5) for _ in range(8))
        vector_checks += check_profile(c)
    print('PASS',profiles,'exhaustive capacity profiles; 400 seeded higher-capacity profiles; checked',vector_checks,'unique utility profiles')

if __name__=='__main__':
    run()
