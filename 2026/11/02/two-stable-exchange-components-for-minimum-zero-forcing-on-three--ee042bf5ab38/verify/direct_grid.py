#!/usr/bin/env python3
"""Independent direct zero-forcing and reconfiguration enumeration on small grids."""
from collections import Counter, deque
from itertools import combinations

TEMPLATES = (
    (0, 3, 1), (0, 6, 4), (1, 1, 1), (1, 3, 0),
    (3, 0, 1), (3, 2, 0), (4, 4, 4), (4, 6, 0),
    (5, 1, 0), (5, 4, 0), (6, 0, 4), (6, 2, 0),
    (7, 0, 0),
)

def edges(n):
    g = [set() for _ in range(3*n)]
    for c in range(n):
        for r in range(3):
            x = 3*c+r
            for dc, dr in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                if 0 <= c+dc < n and 0 <= r+dr < 3:
                    g[x].add(3*(c+dc)+r+dr)
    return g

def forces(adjacency, blue):
    visited = set(blue)
    while True:
        additions = set()
        for v in visited:
            w = adjacency[v] - visited
            if len(w) == 1:
                additions.update(w)
        if not additions:
            return len(visited) == len(adjacency)
        visited.update(additions)

def pattern_vertices(pattern, offset):
    return frozenset(3*(offset+j)+r for j,mask in enumerate(pattern)
                     for r in range(3) if (mask >> r) & 1)

def components(neighbors):
    unseen = set(range(len(neighbors)))
    cs=[]
    while unseen:
        root=unseen.pop()
        q=[root]
        for x in q:
            for y in neighbors[x]:
                if y in unseen:
                    unseen.remove(y)
                    q.append(y)
        cs.append(q)
    return cs

def eccentricities(neighbors):
    out=[]
    for i in range(len(neighbors)):
        dist={i:0}
        q=deque([i])
        while q:
            v=q.popleft()
            for w in neighbors[v]:
                if w not in dist:
                    dist[w]=dist[v]+1
                    q.append(w)
        out.append((len(dist),max(dist.values())))
    return out

def run():
    for n in range(3,11):
        adj=edges(n)
        assert all(not forces(adj, S) for S in combinations(range(3*n),2))
        sets=[frozenset(S) for S in combinations(range(3*n),3)
              if forces(adj,S)]
        index={S:k for k,S in enumerate(sets)}
        neighbors=[set() for _ in sets]
        for i, S in enumerate(sets):
            for v in range(3*n):
                if v in S:continue
                for u in S:
                    j=index.get(frozenset((S-{u})|{v}))
                    if j is not None:neighbors[i].add(j)
        cc=sorted([len(c) for c in components(neighbors)])
        e=sum(map(len,neighbors))//2
        if n==3:
            assert (len(sets), e, cc)==(20,44,[20])
        if n==4:
            assert (len(sets), e, cc)==(26,56,[26])
        if n>=5:
            assert (len(sets),e,cc)==(26,48,[13,13])
            predicted=set(pattern_vertices(p,0) for p in TEMPLATES)
            predicted|=set(pattern_vertices(p[::-1],n-3) for p in TEMPLATES)
            assert set(sets)==predicted
            assert Counter(len(x) for x in neighbors)=={4:16,3:4,2:4,6:2}
            assert Counter(eccentricities(neighbors))=={(13,3):10,(13,4):12,(13,5):4}
    # Inspect the finite reference graph H without a grid-length assumption.
    blocks=[pattern_vertices(p,0) for p in TEMPLATES]
    H=[{j for j in range(13) if j!=i and len(blocks[i]&blocks[j])==2}
       for i in range(13)]
    assert len(components(H))==1
    assert sum(map(len,H))//2==24
    assert Counter(map(len,H))=={4:8,3:2,2:2,6:1}
    assert Counter(eccentricities(H))=={(13,3):5,(13,4):6,(13,5):2}
    print('DIRECT_FORCING_ALL_SMALL_GRIDS_PASS')
    print('REFERENCE_COMPONENT_13_VERTICES_24_EDGES_PASS')

if __name__=='__main__':run()
