"""Exhaustive independent-set enumeration and exchange graphs, using only stdlib."""
from itertools import combinations, permutations
from collections import Counter, deque

def graph(kind):
    V=list(range(16)); e=set()
    for i,j in combinations(V,2):
        a,b=divmod(i,4); c,d=divmod(j,4)
        if kind=='rook':
            linked=(a==c or b==d)
        else:
            dif=((c-a)%4,(d-b)%4)
            linked=dif in {(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}
        if linked: e.add((i,j))
    return e

def independent(s,edges):
    return all((a,b) not in edges for a,b in combinations(s,2))

def bfs(G,start):
    dist={start:0}; Q=deque([start])
    while Q:
        x=Q.popleft()
        for y in G[x]:
            if y not in dist: dist[y]=dist[x]+1; Q.append(y)
    return dist

def inspect(kind):
    ed=graph(kind)
    assert len(ed)==48
    assert sum(independent(c,ed) for c in combinations(range(16),5))==0
    states=[frozenset(s) for s in combinations(range(16),4) if independent(s,ed)]
    assert len(states)==(16 if kind=='shrikhande' else 24)
    G={s:set() for s in states}
    for a,b in combinations(states,2):
        if len(a&b)==2: G[a].add(b); G[b].add(a)
        assert len(a&b)!=3
    deg=Counter(len(G[x]) for x in G)
    ecount=sum(map(len,G.values()))//2
    dists={x:bfs(G,x) for x in G}
    assert all(len(ds)==len(G) for ds in dists.values())
    diameter=max(max(d.values()) for d in dists.values())
    radius=min(max(d.values()) for d in dists.values())
    col={};
    for root in G:
        if root in col: continue
        col[root]=0; Q=[root]
        for s in Q:
            for t in G[s]:
                if t not in col: col[t]=1-col[s]; Q.append(t)
                else: assert col[t]!=col[s]
    if kind=='shrikhande':
        assert (len(states),ecount,deg,diameter,radius)==(16,24,Counter({2:12,6:4}),4,3)
        assert Counter(tuple(Counter(ds.values())[j] for j in range(max(ds.values())+1)) for ds in dists.values())==Counter({(1,6,3,6):4,(1,2,9,2,2):12})
    else:
        assert (len(states),ecount,deg,diameter,radius)==(24,72,Counter({6:24}),3,3)
        assert all(Counter(ds.values())==Counter({0:1,1:6,2:11,3:6}) for ds in dists.values())
    print(kind.upper(), 'PASS', 'n',len(states),'edges',ecount,'degree_distribution',sorted(deg.items()),'radius',radius,'diameter',diameter)

for k in ('shrikhande','rook'): inspect(k)
print('BRUTEFORCE_PASS')
