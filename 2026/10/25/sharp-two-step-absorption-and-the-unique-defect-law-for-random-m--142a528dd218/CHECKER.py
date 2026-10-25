#!/usr/bin/env python3
"""Exhaustive verification of Boolean-square universal relation in small dimensions."""
from fractions import Fraction

def compute(n):
    total=1 << (n*n)
    mask=(1<<n)-1
    smooth=0
    success=0
    failures=0
    missing_sum=0
    single_off=0
    single_diag=0
    unique_off=0
    unique_diag=0
    for b in range(total):
        row=[(b >> (n*i)) & mask for i in range(n)]
        col=[sum(((row[i]>>j)&1)<<i for i in range(n)) for j in range(n)]
        sq=[sum((any((row[i]>>k)&1 and (row[k]>>j)&1 for k in range(n)))<<j for j in range(n)) for i in range(n)]
        deficit=n*n-sum(v.bit_count() for v in sq)
        missing_sum+=deficit
        if not (sq[0]&1):single_diag+=1
        if deficit==1:
            miss=[(i,j) for i in range(n) for j in range(n) if not (sq[i]>>j)&1]
            if miss[0][0]!=miss[0][1]:unique_off+=1
            else:unique_diag+=1
        if n>1 and not (sq[0]&2):single_off+=1
        if all(row) and all(col):
            smooth+=1
            if all(x==mask for x in sq):success+=1
            else:failures+=1
    q=Fraction(3,4)
    diag=Fraction(1,2)*q**(n-1)
    off=Fraction(5,8)*q**(n-2) if n>1 else Fraction(0)
    expectation = n*diag+n*(n-1)*off
    assert missing_sum == expectation*total,(n,missing_sum,expectation*total)
    assert single_diag==diag*total,(n,single_diag,diag*total)
    if n>1:assert single_off==off*total,(n,single_off,off*total)
    assert smooth==success+failures
    print('n=%d matrices=%d smooth=%d square_universal=%d failures=%d expected_missing=%s unique_off=%d unique_diag=%d' %(n,total,smooth,success,failures,str(expectation),unique_off,unique_diag))

for n in range(1,5):compute(n)
print('ALL_BOOLEAN_RELATION_SQUARE_CHECKS_PASSED')
