#!/usr/bin/env python3
"""Independent exact enumeration for binary adjacent-pair ambiguity."""
from collections import Counter
from itertools import product
from math import comb

def signature(word):
    return tuple(sum(word[j:j+2] == pair for j in range(len(word)-1))
                 for pair in ('00','01','10','11'))

def predicted(n):
    if n == 1: return 2
    if n == 2: return 1
    h=(n-3)//4
    return (n-1)*comb((n-3)//2,h)*comb((n-2)//2,h)//(h+1)

def maximizers(n):
    N=n-1; h=(n-3)//4; q=N//2; r=(N+1)//2
    out=set()
    for t in ((h+1,h+2) if n%4==2 else (h+1,)):
        out.add((q-t,t,t,r-t))
        out.add((r-t,t,t,q-t))
    return out

def by_runs(c):
    a,b,e,d=c
    if abs(b-e)>1:return 0
    if b==e==0:return 1 if a==0 or d==0 else 0
    if b==e:
        t=b
        return (comb(a+t,t)*comb(d+t-1,t-1)
                +comb(a+t-1,t-1)*comb(d+t,t))
    t=min(b,e)
    return comb(a+t,t)*comb(d+t,t)

for n in range(1,18):
    observed=Counter(signature(''.join(bits)) for bits in product('01',repeat=n))
    optimum=max(observed.values())
    assert optimum==predicted(n),(n,optimum,predicted(n))
    if n>=7:
        assert {c for c,count in observed.items() if count==optimum}==maximizers(n),n
    if n>=2:
        for c,num in observed.items():
            assert by_runs(c)==num,(n,c,num,by_runs(c))

for n in range(3,121):
    N=n-1;best=0;opt=[]
    for b in range(N+1):
        for e in (b-1,b,b+1):
            if e<0 or b+e>N:continue
            for a in range(N-b-e+1):
                c=(a,b,e,N-b-e-a)
                size=by_runs(c)
                if size>best:best=size;opt=[c]
                elif size==best:opt.append(c)
    assert best==predicted(n),(n,best,predicted(n))
    if n>=7:
        assert set(opt)==maximizers(n),(n,set(opt),maximizers(n))
print('VERIFY_OK exhaustive_lengths=1..17 all_profiles_lengths=3..120')
