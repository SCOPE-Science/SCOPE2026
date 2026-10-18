#!/usr/bin/env python3
"""Direct uncoloured graph automorphism test on small rooted cycle squares."""
import networkx as nx
from networkx.algorithms.isomorphism import GraphMatcher

def graph(n):
    g=nx.Graph();g.add_nodes_from(range(n*n))
    for a in range(n):
        for b in range(n):
            v=a*n+b
            g.add_edge(v,((a+1)%n)*n+b)
            g.add_edge(v,a*n+(b+1)%n)
    for v in g:g.nodes[v]['mark']=int(v==0)
    return g

def main():
    for n in (5,6,7):
        g=graph(n)
        gm=GraphMatcher(g,g,node_match=lambda x,y:x['mark']==y['mark'])
        maps=list(gm.isomorphisms_iter())
        assert len(maps)==8,(n,len(maps))
        seen={}
        for v in g:
            x,y=divmod(v,n)
            k=tuple(sorted((min(x,n-x),min(y,n-y))))
            seen.setdefault(k,set()).add(v)
        for v in g:
            assert {p[v] for p in maps}==seen[tuple(sorted((min(v//n,n-v//n),min(v%n,n-v%n))))],(n,v)
        print('PASS rooted graph automorphisms n=%d: order=8, orbit classes=%d' %(n,len(seen)))
if __name__=='__main__':main()
