#!/usr/bin/env python3
"""Finite discrete-Morse verification for one-arc-punctured bidirected cycles.

The vertices of the digraph are 0,...,N-1.  It has forward arcs
f_i:i->i+1 for every i, and backward arcs b_i:i+1->i for i=1,...,N-1.
All indices are cyclic.  Faces are directed linear forests.
"""
from collections import Counter, deque


def dominating_sets(N):
    m=N-1
    neighborhoods=[sum(1 << ((j+t)%N) for t in (-1,0,1))
                   for j in range(1,N)]
    allsites=(1<<N)-1
    coverage=[0]*(1<<m)
    dom=set()
    for mask in range(1,1<<m):
        bit=mask & -mask
        i=bit.bit_length()-1
        coverage[mask]=coverage[mask^bit] | neighborhoods[i]
        if coverage[mask]==allsites:
            dom.add(mask)
    return dom


def match_dominating(dom,N):
    live=set(dom)
    edges={}
    for i in range(N-1):
        bit=1<<i
        pairs=[(s,s|bit) for s in live if not(s&bit) and s|bit in live]
        for low, high in pairs:
            live.remove(low)
            live.remove(high)
            edges[low]=high
    return live,edges


def acyclic_directed_hasse(dom,paired,N):
    # Every covering relation is present: matched ones point down;
    # all other relations point up. Kahn topological sort is exhaustive.
    m=N-1
    indeg={v:0 for v in dom}
    out={v:[] for v in dom}
    edge_count=0
    for low in dom:
        for i in range(m):
            bit=1<<i
            if (low&bit)==0:
                high=low|bit
                if high in dom:
                    if paired.get(low)==high:
                        out[high].append(low)
                        indeg[low]+=1
                    else:
                        out[low].append(high)
                        indeg[high]+=1
                    edge_count+=1
    queue=deque(v for v,d in indeg.items() if d==0)
    processed=0
    while queue:
        v=queue.popleft()
        processed+=1
        for w in out[v]:
            indeg[w]-=1
            if not indeg[w]:
                queue.append(w)
    assert processed == len(dom), ('directed cycle',N,processed,len(dom))
    return edge_count


def target_faces(N):
    if N%4==1:
        return set()
    if N%4==2:
        return {sum(1<<(i-1) for i in range(1,N,2))}
    if N%4==3:
        return {sum(1<<(i-1) for i in range(1,N,4)) |
                sum(1<<(i-1) for i in range(2,N-2,4))}
    return {sum(1<<(i-1) for i in range(1,N,2)),
            sum(1<<(i-1) for i in range(1,N,4)) |
            sum(1<<(i-1) for i in range(2,N,4))}


def direct_faces(N):
    # Independent construction: inspect all arc pairs for indegree/outdegree
    # violations and directed 2-cycles, then remove the full forward cycle.
    arcs=[(i,(i+1)%N) for i in range(N)] + [((i+1)%N,i) for i in range(1,N)]
    adj=[0]*len(arcs)
    for i,(u,v) in enumerate(arcs):
        for j,(w,z) in enumerate(arcs):
            if i!=j and (u==w or v==z or (u==z and v==w)):
                adj[i]|=1<<j
    faces=[0]
    for i in range(len(arcs)):
        new=[f|(1<<i) for f in faces if not (f&adj[i])]
        faces.extend(new)
    faces.remove((1<<N)-1)
    return faces


def direct_morse_critical(N):
    faces=set(direct_faces(N))
    for i in range(2*N-1):
        bit=1<<i
        pairs=[(s,s|bit) for s in faces if not(s&bit) and s|bit in faces]
        for low,high in pairs:
            faces.remove(low);faces.remove(high)
    return faces


def main():
    total_dom=0
    total_hasse=0
    for N in range(4,21):
        dom=dominating_sets(N)
        critical,pairs=match_dominating(dom,N)
        assert critical==target_faces(N),(N,critical,target_faces(N))
        m=N-1
        target=0 if N%4==1 else (2 if N%4==0 else 1)
        assert len(critical)==target
        if N!=5:
            assert all(s.bit_count()-1==(N-2)//2 for s in critical)
        e=acyclic_directed_hasse(dom,pairs,N)
        total_dom+=len(dom);total_hasse+=e
        if N<=10:
            raw=direct_morse_critical(N)
            bmask=(1<<m)-1
            lifted={s<<N for s in critical} | {sum(1<<j for j in range(1,N))}
            assert raw==lifted,(N,raw,lifted)
        print('N=%02d dominating=%6d hasse=%7d paired=%6d low=%d top_dim=%d OK' %
              (N,len(dom),e,len(pairs),len(critical),N-2))
    print('ALL_OK 17 orders; %d dominating faces; %d verified Hasse edges' %
          (total_dom,total_hasse))

if __name__=='__main__':
    main()
