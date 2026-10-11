#!/usr/bin/env python3
"""Independent graph-and-chain reconstruction over the field with two elements."""
from itertools import permutations,product
from decimal import Decimal,getcontext
from collections import Counter

getcontext().prec=50
s=Decimal('1.84')
for _ in range(22):
 s=s-(s**3-s*s-s-1)/(3*s*s-2*s-1)
assert abs(s**3-s*s-s-1)<Decimal('1e-45')
coords=[]
for p in permutations((Decimal(1),1/s,s)):
    perm=tuple((Decimal(1),1/s,s).index(z) for z in p)
    inversions=sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))
    for signs in product((-1,1),repeat=3):
        if (sum(z==1 for z in signs)-inversions)%2:continue
        coords.append(tuple(signs[i]*p[i] for i in range(3)))
assert len(coords)==24
sqdist=lambda v,w: sum((x-y)**2 for x,y in zip(v,w))
dist=sorted(set(round(sqdist(v,w),25) for i,v in enumerate(coords) for w in coords[i+1:]))
assert len(dist)>1
edges=[(i,j) for i in range(24) for j in range(i+1,24)
       if round(sqdist(coords[i],coords[j]),25)==dist[0]]
assert len(edges)==60
neighbor=[0]*24
for i,j in edges:neighbor[i]|=1<<j;neighbor[j]|=1<<i
assert set(n.bit_count() for n in neighbor)=={5}
# Construct independent sets by include/exclude recursion, independent of the
# output-order traversal used in the integral Morse certificate.
fByDim=[set() for _ in range(9)]
def explore(remaining,selected):
    if not remaining:
        if selected:fByDim[selected.bit_count()].add(selected)
        return
    bit=remaining&(-remaining)
    v=bit.bit_length()-1
    explore(remaining^bit,selected)
    explore((remaining^bit)&~neighbor[v],selected|bit)
explore((1<<24)-1,0)
assert [len(fByDim[k]) for k in range(1,9)]==[24,216,912,1854,1680,564,48,3]
# Exact F_2 simplicial boundary ranks, using xor column elimination.
def boundary_rank(cells,facets):
    labels={f:i for i,f in enumerate(facets)}
    pivots={}
    for c in sorted(cells):
        col=0;bits=c
        while bits:
            b=bits&(-bits);bits-=b
            col ^= 1 << labels[c^b]
        while col:
            j=col.bit_length()-1
            if j in pivots:col^=pivots[j]
            else:pivots[j]=col;break
    return len(pivots)
ranks={k:boundary_rank(fByDim[k+1],fByDim[k]) for k in range(1,8)}
# For the (unreduced) chains, rank of d_1=23 since the 1-skeleton is connected.
assert ranks=={1:23,2:193,3:719,4:1135,5:519,6:45,7:3},ranks
betti={k-1:len(fByDim[k])-ranks.get(k,0)-ranks.get(k-1,0) for k in range(1,9)}
assert betti=={0:1,1:0,2:0,3:0,4:26,5:0,6:0,7:0},betti
print('decimal_coordinates=24 distinct_edges=60 min_squared_distance=',dist[0])
print('independent_set_counts=',[len(fByDim[k]) for k in range(1,9)])
print('mod2_boundary_ranks=',ranks)
print('unreduced_mod2_betti=',betti)
