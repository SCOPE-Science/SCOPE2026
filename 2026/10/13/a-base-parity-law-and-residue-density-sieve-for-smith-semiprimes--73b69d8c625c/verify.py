#!/usr/bin/env python3
from math import gcd, isqrt

def primes_upto(n):
    s=bytearray(b"\x01")*(n+1)
    if n>=0:s[0]=0
    if n>=1:s[1]=0
    for p in range(2,isqrt(n)+1):
        if s[p]:
            s[p*p:n+1:p]=b"\x00"*(((n-p*p)//p)+1)
    return [i for i in range(2,n+1) if s[i]]

def dsum(n,b):
    z=0
    while n:
        n,r=divmod(n,b); z+=r
    return z

def phi(n):
    if n==1:return 1
    z=n; r=n; p=2
    while p*p<=z:
        if z%p==0:
            while z%p==0:z//=p
            r-=r//p
        p+=1
    if z>1:r-=r//z
    return r

def acount_formula(m):
    if m==1:return 1
    z=m; ans=1; p=2
    while p*p<=z:
        if z%p==0:
            a=0
            while z%p==0:z//=p; a+=1
            ans*=p**(a-1)*(p-2)
        p+=1
    if z>1: ans*=z-2
    return ans

LIMIT=500000
P=primes_upto(LIMIT//2+10)
semis=[]
for i,p in enumerate(P):
    if p*p>LIMIT: break
    semis.append((p*p,p,p))
    for q in P[i+1:]:
        n=p*q
        if n>LIMIT: break
        semis.append((n,p,q))

odd_summary={}
for B in range(2,21):
    smith=[]
    m=B-1
    for n,p,q in semis:
        if dsum(n,B)==dsum(p,B)+dsum(q,B):
            smith.append((n,p,q))
            assert (p-1)*(q-1)%m==1%m if m>1 else True
            if B%2==0 and p!=q and m>1:
                assert gcd(p,m)==gcd(q,m)==gcd(p-1,m)==gcd(q-1,m)==1
                r=p%m
                t=(1+pow(r-1,-1,m))%m
                assert q%m==t
    if B==3:
        assert smith==[]
    if B>=5 and B%2==1:
        assert smith==[(4,2,2)], (B,smith[:10])
    if B%2==1:
        odd_summary[B]=len(smith)

for B in range(2,41,2):
    m=B-1
    A=[r for r in range(m) if gcd(r,m)==1 and gcd(r-1,m)==1] if m>1 else [0]
    assert len(A)==acount_formula(m)
    if m>1:
        for r in A:
            t=(1+pow(r-1,-1,m))%m
            assert t in A
            assert (1+pow(t-1,-1,m))%m==r

# Decimal specialization.
allowed={(2,2),(5,8),(8,5)}
for n,p,q in semis:
    if p!=q and dsum(n,10)==dsum(p,10)+dsum(q,10):
        assert (p%9,q%9) in allowed

# Finite compatible proportions; these are only corroborative.
rows=[]
for B in (4,6,8,10,12,16):
    m=B-1
    compat=sum(1 for n,p,q in semis if ((p-1)*(q-1)-1)%m==0)
    c=acount_formula(m)/(phi(m)**2)
    rows.append((B,compat,len(semis),compat/len(semis),c))

print('VERIFY_OK',f'semiprimes={len(semis)}',f'odd={odd_summary}',f'rows={rows}')
