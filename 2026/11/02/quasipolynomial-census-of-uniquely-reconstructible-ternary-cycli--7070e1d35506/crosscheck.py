#!/usr/bin/env python3
"""Independent brute-force reconstruction of all ternary necklaces through length 12."""
from itertools import product
from collections import defaultdict

def rotate_min(w):
    best=w
    for j in range(1,len(w)):
        s=w[j:]+w[:j]
        if s<best:best=s
    return best

def expected(n):
    if n<6:return [0,3,6,11,24,45][n]
    return n*n+9*n-26+[0,7,4,3,4,7][n%6]

if __name__=='__main__':
    for n in range(1,13):
        d=defaultdict(set)
        for w in product(range(3),repeat=n):
            k=[0]*9
            for j in range(n):k[3*w[j]+w[(j+1)%n]]+=1
            d[tuple(k)].add(rotate_min(w))
        actual=sum(len(s)==1 for s in d.values())
        assert actual==expected(n),(n,actual,expected(n))
    print('CROSSCHECK_OK: direct words and canonical necklaces through length 12')
