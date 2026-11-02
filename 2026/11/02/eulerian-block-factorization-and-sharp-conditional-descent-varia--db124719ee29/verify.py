"""Exact finite checks for record-conditioned descent blocks and sharp variance bounds.

The all-size proof is mathematical; the tests provide an independent finite check.
Run: python3 verify.py
"""
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import permutations, combinations
from math import factorial

checks = 0

def verify(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)

@lru_cache(None)
def eulerian(n):
    if n == 1:
        return (1,)
    old = eulerian(n - 1)
    return tuple((d + 1) * (old[d] if d < len(old) else 0)
                 + (n - d) * (old[d - 1] if d > 0 else 0)
                 for d in range(n))

def convolution(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            out[i + j] += x*y
    return out

def zero_blocks(mask, n):
    blocks=[]
    j=1
    while j <= n:
        if mask & (1 << (j-1)):
            j += 1
            continue
        first=j
        while j <= n and not (mask & (1 << (j-1))):
            j += 1
        blocks.append(j-first)
    return blocks

def predicted_counts(mask,n,total):
    blocks=zero_blocks(mask,n)
    m=len(blocks)
    coefficient=[1]
    denominator=1
    for length in blocks:
        coefficient=convolution(coefficient,eulerian(length))
        denominator *= factorial(length)
    coefficient=[0]*m+coefficient
    assert total % denominator == 0
    return [v * (total//denominator) for v in coefficient]

def conditional_moments(blocks):
    z=sum(blocks)
    m=len(blocks)
    mean=Fraction(z+m,2)
    var=sum((Fraction(length+1,12) if length>=2 else Fraction(0)) for length in blocks)
    return mean,var

for n in range(1,10):
    rows=defaultdict(lambda:defaultdict(int))
    for p in permutations(range(1,n+1)):
        mask=0
        mx=0
        d=0
        for j,x in enumerate(p):
            if x>mx:
                mask |= 1<<j
                mx=x
            if j and p[j-1]>x:
                d+=1
        rows[mask][d]+=1
    for mask,row in rows.items():
        total=sum(row.values())
        pred=predicted_counts(mask,n,total)
        verify(tuple(row.get(i,0) for i in range(n)) == tuple(pred+[0]*(n-len(pred))),
               f'n={n},mask={mask}: distribution')
        mean=sum(Fraction(d*v,total) for d,v in row.items())
        var=sum(Fraction(v,total)*(d-mean)**2 for d,v in row.items())
        pmean,pvar=conditional_moments(zero_blocks(mask,n))
        verify(mean==pmean and var==pvar, f'n={n},mask={mask}: moments')
    verify(len(rows)==2**(n-1), f'n={n}: every record pattern occurs')
    print('enumeration',n,'patterns',len(rows),'OK')

for n in range(1,16):
    for k in range(1,n+1):
        z=n-k
        variances=[]
        for rec_indices in combinations(range(2,n+1),k-1):
            mask = 1 | sum(1<<(j-1) for j in rec_indices)
            blocks=zero_blocks(mask,n)
            variances.append(conditional_moments(blocks)[1])
        if z<=1:
            lo=hi=Fraction(0)
        else:
            lo=Fraction(0) if k>=z else Fraction(z-k+2,12)
            hi=Fraction(z+min(k,z//2),12)
        verify(min(variances)==lo and max(variances)==hi,
               f'n={n},records={k}: extrema')
print('ALL CHECKS PASSED:',checks)
