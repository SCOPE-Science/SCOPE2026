#!/usr/bin/env python3
"""Exact independent support certificate and finite consistency check."""
from fractions import Fraction as F
from functools import reduce
from math import isqrt
from pathlib import Path
import csv

LIMIT = 400_000
MAXPSI = 1_300_000
Q = (17,23,31,47,53,71,107,127,191,383)

def ratio(primes):
    return reduce(lambda z,p:z*F(p+1,p),primes,F(1,1)) / 3

def prime(x):
    if x < 2: return False
    for d in range(2,isqrt(x)+1):
        if x%d==0: return False
    return True

def smooth23(x):
    while x%2==0: x//=2
    while x%3==0: x//=3
    return x==1

assert ratio([2,3,5,7,11]) == F(384,385)  # product divided by 3
assert ratio([2,3,5,7,11,13]) == F(768,715)
assert ratio([2,3,5,7,11,383]) == F(147456,147455)
assert ratio([2,3,5,7,17,23]) == F(13824,13685)
for support in ([2,5,7,11,13,17], [2,3,7,11,13,17],
                [2,3,5,11,13,17], [2,3,5,7,23,29]):
    assert ratio(support) < 1
assert F(2304,715) < F(15,4)
assert F(92160,46189) < 2
assert F(27648,12155) < 3

q=tuple(v for v in range(12,384) if prime(v) and smooth23(v+1))
assert q==Q,q
uv=tuple(v for v in range(18,31) if prime(v) and smooth23(v+1))
assert uv==(23,),uv

rows=[]
for u,v in [(11,q) for q in Q]+[(17,23)]:
    r=ratio((2,3,5,7,u,v))
    assert r>1
    rows.append((u,v,r.numerator,r.denominator,2*3*5*7*u*v))
with Path(__file__).with_name('support_catalog.csv').open(newline='',encoding='utf-8') as f:
    csvrows=list(csv.reader(f))
assert csvrows[0]==['u','v','ratio_numerator','ratio_denominator','least_member']
assert [tuple(map(int,x)) for x in csvrows[1:]]==rows

spf=list(range(MAXPSI+1));spf[0]=0;spf[1]=1
for p in range(2,isqrt(MAXPSI)+1):
    if spf[p]==p:
        for m in range(p*p,MAXPSI+1,p):
            if spf[m]==m:spf[m]=p

def factor(n):
    result=[]
    while n>1:
        p=spf[n];e=0
        while n%p==0:
            n//=p;e+=1
        result.append((p,e))
    return result

def phi(n):
    ans=n
    for p,e in factor(n):
        ans=ans//p*(p-1)
    return ans

hits=[]
for n in range(2,LIMIT+1):
    f=factor(n)
    ps=n
    for p,e in f:
        ps=ps//p*(p+1)
    assert ps<=MAXPSI,(n,ps)
    actual=phi(ps)>n
    support={p for p,e in f}
    predicted=(len(support)==6 and {2,3,5,7}.issubset(support)
               and (support=={2,3,5,7,17,23} or
                    (11 in support and len(support-{2,3,5,7,11})==1 and
                     next(iter(support-{2,3,5,7,11})) in Q))
               and all(e==1 for p,e in f if p>=5))
    assert actual==predicted,(n,ps,phi(ps),f,actual,predicted)
    if actual:hits.append(n)
assert hits[0]==39270
assert hits[:5]==[39270,53130,71610,78540,82110]
print('VERIFY_OK',f'limit={LIMIT}',f'hits={len(hits)}',
      f'first_five={hits[:5]}',f'support_templates={len(rows)}',
      f'largest_prime={Q[-1]}',f'boundary_ratio={F(147456,147455)}')
