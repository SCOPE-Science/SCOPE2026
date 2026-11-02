"""Exhaustive verification for short alternating-cycle flips of cyclic 4-bit Gray codes.
Run with Python >=3.10: python3 verify.py. Uses only the standard library.
"""
from collections import Counter, deque
from itertools import combinations

V = range(16)
EDGES = [(u,v) for u in V for v in range(u+1,16) if (u^v).bit_count()==1]
assert len(EDGES)==32
INDEX = {e:i for i,e in enumerate(EDGES)}
ADJ = [[w for w in V if (v^w).bit_count()==1] for v in V]

def edge_mask(path):
    return sum(1 << INDEX[tuple(sorted((a,b)))] for a,b in zip(path,path[1:]+path[:1]))

def hamiltonians():
    out=[]
    def dfs(path, used):
        if len(path)==16:
            if path[-1] in ADJ[0] and path[1]<path[-1]:
                out.append(edge_mask(path))
            return
        for w in ADJ[path[-1]]:
            if not ((used>>w)&1):
                dfs(path+[w],used | (1<<w))
    dfs([0],1)
    assert len(out)==len(set(out))==1344
    return out

def short_cycles(length):
    found=set()
    def dfs(path,used):
        v=path[-1]
        if len(path)==length:
            if path[0] in ADJ[v] and path[1]<v:
                found.add(edge_mask(path))
            return
        for w in ADJ[v]:
            if w>path[0] and not ((used>>w)&1):
                dfs(path+[w],used|(1<<w))
    for v in V:
        dfs([v],1<<v)
    return found

def exchange_graph(states,local_cycles):
    loc={v:i for i,v in enumerate(states)}
    graph=[set() for _ in states]
    for i,m in enumerate(states):
        for f in local_cycles:
            if (m&f).bit_count()*2 != f.bit_count():
                continue
            j=loc.get(m^f)
            if j is not None:
                graph[i].add(j)
    return graph

def components(graph):
    n=len(graph);visited=set();hist=Counter()
    for s in range(n):
        if s in visited:continue
        q=[s];visited.add(s)
        for v in q:
            for w in graph[v]:
                if w not in visited:
                    visited.add(w);q.append(w)
        hist[len(q)]+=1
    return hist

def eccentricities(graph):
    ecc=Counter()
    for s in range(len(graph)):
        dist={s:0};q=deque([s])
        while q:
            v=q.popleft()
            for w in graph[v]:
                if w not in dist:
                    dist[w]=dist[v]+1;q.append(w)
        assert len(dist)==len(graph)
        ecc[max(dist.values())]+=1
    return ecc

STATES=hamiltonians()
F4=short_cycles(4); F6=short_cycles(6)
assert len(F4)==24 and len(F6)==128
G4=exchange_graph(STATES,F4)
G6=exchange_graph(STATES,F6)
G46=exchange_graph(STATES,F4|F6)
for g in (G4,G6,G46):
    assert all(i in g[j] for i in range(len(g)) for j in g[i])
count_edges=lambda g:sum(map(len,g))//2
assert count_edges(G4)==1920 and components(G4)==Counter({1:240,1104:1})
assert count_edges(G6)==9408 and components(G6)==Counter({1344:1})
assert count_edges(G46)==11328 and components(G46)==Counter({1344:1})
e6=eccentricities(G6);e46=eccentricities(G46)
assert e6==e46==Counter({5:432,6:912})
print('ENUMERATION_OK Hamiltonian_cycles=1344 square_cycles=24 six_cycles=128')
print('SQUARE_EXCHANGE_OK edges=1920 components=240x1+1x1104')
print('HEXAGON_EXCHANGE_OK edges=9408 connected=1 ecc5=432 ecc6=912')
print('COMBINED_EXCHANGE_OK edges=11328 connected=1 ecc5=432 ecc6=912')
print('FULL_VERIFY_OK')
