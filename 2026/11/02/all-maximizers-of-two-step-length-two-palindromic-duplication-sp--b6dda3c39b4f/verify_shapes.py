#!/usr/bin/env python3
"""Independent structural-shape and sampling checks; not an infinite theorem proof."""
from itertools import product
from random import Random

def dup(s,i):
    return s[:i+2]+s[i:i+2][::-1]+s[i+2:]

def shapes(s):
    n=len(s)
    r={}
    for a in range(n-1):
        t=dup(s,a)
        r[('P',a,a)]=dup(t,a)
        r[('L',a)]=dup(t,a+1)
        r[('M',a)]=dup(t,a+2)
        if a+2<n: r[('R',a)]=dup(t,a+3)
        for b in range(a+1,n-1):
            r[('P',a,b)]=dup(dup(s,b),a)
    assert len(r)==(n*n+5*n-8)//2
    return r

def expected_proper(s):
    return all(s[i]!=s[i+1] for i in range(len(s)-1))

for q,limit in ((2,12),(3,9),(4,7)):
    for n in range(2,limit+1):
        num=0
        for s in product(range(q),repeat=n):
            shape_outputs=shapes(s)
            is_injective=len(set(shape_outputs.values()))==len(shape_outputs)
            assert is_injective==expected_proper(s), (q,n,s)
            num+=is_injective
        assert num==q*(q-1)**(n-1)
        print(f'SHAPES q={q} n={n}: {num} injective shape maps')

rng=Random(20261027)
for q,n,trials in ((3,35,200),(4,60,200),(7,45,200)):
    for _ in range(trials):
        s=[rng.randrange(q)]
        for j in range(1,n):
            nxt=rng.randrange(q-1)
            if nxt>=s[-1]:nxt+=1
            s.append(nxt)
        sh=shapes(tuple(s))
        assert len(set(sh.values()))==len(sh)
    print(f'LONG PROPER RANDOM q={q} n={n} samples={trials}: all shape maps injective')
print('STRUCTURAL FINITE CHECKS PASSED')
