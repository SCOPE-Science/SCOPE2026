#!/usr/bin/env python3
"""Direct finite census of commuting idempotents of incidence algebras.

Enumerates algebra elements as arrays indexed by a closed incidence relation;
checks convolution identities directly. Separately enumerates colorings of the
undirected comparability graph. No external packages needed.
"""
from itertools import product
from collections import Counter


def transitive_rel(n, edges):
    R = {(i, i) for i in range(n)} | set(edges)
    while True:
        U = R | {(i, k) for i,j in R for jj,k in R if j == jj}
        if U == R:
            break
        R=U
    if any(i!=j and (j,i) in R for i,j in R):
        raise ValueError('not a poset')
    return sorted(R)


def polynomial_count(n, offdiag, q, k):
    total=0
    for c in product(range(1<<k), repeat=n):
        w = sum(c[i]!=c[j] for i,j in offdiag)
        total += q**w
    return total


def census(n, relations, q, k):
    rel = transitive_rel(n,relations)
    off = [(i,j) for i,j in rel if i!=j]
    mid = { (i,j):[(i,h,h,j) for h in range(n) if (i,h) in rel and (h,j) in rel] for i,j in rel }
    positions={p:t for t,p in enumerate(rel)}
    coords=[ [ (positions[i,h], positions[h,j]) for _,h,_,_ in mid[i,j] ] for i,j in rel ]
    def prod(a,b):
        return tuple(sum(a[s]*b[t] for s,t in pairs)%q for pairs in coords)
    els=product(range(q),repeat=len(rel))
    idem = [x for x in els if prod(x,x)==x]
    if k==1: brute=len(idem)
    elif k==2:
        brute=sum(prod(x,y)==prod(y,x) for x in idem for y in idem)
    elif k==3:
        commuting = [[prod(x,y)==prod(y,x) for y in idem] for x in idem]
        brute=sum(1 for a in range(len(idem)) for b in range(len(idem)) for c in range(len(idem)) if commuting[a][b] and commuting[b][c] and commuting[a][c])
    else: raise ValueError('k must be <=3')
    expect=polynomial_count(n,off,q,k)
    print(f'n={n} q={q} k={k} relations={len(rel)} idempotents={len(idem)} brute={brute} predicted={expect}',flush=True)
    assert brute==expect,(n,q,k,brute,expect)

if __name__ == '__main__':
    tests=[
       ('singleton',1,[],2,(1,2,3)),
       ('2-chain',2,[(0,1)],2,(1,2,3)),
       ('3-chain',3,[(0,1),(1,2)],2,(1,2,3)),
       ('3-chain-q3',3,[(0,1),(1,2)],3,(1,2)),
       ('3-V',3,[(0,2),(1,2)],2,(1,2,3)),
       ('4-diamond',4,[(0,1),(0,2),(1,3),(2,3)],2,(1,2)),
       ('4-bipartite',4,[(0,2),(0,3),(1,2),(1,3)],2,(1,2)),
       ('4-chain',4,[(0,1),(1,2),(2,3)],2,(1,2)),
       ('4-star',4,[(0,1),(0,2),(0,3)],3,(1,2)),
    ]
    for name,n,edges,q,ks in tests:
        print(name)
        for k in ks: census(n,edges,q,k)
    print('CHECKER_OK')
