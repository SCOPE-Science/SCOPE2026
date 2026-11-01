"""Independent mod-two boundary-rank cross-check for 24-cell neighborhood complex.
No discrete-Morse input and no external dependencies.
"""
from itertools import combinations,product
from collections import Counter,defaultdict
V=[]
for a,b in combinations(range(4),2):
    for s,t in product((-1,1),repeat=2):
        x=[0]*4;x[a]=s;x[b]=t;V.append(tuple(x))
faces=set()
for v in V:
    near=[i for i,w in enumerate(V) if sum(v[k]*w[k] for k in range(4))==1]
    assert len(near)==8
    for mask in range(1,1<<8):
        faces.add(sum(1<<near[j] for j in range(8) if mask>>j&1))
dims=defaultdict(list)
for f in faces:dims[f.bit_count()-1].append(f)
for d in dims:dims[d].sort()
rank={}
for d in sorted(dims,reverse=True):
    if d==0:continue
    previous={f:i for i,f in enumerate(dims[d-1])}
    pivots={}
    for top in dims[d]:
        vector=0
        for b in range(24):
            if top>>b&1:vector ^= 1<<previous[top^(1<<b)]
        while vector:
            pivot=vector.bit_length()-1
            if pivot not in pivots:
                pivots[pivot]=vector
                break
            vector ^= pivots[pivot]
    rank[d]=len(pivots)
betti={d:len(seq)-rank.get(d,0)-rank.get(d+1,0) for d,seq in dims.items()}
assert betti=={0:1,1:1,2:0,3:48,4:0,5:0,6:0,7:0},betti
print('BOUNDARY_RANKS',dict(sorted(rank.items())))
print('BETTI_F2',dict(sorted(betti.items())))
print('MOD2_VERIFY_OK')
