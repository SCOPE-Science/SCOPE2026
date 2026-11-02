"""Finite, exact consistency checks for the biased-cycle range coupling.
This supplements, and does not replace, the infinite-path proof.
"""
from fractions import Fraction as F
from collections import defaultdict
from itertools import product

checks=0
for n in range(3,9):
    for p in (F(2,3),F(3,4),F(4,5)):
        q=1-p; r=q/p
        # The state is visited arc lengths (left,right), position = current end.
        cur={(0,0,'O'):F(1)}
        for m in range(1,n):
            nxt=defaultdict(F)
            for (a,b,side),weight in cur.items():
                if side=='O':
                    branches=[('R',p),('L',q)]
                elif side=='R':
                    right=(1-r**m)/(1-r**(m+1))
                    branches=[('R',right),('L',1-right)]
                else:
                    right=(1-r)/(1-r**(m+1))
                    branches=[('R',right),('L',1-right)]
                for direction,rate in branches:
                    nxt[(a+int(direction=='L'),b+int(direction=='R'),direction)]+=weight*rate
            cur=nxt
        pmf=defaultdict(F)
        for (a,b,side),weight in cur.items():
            k=b if side=='R' else n-a
            pmf[k]+=weight
        for k in range(1,n):
            expected=(1-r)*r**(n-1-k)/(1-r**(n-1))
            assert pmf[k]==expected,(n,p,k,pmf[k],expected)
            checks+=1
        assert sum(pmf.values())==1;checks+=1
# Pathwise exact range/cover equivalence for all short paths (independent of p).
for t in range(1,13):
    for inc in product((-1,1),repeat=t):
        x=0;lo=hi=0; first={}
        for s,step in enumerate(inc,1):
            x+=step;lo=min(lo,x);hi=max(hi,x)
            if hi-lo not in first:first[hi-lo]=s
        for n in range(3,min(8,t+2)):
            if n-1 not in first:continue
            visit=set();y=0;visit.add(y)
            tt=None;lk=None
            for i,s in enumerate(inc,1):
                y=(y+s)%n;visit.add(y)
                if len(visit)==n:
                    tt=i;lk=y;break
            assert tt==first[n-1]
            checks+=1
# Deterministically construct some long biased-walk prefixes and check that
# sufficiently large cycles have last deficit equal to the (observed) global min.
import random
rng=random.Random(261015115)
for _ in range(24):
    steps=[1 if rng.random()<0.75 else -1 for _ in range(40000)]
    pos=0; lo=0;hi=0; mins=[0]; range_hits={};hitting={}
    for i,step in enumerate(steps,1):
        pos+=step
        lo=min(lo,pos);hi=max(hi,pos)
        hitting.setdefault(pos,i)
        range_hits.setdefault(hi-lo,i)
    j=-lo
    for n in (100,250,500,1000,2000):
        if n-1-j<1:continue
        assert range_hits[n-1]==hitting[n-1-j],(j,n)
        assert (n-1-j)%n==n-1-j
        checks+=2
print('PASS exact finite assertions:',checks)
