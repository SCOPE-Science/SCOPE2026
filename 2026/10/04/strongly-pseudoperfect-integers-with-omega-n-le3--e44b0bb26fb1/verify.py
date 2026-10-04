#!/usr/bin/env python3
from math import isqrt

def factor_mult(n):
    x=n
    out=[]
    p=2
    while p*p<=x:
        while x%p==0:
            out.append(p); x//=p
        p += 1 if p==2 else 2
    if x>1: out.append(x)
    return out

def divisors(n):
    ds=[]
    for d in range(1,isqrt(n)+1):
        if n%d==0:
            ds.append(d)
            if d*d!=n:
                ds.append(n//d)
    return sorted(ds)

def strongly_pseudoperfect(n):
    ds=divisors(n)
    seen=set()
    weights=[]
    for d in ds:
        if d in seen: continue
        e=n//d
        seen.add(d); seen.add(e)
        weights.append(d if d==e else d+e)
    target=2*n
    possible={0}
    for w in weights:
        possible |= {s+w for s in list(possible) if s+w<=target}
    return target in possible

def main():
    # Exact small-shape inequalities.
    for p in [2,3,5,7,11,13]:
        assert 1+p < 2*p
        assert 1+p+p*p < 2*p*p
        assert 1+p+p*p+p**3 < 2*p**3

    # p^2 q abundant candidates are exactly these for a broad prime range.
    primes=[2,3,5,7,11,13,17,19,23,29,31,37,41,43]
    cand=[]
    for p in primes:
        for q in primes:
            if p==q: continue
            n=p*p*q
            sigma=(p*p+p+1)*(q+1)
            if sigma>=2*n:
                cand.append(n)
    assert sorted(set(cand)) == [12,18,20,28]
    assert not strongly_pseudoperfect(12)
    assert not strongly_pseudoperfect(18)
    assert not strongly_pseudoperfect(20)
    assert strongly_pseudoperfect(28)

    # Regression enumeration.
    low=[]
    spp=[]
    for n in range(1,10001):
        if strongly_pseudoperfect(n):
            spp.append(n)
            if len(factor_mult(n))<=3:
                low.append(n)
    assert low == [6,28]
    assert strongly_pseudoperfect(36)
    assert len(factor_mult(36))==4
    assert sum(divisors(6))==12
    assert sum(divisors(28))==56
    assert sum(divisors(36))==91

    print("VERIFY_OK")
    print("omega_le_3=[6,28]")
    print("sharp_nonperfect_witness=36")
    print("enumeration_limit=10000")
    print("first_terms=" + ",".join(map(str,spp[:12])))

if __name__=="__main__":
    main()
