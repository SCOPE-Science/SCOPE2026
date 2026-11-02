"""Standalone finite cross-check of canonical-cover automorphism orders.
The proof for arbitrary clique-bouquet sizes is structural; this independent
enumeration examines small labeled graphs without using group order formulas
inside the automorphism enumerator.
"""
from collections import Counter
from math import factorial
import networkx as nx


def bouquet(blades):
    graph=nx.Graph()
    graph.add_node(0)
    v=1
    for r in blades:
        vertices=list(range(v,v+r));v+=r
        for x in vertices:
            graph.add_edge(0,x)
        for i,x in enumerate(vertices):
            for y in vertices[i+1:]:
                graph.add_edge(x,y)
    return graph


def double_cover(graph):
    cover=nx.Graph()
    for vertex in graph:
        for side in (0,1):
            cover.add_node((vertex,side))
    for u,v in graph.edges():
        cover.add_edge((u,0),(v,1))
        cover.add_edge((u,1),(v,0))
    return cover


def expected_orders(blades):
    c=Counter(blades)
    base=1
    for r,t in c.items():
        base*=factorial(r)**t*factorial(t)
    k=c.get(2,0)
    if len(blades)==1:
        return factorial(blades[0]+1),2*factorial(blades[0]+1),1
    lift=2*factorial(2*k)
    for r,t in c.items():
        if r>=3:
            lift*=factorial(r)**t*factorial(t)
    return base,lift,factorial(2*k)//(2**k*factorial(k))


def number_of_automorphisms(graph):
    return sum(1 for _ in nx.algorithms.isomorphism.GraphMatcher(graph,graph).isomorphisms_iter())


def verify():
    cases=[(2,), (3,), (4,), (2,2), (2,3), (3,3), (2,2,3),
           (2,2,2), (2,3,3), (3,4), (2,2,2,3)]
    for blades in cases:
        graph=bouquet(blades)
        cover=double_cover(graph)
        base,full,index=expected_orders(blades)
        brute_base=number_of_automorphisms(graph)
        brute_full=number_of_automorphisms(cover)
        assert (brute_base,brute_full)==(base,full), (
            blades,(brute_base,brute_full),(base,full))
        assert full==2*base*index
        print('CASE',','.join(map(str,blades)),
              'graph_aut',brute_base,'cover_aut',brute_full,'index',index)
    print('VERIFY_OK cases=',len(cases))


if __name__=='__main__':
    verify()
