#!/usr/bin/env python3
"""Exact finite checks for rankwise noncofacial pairs in simplex products."""
from itertools import combinations
from math import comb


def subsets(n):
    return [frozenset(s) for r in range(1,n+1)
            for s in combinations(range(n),r)]


def faces(p,q):
    return [(a,b) for a in subsets(p+1) for b in subsets(q+1)
            if not (len(a)==p+1 and len(b)==q+1)]


def count_direct(p,q,k):
    fs=faces(p,q)
    f=[(a,b) for a,b in fs if len(a)+len(b)-2<=k-1]
    g=[(a,b) for a,b in fs if len(a)+len(b)-2<=p+q-k-1]
    return sum(1 for a,b in f for c,d in g
               if len(a|c)==p+1 and len(b|d)==q+1)


def count_formula(p,q,k):
    return sum(comb(p+1,a)*comb(q+1,k+1-a)
               for a in range(1,p+1) if 1<=k+1-a<=q)


def main():
    pairs=0
    for d in range(2,8):
        for p in range(1,d):
            q=d-p
            for k in range(1,d):
                lhs=count_direct(p,q,k)
                rhs=count_formula(p,q,k)
                assert lhs==rhs,(d,p,q,k,lhs,rhs)
                assert rhs==count_formula(q,p,k)
                assert rhs==count_formula(p,q,d-k)
                pairs+=1
            assert sum(count_formula(p,q,k) for k in range(1,d))==4*(2**p-1)*(2**q-1)
    for d in range(2,50):
        for p in range(1,d//2+1):
            q=d-p
            for k in range(1,d):
                if q>=p+2:
                    assert count_formula(p+1,q-1,k)>count_formula(p,q,k)
                assert count_formula(p,q,k)>=2*comb(d,k)
    print('PASS: complete face-pair enumeration through dimension 7;'
          f' {pairs} rank/shape comparisons; balance and endpoints through dimension 49.')

if __name__=='__main__':
    main()
