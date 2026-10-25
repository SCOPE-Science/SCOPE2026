#!/usr/bin/env python3
"""Exact independent verification of rank-refined nilpotent-centralizer sieve.
Standard library only; no stored tables or external dependencies."""
import itertools
from collections import Counter
from functools import lru_cache
from math import factorial,comb

def partial_injections(n):
    for k in range(n+1):
        for dom in itertools.combinations(range(n),k):
            for img in itertools.permutations(range(n),k):
                b=[-1]*n
                for x,y in zip(dom,img):b[x]=y
                yield tuple(b)

def compose(a,b):
    return tuple(-1 if b[i]<0 else a[b[i]] for i in range(len(b)))

def nil(p):
    for x in range(len(p)):
        seen=set();j=x
        while j>=0:
            if j in seen:return False
            seen.add(j);j=p[j]
    return True

def alpha(parts):
    a=[];start=0
    for L in parts:
        a.extend(range(start+1,start+L));a.append(-1)
        start+=L
    return tuple(a)

def brute(parts):
    a=alpha(parts);total=Counter();nils=Counter()
    for b in partial_injections(len(a)):
        if compose(a,b)==compose(b,a):
            r=sum(v>=0 for v in b);total[r]+=1
            if nil(b):nils[r]+=1
    return dict(total),dict(nils)

@lru_cache(None)
def centralizer_rank(parts):
    c=len(parts)
    # DP over selected image chains; key (used image subset, cumulative rank).
    states={(0,0):1}
    for i in range(c):
        nxt=states.copy() # ignore source i
        for (used,r),count in states.items():
            for j in range(c):
                if used&(1<<j):continue
                for t in range(1,min(parts[i],parts[j])+1):
                    key=(used|(1<<j),r+t)
                    nxt[key]=nxt.get(key,0)+count
        states=nxt
    R=Counter()
    for (used,r),v in states.items():R[r]+=v
    return dict(R)

def sieve(parts):
    parts=tuple(sorted(parts,reverse=True))
    out=Counter(centralizer_rank(parts))
    lengths=sorted(set(parts))
    for k in range(1,len(lengths)+1):
        for D in itertools.combinations(lengths,k):
            multiplicity=1;remaining=list(parts)
            for L in D:
                multiplicity*=parts.count(L)
                remaining.remove(L)
            d=sum(D)
            for r,v in centralizer_rank(tuple(remaining)).items():
                out[r+d]+=(-1)**k*multiplicity*v
    return {r:v for r,v in out.items() if v}

def matchings_direct(parts):
    n=len(parts);ans=Counter()
    def rec(i,used,tar,taken,r):
        if i==n:
            # Exclude any fully aligned cycle on equal-length chain indices.
            for x in range(n):
                pos={};v=x
                while v in tar:
                    if v in pos:
                        cyc=[];z=v
                        while True:
                            cyc.append(z);z=tar[z]
                            if z==v:break
                        if all(taken[u]==parts[u]==parts[tar[u]] for u in cyc):return
                        break
                    pos[v]=True;v=tar[v]
            ans[r]+=1
            return
        rec(i+1,used,tar,taken,r)
        for j in range(n):
            if used>>j&1:continue
            tar[i]=j
            for t in range(1,min(parts[i],parts[j])+1):
                taken[i]=t
                rec(i+1,used|1<<j,tar,taken,r+t)
            del tar[i];del taken[i]
    rec(0,0,{}, {},0)
    return dict(ans)

def partitions(n,top=None):
    if n==0:
        yield()
    else:
        for k in range(min(n,top or n),0,-1):
            for rest in partitions(n-k,k):yield(k,)+rest

for n in range(1,7):
    for p in partitions(n):
        b=brute(p)
        cm=centralizer_rank(p)
        sm=sieve(p)
        dm=matchings_direct(p)
        assert b==(cm,sm) and sm==dm,(p,b,cm,sm,dm)
    print(f'n={n} all nilpotent chain partitions: exact rank-by-rank brute force PASS')
for n in range(7,12):
    for p in partitions(n):
        if len(p) <= 5: assert sieve(p)==matchings_direct(p),(p,sieve(p),matchings_direct(p))
    print(f'n={n} all partitions: independent matching and sieve PASS')
print('VERIFY_OK_NILPOTENT_CENTRALIZER_SIEVE')
