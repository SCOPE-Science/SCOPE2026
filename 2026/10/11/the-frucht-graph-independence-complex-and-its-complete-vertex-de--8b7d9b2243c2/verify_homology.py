"""Independent exact mod-two homology checks for Frucht independence complexes.

Builds the Frucht graph from LCF, not from the edge list used in the
Morse certificate, then computes simplicial boundary ranks over F_2.
Python 3 standard library; run: python verify_homology.py
"""
from collections import Counter
LCF=[-5,-2,-4,2,5,-2,2,5,-2,-5,4,2]
permutation={4:0,3:1,2:2,1:3,7:4,0:5,6:6,5:7,10:8,11:9,8:10,9:11}
assert sorted(permutation.values())==list(range(12))
edges=set()
for i,k in enumerate(LCF):
    edges.add(tuple(sorted((i,(i+k)%12))))
    edges.add(tuple(sorted((i,(i+1)%12))))
assert len(edges)==18
reference_edges=((0,1),(0,6),(0,7),(1,2),(1,7),(2,3),(2,8),(3,4),(3,9),
         (4,5),(4,9),(5,6),(5,10),(6,10),(7,11),(8,9),(8,11),(10,11))
assert {tuple(sorted((permutation[u],permutation[v]))) for u,v in reference_edges}==edges
# The topology is calculated from a second presentation: the LCF cycle.
# For deletion/link parameters, convert the labels into LCF coordinates.
adj=[0]*12
for u,v in edges:
    adj[u]|=1<<v;adj[v]|=1<<u
assert all(m.bit_count()==3 for m in adj)

def homology(mask):
    faces=[]
    for s in range(1,1<<12):
        if s&~mask:continue
        if any((s>>i)&1 and (adj[i]&s) for i in range(12)):continue
        faces.append(s)
    levels={d:sorted(s for s in faces if s.bit_count()==d+1)
            for d in range(max((s.bit_count() for s in faces),default=0))}
    ranks={-1:0}
    # The augmented zero-dimensional boundary has rank one for every
    # nonempty complex; all other matrices are computed independently.
    for d in range(1,len(levels)):
        index={s:i for i,s in enumerate(levels[d-1])}
        pivots={}
        for simplex in levels[d]:
            vec=0
            temp=simplex
            while temp:
                bit=temp&-temp;temp-=bit
                vec ^= 1<<index[simplex^bit]
            while vec:
                pivot=vec.bit_length()-1
                if pivot in pivots:vec^=pivots[pivot]
                else:pivots[pivot]=vec;break
        ranks[d]=len(pivots)
    betti={d:len(levels[d])-ranks.get(d,0)-ranks.get(d+1,0)
           for d in levels}
    if levels:betti[0]-=1
    return Counter(s.bit_count()-1 for s in faces),{d:k for d,k in betti.items() if k}

FULL=(1<<12)-1
f,b=homology(FULL)
assert dict(f)=={0:12,1:48,2:73,3:34,4:1} and b=={2:3},(f,b)
print('full',f,b)
for old in range(12):
    v=permutation[old]
    dface,db=homology(FULL^(1<<v))
    lface,lb=homology((FULL^(1<<v)) & ~adj[v])
    d_expect=4 if old in (2,8) else 2 if old in (0,1,5,7,9,10) else 3
    l_expect=({2:1} if old in (2,8) else {1:1} if old in (0,1,5,7,9,10) else {})
    assert db=={2:d_expect},(old,'deletion',db)
    assert lb==l_expect,(old,'link',lb)
    print(old,'deletion',dict(dface),db,'link',dict(lface),lb)
print('FRUCHT_INDEPENDENT_HOMOLOGY_OK')
