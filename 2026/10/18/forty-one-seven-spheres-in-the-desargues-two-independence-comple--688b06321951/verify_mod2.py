#!/usr/bin/env python3
"""Independent boundary-matrix homology check over F_2 for GP(10,3)."""
from collections import defaultdict
n=10
adj=[0]*20
for i in range(n):
 for u,v in ((i,(i+1)%10),(i,10+i),(10+i,10+(i+3)%10)):
  adj[u]|=1<<v;adj[v]|=1<<u
f_by_dim=defaultdict(list)
for mask in range(1,1<<20):
    s=mask
    while s:
        b=s&-s; v=b.bit_length()-1
        if ((mask&adj[v]).bit_count())>1: break
        s-=b
    else:f_by_dim[mask.bit_count()-1].append(mask)
assert sum(map(len,f_by_dim.values()))==62048
ranks={0:0,12:0}
for d in range(1,12):
    low_index={f:j for j,f in enumerate(f_by_dim[d-1])}
    pivots={}
    for f in f_by_dim[d]:
        x=0;s=f
        while s:
            b=s&-s;s-=b
            x^=1<<low_index[f-b]
        while x:
            p=x.bit_length()-1
            if p in pivots: x^=pivots[p]
            else:
                pivots[p]=x;break
    ranks[d]=len(pivots)
    print('boundary',d,'rank',ranks[d],flush=True)
bettis={d:len(f_by_dim[d])-ranks[d]-ranks[d+1] for d in f_by_dim}
print('reduced bettis:',{d:(k-(1 if d==0 else 0)) for d,k in bettis.items() if k-(1 if d==0 else 0)})
assert {d:(k-(1 if d==0 else 0)) for d,k in bettis.items() if k-(1 if d==0 else 0)} == {7:41}
print('PASS')
