#!/usr/bin/env python3
"""Reproducible finite checks of the edge induced-closure Mobius theorem."""
from itertools import combinations
from collections import defaultdict


def graph_edges(n, code):
    pairs = list(combinations(range(n), 2))
    return [e for i,e in enumerate(pairs) if (code >> i)&1]


def is_triangle_free(n, edges):
    es = {frozenset(e) for e in edges}
    return all(not all(frozenset(p) in es for p in combinations(triple,2)) for triple in combinations(range(n),3))


def is_forest(n, edges):
    root = list(range(n))
    def get(x):
        while root[x]!=x:
            x=root[x]
        return x
    for u,v in edges:
        a,b=get(u),get(v)
        if a==b:return False
        root[a]=b
    return True


def endpoints(mask, edges):
    out=0
    for i,(u,v) in enumerate(edges):
        if (mask>>i)&1:out|=(1<<u)|(1<<v)
    return out


def closure(mask, edges):
    s=endpoints(mask,edges)
    return sum((1<<i) for i,(u,v) in enumerate(edges) if (s>>u)&1 and (s>>v)&1)


def hull_p3_star(mask, edges):
    m=len(edges)
    s=mask
    while True:
        a=s
        for j,(u,v) in enumerate(edges):
            if (s>>j)&1:continue
            neigh=[i for i,(x,y) in enumerate(edges) if (s>>i)&1 and (u in (x,y) or v in (x,y))]
            if any(not(set(edges[i]) & set(edges[k])) for i,k in combinations(neigh,2)):
                a|=(1<<j)
        if a==s:return s
        s=a


def independent_at_minus_one(n, edges, vertex_mask):
    # G[vertex_mask]; direct alternating independent-set sum
    vs=[u for u in range(n) if (vertex_mask>>u)&1]
    total=0
    for bit in range(1<<len(vs)):
        chosen={vs[j] for j in range(len(vs)) if bit>>j&1}
        if all(not(u in chosen and v in chosen) for u,v in edges):
            total+=(-1)**len(chosen)
    return total


def mobius_interval(n, edges, a,b):
    U=endpoints(a,edges); V=endpoints(b,edges)
    R=V & ~U
    touch=0
    for u,v in edges:
        if ((U>>u)&1) and ((R>>v)&1):touch|=1<<v
        if ((U>>v)&1) and ((R>>u)&1):touch|=1<<u
    W=R & ~touch
    return (-1)**R.bit_count() * independent_at_minus_one(n,edges,W)


def check(n, edges):
    m=len(edges)
    all_c={closure(S,edges) for S in range(1<<m)}
    closed=sorted(all_c, key=lambda S:(S.bit_count(),S))
    if any(hull_p3_star(S, edges)!=closure(S,edges) for S in range(1<<m)):
        raise AssertionError(('hull',n,edges))
    mu={}
    pairs=0
    for B in closed:
        for A in closed:
            if A & ~B:continue
            if A==B: val=1
            else:val=-sum(mu[(A,C)] for C in closed if C!=B and not(A & ~C) and not(C & ~B))
            mu[(A,B)]=val
            predicted=mobius_interval(n,edges,A,B)
            assert val==predicted,('mobius',n,edges,A,B,val,predicted)
            if is_forest(n,edges): assert val in (-1,0,1)
            pairs+=1
    return pairs,len(closed)


def main():
    graphs=intervals=0
    max_concepts=0
    for n in range(2,6):
        checked=0
        for code in range(1<<(n*(n-1)//2)):
            edges=graph_edges(n,code)
            if not is_triangle_free(n,edges):continue
            pairs,concepts=check(n,edges)
            graphs+=1;checked+=1;intervals+=pairs
            max_concepts=max(max_concepts,concepts)
        print('TRIANGLE_FREE',n,'graphs',checked,flush=True)
    import random
    rng=random.Random(1729)
    for n in (6,7,8,9):
        for _ in range(60):
            # random rooted tree, with extra leaves for structural variety
            edges=[(v,rng.randrange(v)) for v in range(1,n)]
            pairs,concepts=check(n,edges)
            graphs+=1;intervals+=pairs
            max_concepts=max(max_concepts,concepts)
        print('TREES',n,'random',60,flush=True)
    assert hull_p3_star(3, [(0,1),(1,2),(0,2)])==3
    assert closure(3,[(0,1),(1,2),(0,2)])==7
    print('VERIFY_OK graphs',graphs,'intervals',intervals,'max_concepts',max_concepts,'triangle_free_hull=PASS','mobius_formula=PASS','forest_bound=PASS','triangle_boundary=PASS')

if __name__=='__main__':main()
