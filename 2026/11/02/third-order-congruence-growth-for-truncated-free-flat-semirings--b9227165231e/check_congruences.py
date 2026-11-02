#!/usr/bin/env python3
"""Finite exact checks for congruences of truncated flat word semirings.

This program deals solely with mathematical combinatorial objects.
"""
from itertools import product
from math import comb


def words(n,k):
    return [tuple(x) for j in range(1,k+1) for x in product(range(n), repeat=j)]


def contains(u,v):
    # v is contiguous factor of u
    return any(u[j:j+len(v)] == v for j in range(len(u)-len(v)+1))


def count_lower_upsets(n,k):
    lower=words(n,k-1)
    top=list(product(range(n),repeat=k))
    masks=[sum((1<<j) for j,v in enumerate(lower) if contains(v,w)) for w in lower]
    topmask=[sum((1<<j) for j,v in enumerate(lower) if contains(w,v)) for w in top]
    counts={}
    subtotal=0
    for b in range(1<<len(lower)):
        if any(b&(1<<i) and masks[i] & ~b for i in range(len(lower))):
            continue
        forced=sum(bool(b&z) for z in topmask)
        subtotal+=1 << (len(top)-forced)
        m=sum(bool(b&(1<<i)) for i,w in enumerate(lower) if len(w)==k-1)
        counts[m]=counts.get(m,0)+(1<<(len(top)-forced))
    return subtotal,counts


def count_debruijn(n,k):
    if k==2:
        return sum(comb(n,m) * 2**((n-m)**2) for m in range(n+1))
    if k!=3: raise ValueError('Only k=2,3 supported')
    vertices=list(product(range(n),repeat=2))
    ans=0
    for b in range(1<<(n*n)):
        E={(i,j) for (i,j),z in zip(vertices,range(n*n)) if b & (1<<z)}
        # shorter letter included only when all its adjacent pairs belong to E
        free=sum(all((a,x) in E and (x,a) in E for a in range(n)) for x in range(n))
        internal=sum((i,j) in E and (j,l) in E for i,j,l in product(range(n),repeat=3))
        forced=2*n*len(E)-internal
        ans+=2**(free+n**3-forced)
    return ans


def check_direct(n,k):
    # Completely independent direct exhaustive checking of all prospective zero-classes.
    all_words=words(n,k)
    valid=0
    for mask in range(1<<len(all_words)):
        selected=[w for i,w in enumerate(all_words) if mask & (1<<i)]
        if all(not contains(w,u) or mask&(1<<i)
               for u in selected for i,w in enumerate(all_words)):
            valid+=1
    return valid


def main():
    for n,k in [(2,2),(3,2),(4,2),(2,3),(3,3),(2,4)]:
        a,by_m=count_lower_upsets(n,k)
        b=count_debruijn(n,k) if k<=3 else None
        c=check_direct(n,k) if sum(n**j for j in range(1,k+1))<=14 else None
        assert b is None or a==b,(n,k,a,b)
        assert c is None or a==c,(n,k,a,c)
        base=1<<(n**k)
        first=(n**(k-1)+n)*base//(1<<(2*n)) if 2*n<=n**k else None
        assert by_m[0]==base
        assert by_m[1]==first
        print('n=',n,'k=',k,'count=',a,'by_m=',by_m,
              'exact_formula=',b,'direct=',c,'first_correction=',first)
    # Pair-overlap statistic for the cubic correction, by direct arc enumeration.
    for n,k in [(2,3),(3,3),(4,3),(5,3),(2,4),(3,4),(2,5)]:
        from itertools import combinations
        V=list(product(range(n),repeat=k-1))
        expected=comb(len(V),2)+2*n*(len(V)-1)+3*n*(n-1)
        histogram={0:0,1:0,2:0}
        for u,v in combinations(V,2):
            e=sum(w[:-1] in (u,v) and w[1:] in (u,v)
                  for w in product(range(n),repeat=k))
            assert e<=2,(n,k,u,v,e)
            histogram[e]+=1
        actual=sum(2**e * t for e,t in histogram.items())
        assert expected==actual,(n,k,expected,actual,histogram)
        print('PAIR_CHECK n=',n,'k=',k,'histogram=',histogram,
              'weighted=',actual,'predicted=',expected)
    print('VERIFY_OK')

if __name__=='__main__': main()
