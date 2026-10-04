#!/usr/bin/env python3
from math import gcd

def partitions(n, hi=None):
    if hi is None or hi > n: hi=n
    if n==0:
        yield (); return
    for a in range(hi,0,-1):
        for rest in partitions(n-a,a):
            yield (a,)+rest

def divisors(n):
    out=[]
    d=1
    while d*d<=n:
        if n%d==0:
            out.append(d)
            if d*d!=n: out.append(n//d)
        d+=1
    return out

def is_perfect(n):
    return n>1 and sum(divisors(n))==2*n

patterns={}
for om in range(1,9):
    patterns[om]=[]
    for exps in partitions(om):
        tau=1
        for e in exps: tau*=e+1
        if is_perfect(tau): patterns[om].append((exps,tau))
assert patterns[3]==[((2,1),6)]
assert patterns[5]==[((5,),6)]
assert all(not patterns[k] for k in (1,2,4,6,7))
assert patterns[8]==[((6,1,1),28)]

def primes_upto(n):
    s=bytearray(b'\x01')*(n+1); s[:2]=b'\x00\x00'
    for p in range(2,int(n**0.5)+1):
        if s[p]: s[p*p:n+1:p]=b'\x00'*(((n-p*p)//p)+1)
    return [i for i in range(2,n+1) if s[i]]
P=[p for p in primes_upto(200) if p&1]
# p^5 obstruction: two odd factors are coprime and >1.
for p in P:
    A=p*p+p+1; B=p*p-p+1
    assert A>1 and B>1 and gcd(A,B)==1
# p^2 q: finite direct sanity check against all even perfects below the finite sigma range.
perfects={6,28,496,8128,33550336}
hits=[]
for p in P:
    A=p*p+p+1
    for q in P:
        if q==p: continue
        if A*(q+1) in perfects: hits.append((p,q))
assert not hits
mod8={r:sum(pow(r,j,8) for j in range(7))%8 for r in (1,3,5,7)}
assert mod8=={1:7,3:5,5:3,7:1}
print('VERIFY_OK', 'patterns='+repr(patterns), 'p2q_hits=0', 'phi7_mod8='+repr(mod8))
