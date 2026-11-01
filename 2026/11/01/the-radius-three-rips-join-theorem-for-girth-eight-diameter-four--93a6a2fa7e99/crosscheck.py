#!/usr/bin/env python3
"""Independent simplicial mod-two chain crosscheck at all nontrivial GQ(2,2) Rips scales."""
from itertools import combinations
from collections import defaultdict,deque


def rank_mod2(columns):
    piv={}
    for x in columns:
        while x:
            hi=x.bit_length()-1
            if hi in piv:x ^= piv[hi]
            else:piv[hi]=x;break
    return len(piv)


def complexes_from_edges(pairs, n, scale):
    near=[set() for _ in range(n)]
    for u,v in pairs:
        near[u].add(v);near[v].add(u)
    d=[]
    for x in range(n):
        ds={x:0}; Q=deque([x])
        while Q:
            u=Q.popleft()
            for v in near[u]:
                if v not in ds:ds[v]=ds[u]+1;Q.append(v)
        assert len(ds)==n
        d.append(ds)
    threshold=[{v for v in range(n) if d[u][v]<=scale and v!=u} for u in range(n)]
    # Bron-Kerbosch enumerates all maximal cliques, then collect all faces.
    maximal=[]
    def bk(R,P,X):
        if not P and not X:
            maximal.append(tuple(sorted(R)));return
        pivot=max(P|X,key=lambda x:len(P&threshold[x]),default=None)
        for v in sorted(P-(threshold[pivot] if pivot is not None else set())):
            bk(R|{v},P&threshold[v],X&threshold[v]); P.remove(v);X.add(v)
    bk(set(),set(range(n)),set())
    faces=defaultdict(set)
    for m in maximal:
        for k in range(1,len(m)+1):
            faces[k-1].update(combinations(m,k))
    faces=[sorted(faces[k]) for k in range(max(faces)+1)]
    ranks=[0]*(len(faces)+1)
    for k in range(1,len(faces)):
        idx={f:i for i,f in enumerate(faces[k-1])}
        cols=[sum(1<<idx[f[:j]+f[j+1:]] for j in range(len(f))) for f in faces[k]]
        ranks[k]=rank_mod2(cols)
    beta=[len(faces[k])-ranks[k]-ranks[k+1] for k in range(len(faces))]
    return tuple(len(f) for f in faces),tuple(beta),len(maximal)


def main():
    # GQ(2,2): points = pairs of a 6-element ground set;
    # lines = 3-pair partitions, incidence by inclusion.
    duads=list(combinations(range(6),2))
    duad_idx={p:i for i,p in enumerate(duads)}
    synthemes=set()
    for x,y,z in combinations(duads,3):
        if len(set(x+y+z))==6:
            synthemes.add(tuple(sorted((duad_idx[x],duad_idx[y],duad_idx[z]))))
    synthemes=sorted(synthemes)
    assert len(synthemes)==15
    edges=[(i,15+j) for j,ss in enumerate(synthemes) for i in ss]
    assert len(edges)==45
    expected={
        0:((30,), (30,),30),
        1:((30,45),(1,16),45),
        2:((30,135,120,30),(1,16,0,0),30),
        3:((30,315,1380,2475,1350,225),(1,0,0,256,0,0),225)
    }
    # max-clique count at scale 0 = 30 vertices; scale1 = 45 edges;
    # scale2 = 30 neighborhood simplices; scale3 = 15x15 facets =225.
    for r in range(4):
        f,b,m=complexes_from_edges(edges,30,r)
        assert (f,b,m)==expected[r],(r,f,b,m,expected[r])
        print('W2_radius',r,'f_vector',f,'GF2_betti',b,'maximal_facets',m)
    print('GQ_W2_FULL_CHAIN_CROSSCHECK_OK')

if __name__=='__main__':main()
