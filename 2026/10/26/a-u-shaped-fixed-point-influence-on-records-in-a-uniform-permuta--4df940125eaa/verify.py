#!/usr/bin/env python3
"""Exact checks for fixed-point and record-count covariance identities."""
from fractions import Fraction as Q
from itertools import permutations
from math import comb, factorial

checks = 0
objects = 0
for n in range(2, 9):
    factor = factorial(n)
    record_mixed = [[0] * n for _ in range(n)]
    fixed_record = [0] * n
    joint_total = total_records = total_fixed = 0
    for p in permutations(range(1, n + 1)):
        objects += 1
        peak = 0
        records = []
        for value in p:
            records.append(int(value > peak))
            peak = max(peak, value)
        fixed = [int(p[j] == j + 1) for j in range(n)]
        rcount, fcount = sum(records), sum(fixed)
        joint_total += rcount * fcount
        total_records += rcount
        total_fixed += fcount
        for j in range(n):
            fixed_record[j] += fixed[j] * rcount
            for i in range(n):
                record_mixed[j][i] += fixed[j] * records[i]
    for j in range(1, n + 1):
        actual = Q(fixed_record[j-1], factorial(n-1))
        expected = sum(Q(1, i) for i in range(1, n+1)) + Q(1, comb(n-1,j-1)) - Q(1,n)
        assert actual == expected, (n, j, actual, expected)
        checks += 1
        for i in range(1,n+1):
            cov = Q(record_mixed[j-1][i-1],factor)-Q(1,n*i)
            if i==1 or j>i:
                predicted=Q(0)
            elif j<i:
                predicted=Q(1,n*i*(i-1))
            else:
                predicted=Q(1,n)*(Q(1,comb(n-1,i-1))-Q(1,i))
            assert cov == predicted, (n,j,i,cov,predicted)
            checks += 1
    total_cov = Q(joint_total, factor)-Q(total_fixed*total_records,factor**2)
    assert total_cov == sum((Q(1,n*comb(n-1,k)) for k in range(1,n)),Q(0))
    checks += 1

for n in range(5,101):
    for j in range(1,n+1):
        delta = Q(1,comb(n-1,j-1))-Q(1,n)
        assert (delta>0)==(j<=2 or j>=n-1), (n,j,delta)
        assert delta==Q(1,comb(n-1,n-j))-Q(1,n)
        checks+=2

print(f'VERIFY_OK {objects} enumerated permutations; {checks} exact assertions')
