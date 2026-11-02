#!/usr/bin/env python3
"""Independent cycle-convex Carathéodory checks for cactus graphs."""
from functools import lru_cache
from itertools import combinations
import networkx as nx

def is_cactus(G):
    cycles=nx.cycle_basis(G)
    edges=[]
    for cyc in cycles:
        edges.extend(frozenset((cyc[i],cyc[(i+1)%len(cyc)])) for i in range(len(cyc)))
    return len(edges)==len(set(edges))

def predicted(G):
    cycles=[tuple(c) for c in nx.cycle_basis(G)]
    inc={v:[] for v in G}
    for j,c in enumerate(cycles):
        for v in c:inc[v].append(j)
    @lru_cache(None)
    def msg(v,parent):
        val=1
        for j in inc[v]:
            if j!=parent:
                val=max(val,sum(msg(u,j) for u in cycles[j] if u!=v))
        return val
    return max((msg(v,-1) for v in G),default=0)

def predicted_witness(G):
    cycles=[tuple(c) for c in nx.cycle_basis(G)]
    inc={v:[] for v in G}
    for j,c in enumerate(cycles):
        for v in c:inc[v].append(j)
    @lru_cache(None)
    def build(v,parent):
        best=(v,)
        for j in inc[v]:
            if j==parent:continue
            candidate=tuple(s for u in cycles[j] if u!=v for s in build(u,j))
            if len(candidate)>len(best):best=candidate
        return best
    w=max(G,key=lambda v:len(build(v,-1)))
    seed=set(build(w,-1))
    assert len(seed)==len(build(w,-1))
    def hull(T):
        T=set(T)
        while True:
            pieces=list(nx.connected_components(G.subgraph(T)))
            add={v for v in G if v not in T and any(len(set(G[v])&T&comp)>=2 for comp in pieces)}
            if not add:return T
            T.update(add)
    assert w in hull(seed)
    assert all(w not in hull(seed-{s}) for s in seed)
    return len(seed)

def brute(G):
    vertices=list(G)
    def hull(S):
        S=set(S)
        while True:
            new=S.copy()
            pieces=list(nx.connected_components(G.subgraph(S)))
            for v in G:
                if v in S:continue
                neighbors=set(G.neighbors(v)) & S
                if any(len(neighbors & piece)>=2 for piece in pieces):
                    new.add(v)
            if new==S:return S
            S=new
    best=0
    for mask in range(1<<len(vertices)):
        S={vertices[i] for i in range(len(vertices)) if mask>>i&1}
        if len(S)<=best:continue
        H=hull(S)
        mandatory=H.copy()
        for v in S:mandatory &= H-hull(S-{v})
        if mandatory:best=len(S)
    return best

def main():
    checked=0
    for G in nx.graph_atlas_g():
        if not G or not nx.is_connected(G) or not is_cactus(G):continue
        a=predicted(G); b=brute(G); assert a==predicted_witness(G)
        assert a==b,(G.number_of_nodes(),G.edges(),a,b)
        checked+=1
    print('ALL_CONNECTED_CACTI_GRAPH_ATLAS_THROUGH_7_OK',checked)
    # Families with multiple branches and distinct cutpoints.
    for lengths in [(3,3,3,3),(3,4,5),(4,4,4),(3,3,3,3,3)]:
        G=nx.Graph(); next_v=1; shared=0
        for i,k in enumerate(lengths):
            c=[shared]+list(range(next_v,next_v+k-1)); next_v+=k-1
            G.add_edges_from((c[j],c[(j+1)%k]) for j in range(k))
            if i%2:shared=c[1]
        a=predicted(G); b=brute(G); assert a==predicted_witness(G)
        assert a==b,(lengths,a,b)
        print('BRANCHED_CACTUS_OK',lengths,G.number_of_nodes(),a)
    print('VERIFY_OK')
if __name__=='__main__':main()
