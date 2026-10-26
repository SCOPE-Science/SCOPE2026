#!/usr/bin/env python3
"""Finite checks for exact type-count and overlap-matching inequalities."""
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from random import Random

@lru_cache(None)
def geometry(n):
    pairs = list(combinations(range(n), 2))
    triples = list(combinations(range(n), 3))
    ids = {e: i for i, e in enumerate(pairs)}
    masks = [sum(1 << ids[e] for e in combinations(t, 2)) for t in triples]
    four = [tuple(i for i, t in enumerate(triples) if set(t) <= set(q))
            for q in combinations(range(n), 4)]
    return pairs, triples, masks, four

def valid_old(n, h):
    return all(sum((h >> j) & 1 for j in q) < 4 for q in geometry(n)[3])

def overlap(n, h):
    triples = geometry(n)[1]
    ts = [t for j, t in enumerate(triples) if (h >> j) & 1]
    es = [(i, j) for i in range(len(ts)) for j in range(i+1, len(ts))
          if len(set(ts[i]) & set(ts[j])) == 2]
    return ts, es

def matching(m, edges):
    nbrs = [0]*m
    for i,j in edges:
        nbrs[i] |= 1 << j
        nbrs[j] |= 1 << i
    @lru_cache(None)
    def solve(mask):
        if mask == 0: return 0
        low = mask & -mask
        i = low.bit_length()-1
        ans = solve(mask ^ low)
        p = (mask ^ low) & nbrs[i]
        while p:
            bit = p & -p
            ans = max(ans, 1 + solve((mask ^ low) ^ bit))
            p ^= bit
        return ans
    return solve((1 << m)-1)

def type_polynomial(n, h):
    masks = [cl for j,cl in enumerate(geometry(n)[2]) if (h >> j) & 1]
    N = len(geometry(n)[0]); a = [0]*(N+1)
    for s in range(1 << N):
        if all((s & cl) != cl for cl in masks):
            a[s.bit_count()] += 1
    return a

def biased(pol, p):
    N=len(pol)-1
    return sum((v*p**i*(1-p)**(N-i) for i,v in enumerate(pol)),Fraction(0))

def bound(p, m, nu):
    return (1-p**3)**(m-2*nu)*(1-2*p**3+p**5)**nu

def run():
    samples = 0; eq = 0; strict = 0
    for n in range(3,6):
        for h in range(1 << len(geometry(n)[1])):
            if not valid_old(n,h): continue
            ts,ed=overlap(n,h)
            m=len(ts); nu=matching(m,ed)
            pol=type_polynomial(n,h)
            isolated_pair_components = len(ed) == nu and all(
                sum((i == a or i == b) for a,b in ed) <= 1
                for i in range(m))
            for p in (Fraction(1,3),Fraction(1,2),Fraction(2,3)):
                actual=biased(pol,p); estimate=bound(p,m,nu)
                assert actual >= estimate,(n,h,p,actual,estimate)
                assert (actual == estimate) == isolated_pair_components,(n,h,p)
            samples += 1;eq+=isolated_pair_components;strict+=not isolated_pair_components
    rng=Random(20261021)
    random_checks = 0
    n=6
    for _ in range(1000):
        h=sum((rng.randrange(100)<25)<<j for j in range(len(geometry(n)[1])))
        if not valid_old(n,h):continue
        ts,ed=overlap(n,h)
        m=len(ts);nu=matching(m,ed)
        pol=type_polynomial(n,h)
        iso=len(ed)==nu and all(sum(i in edge for edge in ed)<=1 for i in range(m))
        a=biased(pol,Fraction(1,2));b=bound(Fraction(1,2),m,nu)
        assert a>=b and ((a==b)==iso)
        random_checks += 1
        if random_checks==35: break
    assert random_checks==35
    for s in range(1,9):
        n=s+2
        # no brute force past n=6: directly enumerate clauses of a pencil
        p=Fraction(1,2)
        factor=(1-p)+p*(1-p*p)**s
        assert factor==Fraction(1,2)*(1+Fraction(3,4)**s)
        assert factor>=bound(p,s,s//2)
    print('ALL_CHECKS_PASS')
    print('complete_valid_base_hypergraphs_n3_to_n5',samples)
    print('matching_equality_base_cases',eq)
    print('strict_base_cases',strict)
    print('rational_biases_tested','1/3,1/2,2/3')
    print('n6_random_independent_base_cases',random_checks)
    print('pencil_formula_checks',8)

if __name__ == '__main__':
    run()
