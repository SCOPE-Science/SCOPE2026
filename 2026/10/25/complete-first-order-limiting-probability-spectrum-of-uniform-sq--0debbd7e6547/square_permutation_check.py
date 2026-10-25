"""Exact finite checks for square permutations and cycle-count generating functions.

Run: python3 square_permutation_check.py. Standard library only.
The checks are finite diagnostics, not proofs of asymptotic or logical laws.
"""
from fractions import Fraction
from itertools import permutations
from math import factorial

MAX_N = 8

def cycles(p):
    visited = set()
    counts = [0] * (len(p) + 1)
    for a in range(len(p)):
        if a in visited:
            continue
        length = 0
        b = a
        while b not in visited:
            visited.add(b)
            length += 1
            b = p[b]
        counts[length] += 1
    return counts

def multiply(a,b,upto):
    ans = [Fraction(0) for _ in range(upto+1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b[:upto+1-i]):
            ans[i+j] += x*y
    return ans

def polynomial_for_length(j,upto):
    result = [Fraction(0) for _ in range(upto+1)]
    for count in range(upto//j+1):
        if (j % 2) == 0 and (count % 2):
            continue
        result[count*j] = Fraction(1, j**count * factorial(count))
    return result

def coefficients(upto, required=None):
    product = [Fraction(1)]+[Fraction(0)]*upto
    for j in range(1,upto+1):
        factor=polynomial_for_length(j,upto)
        if required and j in required:
            c=required[j]
            factor = [Fraction(0) for _ in range(upto+1)]
            if c*j<=upto and (j%2 or c%2==0):
                factor[c*j] = Fraction(1, j**c*factorial(c))
        product=multiply(product,factor,upto)
    return product

whole=coefficients(MAX_N)
fixed0=coefficients(MAX_N,{1:0})
even0=coefficients(MAX_N,{2:0})
small=coefficients(MAX_N,{1:1,2:0})
checked=0
for n in range(1,MAX_N+1):
    total=fixed=without2=first1_no2=0
    for p in permutations(range(n)):
        c=cycles(p)
        if any(c[j]%2 for j in range(2,n+1,2)):
            continue
        total+=1
        fixed+=(c[1]==0)
        without2+=(n<2 or c[2]==0)
        first1_no2+=(c[1]==1 and (n<2 or c[2]==0))
    assert total == factorial(n)*whole[n], (n,total,whole[n])
    assert fixed == factorial(n)*fixed0[n], (n,fixed,fixed0[n])
    assert without2 == factorial(n)*even0[n], (n,without2,even0[n])
    assert first1_no2 == factorial(n)*small[n], (n,first1_no2,small[n])
    checked += total
print('SQUARE_PERM_EXACT_OK',MAX_N,checked,'4x8_coeff_checks',int(factorial(MAX_N)*whole[MAX_N]))
