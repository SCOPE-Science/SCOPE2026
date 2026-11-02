#!/usr/bin/env python3
"""Finite sanity checks for a structural theorem on 2,4-distance codes.

The infinite proof is mathematical and does not depend on this script.
"""
from itertools import combinations, product
from math import comb


def code(center, alternative):
    n = len(center)
    words = [tuple(center)]
    for i,j in combinations(range(n),2):
        x=list(center)
        x[i]=alternative[i]; x[j]=alternative[j]
        words.append(tuple(x))
    return frozenset(words)


def distance(x,y):
    return sum(a!=b for a,b in zip(x,y))


def check_code(c,n):
    assert len(c)==1+comb(n,2)
    for x,y in combinations(c,2):
        assert distance(x,y) in (2,4)
    centers=[x for x in c if all(distance(x,y)==2 for y in c if x!=y)]
    assert len(centers)==1
    return centers[0]


def check_injectivity(q,n):
    profiles={}
    for center in product(range(q),repeat=n):
        opts=[[v for v in range(q) if v!=center[i]] for i in range(n)]
        for alternative in product(*opts):
            c=code(center,alternative)
            assert len(c)==1+comb(n,2)
            h=tuple(sorted(c))
            assert h not in profiles
            profiles[h]=(center,alternative)
    assert len(profiles)==(q*(q-1))**n
    for c in profiles:
        check_code(c,n)
    print(f'q={q} n={n} injective={(q*(q-1))**n} all_size={1+comb(n,2)} all_valid=yes unique_center=yes')


def check_large(q,n):
    center=tuple((7*i+3)%q for i in range(n))
    alt=tuple((v+1)%q for v in center)
    c=code(center,alt)
    assert check_code(c,n)==center
    print(f'q={q} n={n} constructed_size={len(c)} all_distances_in_2_4=yes unique_center=yes')


if __name__=='__main__':
    for q,n in [(2,5),(3,4),(3,5),(4,4)]:
        check_injectivity(q,n)
    for q,n in [(3,17),(4,17),(3,24),(4,24)]:
        check_large(q,n)
