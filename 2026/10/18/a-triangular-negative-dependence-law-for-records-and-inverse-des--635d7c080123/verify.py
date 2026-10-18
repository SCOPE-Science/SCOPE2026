#!/usr/bin/env python3
"""Independent exhaustive checks of the triangular record/inverse-descent covariance law.
Python 3 standard library only.
"""
from fractions import Fraction as F
from math import comb, factorial
from itertools import permutations

def formula(n, i, j):
    if i == 1 or i > j+1:
        return F(0)
    return -F(i-1, 2*n*(n-1)) * F(comb(j-1, i-2), comb(n-2, i-2))

def records(perm):
    out = []
    last = 0
    for val in perm:
        is_record = int(val > last)
        out.append(is_record)
        last = max(last, val)
    return tuple(out)

def inv_des(perm, j):
    return int(perm.index(j) > perm.index(j+1))

def swap_adjacent_values(perm, j):
    return tuple(j+1 if v==j else j if v==j+1 else v for v in perm)

def check(n):
    sumR = [0]*n
    sumJ = [0]*(n-1)
    sumRJ = [[0]*(n-1) for _ in range(n)]
    num = 0
    strict_pair_coupling = 0
    for perm in permutations(range(1,n+1)):
        num += 1
        r = records(perm)
        for i, v in enumerate(r): sumR[i] += v
        js = [inv_des(perm,j) for j in range(1,n)]
        for j, v in enumerate(js):sumJ[j]+=v
        for i,ri in enumerate(r):
            if ri:
                for j,d in enumerate(js):sumRJ[i][j] += d
        for j in range(1,n):
            if js[j-1]: continue
            other = swap_adjacent_values(perm, j)
            after = records(other)
            diffs = [i+1 for i in range(n) if r[i]!=after[i]]
            assert all(a>=b for a,b in zip(r, after))
            high = [v for v in perm if v>=j]
            expected = [perm.index(j+1)+1] if high[:2]==[j,j+1] else []
            assert diffs==expected,(n,perm,j,diffs,expected)
            if diffs: strict_pair_coupling+=1
    assert num==factorial(n)
    verified = 0
    for i in range(1,n+1):
        for j in range(1,n):
            computed=F(sumRJ[i-1][j-1],num)-F(sumR[i-1]*sumJ[j-1],num*num)
            expected=formula(n,i,j)
            assert computed==expected,(n,i,j,computed,expected)
            verified+=1
    for j in range(1,n):
        m=n-j+1
        expected_total=-F(1,2*m*(m-1))
        assert sum((formula(n,i,j) for i in range(1,n+1)), F(0))==expected_total
    assert sum((formula(n,i,j) for i in range(1,n+1) for j in range(1,n)), F(0)) == -F(n-1,2*n)
    print(f'n={n}: {num} permutations, {verified} exact covariance entries, {strict_pair_coupling} monotone strict coupling pairs')
    return verified

if __name__=='__main__':
    total=sum(check(n) for n in range(2,9))
    print('PASS: all cross-covariance entries and every conditional swap coupling through n=8')
    print('covariance entries checked:',total)
