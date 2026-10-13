#!/usr/bin/env python3
"""Independent finite checks of a generator-census formula for monadic Gödel powers.
Only Python standard library; run: python3 verify.py.
"""
from itertools import product
from collections import Counter
from math import comb, factorial


def rank_capacity(r,n):
    weights = sorted((b.bit_count() for b in range(1 << r)), reverse=True)
    if n > len(weights):
        return -1
    return sum(weights[:n])


def minimum_rank(k,n):
    for r in range(0,k+n+2):
        if n <= (1<<r) and k-2 <= rank_capacity(r,n):
            return r
    raise AssertionError('search bound')


def count_formula(k,n,r):
    # Coefficient of z^n in the complete inclusion-exclusion generating function.
    if n > (1 << r):
        return 0
    ans=0
    for missing in range(k-1):
        alpha=k-1-missing
        coeff=[1]+[0]*n
        for mask in range(1 << r):
            term=alpha ** mask.bit_count()
            for degree in range(n,0,-1):
                coeff[degree] += coeff[degree-1]*term
        ans+=((-1)**missing)*comb(k-2,missing)*coeff[n]
    return factorial(n)*ans


def criterion(gens,k,n):
    codes=[];seen=set()
    for i in range(n):
        codes.append(tuple(int(g[i]>0) for g in gens))
        seen.update(g[i] for g in gens)
    return len(set(codes))==n and set(range(1,k-1)).issubset(seen)


def full_closure(gens,k,n):
    # Materialise closure under full pointwise lattice/Heyting signature and
    # genuinely global all/exists operators, not zero-signature shortcuts.
    zero=(0,)*n; one=(k-1,)*n
    have={zero,one}; todo=[]
    def add(x):
        if x not in have:
            have.add(x);todo.append(x)
    for g in gens:add(g)
    while todo:
        a=todo.pop()
        add((min(a),)*n);add((max(a),)*n)
        for b in tuple(have):
            add(tuple(min(x,y) for x,y in zip(a,b)))
            add(tuple(max(x,y) for x,y in zip(a,b)))
            add(tuple((k-1) if x<=y else y for x,y in zip(a,b)))
            add(tuple((k-1) if y<=x else x for x,y in zip(a,b)))
        if len(have)==k**n:
            return True
    return len(have)==k**n

cases=[(2,1,0),(2,2,1),(2,3,2),(2,4,2),
       (3,1,1),(3,2,1),(3,2,2),(3,3,2),(3,4,2),
       (4,1,1),(4,1,2),(4,2,1),(4,2,2),
       (5,1,2),(5,1,3),(5,2,1),(5,2,2)]
checks=0
for k,n,r in cases:
    total=0;direct_count=0;criter_count=0
    universe=list(product(range(k),repeat=n))
    for gens in product(universe,repeat=r):
        total+=1;cks=criterion(gens,k,n)
        dr=full_closure(gens,k,n)
        assert cks==dr, (k,n,r,gens,cks,dr)
        criter_count+=cks;direct_count+=dr
    expected=count_formula(k,n,r)
    assert expected==direct_count,(k,n,r,expected,direct_count)
    checks+=total
    print('PARAM',k,n,r,'tuples',total,'generating',expected)

# Entire formula independently enumerated via zero-code assignments, not term closure.
code_comparisons=0
for k in range(2,8):
  for r in range(0,5):
    for n in range(1,min(1<<r,5)+1):
        f=count_formula(k,n,r)
        brute=0
        for patterns in product(range(1<<r),repeat=n):
            if len(set(patterns))<n:continue
            weight=sum(mask.bit_count() for mask in patterns)
            ways=sum((-1)**h*comb(k-2,h)*(k-1-h)**weight for h in range(k-1))
            brute+=ways
        assert f==brute,(k,n,r,f,brute)
        assert (f>0)==(n <=1<<r and k-2<=rank_capacity(r,n))
        code_comparisons+=1

for k in range(2,18):
    for n in range(1,18):
        d=minimum_rank(k,n)
        assert n<=2**d and k-2<=rank_capacity(d,n)
        if d:
            assert n>2**(d-1) or k-2>rank_capacity(d-1,n)

print('VERIFY_OK direct_generation_tests',checks,'parameter_cases',len(cases),
      'independent_code_enumerations',code_comparisons,'rank_boundary_tests',16*17)
