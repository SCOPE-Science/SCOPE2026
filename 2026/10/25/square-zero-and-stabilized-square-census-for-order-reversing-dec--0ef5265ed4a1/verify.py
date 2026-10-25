#!/usr/bin/env python3
"""Independent exhaustive small-chain check of a width/height square dichotomy."""
from itertools import combinations, combinations_with_replacement
from collections import Counter
from math import comb

def zero_or_composition(f,g):
    return {x:g[f[x]] for x in f if f[x] in g}

def count(n):
    obs=Counter(); total=0
    for w in range(1,n+1):
        for domain in combinations(range(1,n+1),w):
            d=domain[0]
            for vals in combinations_with_replacement(range(1,d+1),w):
                f=dict(zip(domain,reversed(vals)))
                assert all(f[x]<=x for x in domain)
                f2=zero_or_composition(f,f)
                f3=zero_or_composition(f2,f)
                assert f3==f2
                assert zero_or_composition(f2,f2)==f2
                assert not f2 or set(f2.values())=={d}
                assert (not f2)==(f[d]<d)
                h=len(set(vals))
                obs[(w,h,int(bool(f2)))] +=1
                total +=1
    nonzero=0; zero=0
    for w in range(1,n+1):
        for h in range(1,w+1):
            strong=comb(w-1,h-1)*comb(n,w+h-1) if w+h-1<=n else 0
            weak=comb(w-1,h-1)*comb(n,w+h) if w+h<=n else 0
            assert obs[(w,h,1)]==strong,(n,w,h,obs[(w,h,1)],strong)
            assert obs[(w,h,0)]==weak,(n,w,h,obs[(w,h,0)],weak)
            nonzero+=strong;zero+=weak
    assert total==nonzero+zero
    return n,total,nonzero,zero
if __name__=='__main__':
    for n in range(1,10):
        print('CHAIN',*count(n))
    print('VERIFY_OK')
