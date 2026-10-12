#!/usr/bin/env python3
import itertools
from collections import Counter
from math import comb


def derangements(n):
    for p in itertools.permutations(range(n)):
        if all(p[i] != i for i in range(n)):
            yield p


def c2_count(p):
    n=len(p)
    return sum(1 for i in range(n) if i < p[i] and p[p[i]] == i)


def adjacent_in_cycle(p,i,j):
    return p[i] == j or p[j] == i


def subfactorial(n):
    if n == 0: return 1
    if n == 1: return 0
    d0,d1=1,0
    for k in range(2,n+1):
        d0,d1=d1,(k-1)*(d1+d0)
    return d1

subset_checks=0
matching_checks=0
aggregate_checks=0
cycle_type_checks=0
for n in range(3,9):
    ders=list(derangements(n))
    dn=subfactorial(n)
    assert len(ders)==dn
    aggregate=[0]*(n+1)
    got_by_matching=[[0]*(n+1) for _ in ders]
    # Directly test every subset F of every perfect matching M_p.
    for mask in range(1<<n):
        selected=tuple(i for i in range(n) if (mask>>i)&1)
        U=tuple(i for i in range(n) if not ((mask>>i)&1))
        counts=Counter(tuple(p[i] for i in selected) for p in ders)
        for idx,p in enumerate(ders):
            direct=(counts[tuple(p[i] for i in selected)]==1)
            predicted=(len(U)<=1) or (len(U)==2 and adjacent_in_cycle(p,U[0],U[1]))
            assert direct==predicted, (n,p,selected,U,direct,predicted)
            subset_checks += 1
            if direct:
                k=len(selected)
                aggregate[k] += 1
                got_by_matching[idx][k] += 1
    # Per-matching enumerator.
    for idx,p in enumerate(ders):
        t=c2_count(p)
        expected=[0]*(n+1)
        expected[n]=1
        expected[n-1]=n
        expected[n-2]=n-t
        assert got_by_matching[idx]==expected, (n,p,got_by_matching[idx],expected)
        matching_checks += 1
        mins=sum(1 for omitted in itertools.combinations(range(n),2) if adjacent_in_cycle(p,*omitted))
        assert mins==n-t
        cycle_type_checks += 1
    # Aggregate formula.
    expected=[0]*(n+1)
    expected[n]=dn
    expected[n-1]=n*dn
    expected[n-2]=n*dn-comb(n,2)*subfactorial(n-2)
    assert aggregate==expected, (n,aggregate,expected)
    aggregate_checks += 1

print('VERIFY_OK '
      f'n_range=3..8 subset_checks={subset_checks} '
      f'matching_checks={matching_checks} aggregate_checks={aggregate_checks} '
      f'cycle_type_checks={cycle_type_checks} max_order=16')
