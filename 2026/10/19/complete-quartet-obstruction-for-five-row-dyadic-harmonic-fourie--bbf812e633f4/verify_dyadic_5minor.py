#!/usr/bin/env python3
"""Exact tests of the five-row dyadic Fourier-minor classification.
Uses only integer pair-sum multiplicities and cyclotomic parity, not floating point.
"""
from itertools import combinations
from collections import Counter
from math import comb

ROWS=(0,1,2,4,5)

def vanishing_e2(cols,n):
    multiplicity=[0]*n
    for a,b in combinations(cols,2):
        multiplicity[(a+b)%n]+=1
    return all(multiplicity[t]==multiplicity[t+n//2] for t in range(n//2))

def quartet(cols,n):
    s=set(cols)
    q=n//4
    cosets=[{a,(a+q)%n,(a+2*q)%n,(a+3*q)%n} for a in range(q)]
    return any(c.issubset(s) for c in cosets)

for n in (8,16,32):
    seen=0
    for cols in combinations(range(n),5):
        zero=vanishing_e2(cols,n)
        expected=quartet(cols,n)
        assert zero==expected,(n,cols,zero,expected)
        seen+=zero
    expected_count=(n//4)*(n-4)
    assert seen==expected_count,(n,seen,expected_count)
    print('N=%d: all %d column sets checked; singular=%d; formula=%d'%(n,comb(n,5),seen,expected_count))

# Independent integral determinant quotient identity at five indeterminates,
# tested via alternating evaluation for several small integer nodes.
from itertools import permutations
from math import prod
for nodes in ((1,2,3,4,5),(0,2,3,5,7),(-3,-1,1,2,6),(1,2,4,8,16)):
    det=0
    for perm in permutations(range(5)):
        inv=sum(perm[i]>perm[j] for i in range(5) for j in range(i+1,5))
        term=prod(nodes[perm[i]]**ROWS[i] for i in range(5))
        det+=(-1)**inv*term
    vand=prod(nodes[j]-nodes[i] for i in range(5) for j in range(i+1,5))
    e2=sum(nodes[i]*nodes[j] for i in range(5) for j in range(i+1,5))
    assert det==vand*e2,(nodes,det,vand*e2)
print('integer Vandermonde/e2 determinant identity tested')
print('VERIFY_OK')
