#!/usr/bin/env python3
"""Reproduce first two binary valuation layers of the classical Narayana triangle.

All comparisons are exact integer arithmetic. This finite replay supports, but
does not replace, the all-length digit-mask proof in RESULT.md.
"""
from math import comb

def pop(x):
    return x.bit_count()

def bval(m,j):
    assert 0 <= j <= m
    return pop(j)+pop(m-j)-pop(m)

def valuation2(a):
    assert a > 0
    return (a & -a).bit_length()-1

def fast_narayana_valuation(n,k):
    return bval(n,k)+bval(n,k-1)-valuation2(n)

def count_even_branch(m):
    return sum(bval(m,j)+bval(m-1,j-1)==1 for j in range(1,m+1))

def count_odd_branch(m):
    return sum(bval(m,j)+bval(m,j+1)==1 for j in range(m))

def even_branch_formula(m):
    r=valuation2(m);u=m>>r
    term_one=(1 << pop(u-1)) if r>=1 else 0
    term_two=(1 << pop(u>>2)) if (u&3)==3 else 0
    return term_one+term_two

def odd_branch_formula(m):
    t=valuation2(m+1)
    return 2*(1 << pop(m>>(t+2))) if ((m>>(t+1))&1) else 0

for m in range(1,257):
    assert count_even_branch(m)==even_branch_formula(m),('E',m)
    assert count_odd_branch(m)==odd_branch_formula(m),('O',m)

# Independent exact binomial-integer evaluation of every entry of first 127 rows.
for n in range(1,128):
    for k in range(1,n+1):
        q,r=divmod(comb(n,k)*comb(n,k-1),n)
        assert r==0
        assert valuation2(q)==fast_narayana_valuation(n,k),(n,k)

for L in range(1,11):
    odd=one=0
    for n in range(1,1<<L):
        for k in range(1,n+1):
            v=fast_narayana_valuation(n,k)
            odd+=(v==0)
            one+=(v==1)
    assert odd==(5*3**(L-1)-3)//2,(L,'odd',odd)
    if L>=2:
        assert one==3**(L-1)-3,(L,'one',one)
    else:assert one==0
    print('L',L,'odd',odd,'exactly_two',one)
print('VERIFY_OK')
