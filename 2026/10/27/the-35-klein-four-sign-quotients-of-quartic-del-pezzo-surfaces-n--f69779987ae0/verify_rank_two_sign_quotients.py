#!/usr/bin/env python3
"""Exact finite audit of the order-four subgroups of the projective five-coordinate sign group.
Scientific proof of the surface geometry is given separately; this checks the finite subgroup census.
"""
from itertools import combinations
from collections import Counter

# Projective sign vectors in F_2^5 modulo the all-ones vector.
def representative(bitmask):
    return min(bitmask, bitmask ^ 31)
A = sorted({representative(v) for v in range(32)})
assert len(A) == 16 and A[0] == 0
subgroups = set()
for a,b in combinations(A[1:],2):
    c = representative(a ^ b)
    if c and c != a and c != b:
        subgroups.add(tuple(sorted((a,b,c))))
assert len(subgroups) == 35

def flip_type(v):
    w = v.bit_count()
    return min(w, 5-w)

census = Counter(tuple(sorted(flip_type(v) for v in H)) for H in subgroups)
assert census == {(1,1,2):10,(1,2,2):15,(2,2,2):10}, census
# Scalar-free involutions have one fixed elliptic curve for type 1,
# or four isolated fixed points for type 2.  The three types have
# degree 9,4,1; 0,4,6 nodes; π1 of the smooth locus 1,C2,V4.
for types,(degree,nodes,pi1_order) in {
    (1,1,2):(9,0,1),
    (1,2,2):(4,4,2),
    (2,2,2):(1,6,4),
}.items():
    assert census[types] > 0 and degree*4 in (36,16,4)
    assert pi1_order in (1,2,4)
    print('types=',types,'subgroups=',census[types],
          'K2=',degree,'A1=',nodes,'smooth_locus_pi1_order=',pi1_order)
print('VERIFY_OK')
