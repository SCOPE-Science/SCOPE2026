#!/usr/bin/env python3
"""Independent GF(2) elimination of Hamming-distance-three adjacency maps."""
from itertools import combinations
from math import comb

def rank(rows):
    pivots={}
    for x in rows:
        while x:
            j=x.bit_length()-1
            if j not in pivots:
                pivots[j]=x
                break
            x^=pivots[j]
    return len(pivots)

def matrix(n):
    s=1<<n
    offsets=[sum(1<<i for i in c) for c in combinations(range(n),3)]
    return [sum(1<<(v^d) for d in offsets) for v in range(s)]

def apply(rows, x):
    # matrix as rows: output bit i dot input vector
    return sum(((row&x).bit_count()%2)<<i for i,row in enumerate(rows))

for n in range(3,12):
    rows=matrix(n)
    v=1<<n
    r=rank(rows)
    predicted={0:2**(n-1),1:2**(n-1)-2**((n-1)//2),2:2**(n-2)-2**(n//2-1),3:v}[n%4]
    assert r==predicted,(n,r,predicted)
    # Every row of A^2 must be identity or zero (via rowwise GF2 matrix product)
    for i,row in enumerate(rows):
        outcome=0
        while row:
            lsb=row&-row
            j=lsb.bit_length()-1
            outcome^=rows[j]
            row^=lsb
        assert outcome==((1<<i) if n%4==3 else 0), (n,i)
    if n%4==3:
        assert rank([row^(1<<i) for i,row in enumerate(rows)])==v//2
    print(f'n={n} size={v} rank={r} expected={predicted} square={"identity" if n%4==3 else "zero"}')
print('PASS direct graph-matrix rank and square checks')
