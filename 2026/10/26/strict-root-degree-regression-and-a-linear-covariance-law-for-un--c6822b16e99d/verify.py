#!/usr/bin/env python3
"""Exact finite verification of contour-area regression for uniform plane trees.
No external dependencies; independent Dyck-path enumeration and coefficient formulas.
"""
from fractions import Fraction
from math import comb

def c(m, r):
    if r < 1 or r > m: return 0
    return r * comb(2*m-r-1, m-r) // m

def total_area(n, r):
    return sum(m*c(m,r)*comb(2*(n-m), n-m) for m in range(r,n+1))

def gen(n):
    if n == 0:
        yield ''
    else:
        for k in range(n):
            for inner in gen(k):
                for suffix in gen(n-1-k):
                    yield '('+inner+')'+suffix

def stats(word):
    h=area=returns=0
    for step in word:
        area += h
        if step=='(': h+=1
        else:
            h-=1
            if h==0: returns+=1
    assert h==0
    return area,returns

def main():
    checks=0
    for n in range(1,10):
        observed_count=[0]*(n+1);observed_area=[0]*(n+1)
        for word in gen(n):
            a,r=stats(word)
            observed_count[r]+=1
            observed_area[r]+=a
        assert sum(observed_count)==comb(2*n,n)//(n+1);checks+=1
        for r in range(1,n+1):
            assert observed_count[r]==c(n,r),(n,r,'count');checks+=1
            assert observed_area[r]==total_area(n,r),(n,r,'area');checks+=1
        means=[Fraction(observed_area[r],observed_count[r]) for r in range(1,n+1)]
        assert all(means[i]>means[i+1] for i in range(n-1));checks+=1
        if n>=2:
            assert means[0]-means[1]==n;checks+=1
        # Independently compute covariance from enumerated paths.
        count=sum(observed_count)
        ea=Fraction(sum(observed_area),count)
        er=Fraction(sum(r*observed_count[r] for r in range(1,n+1)),count)
        ear=Fraction(sum(r*observed_area[r] for r in range(1,n+1)),count)
        assert er==Fraction(3*n,n+2);checks+=1
        if n>=2: assert ear-ea*er<0;checks+=1
    # algebraic coefficient version for larger dimensions, with no path enumeration
    for n in range(10,61):
        means=[Fraction(total_area(n,r),c(n,r)) for r in range(1,n+1)]
        assert all(means[i]>means[i+1] for i in range(n-1)); checks+=1
        assert means[0]-means[1]==n;checks+=1
        for r in range(2,n):
            for m in range(r+1,n):
                assert Fraction(c(m,r+1),c(m,r)) < Fraction(c(n,r+1),c(n,r));checks+=1
    print(f'PASS: {checks} deterministic exact assertions; Dyck paths exhaustively enumerated through semilength 9.')

if __name__=='__main__': main()
