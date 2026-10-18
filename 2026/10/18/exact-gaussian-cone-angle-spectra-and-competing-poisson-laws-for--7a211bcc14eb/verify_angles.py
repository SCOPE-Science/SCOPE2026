#!/usr/bin/env python3
"""Exact finite normal-fan combinatorics of graphical zonotopes.
All orientations are encoded as signs of existing edges in a total vertex order.
"""
from itertools import permutations
from collections import Counter, defaultdict
from fractions import Fraction
from math import factorial, comb


def analytic_counts(n, k):
    out = {}
    for s in range(k + 1):
        numerator = sum((-1)**(t-s) * comb(t,s) * comb(k,t) * 2**t * factorial(n-t) for t in range(s,k+1))
        assert numerator % 2**s == 0
        out[s] = numerator // 2**s
    return out


def exact_moments(n, k):
    nfact = factorial(n)
    return (sum(Fraction(comb(k,s) * 2**s * factorial(n-s), nfact) for s in range(k+1)),
            sum(Fraction(comb(k,s) * (-1)**s * factorial(n-s), nfact) for s in range(k+1)))


def test(n,k):
    pairs = [(2*i, 2*i+1) for i in range(k)]
    deleted = {tuple(sorted(e)) for e in pairs}
    edges = [(u,v) for u in range(n) for v in range(u+1,n) if (u,v) not in deleted]
    orientations = defaultdict(list)
    Js=Counter()
    for perm in permutations(range(n)):
        pos={v:i for i,v in enumerate(perm)}
        j=sum(abs(pos[u]-pos[v])==1 for u,v in pairs)
        Js[j]+=1
        orientation=tuple(pos[u]<pos[v] for u,v in edges)
        orientations[orientation].append((perm,j))
    profile=Counter()
    for configs in orientations.values():
        sz=len(configs)
        j_set={j for _,j in configs}
        assert len(j_set)==1, (n,k,j_set)
        j=next(iter(j_set))
        assert sz==2**j, (n,k,configs)
        profile[j]+=1
    formula = analytic_counts(n,k)
    assert formula == {i: profile[i] for i in range(k+1)}, (n,k,profile,formula)
    a2, a_half=exact_moments(n,k)
    assert len(orientations) == factorial(n)*a_half
    collide=sum(Fraction(len(xs)**2,factorial(n)**2) for xs in orientations.values())
    assert collide == a2 / factorial(n)
    moments_by_perms = sum(Fraction(2**s*j,factorial(n)) for s,j in Js.items())
    assert moments_by_perms == a2
    return n,k,len(orientations),str(collide),dict(profile)

if __name__=='__main__':
    cases=0
    for n in range(2,9):
        for k in range(0,n//2+1):
            ans=test(n,k); cases+=1
            print('PASS',*ans)
    print('ALL PASS,',cases,'exact test pairs')
