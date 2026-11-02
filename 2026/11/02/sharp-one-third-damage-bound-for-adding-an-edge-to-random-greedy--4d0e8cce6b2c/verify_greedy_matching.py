"""Exact finite checks for a sharp random-greedy matching edge perturbation theorem.
Only Python standard library is required. Finite checks supplement, not replace, the proof.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import permutations

def complete_edges(n):
    return tuple((a,b) for a in range(n) for b in range(a+1,n))

@lru_cache(None)
def expected(n, graph):
    if not graph:
        return Fraction(0)
    total = Fraction(0)
    for a,b in graph:
        total += 1+expected(n, tuple(edge for edge in graph if a not in edge and b not in edge))
    return total/len(graph)

def direct_greedy(edges, ordering):
    occupied = set()
    count = 0
    for i in ordering:
        a,b = edges[i]
        if a not in occupied and b not in occupied:
            occupied.add(a);occupied.add(b); count+=1
    return count

def test():
    checks = 0
    for n in range(2,7):
        edges = complete_edges(n)
        N=len(edges)
        for mask in range(1<<N):
            graph=tuple(edges[j] for j in range(N) if mask>>j&1)
            old=expected(n,graph)
            for i,(u,v) in enumerate(edges):
                if mask>>i&1: continue
                plus=tuple(sorted(graph+(edges[i],)))
                delta=expected(n,plus)-old
                assert -Fraction(1,3)<=delta<=1, (n, mask, i, delta)
                checks+=2
                if not any(u in f for f in graph) or not any(v in f for f in graph):
                    assert delta>=0
                    checks+=1
            for v in range(n):
                deleted=tuple(e for e in graph if v not in e)
                assert 0<=old-expected(n,deleted)<=1
                checks+=2
    assert expected(4,((0,1),(2,3)))==2
    assert expected(4,((0,1),(0,2),(2,3)))==Fraction(5,3)
    checks+=2
    for n in range(2,5):
        edges=complete_edges(n)
        for mask in range(1<<len(edges)):
            graph=tuple(edges[j] for j in range(len(edges)) if mask>>j&1)
            if len(graph)>6: continue
            direct=Fraction(sum(direct_greedy(graph,order) for order in permutations(range(len(graph)))))
            import math
            direct/=math.factorial(len(graph))
            assert direct==expected(n,graph)
            checks+=1
            for v in range(n):
                sub=tuple(e for e in graph if v not in e)
                for order in permutations(range(len(graph))):
                    g=direct_greedy(graph,order)
                    induced=tuple(e for e in (graph[j] for j in order) if v not in e)
                    h=direct_greedy(induced,tuple(range(len(induced))))
                    assert g-h in (0,1)
                    checks+=1
    print('PASS: exact assertions',checks,'cached expectations',expected.cache_info().currsize)

if __name__=='__main__':
    test()
