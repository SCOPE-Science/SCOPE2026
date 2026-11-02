#!/usr/bin/env python3
"""Exhaustive direct read-pool checks for fixed-composition longest-read spectra."""
from collections import Counter, defaultdict
from itertools import combinations_with_replacement
from math import comb, factorial


def divisors(n):
    return [d for d in range(1,n+1) if n%d==0]


def mu(n):
    result=1
    p=2
    while p*p<=n:
        if n%p==0:
            n//=p
            if n%p==0: return 0
            result=-result
            while n%p==0: n//=p
        p+=1
    return -result if n>1 else result


def gcd_all(xs):
    from math import gcd
    r=0
    for x in xs: r=gcd(r,x)
    return r


def multinomial(xs):
    return factorial(sum(xs))//__import__('math').prod(factorial(x) for x in xs)


def primitive_necklaces(c):
    d=sum(c)
    return sum(mu(h)*multinomial([v//h for v in c])
               for h in divisors(gcd_all(c)))//d


def even_cycles(c):
    n=sum(c)
    return {d: primitive_necklaces([v//(n//d) for v in c])
            for d in divisors(n)
            if d%2==0 and all(v%(n//d)==0 for v in c)}


def theoretical(c,k):
    T=multinomial(c)
    cycles=even_cycles(c)
    all_poly=[1]+[0]*k
    unique_poly=[1]+[0]*k
    for d,mult in cycles.items():
        r=d//2
        for _ in range(mult):
            for polynomial, exponent in ((all_poly,1),(unique_poly,2)):
                for _ in range(exponent):
                    for j in range(k,r-1,-1):
                        polynomial[j]-=polynomial[j-r]
    def coeff(poly):
        return sum(poly[j]*comb(T+k-j-1,k-j) for j in range(k+1))
    return coeff(all_poly),coeff(unique_poly)


def compositions(n,q):
    if q==1:
        yield (n,)
    else:
        for j in range(n+1):
            for tail in compositions(n-j,q-1):
                yield (j,)+tail


def source_words(c):
    symbols='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if len(c)>len(symbols):raise ValueError('too many symbols')
    def walk(vec,prefix):
        if sum(vec)==0:
            yield prefix
            return
        for j in range(len(vec)):
            if vec[j]:
                nxt=list(vec);nxt[j]-=1
                yield from walk(nxt,prefix+symbols[j])
    return list(walk(c,''))


def direct(c,k):
    words=source_words(c)
    all_reads=sorted({u for word in words for u in (word[:-1],word[1:])})
    ids={u:i for i,u in enumerate(all_reads)}
    edges=[(ids[word[:-1]],ids[word[1:]]) for word in words]
    counts=defaultdict(int)
    for sample in combinations_with_replacement(range(len(words)),k):
        profile=[0]*len(all_reads)
        for idx in sample:
            a,b=edges[idx]
            profile[a]+=1;profile[b]+=1
        counts[tuple(profile)]+=1
    return len(counts),sum(v==1 for v in counts.values()),Counter(counts.values())


def necklace_period_check(c):
    unseen=set(source_words(c))
    cycle_counts=Counter()
    n=sum(c)
    while unseen:
        s=next(iter(unseen))
        orbit={s[i:]+s[:i] for i in range(n)}
        assert orbit<=unseen
        unseen.difference_update(orbit)
        if len(orbit)%2==0:cycle_counts[len(orbit)]+=1
    assert dict(cycle_counts)=={d:v for d,v in even_cycles(c).items() if v}


def main():
    cases=multisets=0
    for q,maximum,high_k in ((2,8,3),(3,6,3),(4,5,2)):
        for n in range(2,maximum+1):
            for c in compositions(n,q):
                if sum(v>0 for v in c)<2:continue
                necklace_period_check(c)
                for k in range(high_k+1):
                    actual,unique,distribution=direct(c,k)
                    predicted=theoretical(c,k)
                    assert (actual,unique)==predicted,(c,k,(actual,unique),predicted)
                    cases+=1
                    multisets+=comb(multinomial(c)+k-1,k)
    print(f'VERIFY_OK composition_pool_cases={cases} source_multisets={multisets} alphabets=2,3,4')
    for c in ((1,1),(2,2),(1,1,2),(2,2,2),(2,2,4),(1,1,1,1),(3,3,0)):
        print('content=',c,'even_orbits=',even_cycles(c),
              'profiles_uniques=',[theoretical(c,k) for k in range(4)])

if __name__=='__main__':main()
