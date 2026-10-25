#!/usr/bin/env python3
"""Reproduce finite tests of the girth-five ordinary four-cut theorem.

All calculations use integer arithmetic and the Python 3 standard library.
The infinite-family statement is proved combinatorially in the accompanying text.
"""
from itertools import combinations
from math import comb


def generalized_petersen(n, step):
    E = set()
    for i in range(n):
        for a, b in ((i, (i+1)%n), (i, i+n), (i+n, n+(i+step)%n)):
            E.add(tuple(sorted((a,b))))
    return 2*n, E


def cycle(n):
    return n, {tuple(sorted((i, (i+1)%n))) for i in range(n)}


def adjacency(n, E):
    A = [set() for _ in range(n)]
    for a,b in E:A[a].add(b);A[b].add(a)
    return A


def connected(S, A):
    q=[S[0]];v={S[0]}
    for a in q:
        for b in A[a].intersection(S):
            if b not in v:v.add(b);q.append(b)
    return len(v)==len(S)


def pentagons(n, A):
    return [frozenset(S) for S in combinations(range(n),5)
            if all(len(A[v].intersection(S))==2 for v in S)]


def spanning_trees4(n,A):
    return [frozenset(S) for S in combinations(range(n),4) if connected(S,A)]


def types(T,A):
    ds=sorted(len(A[v].intersection(T)) for v in T)
    return 'star' if ds==[1,1,1,3] else 'path' if ds==[1,1,2,2] else 'OTHER'


def one_edge_triples(T,A):
    return [frozenset(S) for S in combinations(sorted(T),3)
            if sum(b in A[a] for a,b in combinations(S,2))==1]


def check(n, E, label, with_smith=False):
    A=adjacency(n,E)
    assert all(a not in A[a] for a in range(n))
    assert all(not any(A[a].intersection(A[b])) for a,b in E) # no triangles
    assert all(len(A[a].intersection(A[b]))<=1 for a,b in combinations(range(n),2)) # no C4
    T=spanning_trees4(n,A); C=pentagons(n,A)
    c4=len(T); c5=len(C)
    stars=[t for t in T if types(t,A)=='star']
    paths=[t for t in T if types(t,A)=='path']
    assert len(stars)+len(paths)==len(T)
    owner={t:[] for t in paths}
    for pent in C:
        pent_paths={t for t in paths if t.issubset(pent)}
        assert len(pent_paths)==5
        for t in pent_paths:owner[t].append(pent)
    assert all(len(pents)<=1 for pents in owner.values())
    # Every isolated-edge triple of a path occurs in at most two four-trees.
    for t in paths:
        for r in one_edge_triples(t,A):
            support=[z for z in T if r.issubset(z)]
            assert len(support) in (1,2)
            if len(support)==2:
                assert len(owner[t])==1
                assert all(z.issubset(owner[t][0]) for z in support)
    # Each star has a private triple consisting of all of its leaves.
    for t in stars:
        center=next(a for a in t if len(A[a].intersection(t))==3)
        leaves=t-{center}
        assert sum(leaves.issubset(z) for z in T)==1
    # Every five-set all of whose four-sets are connected is a pentagon.
    CT=set(T);CC=set(C)
    for S in combinations(range(n),5):
        qualifies=all(frozenset(U) in CT for U in combinations(S,4))
        assert qualifies==(frozenset(S) in CC)
    # No six-set has all of its four-subsets connected.
    for S in combinations(range(n),6):
        assert not all(frozenset(U) in CT for U in combinations(S,4))
    result=comb(n-1,3)-c4+c5
    assert result>=0
    # An independent characteristic-two check of the 3-boundary rank.
    rows={f:i for i,f in enumerate(combinations(range(n),3))}
    piv={};rank=0
    for t in T:
        col=0
        for U in combinations(sorted(t),3):col^=1<<rows[U]
        while col:
            h=col.bit_length()-1
            if h in piv:col^=piv[h]
            else:piv[h]=col;rank+=1;break
    assert rank==c4-c5
    print(label, 'n=',n,'connected4=',c4,'pentagons=',c5,
          'dual_d3_rank_mod2=',rank,'sphere_rank=',result)
    return (n,c4,c5,result)


def main():
    assert check(*generalized_petersen(5,2),'Petersen')==(10,70,12,26)
    assert check(*generalized_petersen(10,2),'Dodecahedron')==(20,140,12,841)
    assert check(*cycle(8),'Cycle8')==(8,8,0,27)
    assert check(*cycle(9),'Cycle9')==(9,9,0,47)
    # A disconnected example tests that connectedness is not an assumption.
    assert check(8,{(0,1),(1,2),(2,3),(3,4),(4,0)},'C5_with_isolates')==(8,5,1,31)
    print('GIRTH_FIVE_FOUR_CUT_CHECKS_OK')

if __name__=='__main__':main()
