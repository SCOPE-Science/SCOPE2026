#!/usr/bin/env python3
"""Exact finite checks of the p-biased affine Fourier projection.

All main equalities for arbitrary dimension are proved mathematically in RESULT.md;
finite checks are consistency tests, not exhaustive proofs.
"""
from fractions import Fraction as F
from itertools import product
from math import comb, floor


def formula(n, p):
    return sum(F(comb(n, j))*p**j*(1-p)**(n-j)*abs(1-n+F(j)/p)
               for j in range(n+1))


def tail_formula(n, p):
    k = ((n-1)*p).numerator // ((n-1)*p).denominator
    prob = F(comb(n-1, k))*p**k*(1-p)**(n-1-k)
    tail = sum(F(comb(n,j))*p**j*(1-p)**(n-j) for j in range(k+1))
    return 1+2*n*(1-p)*prob-2*tail


def row_norm(n, p, x):
    acc = F(0)
    for y in product((0,1),repeat=n):
        mass = p**sum(y)*(1-p)**(n-sum(y))
        kernel = 1+sum((xi-p)*(yi-p)/(p*(1-p)) for xi,yi in zip(x,y))
        acc += mass*abs(kernel)
    return acc


def check():
    assertions=0
    biases=(F(1,8),F(1,5),F(1,3),F(1,2),F(2,3),F(4,5),F(7,8))
    for n in range(2,8):
        for p in biases:
            p0 = min(p,1-p)
            target = formula(n,p0)
            assert target == tail_formula(n,p0)
            assertions+=1
            for x in product((0,1),repeat=n):
                rn=row_norm(n,p,x)
                assert rn<=target,(n,p,x,rn,target)
                assertions+=1
                if x == (1,)*n and p<=F(1,2) or x==(0,)*n and p>=F(1,2):
                    assert rn == target,(n,p,x,rn,target)
                    assertions+=1
        vals=[formula(n,F(j,40)) for j in range(1,21)]
        assert all(vals[i]>vals[i+1] for i in range(len(vals)-1))
        assertions+=1
        m=n//2
        balanced=F(2*m+1)*comb(2*m,m)/4**m
        assert formula(n,F(1,2)) == balanced
        assertions+=1
    print('PASS:', assertions, 'exact-rational assertions; dimensions 2..7; full rows at seven biases')
    return assertions

if __name__=='__main__':
    check()
