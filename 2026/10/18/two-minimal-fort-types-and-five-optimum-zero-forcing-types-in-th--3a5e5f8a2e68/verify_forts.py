#!/usr/bin/env python3
"""Independent Fano-polarity incidence and fort-hitting verifier; stdlib only."""
from collections import Counter
import json,sys
N=14; UNIVERSE=(1<<N)-1

def orthogonal(a,b):return ((a&b).bit_count()&1)==0
adjacent=[0]*N
# Different model: line labels are nonzero normal vectors rather than triples.
for point in range(1,8):
    for normal in range(1,8):
        if orthogonal(point,normal):
            u=point-1; v=normal+6
            adjacent[u] |= (1<<v)
            adjacent[v] |= (1<<u)
assert all(k.bit_count()==3 for k in adjacent)

def is_fort(q):
    if q==0:return False
    for v in range(N):
        if not(q&(1<<v)):
            if (q&adjacent[v]).bit_count()==1:return False
    return True

fort_table=bytearray(is_fort(q) for q in range(1<<N))
minimal=[]
# Exact (all proper submasks), not single-deletion minimality.
for mask in range(1,1<<N):
    if not fort_table[mask]:continue
    sub=(mask-1)&mask
    while sub:
        if fort_table[sub]:break
        sub=(sub-1)&mask
    else:minimal.append(mask)
assert len(minimal)==70
assert Counter(k.bit_count() for k in minimal)=={4:14,7:56}

# Count seed sets by hitting all minimal forts (a wholly separate criterion).
def hitting(seed):
    white=UNIVERSE^seed
    for obstruction in minimal:
        if (obstruction&white)==obstruction:return False
    return True

profile=Counter(); minimum=[]
for seed in range(1<<N):
    if hitting(seed):
        profile[seed.bit_count()]+=1
        if all(not hitting(seed^(1<<i)) for i in range(N) if seed&(1<<i)):
            minimum.append(seed)
assert dict(profile)=={6:700,7:1904,8:2401,9:1862,10:987,11:364,12:91,13:14,14:1}
assert len(minimum)==700 and all(k.bit_count()==6 for k in minimum)

def iterative_coloring(start):
    while True:
        acc=0
        for v,neigh in enumerate(adjacent):
            if start & (1<<v):
                w=neigh & ~start
                if w.bit_count()==1:acc |= w
        if acc==0:return start==UNIVERSE
        start |= acc
assert all(hitting(mask)==iterative_coloring(mask) for mask in range(1<<N))

# Geometry correspondence to the independently supplied triangle model.
if len(sys.argv)>1:
    with open(sys.argv[1],encoding='utf8') as f:cert=json.load(f)
    triangles=cert['lines']
    normal_to_triangle={norm:next((j for j,L in enumerate(triangles) if
        all(orthogonal(norm,p) for p in L)),None) for norm in range(1,8)}
    assert set(normal_to_triangle.values())==set(range(7))
    def from_cert(x):
        y=x&127
        for i in range(7):
            if x&(1<<(7+i)):
                norm=next(norm for norm,j in normal_to_triangle.items() if j==i)
                y|=1<<(6+norm)
        return y
    for item in cert['minimal_fort_orbits']:
        assert from_cert(item['representative_mask']) in minimal
    for item in cert['minimum_zero_forcing_orbits']:
        assert from_cert(item['representative_mask']) in minimum
    assert sum(t['orbit_size'] for t in cert['minimal_fort_orbits'])==len(minimal)
    assert sum(t['orbit_size'] for t in cert['minimum_zero_forcing_orbits'])==len(minimum)
print('VERIFY_FORTS_OK model=dot_product_point_hyperplane masks=16384 all_70_minimal_forts_by_full_submask_test=true')
print('VERIFY_FORTS_OK minimum_fort_size_orbit_sums=4:14,7:56')
print('VERIFY_HITTING_OK all_16384_hitting_tests_agree_with_iterative_zero_forcing=true')
print('VERIFY_HITTING_OK polynomial=6:700,7:1904,8:2401,9:1862,10:987,11:364,12:91,13:14,14:1')
print('VERIFY_HITTING_OK all_inclusion_minimal_sets_size_6=true count=700')
