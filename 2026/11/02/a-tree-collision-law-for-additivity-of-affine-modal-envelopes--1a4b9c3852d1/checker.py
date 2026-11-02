#!/usr/bin/env python3
"""Exhaustive finite checks for the k-summand tree-envelope coincidence formula.
No sampling is used. This checker is independent of the proof's independent-choice argument.
"""
from itertools import product, permutations
from fractions import Fraction
from collections import Counter
from math import factorial


def subtrees(child):
    memo={}
    def rec(v):
        if v not in memo:
            memo[v]=(v,)+tuple(u for c in child[v] for u in rec(c))
        return memo[v]
    return tuple(rec(v) for v in range(len(child)))


def predicted(child,k):
    d=subtrees(child)
    z=Fraction(1)
    for v in range(len(child)):
        z*=Fraction(1+sum(len(d[c])**k for c in child[v]),len(d[v])**k)
    return z


def counted(child,k):
    d=subtrees(child);n=len(child)
    freq=Counter()
    for order in permutations(range(n)):
        minima=tuple(min(s,key=lambda u:order[u]) for s in d)
        freq[minima]+=1
    return Fraction(sum(f**k for f in freq.values()),factorial(n)**k)


def check_semantics(child,k):
    d=subtrees(child);n=len(child)
    allorders=list(permutations(range(n)))
    for perms in product(allorders,repeat=k):
        a=all(min(sum(p[u] for p in perms) for u in s)==sum(min(p[u] for u in s) for p in perms) for s in d)
        b=all(len({min(s,key=lambda u:p[u]) for p in perms})==1 for s in d)
        assert a==b


def run():
    totals=0
    for n in range(1,7):
        for parent in product(*(range(i) for i in range(1,n))):
            child=[[] for _ in range(n)]
            for i,p in enumerate(parent,1):child[p].append(i)
            for k in (2,3,4):
                assert predicted(child,k)==counted(child,k),(n,parent,k)
                totals+=1
            if n<=3:check_semantics(child,3)
        print('n=',n,'trees=',factorial(n-1),'k=2,3,4')
    print('ALL_CHECKS_OK',totals,'exact collision probabilities and direct semantics n<=3')
if __name__=='__main__':run()
