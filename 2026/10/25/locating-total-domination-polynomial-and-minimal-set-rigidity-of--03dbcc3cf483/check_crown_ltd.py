#!/usr/bin/env python3
"""Exhaustive direct-definition verification for crown-graph locating-total domination.

Run with a standard Python 3 interpreter; requires no third-party packages.
"""
from collections import Counter
from math import comb, factorial


def neighborhoods(n):
    return [sum(1 << (n+j) for j in range(n) if i != j) for i in range(n)] + [sum(1 << j for j in range(n) if i != j) for i in range(n)]


def is_locating_total(n, mask, neighbors):
    seen = set()
    for vertex in range(2*n):
        signature = neighbors[vertex] & mask
        if not signature:
            return False
        if not (mask >> vertex) & 1:
            if signature in seen:
                return False
            seen.add(signature)
    return True


def profile(n, mask):
    a = (mask & ((1 << n)-1)).bit_count()
    b = (mask >> n).bit_count()
    missed = sum(not ((mask >> i) & 1 or (mask >> (n+i)) & 1) for i in range(n))
    doubled = sum(bool((mask >> i) & 1 and (mask >> (n+i)) & 1) for i in range(n))
    return a,b,missed,doubled


def coeff(n,a,b):
    if a < 2 or b < 2:
        return 0
    total=0
    for t in (0,1):
        c00=t; c10=n-b-t; c01=n-a-t; c11=a+b-n+t
        if min(c10,c01,c11)>=0:
            total += factorial(n)//(factorial(c00)*factorial(c10)*factorial(c01)*factorial(c11))
    return total


def univariate_coeff(n,k):
    total=0
    for j in range(n+1):
        if n+j==k:total+=comb(n,j)*2**(n-j)
    for j in range(n):
        if n-1+j==k:total+=n*comb(n-1,j)*2**(n-1-j)
    if k==n-1: total-=2*n*n
    if k==n: total-=2*(n*n+1)
    if k==n+1: total-=2*n
    if n==3 and k==2:total+=6
    return total


def family_min(n,a,b,missed,doubled):
    if n in (3,4): return a==2 and b==2 and missed<=1
    return missed==1 and doubled==0 and a>=2 and b>=2

alltested = 0
for n in range(3,10):
    N = neighborhoods(n)
    sizes = Counter()
    bivariate = Counter()
    minimal_sizes = Counter()
    for mask in range(1<<(2*n)):
        actual = is_locating_total(n,mask,N)
        a,b,t,d = profile(n,mask)
        predicted = a>=2 and b>=2 and t<=1
        assert actual==predicted,("classification",n,mask)
        if actual:
            sizes[a+b]+=1
            bivariate[a,b]+=1
            minimal = not any(is_locating_total(n,mask^(1<<v),N) for v in range(2*n) if mask>>v&1)
            assert minimal == family_min(n,a,b,t,d),("minimal_family",n,mask)
            if minimal:minimal_sizes[a+b]+=1
    for a in range(n+1):
        for b in range(n+1):
            assert bivariate[a,b]==coeff(n,a,b),("bivariate",n,a,b)
    for k in range(2*n+1):
        assert sizes[k]==univariate_coeff(n,k),("univariate",n,k)
    count_min = 9 if n==3 else 30 if n==4 else n*(2**(n-1)-2*n)
    assert minimal_sizes=={max(4,n-1):count_min},("minimum",n)
    alltested += 1<<(2*n)
    print(f"n={n}: subsets={1<<(2*n)}, valid={sum(sizes.values())}, minimal_size={max(4,n-1)}, minimal_count={count_min}, classification/coefficient/minimal_families=PASS")
print(f"TOTAL examined vertex subsets: {alltested}; independent original-definition checks: PASS")
