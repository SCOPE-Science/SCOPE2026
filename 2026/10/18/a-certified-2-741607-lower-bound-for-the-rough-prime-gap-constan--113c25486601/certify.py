#!/usr/bin/env python3
"""Exact CRT enumeration and a rational lower certificate for a prime-gap sieve constant.

Python 3.9+ standard library only.  Computes finite local terms, not the infinite tail.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from math import prod

def primes_below(n):
    sieve = bytearray(b'\x01') * n
    if n>0: sieve[0] = 0
    if n>1: sieve[1] = 0
    for p in range(2,int(n**0.5)+1):
        if sieve[p]: sieve[p*p:n:p]=b'\x00'*len(sieve[p*p:n:p])
    return [i for i in range(2,n) if sieve[i]]

def omega_dp(h):
    assert h >= 4 and h%2==0
    offsets=range(2,h,2)
    state={(1<<(h//2-1))-1: 1}
    for p in primes_below(h):
        if p==2: continue  # p=2: endpoints force odd b; every odd interior offset is sieved.
        covers=Counter()
        for b in range(p):
            if b==0 or (b+h)%p==0: continue
            covered=sum((1<<j) for j,i in enumerate(offsets) if (b+i)%p==0)
            covers[covered]+=1
        new={}
        for survivor,count in state.items():
            for covered,mult in covers.items():
                nxt=survivor & ~covered
                new[nxt]=new.get(nxt,0)+count*mult
        state=new
    return state.get(0,0)

def omega_independent_ie(h,B=13):
    # Independent inclusion-exclusion for the primes > B after CRT residues for <= B.
    ps=[p for p in primes_below(h) if p>2]
    small=[p for p in ps if p<=B]
    large=[p for p in ps if p>B]
    offsets=list(range(2,h,2))
    full=(1<<len(offsets))-1
    dist={full:1}
    for p in small:
        masks=Counter()
        for b in range(p):
            if b==0 or (b+h)%p==0: continue
            cover=sum((1<<j) for j,i in enumerate(offsets) if (b+i)%p==0)
            masks[cover]+=1
        updated={}
        for mask,n in dist.items():
            for cover,k in masks.items():
                surviving=mask & ~cover
                updated[surviving]=updated.get(surviving,0)+n*k
        dist=updated
    @lru_cache(maxsize=None)
    def count_large(mask):
        out=0; sub=mask
        while True:
            chosen=[offsets[j] for j in range(len(offsets)) if sub & (1<<j)]
            count=1
            for p in large:
                bad={0,h%p}
                bad.update(x%p for x in chosen)
                count*=p-len(bad)
            out += -count if sub.bit_count()%2 else count
            if sub==0: break
            sub=(sub-1)&mask
        return out
    return sum(n*count_large(mask) for mask,n in dist.items())

KNOWN={4:1,6:2,8:2,10:2,12:8,14:58,16:12,18:376,
       20:1440,22:2622,24:48868,26:7682,28:5664,30:154220,
       32:833688,34:1075458,36:620632,38:7381190,
       40:10176048,42:363563276,44:5319950268,
       46:3066631938,48:270657148848,50:101307938184,
       52:25051650260,54:4828555093560,56:952248263928,
       58:747162295398,60:49562298435088,
       62:673737239242910,64:870323053429248}

def main():
    assert list(KNOWN)==list(range(4,65,2))
    summ=Fraction(0)
    for h, expected in KNOWN.items():
        result=omega_dp(h)
        assert result==expected, (h,result,expected)
        if h<=44:
            independent=omega_independent_ie(h)
            assert independent==expected, ('inclusion-exclusion',h,independent,expected)
        den=prod(p-2 for p in primes_below(h) if p>2)
        summ+=Fraction(result,den)
        print(f'{h} {result}',flush=True)
    assert summ==Fraction(61370211356863231369,29555095284933631875)
    print('R64=',summ)
    # Rigorous integer-floor lower approximation for the finite prime product.
    scale=10**18
    s2_floor=2*scale
    ps=[p for p in primes_below(1000001) if p>2]
    for p in ps:
        s2_floor=s2_floor*((p-1)**2-1)//((p-1)**2)
    assert len(ps)==78497, len(ps)
    assert s2_floor==1320323721179642234, s2_floor
    # Bernoulli bound for all omitted primes: product >=1 - sum 1/(p-1)^2.
    # For p>1,000,000, sum is <= sum_{n>=1,000,000} 1/n^2 <= 1/999999.
    lower=summ*Fraction(s2_floor,scale)*Fraction(999998,999999)
    assert lower>Fraction(2741607,10**6), (float(lower),'insufficient')
    print('rigorous rational bound=',lower)
    print('rigorous bound decimal=',format(float(lower),'.13f'))
    print('SUCCESS: c > 2.741607; no conditional assumption is used in the constant bound')
if __name__=='__main__':main()
