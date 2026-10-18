#!/usr/bin/env python3
"""Independent mod-two chain-rank reconstruction using the LCF representation of the Frucht graph."""
from collections import Counter
from itertools import combinations
LCF=(-5,-2,-4,2,5,-2,2,5,-2,-5,4,2)
OLD_TO_LCF={4:0,3:1,2:2,1:3,7:4,0:5,6:6,5:7,10:8,11:9,8:10,9:11}
REF=((0,1),(0,6),(0,7),(1,2),(1,7),(2,3),(2,8),(3,4),(3,9),
     (4,5),(4,9),(5,6),(5,10),(6,10),(7,11),(8,9),(8,11),(10,11))

def main():
    graph_edges={tuple(sorted((i,(i+1)%12))) for i in range(12)}
    graph_edges.update(tuple(sorted((i,(i+LCF[i])%12))) for i in range(12))
    assert len(graph_edges)==18
    assert graph_edges=={tuple(sorted((OLD_TO_LCF[u],OLD_TO_LCF[v]))) for u,v in REF}
    E=tuple(sorted(graph_edges)); n=len(E)
    faces=[[] for _ in range(6)]
    for m in range(1,1<<n):
        vertices=[]
        for i,(a,b) in enumerate(E):
            if m&(1<<i):vertices.extend((a,b))
        if len(vertices)!=len(set(vertices)):continue
        faces[m.bit_count()-1].append(m)
    assert [len(x) for x in faces]==[18,117,333,397,152,8]
    dims=[];prev_rank=0
    for k in range(5,-1,-1):
        if k==0:
            rk=0
        else:
            rows={x:i for i,x in enumerate(faces[k-1])}
            pivots={}
            for mask in faces[k]:
                col=0
                for i in range(n):
                    if mask&(1<<i):col ^= 1<<rows[mask^(1<<i)]
                while col:
                    pivot=col.bit_length()-1
                    if pivot not in pivots:
                        pivots[pivot]=col
                        break
                    col ^= pivots[pivot]
            rk=len(pivots)
        dims.append((k,len(faces[k]),rk,prev_rank))
        prev_rank=rk
    ranks={k:c-rk-higher for k,c,rk,higher in dims}
    assert ranks=={0:1,1:0,2:0,3:20,4:0,5:0},ranks
    assert sum((-1)**k*len(faces[k]) for k in range(6))==-19
    print('LCF_GRAPH_ISOMORPHISM_OK',len(E),'edges')
    print('BOUNDARY_RANKS_BY_DIM',tuple((k,rk) for k,c,rk,h in sorted(dims)))
    print('MOD2_BETTI',tuple(ranks[k] for k in range(6)))
    print('FRUCHT_INDEPENDENT_HOMOLOGY_OK')
if __name__=='__main__':main()
