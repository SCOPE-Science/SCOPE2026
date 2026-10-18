#!/usr/bin/env python3
"""Exact two-exponent covers for symmetric-group permutation orders.

Use: python3 verify.py. Pure Python standard library, no downloaded tables.
Every integer calculation is exact. No extrapolation beyond KMAX.
"""
from functools import lru_cache
from itertools import combinations
from math import gcd, lcm

KMIN, KMAX = 3, 40

def primes_upto(n):
    return [p for p in range(2,n+1) if all(p % q for q in range(2, int(p**0.5)+1))]

def prime_powers(n):
    out=[]
    for p in primes_upto(n):
        x=p
        while x<=n:
            out.append((x,p))
            x*=p
    return sorted(out)

@lru_cache(None)
def permutation_orders(n):
    """Complete orders from all integer partitions, deduplicated inductively."""
    if n==0:
        return frozenset([1])
    return frozenset(lcm(c, t) for c in range(1,n+1)
                     for t in permutation_orders(n-c))

def all_divisors(n):
    """Generate divisors using trial division and exact exponent expansion."""
    factors=[]
    d=2
    while d*d<=n:
        if n%d==0:
            a=0
            while n%d==0:
                n//=d; a+=1
            factors.append((d,a))
        d += 1 if d==2 else 2
    if n>1:
        factors.append((n,1))
    out=[1]
    for p,a in factors:
        new=[]
        t=1
        for _ in range(a+1):
            new.extend(x*t for x in out)
            t*=p
        out=new
    return sorted(out)

def edge_residual(d, vertices, edges):
    """Least right cover from prime-power vertices and compatible edges."""
    residual=1
    for s,p in vertices:
        if d%s:
            residual=lcm(residual,s)
    for s,t in edges:
        if d%s or d%t:
            residual=lcm(residual,s,t)
    return residual

def check_case(n):
    O=sorted(permutation_orders(n))
    E=lcm(*range(1,n+1))
    assert lcm(*O)==E
    divisors=all_divisors(E)
    vertices=prime_powers(n)
    edges=[(a,b) for (a,p),(b,q) in combinations(vertices,2)
                 if p!=q and a+b<=n]
    # The first computation is directly over every permutation order.
    # The second uses only prime-power vertices and edges.
    best=E
    optimal=[]
    for d in divisors:
        from_orders=lcm(*(q for q in O if d%q))
        from_graph=edge_residual(d,vertices,edges)
        assert from_orders==from_graph, (n,d,from_orders,from_graph)
        score=max(d,from_orders)
        if score<best:
            best=score; optimal=[(d,from_orders)]
        elif score==best:
            optimal.append((d,from_orders))
    witness=min(tuple(sorted(x)) for x in optimal)
    assert all(witness[0]%q==0 or witness[1]%q==0 for q in O)
    # A bound below best cannot work: any right cover must be divisible
    # by the computed residual for its left member.
    assert all(max(d,lcm(*(q for q in O if d%q)))>=best for d in divisors)
    return n,best,witness,len(O),len(vertices),len(edges),len(divisors)


def main():
    print('Exact optimal two-exponent covers of element orders in S_n')
    print('n  B2(n)  witness=(d1,d2)  |orders| |P| |edges| tau(E)')
    cases=[]
    for k in range(KMIN,KMAX+1):
        r=check_case(k)
        cases.append(r)
        print('%2d %12d (%d,%d) %d %d %d %d'%(r[0],r[1],r[2][0],r[2][1],*r[3:]))
    assert len(cases)==38
    assert cases[0][:3]==(3,3,(2,3))
    assert cases[-1][:3]==(40,53542288800,(35959964040,53542288800))
    print('CASES',len(cases))
    print('ALL ORDER AND PRIME-POWER GRAPH CROSSCHECKS PASSED')

if __name__=='__main__':
    main()
