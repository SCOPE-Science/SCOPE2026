#!/usr/bin/env python3
"""Finite exact acyclic matching and homology check for the Frucht dissociation complex.
Uses only Python 3 standard library; all graph edges are specified below.
"""
from collections import Counter, deque
import json

EDGES = ((0,1),(0,6),(0,7),(1,2),(1,7),(2,3),(2,8),
         (3,4),(3,9),(4,5),(4,9),(5,6),(5,10),(6,10),
         (7,11),(8,9),(8,11),(10,11))
ORDER = (9,0,1,7,8,10,4,11,2,3,5,6)
N=12

def graph():
    adj=[0]*N
    for u,v in EDGES:
        adj[u]|=1<<v; adj[v]|=1<<u
    assert len(set(EDGES))==18
    assert all(row.bit_count()==3 for row in adj)
    return adj

def comp_size_at_most_two(mask,adj):
    remaining=mask
    while remaining:
        frontier=remaining & -remaining
        visited=0
        while frontier:
            vbit=frontier & -frontier;frontier ^= vbit
            if visited & vbit:continue
            visited |= vbit
            v=vbit.bit_length()-1
            frontier |= mask & adj[v] & ~visited
        if visited.bit_count()>2:return False
        remaining &=~visited
    return True

def simplices(adj):
    faces=set()
    for s in range(1,1<<N):
        condition=all((s&adj[v]).bit_count()<=1 for v in range(N) if s&(1<<v))
        assert condition==comp_size_at_most_two(s,adj)
        if condition:faces.add(s)
    assert len(faces)==824
    fvec=[sum(s.bit_count()==d+1 for s in faces) for d in range(7)]
    assert fvec==[12,66,190,293,209,53,1]
    return faces,fvec

def matching(faces):
    alive=set(faces)
    pairs=[]
    for v in ORDER:
        bit=1<<v
        for s in sorted(alive):
            t=s|bit
            if s in alive and not s&bit and t in alive:
                alive.remove(s);alive.remove(t)
                pairs.append((s,t))
    assert len(pairs)==411
    assert alive=={512,338},alive
    return pairs,alive

def verify_acyclic(faces,pairs):
    matched=set(pairs)
    edges=0;deg={s:0 for s in faces};arcs={s:[] for s in faces}
    for upper in faces:
        bits=upper
        while bits:
            bit=bits&-bits;bits-=bit
            lower=upper^bit
            if not lower:continue
            assert lower in faces
            a,b=(lower,upper) if (lower,upper) in matched else (upper,lower)
            arcs[a].append(b);deg[b]+=1;edges+=1
    queue=deque(s for s in faces if deg[s]==0)
    visited=0
    while queue:
        s=queue.popleft();visited+=1
        for t in arcs[s]:
            deg[t]-=1
            if deg[t]==0:queue.append(t)
    assert visited==len(faces),(visited,len(faces))
    return edges

def mod2_rank(faces,degree):
    below=sorted(s for s in faces if s.bit_count()==degree)
    above=sorted(s for s in faces if s.bit_count()==degree+1)
    rows={s:i for i,s in enumerate(below)}
    basis={}
    for s in above:
        col=0;b=s
        while b:
            bit=b&-b;b-=bit
            col ^=1<<rows[s^bit]
        while col:
            p=col.bit_length()-1
            if p not in basis:
                basis[p]=col;break
            col ^=basis[p]
    return len(basis)

def main():
    adj=graph()
    faces,fvec=simplices(adj)
    pairs,critical=matching(faces)
    incidences=verify_acyclic(faces,pairs)
    ranks=[mod2_rank(faces,d) for d in range(1,7)]
    betti=[fvec[d]-(ranks[d-1] if d else 0)
           -(ranks[d] if d<6 else 0) for d in range(7)]
    betti[0]-=1
    assert ranks==[11,55,135,157,52,1]
    assert betti==[0,0,0,1,0,0,0]
    assert sum((-1)**d*n for d,n in enumerate(fvec))==0
    result={'graph_vertices':N,'graph_edges':18,'faces':len(faces),
            'face_vector':fvec,'morse_pairs':len(pairs),
            'critical_by_dimension':dict(sorted(Counter(s.bit_count()-1 for s in critical).items())),
            'hasse_incidences':incidences,'hasse_acyclic':True,
            'mod2_boundary_ranks_d1_to_d6':ranks,'reduced_mod2_betti_d0_to_d6':betti}
    print(json.dumps(result,sort_keys=True))
    print('FRUCHT_TWO_INDEPENDENCE_SPHERE_VERIFIED')

if __name__=='__main__':main()
