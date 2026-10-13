#!/usr/bin/env python3
from collections import Counter, deque
from itertools import combinations
from math import comb


def crown(n):
    adj=[set() for _ in range(2*n)]
    for i in range(n):
        for j in range(n):
            if i!=j:
                adj[i].add(n+j)
                adj[n+j].add(i)
    return adj


def distances(adj):
    N=len(adj); D=[]
    for s in range(N):
        d=[N+1]*N; d[s]=0; q=deque([s])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if d[v]==N+1:
                    d[v]=d[u]+1; q.append(v)
        D.append(d)
    return D


def geodetic(mask,D):
    N=len(D)
    S=[v for v in range(N) if (mask>>v)&1]
    covered=set(S)
    for u,v in combinations(S,2):
        uv=D[u][v]
        for w in range(N):
            if D[u][w]+D[w][v]==uv:
                covered.add(w)
    return len(covered)==N


def structural(n,mask):
    I={i for i in range(n) if (mask>>i)&1}
    J={i for i in range(n) if (mask>>(n+i))&1}
    c=len(I & J); p=len(I); q=len(J)
    return (c>=1 or
            (p==n and q==0) or
            (q==n and p==0) or
            (c==0 and p>=3 and q>=3))


def minimal_structural(n,mask):
    I={i for i in range(n) if (mask>>i)&1}
    J={i for i in range(n) if (mask>>(n+i))&1}
    c=len(I & J); p=len(I); q=len(J)
    if c>=1:
        return p==q==1 and I==J
    if p==n and q==0: return True
    if q==n and p==0: return True
    return c==0 and p==3 and q==3


def formula_coeffs(n):
    out=Counter()
    for k in range(2*n+1):
        a=comb(2*n,k)
        if k<=n:
            a-=comb(n,k)*(2**k)
        if k==n:
            a+=2
        if 6<=k<=n:
            a+=comb(n,k)*(2**k-k*k-k-2)
        if a:
            out[k]=a
    return out

subset_checks=0
geodetic_sets=0
minimal_sets=0
coefficient_checks=0
minimal_checks=0
for n in range(3,9):
    D=distances(crown(n))
    actual=Counter(); mins=Counter()
    geo_masks=[]
    for mask in range(1<<(2*n)):
        g=geodetic(mask,D)
        s=structural(n,mask)
        subset_checks+=1
        if g!=s:
            raise AssertionError(("structural mismatch",n,mask,g,s))
        if g:
            geo_masks.append(mask)
            actual[mask.bit_count()]+=1
            geodetic_sets+=1
    expected=formula_coeffs(n)
    for k in range(2*n+1):
        coefficient_checks+=1
        if actual[k]!=expected[k]:
            raise AssertionError(("coefficient mismatch",n,k,actual[k],expected[k]))
    for mask in geo_masks:
        is_min=True
        for v in range(2*n):
            if (mask>>v)&1 and geodetic(mask & ~(1<<v),D):
                is_min=False; break
        ms=minimal_structural(n,mask)
        minimal_checks+=1
        if is_min!=ms:
            raise AssertionError(("minimal mismatch",n,mask,is_min,ms))
        if is_min:
            mins[mask.bit_count()]+=1
            minimal_sets+=1
    expected_min=Counter({2:n,n:2})
    if n==2:
        expected_min[2]+=2
    if n>=6:
        expected_min[6]+=20*comb(n,6)
    if mins!=expected_min:
        raise AssertionError(("minimal profile mismatch",n,mins,expected_min))
    if min(actual)!=2:
        raise AssertionError(("geodetic number",n,min(actual)))
    if max(mins)!=n:
        raise AssertionError(("upper geodetic number",n,max(mins)))
print(f"VERIFY_OK n_range=3..8 subset_checks={subset_checks} geodetic_sets={geodetic_sets} minimal_sets={minimal_sets} coefficient_checks={coefficient_checks} minimal_checks={minimal_checks} max_order=16")
