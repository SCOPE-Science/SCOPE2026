#!/usr/bin/env python3
"""Finite combinatorial consistency tests for logarithmic-residue component census."""
from itertools import product
from collections import Counter
from math import comb, factorial

def predicted(p,d):
    return (comb(d+p-2,p-2)+(p-1)*((d%p==0)-(d%p==1)))//p

def verify(p,d):
    vectors=[a for a in product(range(1,p),repeat=d) if sum(a)%p==0]
    by_type={tuple(sorted(Counter(a).items())) for a in vectors}
    expected=[(t,p*factorial(d)//__import__('math').prod(factorial(m) for _,m in t)) for t in by_type]
    assert len(by_type)==predicted(p,d),(p,d,len(by_type),predicted(p,d))
    assert sum(deg for _,deg in expected)==p*len(vectors)
    closed=(p-1)**d+(p-1)*(-1)**d
    assert p*len(vectors)==closed,(p,d,len(vectors),closed)
    for t,degree in expected:
        assert sum(j*m for j,m in t)%p==0
        assert sum(m for j,m in t)==d
        assert degree%p==0
    return len(by_type),p*len(vectors)

if __name__=='__main__':
    tests=0
    for p in (3,5,7):
        for d in range(2,7 if p<=5 else 5):
            n,N=verify(p,d)
            print(f'p={p},d={d},components={n},total_fiber={N}')
            tests+=1
    print(f'VERIFY_OK {tests} finite classifications')
