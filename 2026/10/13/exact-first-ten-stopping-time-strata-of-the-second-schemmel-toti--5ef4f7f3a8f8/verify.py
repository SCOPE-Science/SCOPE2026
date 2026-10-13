#!/usr/bin/env python3
"""Exact finite inverse-tree census for Schemmel's second totient.
Only Python standard library. Every inverse branch is constructed from complete
prime-factor and divisor enumeration.  The loop's finite depth is explicit.
"""
from functools import lru_cache
from math import isqrt

LIMIT=10
N_MAX=15*7**(LIMIT-2)

def small_primes(bound):
    sieve=bytearray(b'\x01')*(bound+1)
    sieve[0:2]=b'\x00\x00'
    for d in range(2,isqrt(bound)+1):
        if sieve[d]:
            sieve[d*d::d]=b'\x00'*(((bound-d*d)//d)+1)
    return [i for i in range(bound+1) if sieve[i]]
P=small_primes(isqrt(N_MAX)+2)

def isprime(n):
    if n<2:return False
    for p in P:
        if p*p>n:return True
        if n%p==0:return False
    return True

@lru_cache(maxsize=None)
def factor(n):
    v=n
    out=[]
    for p in P:
        if p*p>v:break
        if v%p==0:
            a=0
            while v%p==0:
                v//=p;a+=1
            out.append((p,a))
    if v>1:out.append((v,1))
    return tuple(out)

@lru_cache(maxsize=None)
def divisors(n):
    ds=[1]
    for p,e in factor(n):
        old=ds[:]
        z=1
        for _ in range(e):
            z*=p
            ds.extend(d*z for d in old)
    return tuple(ds)

def L2(n):
    z=1
    for p,e in factor(n):
        if p==2:return 0
        z*=pow(p,e-1)*(p-2)
    return z

@lru_cache(maxsize=None)
def preimages(m):
    # At prime p, a valuation a>=1 contributes p^(a-1)*(p-2).
    # Thus p-2 | m. Enumerating all divisors m yields all possible primes p.
    groups=[]
    for d in divisors(m):
        p=d+2
        if not isprime(p):continue
        choices=[]
        c=d
        pw=p
        while m%c==0:
            choices.append((c,pw))
            c*=p
            pw*=p
        groups.append((p,choices))
    out=set()
    def take(i,remaining,n):
        if i==len(groups):
            if remaining==1 and n>1:out.add(n)
            return
        p,choices=groups[i]
        take(i+1,remaining,n)
        for c,pw in choices:
            if remaining%c==0:take(i+1,remaining//c,n*pw)
    take(0,m,1)
    return out

level={3}
all_levels={3:1}
rows=[(1,1,3,1)]
assert L2(3)==1
for rank in range(2,LIMIT+1):
    following=set()
    for m in level:following.update(preimages(m))
    assert all(L2(n) in level for n in following)
    level=following
    assert all(n%2==1 and n>1 for n in level)
    for n in level:all_levels[n]=rank
    maximum=max(level)
    bound=15*7**(rank-2)
    matches=sum(n==bound for n in level)
    assert maximum==bound and matches==1
    rows.append((rank,len(level),maximum,matches))
    print('R',rank,'count',len(level),'max',maximum,'uniqueness',matches,flush=True)
assert [r[1] for r in rows]==[1,3,13,54,226,986,4071,16693,67816,275129]
# Small independent forward recurrence check, including levels beyond the tabulated range.
def forward_rank(n):
    r=0
    while n>1:
        n=L2(n)
        r+=1
    return r
for n in range(3,50001,2):
    r=forward_rank(n)
    if r<=LIMIT:
        assert all_levels.get(n)==r, (n,r)
    else:
        assert n not in all_levels
print('EXACT_CERTIFICATE_OK',rows, 'forward_check_odd_up_to=50000')
