#!/usr/bin/env python3
"""Independent, finite checks for line-graph power domination claims."""
from itertools import combinations
from math import comb, factorial
from collections import Counter
import json

def tri(n):
    e = list(combinations(range(n),2))
    adj = []
    for i,(a,b) in enumerate(e):
        adj.append(sum(1<<j for j,(c,d) in enumerate(e) if j!=i and
                       (a==c or a==d or b==c or b==d)))
    return e,adj

def observed_closure(mask,adj):
    seen=mask
    for j,a in enumerate(adj):
        if mask>>j & 1:
            seen |= a
    whole=(1<<len(adj))-1
    while True:
        extra=0
        for j,a in enumerate(adj):
            if seen>>j & 1:
                remaining=a & (whole^seen)
                if remaining and remaining & (remaining-1)==0:
                    extra|=remaining
        extra &= (whole^seen)
        if not extra:
            return seen==whole
        seen |= extra

def has_criterion(mask,n,edges):
    supp=0
    for i,(a,b) in enumerate(edges):
        if mask>>i & 1:
            supp |= (1<<a)|(1<<b)
    return n-supp.bit_count()<=2

def has_minimal_pattern(mask,n,edges):
    deg=[0]*n
    for i,(a,b) in enumerate(edges):
        if mask>>i&1:
            deg[a]+=1;deg[b]+=1
    isolated=sum(d==0 for d in deg)
    if isolated==1:
        return all((mask>>i&1)==0 or (deg[a]==deg[b]==1)
                   for i,(a,b) in enumerate(edges))
    if isolated==2:
        return all((mask>>i&1)==0 or deg[a]==1 or deg[b]==1
                   for i,(a,b) in enumerate(edges))
    return False

def enum_no_isolates(s):
    # inclusion-exclusion, polynomial integer coefficients
    N=comb(s,2)
    out=[0]*(N+1)
    for k in range(N+1):
        out[k]=sum((-1)**j*comb(s,j)*comb(comb(s-j,2),k)
                for j in range(s+1) if k<=comb(s-j,2))
    return out

def expected_poly(n):
    N=comb(n,2)
    ans=[0]*(N+1)
    for u in range(min(n,2)+1):
        a=enum_no_isolates(n-u)
        for k,v in enumerate(a):
            ans[k]+=comb(n,u)*v
    return ans

def expected_min_count(n):
    k=(n-2+1)//2
    if n%2==0:
        t=n-2
        return comb(n,2)*factorial(t)//(2**(t//2)*factorial(t//2))
    m=(n-1)//2
    matches=n*factorial(n-1)//(2**m*factorial(m))
    if m==1:
        return matches
    s=n-2
    tails=comb(n,2)*comb(s,3)*3*factorial(s-3)//(2**(m-2)*factorial(m-2))
    return matches+tails

def full(n):
    edges, adj=tri(n)
    N=len(edges)
    counts=[0]*(N+1)
    mincounts=Counter()
    maximal_bad=0
    for mask in range(1<<N):
        actual=observed_closure(mask,adj)
        expected=has_criterion(mask,n,edges)
        assert actual==expected,(n,mask,'criterion')
        if not actual:
            maximal=all(has_criterion(mask|(1<<j),n,edges)
                        for j in range(N) if not (mask>>j&1))
            if maximal:
                maximal_bad+=1
                assert (mask==0 if n<=4 else
                        mask==sum(1<<j for j,(a,b) in enumerate(edges)
                                  if a not in [v for v in range(n) if
                                                all(not (mask>>k&1 and v in edges[k])
                                                    for k in range(N))]
                                  and b not in [v for v in range(n) if
                                                all(not (mask>>k&1 and v in edges[k])
                                                    for k in range(N))]))
        if actual:
            counts[mask.bit_count()]+=1
            minimal=not any(
                has_criterion(mask^(1<<j),n,edges)
                for j in range(N) if mask>>j&1)
            pattern=has_minimal_pattern(mask,n,edges)
            assert minimal==pattern,(n,mask,'minimal')
            if minimal: mincounts[mask.bit_count()]+=1
    assert maximal_bad==(1 if n<=4 else comb(n,3)),(n,maximal_bad)
    theoretical=expected_poly(n)
    assert counts==theoretical,(n,'polynomial',counts,theoretical)
    lower=(n-1)//2 if n%2 else (n-2)//2
    assert min(i for i,v in enumerate(counts) if v)==lower
    assert counts[lower]==expected_min_count(n)
    upper=max(mincounts)
    assert upper==(1 if n==3 else n-3),(n,upper)
    return {'n':n,'vertices':N,'subsets':1<<N,'min':lower,
            'minimum_count':counts[lower],'maximal_minimal_size':upper,
            'minimal_size_distribution':dict(mincounts),'maximal_non_pds':maximal_bad}

def check_arithmetic():
    for n in range(3,15):
        poly=expected_poly(n)
        N=comb(n,2)
        assert sum(poly)==(1<<N)-sum(comb(N,k)-poly[k] for k in range(N+1))
        assert poly[-1]==1
        assert poly[(n-1)//2 if n%2 else (n-2)//2]==expected_min_count(n)
    return "Inclusion-exclusion and optimizer coefficients checked exactly for 3<=n<=14"

if __name__=='__main__':
    for n in range(3,8):
        print(json.dumps(full(n),sort_keys=True))
    print(check_arithmetic())
    print("VERIFY_OK")
