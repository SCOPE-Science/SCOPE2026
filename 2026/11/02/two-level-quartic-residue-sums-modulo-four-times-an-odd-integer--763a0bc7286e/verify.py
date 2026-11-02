#!/usr/bin/env python3
"""Exact finite corroboration of the quartic subgroup residue-sum law."""
from collections import Counter
from math import gcd


def distinct_prime_factors(n):
    out = []
    d = 2
    while d*d <= n:
        if n%d == 0:
            out.append(d)
            while n%d == 0:
                n//=d
        d += 1 if d == 2 else 2
    if n>1:
        out.append(n)
    return out


def check(q):
    m=4*q
    e=2*q-1
    roots=[x for x in range(1,m,2) if x*x%m==e]
    assert all(gcd(x,m)==1 for x in roots)
    groups={frozenset((1,x,e,(e*x)%m)) for x in roots}
    assert all(len(g)==4 for g in groups)
    good=all(p%4==1 for p in distinct_prime_factors(q))
    expected=(2**len(distinct_prime_factors(q))) if good else 0
    assert len(groups)==expected,(q,expected,len(groups))
    sums=Counter(map(sum,groups))
    if good:
        assert sums=={m:expected//2,2*m:expected//2},(q,sums)
        for g in groups:
            assert m-1 not in g
            gen=next(x for x in g if x*x%m==e)
            paired=frozenset((1,(gen+2*q)%m,e,(e*(gen+2*q))%m))
            assert paired in groups and paired!=g and sum(paired)==3*m-sum(g)
    else:
        assert not sums
    return len(groups)


def main():
    total=0
    subgroups=0
    absent=0
    for q in range(3,2001,2):
        subgroups+=check(q)
        total+=1
        if not all(p%4==1 for p in distinct_prime_factors(q)):
            absent+=1
    print(f'VERIFY_OK odd_q=3..1999 cases={total} empty_cases={absent} subgroups={subgroups} exact_CRT_count=PASS exact_two_level_sums=PASS pairing=PASS no_minus_one=PASS finite_only=YES')

if __name__=='__main__':
    main()
