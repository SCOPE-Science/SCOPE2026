#!/usr/bin/env python3
"""Exact finite endpoint check for consecutive powers of divisor sums.
All rational comparison tests use integer arithmetic; no floating-point comparison of powers.
"""
from math import gcd

LIMIT=10000
sigma=[0]*(LIMIT+2)
tau=[0]*(LIMIT+2)
for d in range(1,LIMIT+2):
    for j in range(d,LIMIT+2,d):
        sigma[j]+=d
        tau[j]+=1

independent_checks=0
full_pow_tests=0
special_equal_exp=[]
equalities=[]
for n in range(1,LIMIT):
    a=n-tau[n]
    b=n+1-tau[n+1]
    A=sigma[n]
    B=sigma[n+1]
    assert a>=0 and b>=0
    if a==0 or b==0:
        match=(A**a==B**b)
    elif a==b:
        special_equal_exp.append(n)
        match=(A==B)
    else:
        independent_checks+=1
        g=gcd(a,b)
        r=a//g;s=b//g
        if s>A.bit_length()-1 or r>B.bit_length()-1:
            match=False
        else:
            full_pow_tests+=1
            match=(A**a==B**b)
    if match:
        equalities.append(n)

assert equalities==[1],equalities
assert 10000**0.5/5 - 1 > 16.6
print('VERIFY_OK', 'full_range=1..9999','equalities='+str(equalities),
      'unequal_exponent_pairs='+str(independent_checks),
      'direct_power_tests='+str(full_pow_tests),
      'equal_positive_exponent_cases='+str(len(special_equal_exp)))
