"""Exact checks for root-degree-conditioned unary counts in uniform plane trees.

Run with Python 3.10 or later: python verify.py
Only Python's standard library is used. Finite checks supplement the proof.
"""
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import product
from math import comb
from fractions import Fraction

checks = 0

def test(statement, message):
    global checks
    assert statement, message
    checks += 1

def forest_total(n,k):
    return k * comb(2*n-k-1,n-k)//n

def forest_unary(n,k,u):
    """Number of ordered k-component plane forests of n vertices, u unary."""
    e=n-k-u
    if e<0 or u<0 or u>n: return 0
    count = int(e==0)
    for v in range(1,min(n-u,e//2)+1):
        count += comb(n-u,v)*comb(e-v-1,v-1)
    numerator = k*comb(n,u)*count
    test(numerator % n == 0,(n,k,u,numerator))
    return numerator//n

def parts(total):
    if total==0:
        yield ()
    else:
        for start in range(1,total+1):
            for rest in parts(total-start):
                yield (start,)+rest

@lru_cache(None)
def trees(vertices):
    if vertices==1: return ((),)
    output=[]
    for sizes in parts(vertices-1):
        for children in product(*(trees(s) for s in sizes)):
            output.append(tuple(children))
    return tuple(output)

def unary_nonroot(tree):
    return sum(len(c)==1 for c in tree for dummy in [None]) + sum(unary_nonroot(c) for c in tree)

for n in range(1,11):
    # Independent structural enumeration of all trees with n+1 vertices.
    tally=defaultdict(Counter)
    for t in trees(n+1):
        tally[len(t)][unary_nonroot(t)]+=1
    test(sum(map(sum,(c.values() for c in tally.values())))==comb(2*n,n)//(n+1),('catalan',n))
    for k in range(1,n+1):
        test(sum(tally[k].values())==forest_total(n,k),('forest',n,k))
        for u in range(n+1):
            test(tally[k][u]==forest_unary(n,k,u),('unary',n,k,u))

# All integer boundary cases and every probability, independently of tree enumeration.
for n in range(2,45):
    for k in range(1,n+1):
        total=forest_total(n,k)
        test(total>0,('nonzero total',n,k))
        test(sum(forest_unary(n,k,u) for u in range(n+1))==total,('sum',n,k))
        if k<n:
            e=n-k
            test(forest_unary(n,k,e)==comb(n-1,k-1),('chains',n,k))
            test(forest_unary(n,k,e-1)==0,('support gap',n,k))
        if k<=n-2:
            e=n-k
            old=Fraction(forest_unary(n,k,e),total)
            new=Fraction(forest_unary(n,k+1,e-1),forest_total(n,k+1))
            test(new/old==Fraction(2*n-k-1,k+1),('ratio',n,k))
            test(new>old>0,('first tail crossover',n,k))
            test(forest_unary(n,k+1,e)==0,('second tail crossover',n,k))
    test(forest_unary(n,n-1,1)==forest_total(n,n-1) and forest_unary(n,n,0)==forest_total(n,n),('endpoint',n))
print('PASS:',checks,'exact checks')
