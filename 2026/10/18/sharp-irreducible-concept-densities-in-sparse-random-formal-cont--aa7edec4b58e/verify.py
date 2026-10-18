#!/usr/bin/env python3
"""Independent finite checks of irreducible-concept proxies in binary contexts.

Run: python3 verify.py
Only Python's standard library is needed. Every context is independently
expanded into its closed extents; irreducibles are counted by lattice covers.
"""
from itertools import product
from fractions import Fraction
from math import comb
from random import Random


def join_irreducible_count(rows, nattr):
    nobj = len(rows)
    extents = set()
    for mask in range(1 << nobj):
        intent = (1 << nattr) - 1
        for g in range(nobj):
            if mask & (1 << g):
                intent &= rows[g]
        extent = 0
        for g in range(nobj):
            if rows[g] & intent == intent:
                extent |= 1 << g
        extents.add(extent)
    if not extents:
        raise AssertionError('empty lattice')
    least = min(extents, key=int.bit_count)
    answer = 0
    for x in extents:
        if x == least:
            continue
        smaller = [y for y in extents if y != x and (y & x) == y]
        maximal = [y for y in smaller if not any(
            z != y and (z & x) == z and (y & z) == y
            for z in smaller)]
        answer += len(maximal) == 1
    return answer


def transpose(rows, nattr):
    return tuple(sum(1 << g for g,r in enumerate(rows) if r & (1 << a))
                 for a in range(nattr))


def local_proxy(rows, nattr):
    high = sum(int(r.bit_count() >= 2) for r in rows)
    singleton_columns = 0
    for a in range(nattr):
        single = sum(int(r == 1 << a) for r in rows)
        higher = sum(int(bool(r & 1 << a) and r.bit_count() >= 2) for r in rows)
        singleton_columns += int(single >= 1 and higher <= 1)
    return high + singleton_columns


def four_cycles(rows):
    total = 0
    for i in range(len(rows)):
        for j in range(i):
            c = (rows[i] & rows[j]).bit_count()
            total += c * (c-1) // 2
    return total


def expected_local_proxy(nobj, nattr, p):
    # Exact finite expectation for rational edge probability p.
    u = p * (1-p)**(nattr-1)
    v = p * (1-(1-p)**(nattr-1))
    high = 1-(1-p)**nattr - nattr*p*(1-p)**(nattr-1)
    single = (1-v)**nobj - (1-p)**nobj + nobj*v*((1-v)**(nobj-1)-(1-p)**(nobj-1))
    return nobj*high + nattr*single


def test_one(rows, nattr):
    nc = four_cycles(rows)
    j = join_irreducible_count(rows,nattr)
    pj = local_proxy(rows,nattr)
    assert abs(j-pj) <= 4*nc+2, (rows,nattr,j,pj,nc)
    cols=transpose(rows,nattr)
    mi = join_irreducible_count(cols,len(rows))
    pm = local_proxy(cols,len(rows))
    assert abs(mi-pm) <= 4*nc+2,(rows,nattr,mi,pm,nc)
    return j,pj,mi,pm,nc


def main():
    contexts=0
    squarefree=0
    exact_expected=0
    for nobj,nattr in ((2,2),(2,3),(3,2),(3,3),(3,4),(4,3),(4,4)):
        sums=[0,0,0,0]
        for rows in product(range(1<<nattr),repeat=nobj):
            j,pj,mi,pm,nc=test_one(rows,nattr)
            contexts+=1
            squarefree+=(nc==0)
            for i,v in enumerate((j,pj,mi,pm)):sums[i]+=v
        if nobj<=3 and nattr<=3:
            exact_j=Fraction(sums[1],2**(nobj*nattr))
            exact_m=Fraction(sums[3],2**(nobj*nattr))
            assert exact_j==expected_local_proxy(nobj,nattr,Fraction(1,2))
            assert exact_m==expected_local_proxy(nattr,nobj,Fraction(1,2))
            exact_expected+=2
    rng=Random(20261014)
    for nobj,nattr in ((5,6),(6,6),(6,7)):
        for _ in range(500):
            rows=tuple(sum((1<<a) for a in range(nattr) if rng.random()<.23)
                       for _ in range(nobj))
            test_one(rows,nattr)
    print('VERIFY_OK',contexts,'exhaustive contexts;',squarefree,
          'square-free contexts;',exact_expected,'exact expectation identities;',
          1500,'additional random contexts; both lattice-dual proxies')

if __name__=='__main__':main()
