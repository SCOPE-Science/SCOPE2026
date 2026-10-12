#!/usr/bin/env python3
from math import gcd, isqrt, log

def primes_upto(n):
    s=bytearray(b"\x01")*(n+1)
    s[0:2]=b"\x00\x00"
    for p in range(2,isqrt(n)+1):
        if s[p]:
            start=p*p
            s[start:n+1:p]=b"\x00"*(((n-start)//p)+1)
    return [i for i in range(2,n+1) if s[i]],s

CHECK=200_000
plist,_=primes_upto(CHECK)
direct_total=direct_bad=0
for i,p in enumerate(plist):
    if p*p>CHECK: break
    for q in plist[i+1:]:
        n=p*q
        if n>CHECK: break
        direct_total+=1
        b1=gcd(n,(p-1)*(q-1))>1
        b2=((q-1)%p==0)
        assert b1==b2
        direct_bad+=int(b1)

LIMIT=2_000_000
qprimes,_=primes_upto(LIMIT//2)
spf=list(range(LIMIT//2+1))
for p in range(2,isqrt(LIMIT//2)+1):
    if spf[p]==p:
        for m in range(p*p,LIMIT//2+1,p):
            if spf[m]==m: spf[m]=p

def factors(n):
    out=[]
    while n>1:
        p=spf[n]; out.append(p)
        while n%p==0: n//=p
    return out

cutoffs=[10_000,100_000,1_000_000,2_000_000]
counts={x:0 for x in cutoffs}
for q in qprimes:
    for p in factors(q-1):
        if p>=q: continue
        n=p*q
        for x in cutoffs:
            if n<=x: counts[x]+=1
scaled=[(x,counts[x],counts[x]*log(x)/x) for x in cutoffs]

N=2_000_000
pn,_=primes_upto(N)
partial=sum(1.0/(p*(p-1)) for p in pn)
lower=partial
upper=partial+1.0/N
assert 0.77315 < lower < upper < 0.77317
print('VERIFY_OK',f'direct_semiprimes={direct_total}',f'direct_bad={direct_bad}',f'scaled={scaled}',f'A_interval=({lower:.10f},{upper:.10f})')
