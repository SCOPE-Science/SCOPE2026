#!/usr/bin/env python3
"""Exact finite checks for residue strata of noncyclic squarefree semiprimes."""
from math import gcd, lcm, isqrt, log

def primes_upto(n):
    sieve=bytearray(b'\x01')*(n+1)
    sieve[:2]=b'\x00\x00'
    for k in range(2,isqrt(n)+1):
        if sieve[k]:
            sieve[k*k::k]=b'\x00'*((n-k*k)//k+1)
    return [i for i in range(2,n+1) if sieve[i]]

def phi(n):
    count=n
    for p in primes_upto(isqrt(n)+1):
        if n%p==0:
            count-=count//p
            while n%p==0:
                n//=p
    if n>1:count-=count//n
    return count

def allowed(m,c):
    if gcd(c,m)==1:
        return True
    g=gcd(c,m)
    if g<2 or any(g%a==0 for a in range(2,isqrt(g)+1)) or m%g:
        return False
    p=g
    return not(m%(p*p)==0 and ((c//p)-1)%p!=0)

def local_compat(m,c,p):
    if m%p:
        return gcd(c,m)==1
    if c%p:
        return False
    k=m//p
    return gcd(c//p,k)==1 and (c//p-1)%gcd(p,k)==0

def tests():
    ps=primes_upto(2700)
    paircount=0
    for m in range(1,78):
        for c in range(m):
            a=allowed(m,c)
            b=any(local_compat(m,c,p) for p in ps if p<=m+2) or gcd(c,m)==1
            assert a==b, (m,c,a,b)
    for m in range(1,75):
        for ix,p in enumerate(ps):
            if p>500:break
            for q in ps[ix+1:]:
                if q>1100: break
                if (q-1)%p:continue
                paircount+=1
                c=p*q%m
                assert local_compat(m,c,p) or p*q<=m*m, (m,p,q,c)
                assert allowed(m,c) or p*q<=m*m,(m,p,q,c)
    print('CHECKED_MODULI',77,'CHECKED_PAIR_INCIDENTS',paircount)
    print('EXAMPLES')
    for m in (2,4,6,8,9,12,18,25,27):
        print(m,[c for c in range(m) if allowed(m,c)])
    for m in (8,9,12):
        for c in range(m):
            if not allowed(m,c):
                for p in ps:
                    if p>m:break
                    for q in ps:
                        if q<=p or (q-1)%p or p*q<=m*m:continue
                        assert (p*q)%m!=c
    print('VERIFY_OK')

if __name__=='__main__': tests()

def density_demonstration(limit=2_000_000):
    ps=primes_upto(limit//2+3)
    root=isqrt(limit)
    out={m:[0]*m for m in (8,9,12)}
    total=0
    for i,p in enumerate(ps):
        if p>root:break
        for q in ps[i+1:]:
            if p*q>limit:break
            if (q-1)%p:continue
            total+=1
            for m,counts in out.items():counts[p*q%m]+=1
    print('LIMIT',limit,'ALL',total,'SCALED_TOTAL',round(total*log(limit)/limit,6))
    for m,counts in out.items():
        print('MODULUS',m,'SCALED_COUNTS',{c:round(v*log(limit)/limit,5) for c,v in enumerate(counts) if v})

if __name__=='__main__': density_demonstration()
