#!/usr/bin/env python3
"""Finite local certificates for induced-matchings in the two (16,6,2,2) graphs.

Usage: python3 check_local.py.  Standard-library only.
"""
from itertools import combinations
from collections import Counter, deque

P = [(a,b) for a in range(4) for b in range(4)]
S = {(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}


def graph(which):
    adjacent = [[False]*16 for _ in range(16)]
    for i,j in combinations(range(16),2):
        a,b=P[i],P[j]
        if which=='R': isedge=(a[0]==b[0] or a[1]==b[1])
        else: isedge=(((a[0]-b[0])%4,(a[1]-b[1])%4) in S)
        adjacent[i][j]=adjacent[j][i]=isedge
    E=[(i,j) for i in range(16) for j in range(i+1,16) if adjacent[i][j]]
    assert len(E)==48
    compatible=[[False]*48 for _ in range(48)]
    for i,j in combinations(range(48),2):
        val=all(x!=y and not adjacent[x][y] for x in E[i] for y in E[j])
        compatible[i][j]=compatible[j][i]=val
    return E,compatible


def breadth(graph,initial):
    d={initial:0};q=deque([initial]);
    while q:
        x=q.popleft()
        for y in graph[x]:
            if y not in d: d[y]=d[x]+1;q.append(y)
    return d


def run(which):
    E,C=graph(which)
    neigh=[{j for j in range(48) if C[i][j]} for i in range(48)]
    degrees=Counter(map(len,neigh))
    center=E.index((0,1)) # (0,0)--(0,1)
    loc=sorted(neigh[center])
    local_pairs=[(a,b) for a,b in combinations(loc,2) if C[a][b]]
    local_distribution=Counter(sum(C[a][b] for a,b in combinations(neigh[i],2)) for i in range(48))
    all_pairs={(a,b) for a,b in combinations(range(48),2) if C[a][b]}
    triples={tuple(sorted((i,a,b))) for i in range(48) for a,b in combinations(neigh[i],2) if C[a][b]}
    max4=any(all(C[a][b] for a,b in combinations(c,2)) for c in combinations(range(48),4))
    if which=='R':
        assert degrees=={9:48} and local_distribution=={0:48} and len(all_pairs)==216 and not triples
        assert len(breadth(neigh,0))==48
    else:
        assert degrees=={8:48} and local_distribution=={2:48} and len(all_pairs)==192 and len(triples)==32
        assert sorted(len({v for v in loc if C[u][v]}) for u in loc)==[0,0,0,0,1,1,1,1]
    assert not max4
    m=2 if which=='R' else 3
    mx=[tuple(t) for t in sorted(all_pairs if m==2 else triples)]
    bags=[set(x) for x in mx]
    replacement=[set() for _ in mx]
    for a,b in combinations(range(len(mx)),2):
        if len(bags[a]&bags[b])==m-1:replacement[a].add(b);replacement[b].add(a)
    degreesR=Counter(map(len,replacement))
    components=[];todo=set(range(len(mx)));maxdist=0
    while todo:
        x=min(todo);dist=breadth(replacement,x);todo-=set(dist);components.append(len(dist))
    if which=='R':
        assert components==[216] and degreesR=={16:216}
        maxdist=max(max(breadth(replacement,x).values()) for x in range(len(mx)))
        assert maxdist==3
    else:
        assert components==[1]*32 and degreesR=={0:32}
        maxdist=0
    print(which, 'induced_matching_polynomial', [1,48,len(all_pairs),len(triples)])
    print(which, 'compatibility_degree_counts', sorted(degrees.items()))
    print(which, 'representative_compatible_edges', [tuple(P[j] for j in E[z]) for z in loc])
    print(which, 'representative_compatible_pairs', [(tuple(P[j] for j in E[a]),tuple(P[j] for j in E[b])) for a,b in local_pairs])
    print(which, 'local_edge_counts', sorted(local_distribution.items()))
    print(which, 'reconfiguration_vertices',len(mx), 'edges',sum(map(len,replacement))//2, 'degrees',sorted(degreesR.items()),'components', sorted(components), 'diameter_of_largest_component',maxdist)

if __name__=='__main__':
    run('R');run('S')
