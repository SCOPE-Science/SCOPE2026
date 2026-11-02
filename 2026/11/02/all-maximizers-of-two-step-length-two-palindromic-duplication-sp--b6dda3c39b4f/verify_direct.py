#!/usr/bin/env python3
"""Finite checks of exact-two length-two palindromic and reverse-complement duplication spheres.
Run: python3 verify_direct.py
"""
from itertools import product

def expand(s, start, involution=None):
    pair = s[start:start+2]
    copy = pair[::-1] if involution is None else tuple(involution[a] for a in pair[::-1])
    return s[:start+2] + copy + s[start+2:]

def descendants(s, involution=None):
    n=len(s)
    return {expand(expand(s,i,involution),j,involution)
            for i in range(n-1) for j in range(n+1)}

def proper(s, involution=None):
    if involution is None:
        return all(s[i] != s[i+1] for i in range(len(s)-1))
    return all(s[i+1] != involution[s[i]] for i in range(len(s)-1))

def maximum(n):
    return (n*n+5*n-8)//2

cases=((2,10),(3,8),(4,6),(5,4))
for q,limit in cases:
    for n in range(2,limit+1):
        winner_count=0
        for s in product(range(q),repeat=n):
            actual=len(descendants(s))
            predicted=proper(s)
            assert (actual==maximum(n))==predicted, (q,n,s,actual)
            winner_count+=predicted
        assert winner_count==q*(q-1)**(n-1)
        print(f'PAL q={q} n={n}: {winner_count} maximizing words, bound={maximum(n)}, all classified')

for q,limit in ((2,10),(4,6)):
    inv=tuple(q-1-a for a in range(q))
    for n in range(2,limit+1):
        winners=0
        for s in product(range(q),repeat=n):
            d=len(descendants(s,inv))
            p=proper(s,inv)
            assert (d==maximum(n))==p, (q,n,s,d)
            winners+=p
        assert winners==q*(q-1)**(n-1)
        print(f'RC q={q} n={n}: {winners} maximizing words, all classified')
print('DIRECT FINITE CHECKS PASSED')
