#!/usr/bin/env python3
"""Exact, finite checks of minimum forbidden-mosaic depths and Euler factors."""
from fractions import Fraction
from itertools import combinations

N=200000
spf=list(range(N+1))
for p in range(2,int(N**.5)+1):
    if spf[p]==p:
        for m in range(p*p,N+1,p):
            if spf[m]==m: spf[m]=p
primes=[p for p in range(2,40) if spf[p]==p]
sets=[{2},{3},{5},{7},{2,3},{2,5},{3,5},{2,3,5},{2,3,5,7}]
rows=[]
lookup_lam={}

def direct_contains(n, S, i):
    if i==0 or n<=1: return False
    m=n
    while m>1:
        p=spf[m]; e=0
        while m%p==0: m//=p; e+=1
        if p in S or direct_contains(e,S,i-1): return True
    return False
for S in sets:
    lam=[10**9]*(N+1)
    for n in range(2,N+1):
        rem=n
        depth=10**9
        while rem>1:
            p=spf[rem];e=0
            while rem%p==0:
                rem//=p;e+=1
            if p in S:
                depth=1
                break
            if lam[e]<10**9:
                depth=min(depth,lam[e]+1)
        lam[n]=depth
    lookup_lam[frozenset(S)]=lam
    for n in range(1,1001):
        for j in range(1,5):
            assert (lam[n]<=j)==direct_contains(n,S,j), (S,n,j)
    q=min(S);r=next(p for p in primes if p not in S)
    M=q
    for i in range(1,5):
        if M>N: break
        matches=[n for n in range(1,N+1) if lam[n]==i]
        assert matches and matches[0]==M, (S,i,M,matches[:3])
        rows.append((sorted(S),i,M,len(matches),matches[1] if len(matches)>1 else '-'))
        if i>=3 and len(matches)>1: assert matches[1]>=2*M
        if M>30: break
        M=r**M

# Local factors, independently comparing geometric-series modular exponent tests.
for S in [{2},{3},{2,3},{5}]:
    for p in primes[:7]:
        if p in S: continue
        for depth in (1,2,3):
            # exact rational finite cutoff and direct recursion for k<=60
            cutoff=60
            def avoid(k,i):
                if k<=1 or i==0: return True
                rem=k
                while rem>1:
                    a=spf[rem];e=0
                    while rem%a==0: rem//=a;e+=1
                    if a in S or (i>1 and not avoid(e,i-1)): return False
                return True
            allowed=[k for k in range(0,cutoff+1) if k==0 or avoid(k,depth-1)]
            A=(1-Fraction(1,p))*sum((Fraction(1,p**k) for k in allowed),Fraction(0))
            assert A>0
            # Independently compute identical truncation from first-depth recursion.
            B=(1-Fraction(1,p))*sum((Fraction(1,p**k) for k in range(cutoff+1)
                     if k==0 or lookup_lam[frozenset(S)][k]>depth-1), Fraction(0))
            assert A==B, (S,p,depth)
print('VERIFY_OK')
print('minimal-depth checks:')
for row in rows: print(*row)
print('finite Euler-factor checks: PASS')
