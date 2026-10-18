#!/usr/bin/env python3
"""Independently reconstruct face sets and compute mod-two homology by sparse elimination."""
from collections import defaultdict
from itertools import combinations

def homology(n):
    stable=tuple(frozenset(pair) for pair in combinations(range(n),2)
                 if min((pair[1]-pair[0])%n, (pair[0]-pair[1])%n)>=3)
    common=[tuple(i for i,v in enumerate(stable) if not v.intersection(w)) for w in stable]
    all_faces=set()
    for neighborhood in common:
        for size in range(1,len(neighborhood)+1):
            all_faces.update(combinations(neighborhood,size))
    by_size={size: sorted(f for f in all_faces if len(f)==size)
             for size in range(1,max(map(len,all_faces))+1)}
    ranks={1:0}
    for k in range(2,len(by_size)+1):
        low_indices={face:i for i,face in enumerate(by_size[k-1])}
        pivots={}
        for face in by_size[k]:
            col=0
            for a in range(k):
                col^=1<<low_indices[face[:a]+face[a+1:]]
            while col:
                pivot=col.bit_length()-1
                if pivot not in pivots:
                    pivots[pivot]=col
                    break
                col^=pivots[pivot]
        ranks[k]=len(pivots)
    betti={k-1:len(faces)-ranks.get(k,0)-ranks.get(k+1,0)
           for k,faces in by_size.items()}
    betti[0]-=1
    return stable,common,by_size,ranks,betti

for n in (6,7,8):
    vert,nb,faces,ranks,betti=homology(n)
    print('n',n,'vertices',len(vert),'facets',len(nb),'faces',sum(map(len,faces.values())),
          'f_vector',tuple(map(len,faces.values())),
          'mod2_boundary_ranks',tuple(ranks.get(k,0) for k in range(1,len(faces)+1)),
          'reduced_betti',betti)
    if n<8: assert {k:v for k,v in betti.items() if v}=={1:1}
    else: assert {k:v for k,v in betti.items() if v}=={2:2,3:1}
print('independent_mod2_check_OK')
