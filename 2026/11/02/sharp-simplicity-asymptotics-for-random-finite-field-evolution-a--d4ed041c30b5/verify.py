#!/usr/bin/env python3
"""Exact finite-field consistency checks for the simplicity asymptotic.

Standard-library only.  Enumeration verifies the finite support-cut bounds,
independently tests strong connectivity by graph reachability, and checks
each individual invariant-coordinate-set probability.
"""
from itertools import product
from math import comb, prod


def matrix_rank(a,p):
    b=[list(row) for row in a]; n=len(a); r=0
    for j in range(n):
        k=next((i for i in range(r,n) if b[i][j]),None)
        if k is None: continue
        b[r],b[k]=b[k],b[r]
        inv=pow(b[r][j],-1,p)
        b[r]=[(x*inv)%p for x in b[r]]
        for i in range(n):
            if i!=r and b[i][j]:
                t=b[i][j]
                b[i]=[(x-t*y)%p for x,y in zip(b[i],b[r])]
        r+=1
    return r


def is_closed(a,s):
    n=len(a)
    return all(not a[i][j] for i in range(n) if s & (1<<i)
                              for j in range(n) if not(s & (1<<j)))


def is_strong_by_cuts(a):
    n=len(a)
    return not any(is_closed(a,s) for s in range(1,(1<<n)-1))


def is_strong_by_reachability(a):
    n=len(a)
    for root in range(n):
        seen={root}; fringe=[root]
        while fringe:
            u=fringe.pop()
            for v in range(n):
                if a[u][v] and v not in seen:
                    seen.add(v);fringe.append(v)
        if len(seen)!=n:return False
    return True


def gl_order(n,q):
    return prod(q**n-q**j for j in range(n))


def run_case(n,q):
    total=simple=0
    event_counts=[0]*(1<<n)
    for x in product(range(q),repeat=n*n):
        a=[x[n*i:n*(i+1)] for i in range(n)]
        if matrix_rank(a,q)<n:continue
        total+=1
        strong=is_strong_by_cuts(a)
        assert strong == is_strong_by_reachability(a)
        simple+=strong
        for s in range(1,(1<<n)-1):
            event_counts[s]+=is_closed(a,s)
    assert total==gl_order(n,q)
    for s in range(1,(1<<n)-1):
        k=s.bit_count()
        expected=gl_order(k,q)*gl_order(n-k,q)*q**(k*(n-k))
        assert event_counts[s]==expected,(n,q,s,event_counts[s],expected)
    if n>=3:
        phi=total/(q**(n*n))
        p1=(q-1)/(q**n-1)
        e=comb(2*n,2)*q**(-2*n+3)/phi
        e+=sum(comb(n,k)*q**(-k*(n-k))/phi for k in range(2,n-1))
        assert abs((total-simple)/total-2*n*p1)<=e+1e-12
    print(f'q={q} n={n}: GL={total}; simple={simple}; nonsimple={total-simple}; VERIFIED')

for args in ((2,2),(2,3),(3,2),(3,3),(4,2)):
    run_case(*args)
print('VERIFY_OK')
