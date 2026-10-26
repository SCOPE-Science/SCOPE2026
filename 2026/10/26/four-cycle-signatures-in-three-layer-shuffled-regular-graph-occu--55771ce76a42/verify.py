#!/usr/bin/env python3
"""Finite exact checks for a three-layer path-occupancy formula.
Run: python verify.py. Requires only the Python standard library.
"""
from fractions import Fraction
from itertools import combinations
from math import comb


def cycle_partitions(n, least=3):
    if n == 0:
        yield ()
    for k in range(least, n + 1):
        for rest in cycle_partitions(n-k, k):
            yield (k,)+rest


def neighbors_of_cycles(parts):
    neighborhoods = []
    offset=0
    for m in parts:
        for i in range(m):
            neighborhoods.append(frozenset((offset+(i-1)%m, offset+(i+1)%m)))
        offset += m
    return neighborhoods


def exact_direct(neighbors):
    # Independent finite stochastic reconstruction: after the first relabeling
    # there are two occupied sites, both with unit multiplicity. Enumerate
    # the uniformly relabeled second-layer support, and then all independent
    # incoming-pair choices at the third layer.
    d=len(neighbors)
    pairs=list(combinations(range(d), 2))
    n_pairs=len(pairs)
    zz=[]
    all_hits=0
    for support in pairs:
        sup=frozenset(support)
        zeros=frozenset(v for v in range(d) if not(neighbors[v] & sup))
        zz.append(len(zeros))
        for pair in pairs:
            if pair[0] in zeros and pair[1] in zeros:
                all_hits+=1
    avg=Fraction(sum(zz),n_pairs)
    variance=Fraction(sum((Fraction(k)-avg)**2 for k in zz),n_pairs)
    p3=Fraction(all_hits,n_pairs**2)
    return avg,variance,p3


def formula(neighbors):
    d=len(neighbors)
    assert d >= 7
    C=comb(d,2)
    c4=sum(1 for x in range(d) for y in range(x+1,d) if neighbors[x]==neighbors[y])//2
    numer=C*comb(d-4,2)+d*(d-4)+2*c4
    mean=Fraction((d-2)*(d-3),d-1)
    p3=Fraction(numer,C**2)
    variance=Fraction(2*numer,C)+mean-mean**2
    return mean,variance,p3,c4


def main():
    checks=0
    for d in range(7,18):
        for parts in cycle_partitions(d):
            N=neighbors_of_cycles(parts)
            expected=formula(N)
            got=exact_direct(N)
            assert got==expected[:3], (parts,got,expected)
            checks+=3
            assert expected[3]==parts.count(4),parts
            checks+=1
            # The exact extrema over all cycle decompositions are classified
            # by maximizing or minimizing the number of four-cycle components.
            qmax=max(q for q in range(d//4+1) if d-4*q==0 or d-4*q>=3)
            assert 0<=expected[3]<=qmax
            checks+=1
    c7=exact_direct(neighbors_of_cycles((7,)))
    c43=exact_direct(neighbors_of_cycles((3,4)))
    assert c7==(Fraction(10,3),Fraction(2,9),Fraction(4,21))
    assert c43==(Fraction(10,3),Fraction(26,63),Fraction(86,441))
    assert c43[2]-c7[2]==Fraction(2,441)
    assert c43[1]-c7[1]==Fraction(4,21)
    checks+=4
    print(f'PASS: {checks} exact rational assertions; all cycle partitions of d=7..17; seven-vertex sharp example.')
if __name__=='__main__':main()
