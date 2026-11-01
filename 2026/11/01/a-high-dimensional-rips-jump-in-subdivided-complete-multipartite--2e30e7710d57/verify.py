#!/usr/bin/env python3
"""Finite graph-distance and modular homology checks for subdivided multipartite graphs."""
import json
from collections import deque
from itertools import combinations
from math import prod


def model(sizes):
    orig=tuple(('v',p,i) for p,sz in enumerate(sizes) for i in range(sz))
    edge=tuple(('e',u,v) for u,v in combinations(orig,2) if u[1]!=v[1])
    verts=orig+edge
    adj={x:set() for x in verts}
    for e in edge:
        for v in e[1:]:
            adj[e].add(v);adj[v].add(e)
    D={}
    for v in verts:
        d={v:0};q=deque([v])
        while q:
            w=q.popleft()
            for x in adj[w]:
                if x not in d:d[x]=d[w]+1;q.append(x)
        D[v]=d
    return orig,edge,verts,adj,D

def clique_faces(verts,D,t):
    graph={v:{w for w in verts if v!=w and D[v][w]<=t} for v in verts}
    faces={frozenset()}
    def extend(clique,cands):
        for i,v in enumerate(cands):
            f=clique+(v,)
            faces.add(frozenset(f))
            extend(f,[w for w in cands[i+1:] if w in graph[v]])
    extend((),list(verts))
    return faces

def rank2(columns,rows):
    ix={f:i for i,f in enumerate(rows)}
    basis={}
    for c in columns:
        bit=0
        for v in c:bit^=1<<ix[c-frozenset((v,))]
        while bit:
            p=bit.bit_length()-1
            if p not in basis:basis[p]=bit;break
            bit^=basis[p]
    return len(basis)

def check(sizes):
    O,E,V,A,D=model(sizes)
    k=len(sizes);n=sum(sizes);edges=len(E)
    B=prod(x-1 for x in sizes)
    t=sum(prod(sizes[i] for i in combi) for combi in combinations(range(k),3))
    f0=n;f1=edges;f2=t
    C=f0-f1+f2-1 if k>=3 else B
    jdim=k+2 if k>=3 else 3
    jrank=B*C
    assert max(max(x.values()) for x in D.values())==4
    for e in E:
        for v in O:
            assert D[e][v] in (1,3)
    for e,f in combinations(E,2):
        assert D[e][f]==(2 if set(e[1:])&set(f[1:]) else 4)
    for u,v in combinations(O,2):
        assert D[u][v]==(4 if u[1]==v[1] else 2)
    result={'parts':list(sizes),'vertices':len(V),'edges_original':edges,
      'triangle_count':t,'expected_scale_2_old_sphere_rank':B,'expected_scale_2_extra_2_spheres':t,
      'expected_scale_3_sphere_dimension':jdim,'expected_scale_3_sphere_rank':jrank}
    for t0 in (1,2,3):
        fs=clique_faces(V,D,t0)
        result[f'scale_{t0}_nonempty_faces']=len(fs)-1
        # Graph metric yields exact joins at scale 3.
        if t0==3:
            for f in fs:
                orig=f.intersection(O)
                edg=f.intersection(E)
                assert len({v[1] for v in orig})==len(orig)
                if len(edg)>2:
                    common=set(next(iter(edg))[1:])
                    for e in edg:common.intersection_update(e[1:])
                    # star cliques have a common end or triangles from three graph edges
                    if not common:
                        edges0=list(f.intersection(E))
                        assert len(edges0)==3
                        assert len(set().union(*(set(e[1:]) for e in edges0)))==3
        if t0 in (2,3):
            bydim={j:[f for f in fs if len(f)==j+1] for j in range(max(map(len,fs)))}
            if len(fs)<6500:
                r={j:rank2(bydim[j],bydim[j-1]) for j in bydim if j>=1}
                beta={j:len(bydim[j])-r.get(j,0)-r.get(j+1,0) for j in bydim}
                result[f'scale_{t0}_mod2_betti']=beta
                if t0==2:
                    target={0:1,1:(B if k==2 else 0),2:(t+(B if k==3 else 0))}
                    if k>=4:target[k-1]=B
                    for j,v in beta.items():assert v==target.get(j,0),('r2',sizes,j,v,target)
                if t0==3:
                    for j,v in beta.items():assert v==(1 if j==0 else jrank if j==jdim else 0),('r3',sizes,j,v,jrank,jdim)
    return result

if __name__=='__main__':
    for sizes in [(2,2),(2,3),(3,3),(2,2,2),(2,2,3),(2,2,2,2)]:
        print(json.dumps(check(sizes),sort_keys=True))
