"""Finite reproducibility tests for sparse markings of binary vector spaces.
No asymptotic or logical completeness claim is established by these tests.
"""
from itertools import combinations
from math import comb, factorial, exp
from functools import lru_cache


def is_independent(vectors):
    basis={}
    for v in vectors:
        x=v
        while x:
            p=x.bit_length()-1
            if p in basis: x ^=basis[p]
            else:
                basis[p]=x
                break
        else: return False
    return True

cases=0
for d in range(1,6):
    n=1<<d
    for k in range(min(d,4)+1):
        direct=sum(is_independent(c) for c in combinations(range(n),k))
        expected=1
        for j in range(k): expected*=n-(1<<j)
        expected//=factorial(k)
        assert direct==expected,(d,k,direct,expected)
        cases+=1


def atomic_signature(d,k,selected):
    # P consists of the first k standard basis vectors; all terms are F_2 linear combinations.
    out=[]
    for mask in range(1<<len(selected)):
        x=0
        for i,v in enumerate(selected):
            if mask>>i&1: x ^=v
        out.append((x==0, x in {1<<j for j in range(k)}))
    return tuple(out)


def ef_equiv(d1,k1,d2,k2,rounds):
    n1,n2=1<<d1,1<<d2
    @lru_cache(None)
    def win(a,b):
        if atomic_signature(d1,k1,a)!=atomic_signature(d2,k2,b): return False
        if len(a)==rounds: return True
        return (all(any(win(a+(x,),b+(y,)) for y in range(n2)) for x in range(n1))
                and all(any(win(a+(x,),b+(y,)) for x in range(n1)) for y in range(n2)))
    value=win((),())
    return value, win.cache_info().currsize

assert ef_equiv(3,1,4,1,2)[0]
assert not ef_equiv(3,1,4,2,2)[0]
assert not ef_equiv(4,2,5,3,2)[0]

def factorial_tail(c,upto,extra=80):
    weights=[exp(-c)*c**j/factorial(j) for j in range(upto+extra)]
    return weights
w=factorial_tail(1.0,12)
for n in range(4,10): assert w[n] > sum(w[n+1:])
print('VECTOR_SPARSE_FO_FINITE_OK',cases,'EF2_3','POISSON_GAPS6')
