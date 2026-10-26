#!/usr/bin/env python3
"""Exact labeled-species enumeration of spider forests (independent of graph search)."""
from fractions import Fraction
from collections import Counter
from math import factorial

def spider_component_coefficients(max_n):
    # For a tree of size s rooted at its spider center, its legs are
    # unordered singletons (length 1) and ordered pairs (length 2).
    # Four-vertex paths have two possible roots, so count once.
    coeff={}
    for s in range(3,max_n+1):
        rooted=0
        for pairs in range((s-1)//2+1):
            singles=s-1-2*pairs
            if singles+pairs<2: continue
            rooted+=Fraction(factorial(s-1),factorial(singles)*factorial(pairs))
        labelled=s*rooted
        if s==4: labelled-=12
        coeff[s]=Fraction(labelled,factorial(s))
    return coeff

def all_spider_forests(max_n):
    h=spider_component_coefficients(max_n)
    f=[Counter() for _ in range(max_n+1)]
    f[0][0]=Fraction(1)
    # x F'(x,z)=F(x,z) x H'(x,z): recurrence in x,
    # weight of every tree component on s vertices is z^(s-1).
    for n in range(1,max_n+1):
        for s in range(3,n+1):
            for edges,num in f[n-s].items():
                f[n][edges+s-1]+=Fraction(s,n)*h[s]*num
    return f

def result(n,f):
    p=Counter()
    if n%3==0:
        blocks=n//3
        p[2*blocks]+=Fraction(factorial(n),2**blocks*factorial(blocks))
    for edges,coefficient in f[n-1].items():
        p[edges]+=factorial(n)*coefficient
    assert all(val.denominator==1 for val in p.values())
    return dict(sorted((k,int(v)) for k,v in p.items() if v))

if __name__=='__main__':
    f=all_spider_forests(12)
    for n in range(3,13):
        poly=result(n,f)
        print(f'n={n} minimal_total_domination={poly} total={sum(poly.values())}')
