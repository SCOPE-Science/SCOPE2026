#!/usr/bin/env python3
"""Exact rook/placement evaluation for 4-cycles in derangement switch graphs."""
from math import factorial, comb
from itertools import permutations, combinations

def choose(n,k): return comb(n,k) if 0<=k<=n else 0

def falling_rook(n,poly,free):
    # Rook polynomial given coefficient list; last factor (1+x)^free.
    return sum((-1)**(i+j)*a*comb(free,j)*factorial(n-i-j)
               for i,a in enumerate(poly) for j in range(free+1))

def counts(n):
    assert n>=4
    A=falling_rook(n,[1,8,20,16,4],n-4)
    four=(3*comb(n,4)*A)//4
    assert (3*comb(n,4)*A)%4==0
    B0=sum((-1)**j*comb(n-6,j)*factorial(n-3-j) for j in range(n-5)) if n>=6 else 0
    B1=sum((-1)**j*comb(n-5,j)*factorial(n-3-j) for j in range(n-4)) if n>=5 else 0
    three=comb(n,3)*(9*choose(n-3,3)*B0+3*choose(n-3,2)*B1)
    der=sum((-1)**j*comb(n,j)*factorial(n-j) for j in range(n+1))
    return der,three,four,three+four

for n in range(4,11):
    print(n,*counts(n))
