#!/usr/bin/env python3
"""Exhaustive graph-support check of square-rank SPC product statements.

Public reproducibility utility; Python standard library only.
"""
from itertools import combinations
from math import comb


def beta_for_edge_mask(m, n, mask):
    """GF(q) cycle-space dimension of the bipartite edge set, any q."""
    parent = list(range(m+n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    used=set()
    count=0
    for i in range(m):
        for j in range(n):
            b=i*n+j
            if mask & (1<<b):
                a=i; c=m+j; used.add(a); used.add(c)
                ra,rc=find(a),find(c)
                if ra!=rc: parent[ra]=rc
                count+=1
    comp=len({find(v) for v in used})
    return count-len(used)+comp


def square_masks(m,n,s):
    out=set()
    for rs in combinations(range(m),s+1):
        for cs in combinations(range(n),s+1):
            mask=sum(1<<(i*n+j) for i in rs for j in cs)
            out.add(mask)
    return out


def inspect(m,n):
    # ALL bipartite edge sets are examined; not just candidate constructions.
    best={s: (m*n+1,set()) for s in range(1,min(m,n))}
    for mask in range(1,1<<(m*n)):
        e=mask.bit_count()
        b=beta_for_edge_mask(m,n,mask)
        for s,(v,ss) in best.items():
            if b < s*s or e>v:
                continue
            if e<v:
                best[s]=(e,{mask})
            else:
                ss.add(mask)
    for s,(value,actual) in best.items():
        predicted=(s+1)**2
        expected=square_masks(m,n,s)
        assert value==predicted,(m,n,s,value,predicted)
        assert actual==expected,(m,n,s,len(actual),len(expected))
        assert len(actual)==comb(m,s+1)*comb(n,s+1)
        print(f'graph {m}x{n}, rank={s*s}: minimum={value}, exact supports={len(actual)}')


def field_rank_check(q,a,b):
    # Rows and columns enforce zero sums. Independent equations are all
    # a row equations and the first b-1 column equations.
    rows=[]
    for i in range(a):
        rows.append([int(x//b==i) for x in range(a*b)])
    for j in range(b-1):
        rows.append([int(x%b==j) for x in range(a*b)])
    M=[[u%q for u in row] for row in rows]
    r=0
    for c in range(a*b):
        pivot=next((k for k in range(r,len(M)) if M[k][c]),None)
        if pivot is None:continue
        M[pivot],M[r]=M[r],M[pivot]
        d=pow(M[r][c],-1,q)
        M[r]=[(u*d)%q for u in M[r]]
        for k in range(len(M)):
            if k!=r and M[k][c]:
                z=M[k][c]
                M[k]=[(x-z*y)%q for x,y in zip(M[k],M[r])]
        r+=1
    assert r==a+b-1,(q,a,b,r)
    print(f'field GF({q}), {a}x{b}: independent checks={r}, cycle dimension={a*b-r}')

if __name__=='__main__':
    # Exhaust 2^(m*n) bipartite edge subsets in each instance.
    for m,n in [(2,4),(3,3),(3,4),(4,4)]:
        inspect(m,n)
    for q in [2,3,5,7]:
        for a,b in [(2,2),(3,3),(3,4),(4,4)]:
            field_rank_check(q,a,b)
    print('SPC_SQUARE_RANK_VERIFICATION_OK')
