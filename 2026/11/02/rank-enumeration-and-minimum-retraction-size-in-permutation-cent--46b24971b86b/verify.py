#!/usr/bin/env python3
"""Direct finite checks of rank enumerator for permutation-centralizer idempotents."""
from collections import Counter, defaultdict
from itertools import combinations, product
from math import comb, factorial

def partitions(n,low=1):
    if n==0:
        yield ()
    else:
        for k in range(low,n+1):
            for tail in partitions(n-k,k):
                yield (k,)+tail

def permutation(parts):
    s=list(range(sum(parts)))
    start=0
    for d in parts:
        for i in range(d):
            s[start+i]=start+(i+1)%d
        start+=d
    return tuple(s)

def expected(poly_partition):
    m=Counter(poly_partition); keys=sorted(m)
    out=defaultdict(int)
    for vals in product(*(range(m[d]+1) for d in keys)):
        k=dict(zip(keys,vals)); weight=sum(d*k[d] for d in keys)
        count=1
        for e in keys:
            phase=sum(d*k[d] for d in keys if e%d==0)
            count*=comb(m[e],k[e])*phase**(m[e]-k[e])
        out[weight]+=count
    return {rank:value for rank,value in out.items() if value}

def exact_min_rank(parts):
    m=Counter(parts)
    mins=[d for d in m if not any(e!=d and d%e==0 for e in m)]
    rank=sum(mins)
    count=1
    for d in mins: count*=m[d]*d**(m[d]-1)
    for e in m:
        if e not in mins:
            count*=sum(d for d in mins if e%d==0)**m[e]
    return rank,count

def all_idempotents(n):
    universe=range(n)
    for k in range(1,n+1):
        for roots in combinations(universe,k):
            other=[i for i in universe if i not in roots]
            for images in product(roots,repeat=n-k):
                f=list(range(n))
                for i,v in zip(other,images): f[i]=v
                yield k,tuple(f)

def independent_check(n):
    ids=list(all_idempotents(n))
    all_p=list(partitions(n))
    for parts in all_p:
        sig=permutation(parts)
        observed=Counter()
        for rank,f in ids:
            if all(f[sig[i]]==sig[f[i]] for i in range(n)):
                observed[rank]+=1
        want=expected(parts)
        assert dict(observed)==want,(n,parts,dict(observed),want)
        r,c=exact_min_rank(parts)
        assert min(want)==r and want[r]==c,(n,parts,r,c,want)
    weighted={r:0 for r in range(1,n+1)}
    for parts in all_p:
        m=Counter(parts)
        z=1
        for d,num in m.items(): z*=d**num*factorial(num)
        for rank,count in expected(parts).items():
            weighted[rank]+=factorial(n)//z*count
    right=Counter(len(p) for p in all_p)
    assert all(weighted[r]==factorial(n)*right[r] for r in range(1,n+1))
    print(f'n={n} types={len(all_p)} idempotents_tested_per_type={len(ids)} average_total={sum(right.values())} VERIFY_OK')

if __name__=='__main__':
    for n in range(1,9): independent_check(n)
    print('ALL_VERIFY_OK')
