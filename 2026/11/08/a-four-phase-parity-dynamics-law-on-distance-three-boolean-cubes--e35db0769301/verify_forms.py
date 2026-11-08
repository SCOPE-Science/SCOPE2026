#!/usr/bin/env python3
"""Exact graded GF(2) ranks of wedge-multiplication by e2/e3."""
from itertools import combinations

def rank_vectors(vals):
    pivot={}
    for v in vals:
        while v:
            k=v.bit_length()-1
            if k not in pivot:
                pivot[k]=v
                break
            v^=pivot[k]
    return len(pivot)

def graded_rank(n,degree):
    total=0
    details=[]
    for k in range(n-degree+1):
        targets={sum(1<<i for i in c):p for p,c in enumerate(combinations(range(n), k+degree))}
        vectors=[]
        for source in combinations(range(n),k):
            cm=sum(1<<i for i in source)
            free=[i for i in range(n) if not cm>>i&1]
            v=0
            for choice in combinations(free,degree):
                t=cm|sum(1<<i for i in choice)
                v^=1<<targets[t]
            vectors.append(v)
        rr=rank_vectors(vectors)
        details.append(rr)
        total+=rr
    return total,details

for n in range(2,13):
    r2,l2=graded_rank(n,2)
    if n%2:
        expected2=(1<<(n-1))-(1<<((n-1)//2))
    else:
        expected2=(1<<(n-1))-(1<<(n//2-1))
    assert r2==expected2,(n,r2,expected2)
    if n>=3:
        r3,l3=graded_rank(n,3)
        expected3=(1<<(n-2))-(1<<(n//2-1))
        assert r3==expected3,(n,r3,expected3)
    print(f'n={n}: rank(e2)={r2}, rank(e3)={r3 if n>=3 else "NA"}; graded components e2={l2}')
print('PASS all exact graded rank checks')
