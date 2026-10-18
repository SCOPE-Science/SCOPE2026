#!/usr/bin/env python3
"""Independent independent-set-partition/union-find verification of recoloring components."""
from collections import Counter
from itertools import permutations

# Independent full neighborhood-mask encoding of the same labeled graph.
# Bit j in A[i] indicates an edge between i and j.
A=[0x252,0x0a5,0x14a,0x294,0x129,0xc12,
   0xc05,0x90a,0x494,0xc09,0x360,0x2e0]
assert all((A[i] >> i & 1)==0 for i in range(12))
assert all(bool(A[i] >> j & 1)==bool(A[j] >> i & 1)
           for i in range(12) for j in range(12))
assert all(x.bit_count()==4 for x in A)
FULL=(1<<12)-1
# Compute all independent subsets via a mask recurrence (without assigning colors).
indep=[False]*(FULL+1);indep[0]=True
for mask in range(1,FULL+1):
    bit=mask & -mask;v=bit.bit_length()-1;old=mask^bit
    indep[mask]=indep[old] and not (A[v] & old)
by_first=[[] for _ in range(12)]
for mask in range(1,FULL+1):
    if indep[mask]:
        by_first[(mask&-mask).bit_length()-1].append(mask)
parts=[]
def visit(rem,blocks):
    if len(blocks)==4:
        if rem==0:parts.append(tuple(blocks))
        return
    if rem.bit_count()<4-len(blocks):return
    v=(rem&-rem).bit_length()-1
    # The block containing the least remaining vertex is chosen next.
    # Any candidate must be independent and wholly contained in rem.
    for group in by_first[v]:
        if (group&rem)==group:
            visit(rem^group,blocks+[group])
visit(FULL,[])
assert len(parts)==751
colorings=set()
for partition in parts:
    for perm in permutations(range(4)):
        arr=[-1]*12
        for block,color in zip(partition,perm):
            for v in range(12):
                if (block>>v)&1:arr[v]=color
        assert all(x>=0 for x in arr)
        colorings.add(tuple(arr))
assert len(colorings)==18024
colors=sorted(colorings); pos={c:i for i,c in enumerate(colors)}
par=list(range(len(colors))); size=[1]*len(colors)
def find(x):
    while par[x]!=x:
        par[x]=par[par[x]];x=par[x]
    return x
def union(x,y):
    x=find(x);y=find(y)
    if x!=y:
        if size[x]<size[y]:x,y=y,x
        par[y]=x;size[x]+=size[y]
edges=0
for i,c in enumerate(colors):
    for v in range(12):
        forbidden=0
        bits=A[v]
        while bits:
            bit=bits & -bits
            forbidden|=1<<c[bit.bit_length()-1]
            bits^=bit
        for t in range(4):
            if c[v]!=t and not ((forbidden>>t)&1):
                alt=list(c);alt[v]=t
                j=pos[tuple(alt)]
                if j>i:
                    edges+=1;union(i,j)
cc=Counter(find(i) for i in range(len(colors)))
assert sorted(cc.values())==[9012,9012]
print('INDEPENDENT_PARTITIONS 751; LABELED_4_COLORINGS 18024')
print('ONE_VERTEX_COMPONENT_SIZES 9012 9012')
print('ONE_VERTEX_EDGES',edges)
print('INDEPENDENT_VERIFY_OK')
