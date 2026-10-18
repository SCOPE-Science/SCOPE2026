#!/usr/bin/env python3
"""Direct mod-2 connected-dominating cochain census on the Read-Wilson atlas."""
from collections import Counter
import networkx as nx

def connected_dominating(mask, adj, n):
    if not mask:
        return False
    closed=mask
    for v in range(n):
        if (mask>>v)&1:
            closed |= adj[v]
    if closed!=(1<<n)-1:
        return False
    visited=mask & -mask
    while True:
        expanded=visited
        for v in range(n):
            if (visited>>v)&1:
                expanded |= (adj[v] & mask)
        if expanded==visited:
            return visited==mask
        visited=expanded

def rank(vectors):
    rows={}
    for x in vectors:
        while x:
            p=x.bit_length()-1
            if p not in rows:
                rows[p]=x
                break
            x ^= rows[p]
    return len(rows)

def direct_bold(G):
    n=len(G)
    adj=[sum(1<<v for v in G[u]) for u in range(n)]
    cd=[m for m in range(1<<n) if connected_dominating(m,adj,n)]
    levels=[[m for m in cd if m.bit_count()==k] for k in range(n+1)]
    diffrank={}
    for k in range(n):
        rowpos={mask:i for i,mask in enumerate(levels[k+1])}
        columns=[]
        for S in levels[k]:
            vec=0
            for v in range(n):
                if not ((S>>v)&1):
                    T=S | (1<<v)
                    # D is upward-closed
                    vec ^= 1<<rowpos[T]
            columns.append(vec)
        diffrank[k]=rank(columns)
    betti={k:len(levels[k])-diffrank.get(k-1,0)-diffrank.get(k,0) for k in range(n+1)}
    assert all(v>=0 for v in betti.values())
    euler=sum((-1)**k * len(levels[k]) for k in range(n+1))
    assert euler==sum((-1)**k*v for k,v in betti.items())
    return euler, {k:v for k,v in betti.items() if v},[len(x) for x in levels]

def main():
    atlas=nx.graph_atlas_g()
    assert len(atlas)==1253
    result=[]; tested=Counter(); zerochi=Counter(); zerochi_acyclic=Counter()
    for i,G in enumerate(atlas):
        n=len(G)
        if not n or not nx.is_connected(G): continue
        tested[n]+=1
        chi,bettis,_=direct_bold(G)
        if chi==0:
            zerochi[n]+=1
            if not bettis:zerochi_acyclic[n]+=1
            else:result.append([i,n,G.number_of_edges(),nx.to_graph6_bytes(G,header=False).strip().decode(),bettis])
    print('tested',dict(sorted(tested.items())))
    print('chi_zero',dict(sorted(zerochi.items())))
    print('chi_zero_acyclic',dict(sorted(zerochi_acyclic.items())))
    print('nonzero_zero_chi',result)
    G=atlas[1212]
    print('witness_counts',direct_bold(G))
    assert result==[[1212,7,15,'Fhf~o',{2:1,3:1}]]
    # Independent positive controls from Caputi--Celoria--Collari (2022).
    for n in range(3,9):
        assert direct_bold(nx.complete_graph(n))[1]=={1:1}
    for n in range(5,10):
        assert direct_bold(nx.cycle_graph(n))[1]=={n-2:1}
    for m,n in [(2,2),(2,3),(3,4)]:
        assert direct_bold(nx.complete_bipartite_graph(m,n))[1]=={2:1}
    for n in range(3,9):
        assert direct_bold(nx.path_graph(n))[1]=={}
    for n in range(5,9):
        g=nx.disjoint_union(nx.cycle_graph(n),nx.empty_graph(2))
        for a in range(n):
            for b in (n,n+1):
                g.add_edge(a,b)
        expected={2:1,n-2:1} if n!=4 else {2:2}
        assert direct_bold(g)[1]==expected
    print('controls: complete graphs, cycles, complete bipartite graphs, paths, suspended cycles PASS')

if __name__=='__main__':main()
