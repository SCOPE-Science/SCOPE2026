#!/usr/bin/env python3
"""Direct graph-vertex cross-check of four-round Hamming-graph tuple types.

Independent of coordinate-partition extension enumeration: every selected
third and fourth vertex is enumerated as an actual graph vertex.
"""
from itertools import product
from verify_hamming_symbolic import pair_type

def direct_pair_type(d,a,j):
    V=list(product(range(a),repeat=d))
    x=(0,)*d
    y=(1,)*j+(0,)*(d-j)
    def dist(u,v):return min(2,sum(t!=w for t,w in zip(u,v)))
    extensions=set()
    for z in V:
        old=(dist(x,y),dist(x,z),dist(y,z))
        atom=set()
        for w in V:
            atom.add((dist(x,w),dist(y,w),dist(z,w)))
        mask=0
        for pattern in atom:
            mask |= 1 << (pattern[0]*9+pattern[1]*3+pattern[2])
        extensions.add((old,mask))
    return (dist(x,y),frozenset(extensions))

for a,d in ((2,1),(2,2),(2,3),(2,4),(2,5),(3,1),(3,2),(3,3),
            (3,4),(4,1),(4,2),(4,3)):
    for j in range(d+1):
        assert direct_pair_type(d,a,j)==pair_type(d,a,j),(a,d,j)
    print('DIRECT_PAIR_TYPES_OK',a,d,a**d)
print('DIRECT_VERIFY_OK')
