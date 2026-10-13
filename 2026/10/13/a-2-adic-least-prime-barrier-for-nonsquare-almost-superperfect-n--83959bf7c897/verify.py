#!/usr/bin/env python3
from math import isqrt

def v2(n):
    c=0
    while n%2==0 and n:
        c+=1; n//=2
    return c

def primes_upto(N):
    s=bytearray(b'\x01')*(N+1); s[:2]=b'\x00\x00'
    for p in range(2,isqrt(N)+1):
        if s[p]: s[p*p:N+1:p]=b'\x00'*(((N-p*p)//p)+1)
    return [i for i in range(2,N+1) if s[i]]

# Local LTE identity on a nontrivial finite grid.
for p in [q for q in primes_upto(300) if q>2]:
    for a in range(1,20,2):
        sig=(p**(a+1)-1)//(p-1)
        assert v2(sig)==v2(p+1)+v2(a+1)-1
    for a in range(2,20,2):
        sig=(p**(a+1)-1)//(p-1)
        assert v2(sig)==0

for b in range(2,18,2):
    num=2**(b+1); den=num-1
    assert num/den == 2/(2-2**(-b))
    assert (1+1/den)==num/den

LIMIT=200000
# Sieve sigma values up to a safe envelope, then factor larger sigma(n) directly if needed.
sigma=[0]*(LIMIT+1)
for d in range(1,LIMIT+1):
    for m in range(d,LIMIT+1,d): sigma[m]+=d

def sigma_trial(n):
    x=n; ans=1; p=2
    while p*p<=x:
        if x%p==0:
            pp=1; sm=1
            while x%p==0:
                x//=p; pp*=p; sm+=pp
            ans*=sm
        p=3 if p==2 else p+2
    if x>1: ans*=x+1
    return ans

hits=[]
for n in range(2,LIMIT+1):
    s=sigma[n]
    ss=sigma[s] if s<=LIMIT else sigma_trial(s)
    if ss==2*n-1: hits.append(n)
assert hits==[], hits
print('VERIFY_OK',f'limit={LIMIT}',f'asp_gt1_hits={hits}', 'lte_grid=passed', 'thresholds=passed')
