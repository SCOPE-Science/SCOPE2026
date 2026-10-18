"""Full graph automorphism spot-checks independent of the multipartite automorphism formula.
Requires NetworkX; intended as a finite consistency test, not a proof.
"""
from itertools import combinations_with_replacement
import networkx as nx


def graph(sizes):
    labels=[i for i,a in enumerate(sizes) for _ in range(a)]
    edges=[(x,y) for x in range(len(labels)) for y in range(x+1,len(labels)) if labels[x]!=labels[y]]
    g=nx.Graph()
    g.add_nodes_from(range(len(edges)))
    for i,(a,b) in enumerate(edges):
        for j,(c,d) in enumerate(edges[:i]):
            if a==c or a==d or b==c or b==d:g.add_edge(i,j)
    types=[tuple(sorted((sizes[labels[a]],sizes[labels[b]]))) for a,b in edges]
    return g,types


def full_orbits(g):
    parent=list(range(len(g)))
    def find(i):
        while parent[i]!=i:
            parent[i]=parent[parent[i]];i=parent[i]
        return i
    count=0
    for iso in nx.algorithms.isomorphism.GraphMatcher(g,g).isomorphisms_iter():
        count+=1
        for a,b in iso.items():
            parent[find(a)]=find(b)
    return [find(i) for i in range(len(g))],count


def equivalent(c,d):
    return all((c[i]==c[j])==(d[i]==d[j]) for i in range(len(c)) for j in range(i))


def verify():
    cases=[(1,2,2,3),(1,1,2,3),(1,2,3),(2,2,2),(1,1,1,2),(1,2,2),(1,2,4)]
    checks=0
    for sz in cases:
        g,types=graph(sz)
        orb,count=full_orbits(g)
        assert equivalent(orb,types),(sz,orb,types)
        print(f'PASS full automorphisms sizes={sz}, automorphisms={count}, edge-orbits={len(set(orb))}')
        checks+=1
    print(f'PASS full automorphism groups checked={checks}')

if __name__=='__main__':verify()
