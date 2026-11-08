#!/usr/bin/env python3
"""Exact integer checks for shared Walsh spectra of eight-point affine simplices."""
from collections import Counter
from itertools import combinations

N = 128
A = (0, 1, 2, 4, 8, 16, 32, 64)

def parity(n):
    return n.bit_count() & 1

def walsh_mask(support, diff):
    return sum(1 - 2*parity(x & diff) for x in support)

weight4 = [i for i in range(1,N) if i.bit_count()==4]
planes=set()
for a,b,c in combinations(weight4,3):
    nonzero={a,b,c,a^b,a^c,b^c,a^b^c}
    if len(nonzero)==7 and all(x.bit_count()==4 for x in nonzero):
        planes.add(tuple(sorted(nonzero)))
assert len(planes)==30, len(planes)

specs=set()
for L in planes:
    L=(0,)+L
    for t in range(N):
        specs.add(tuple(sorted(v^t for v in L)))
assert len(specs)==480, len(specs)

# Independent direct test against the defining Walsh inner products for both supports.
for S in specs:
    assert all(walsh_mask(A, x^y)==0 for x,y in combinations(S,2))
counts={}
for u in range(64):
    B=(0,1,2,4,8,16,32,64 | u)
    count=sum(all(walsh_mask(B,x^y)==0 for x,y in combinations(S,2)) for S in specs)
    counts[u]=count
    h=u.bit_count()
    expected=480 if h==0 else 96 if h in (3,4) else 0
    assert count==expected, (u,h,count,expected)

# An independent incidence check on all 128 binary 7-coordinate mutations.
incidence={h:Counter() for h in range(8)}
for u in range(128):
    n=sum(all(parity(u & v)==0 for v in L) for L in planes)
    incidence[u.bit_count()][n]+=1
assert incidence=={
    0:Counter({30:1}), 1:Counter({0:7}), 2:Counter({0:21}),
    3:Counter({6:35}), 4:Counter({6:35}), 5:Counter({0:21}),
    6:Counter({0:7}), 7:Counter({30:1})
},incidence
print('CHECK_OK subspaces=30 spectra=480 mutations=64 direct_pair_tests=%d incidence_vectors=128'% (64*480*28))
