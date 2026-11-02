#!/usr/bin/env python3
"""Exact combinatorial checks for a partially whiskered graph identity."""
from functools import lru_cache
from itertools import combinations
from math import comb
from random import Random


def edges_to_adj(n, edgebits):
    adj=[0]*n
    i=0
    for a in range(n):
        for b in range(a+1,n):
            if (edgebits>>i)&1:
                adj[a] |= 1<<b; adj[b] |= 1<<a
            i+=1
    return adj


def polynomial(adj):
    # Deletion / closed-neighborhood deletion independent-set recurrence.
    @lru_cache(None)
    def rec(mask):
        if not mask: return (1,)
        bit=mask&(-mask); v=bit.bit_length()-1
        a=rec(mask^bit)
        b=rec((mask^bit)&~adj[v])
        c=[0]*max(len(a), len(b)+1)
        for j,t in enumerate(a): c[j]+=t
        for j,t in enumerate(b): c[j+1]+=t
        return tuple(c)
    return rec((1<<len(adj))-1)


def literal_polynomial(adj):
    out=[0]*(len(adj)+1)
    for mask in range(1<<len(adj)):
        if all(not ((mask>>i)&1 and adj[i]&mask) for i in range(len(adj))):
            out[mask.bit_count()]+=1
    while out and out[-1]==0: out.pop()
    return tuple(out)


def construct(base,h):
    n=len(base); A={v for v in range(n) if base[h]>>v&1}
    B={v for v in range(n) if v!=h and v not in A}
    W=list(base)
    for v in range(n):
        for _ in range(0 if v==h else 1 if v in A else 2):
            k=len(W)
            W.append(1<<v)
            W[v]|=1<<k
    return W,A,B


def root_poly(base, removed):
    ids=[j for j in range(len(base)) if j != removed]
    new=[sum(1<<k for k,j in enumerate(ids) if base[i]>>j&1) for i in ids]
    return polynomial(new)


def predicted_gamma_poly(base,h,A,B):
    Q=root_poly(base,h)
    d=len(A)+2*len(B)+1
    out=[0]*(d+1)
    for r,qr in enumerate(Q):
        for j in range(d-2*r+1):
            out[r+j]+=qr*comb(d-2*r,j)
    return tuple(out)


def check(base,h,do_literal=False):
    W,A,B=construct(base,h)
    if not A: return False
    p=polynomial(W)
    d=len(A)+2*len(B)+1
    assert len(p)==d+1 and p[-1]==1, ('max',base,h)
    subids=sorted(A)
    a_adj=[sum(1<<k for k,j in enumerate(subids) if base[v]>>j&1) for v in subids]
    independent_A=sum(polynomial(a_adj))
    defect=independent_A-1-len(A)
    assert p[d-1]-p[1]==defect, ('defect',base,h,p,defect)
    A_clique=all((base[u]>>v)&1 for u,v in combinations(A,2))
    assert (p==p[::-1])==A_clique, ('equiv',base,h,p)
    if A_clique:
        assert p==predicted_gamma_poly(base,h,A,B), ('gamma',base,h,p)
    if do_literal:
        assert p==literal_polynomial(W),('literal',base,h)
    return True


def main():
    cnt=0; literal=0; clique=0; nonclique=0
    for n in range(2,6):
        for edge_bits in range(1<<(n*(n-1)//2)):
            base=edges_to_adj(n,edge_bits)
            for h in range(n):
                if not base[h]: continue
                do_literal=n<=4
                check(base,h,do_literal)
                cnt+=1; literal+=bool(do_literal)
                A=[v for v in range(n) if (base[h]>>v)&1]
                isclique=all((base[u]>>v)&1 for u,v in combinations(A,2))
                clique+=isclique; nonclique+=not isclique
    rng=Random(20261027); large=0
    for n in (6,7,8):
        for _ in range(250):
            ebits=rng.getrandbits(n*(n-1)//2)
            base=edges_to_adj(n,ebits)
            for h in range(n):
                if check(base,h): large+=1
    print('ALL_LABELED_CHECK',cnt, 'CLIQUE',clique,'NONCLIQUE',nonclique)
    print('LITERAL_BRUTE_FORCE_CHECK',literal)
    print('LARGER_RANDOM_CHECK',large)
    print('VERIFY_OK')

if __name__=='__main__': main()
