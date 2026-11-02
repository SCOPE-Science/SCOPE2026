#!/usr/bin/env python3
"""Second verifier, independently written with explicit recursive generation and boolean depth feasibility."""
import json
from functools import lru_cache
from itertools import combinations
from pathlib import Path


def make_graph(kind,n):
    graph={u:set() for u in range(n)}
    for i in range(n-1):
        graph[i].add(i+1);graph[i+1].add(i)
    if kind=='C':graph[0].add(n-1);graph[n-1].add(0)
    return graph


def maximal_sets(graph):
    n=len(graph); out=[]
    def choose(i,chosen):
        if i==n:
            chosen=set(chosen)
            if all(v in chosen or graph[v]&chosen for v in graph):
                out.append(frozenset(chosen))
            return
        choose(i+1,chosen)
        if not(graph[i]&set(chosen)):
            choose(i+1,chosen+(i,))
    choose(0,())
    return tuple(sorted(set(out), key=lambda x:tuple(sorted(x))))


def vcdim(H,n):
    best=0
    for r in range(1,n+1):
        exists=False
        for support in combinations(range(n),r):
            patterns={tuple(int(v in h) for v in support) for h in H}
            if len(patterns)==2**r:exists=True;break
        if exists:best=r
        else:break
    return best


def ldim(H,n):
    h=tuple(range(len(H)))
    @lru_cache(None)
    def can_depth(active, available, depth):
        if depth==0:return True
        if len(active)<2**depth:return False
        for v in available:
            a=tuple(i for i in active if v in H[i]);b=tuple(i for i in active if v not in H[i])
            if can_depth(a,tuple(x for x in available if x!=v),depth-1) and can_depth(b,tuple(x for x in available if x!=v),depth-1):
                return True
        return False
    k=0
    while can_depth(h,tuple(range(n)),k+1):k+=1
    return k


def main():
    cert=json.loads(Path(__file__).with_name('certificate.json').read_text())
    ncases=0
    for row in cert['table']:
        kind,n=row['kind'],row['n']
        H=maximal_sets(make_graph(kind,n))
        assert len(H)==row['concept_count']
        assert vcdim(H,n)==row['vc']
        assert ldim(H,n)==row['ldim']
        ncases+=1
    print('INDEPENDENT_DEGREE_TWO_CROSSCHECK_PASS',ncases)

if __name__=='__main__':main()
