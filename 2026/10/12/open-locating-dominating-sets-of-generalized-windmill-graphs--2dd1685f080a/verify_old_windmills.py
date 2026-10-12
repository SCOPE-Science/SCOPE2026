#!/usr/bin/env python3
from collections import Counter
from math import comb


def graph(r, m):
    blocks=[]
    v=1
    for _ in range(r):
        B=list(range(v,v+m)); v+=m; blocks.append(B)
    adj=[set() for _ in range(v)]
    for B in blocks:
        for x in B:
            adj[0].add(x); adj[x].add(0)
        for i,x in enumerate(B):
            for y in B[i+1:]:
                adj[x].add(y); adj[y].add(x)
    return adj, blocks


def is_old(adj, mask):
    signatures=[]
    for nbrs in adj:
        sig=0
        for w in nbrs:
            if mask >> w & 1:
                sig |= 1 << w
        if sig == 0:
            return False
        signatures.append(sig)
    return len(signatures)==len(set(signatures))


def predicted(r,m,blocks,mask):
    c=bool(mask & 1)
    chosen=lambda B: sum((mask >> v) & 1 for v in B)
    if m>=3:
        return all(m-chosen(B) <= 1 for B in blocks)
    # m=2 friendship boundary
    if not c:
        return all(chosen(B)==2 for B in blocks)
    vals=[chosen(B) for B in blocks]
    return all(x>=1 for x in vals) and sum(x==1 for x in vals) <= 1


def expected_poly(r,m):
    out=Counter()
    if m>=3:
        # (1+x)(x^m+m x^(m-1))^r
        for omitted in range(r+1):
            base_size=r*m-omitted
            ways=comb(r,omitted)*(m**omitted)
            out[base_size]+=ways
            out[base_size+1]+=ways
    else:
        out[2*r]=2*r+1
        out[2*r+1]=1
    return out

pairs=[]
subset_checks=0
minimum_checks=0
max_order=0
for r,m in [(2,2),(3,2),(4,2),(5,2),(2,3),(3,3),(4,3),(2,4),(3,4),(2,5)]:
    adj,blocks=graph(r,m)
    n=len(adj); max_order=max(max_order,n)
    got=Counter(); pred=Counter()
    for mask in range(1<<n):
        actual=is_old(adj,mask)
        claimed=predicted(r,m,blocks,mask)
        subset_checks+=1
        if actual != claimed:
            raise AssertionError((r,m,mask,actual,claimed))
        if actual:
            k=mask.bit_count(); got[k]+=1; pred[k]+=1
    exp=expected_poly(r,m)
    if got != exp:
        raise AssertionError((r,m,got,exp))
    mn=min(got)
    expected_min=r*(m-1) if m>=3 else 2*r
    expected_count=(m**r) if m>=3 else (2*r+1)
    if mn != expected_min or got[mn] != expected_count:
        raise AssertionError((r,m,mn,got[mn],expected_min,expected_count))
    minimum_checks+=1
    pairs.append((r,m))
print(f"VERIFY_OK parameter_pairs={len(pairs)} subset_checks={subset_checks} minimum_checks={minimum_checks} max_order={max_order}")
