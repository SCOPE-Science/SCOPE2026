#!/usr/bin/env python3
"""Exact finite reproducibility checks for the two-margin cube section theorem."""
from fractions import Fraction
from itertools import product

def witness(n,m):
    if not n%2 and not m%2:
        return [[(-1)**(i+j) for j in range(m)] for i in range(n)]
    if not n%2:
        return [[(-1)**(i+j) if j<m-1 else 0 for j in range(m)] for i in range(n)]
    if not m%2:
        return [[(-1)**(i+j) if i<n-1 else 0 for j in range(m)] for i in range(n)]
    if n>m:
        t=witness(m,n)
        return [list(row) for row in zip(*t)]
    k=(n-1)//2
    base=[[0 if (j-i)%n==0 else (1 if (j-i)%n<=k else -1) for j in range(n)] for i in range(n)]
    v=[0]+[1]*k+[-1]*k
    for t in range((m-n)//2):
        for i in range(n):
            base[i]+=[v[i],-v[i]]
    return base

def M(n,m):
    if n%2==0 and m%2==0:return n*m
    if n%2==0:return n*(m-1)
    if m%2==0:return m*(n-1)
    return n*m-max(n,m)

checks=0
for n in range(2,26):
    for m in range(2,26):
        a=witness(n,m)
        assert len(a)==n and all(len(row)==m for row in a)
        assert all(sum(row)==0 for row in a)
        assert all(sum(a[i][j] for i in range(n))==0 for j in range(m))
        assert max(abs(z) for row in a for z in row)==1
        assert sum(z*z for row in a for z in row)==M(n,m)
        c=Fraction((n-1)*(m-1),n*m)
        p=[[Fraction(int(i==0))-Fraction(1,n) for i in range(n)]]
        q=[Fraction(int(j==0))-Fraction(1,m) for j in range(m)]
        assert sum(x*x for x in p[0])*sum(y*y for y in q)==c
        assert c*M(n,m)<= (n-1)*(m-1)
        checks+=7
# Exhaustive 3 x 3 search at the vertices of coordinate cube intersected with margin hyperplanes,
# using all 3^9 ternary matrices; confirms the boundary and the attained maximum.
maximum=0
for digits in product((-1,0,1),repeat=9):
    if any(sum(digits[3*i:3*i+3]) for i in range(3)):
        continue
    if any(sum(digits[i+3*j] for j in range(3)) for i in range(3)):
        continue
    maximum=max(maximum,sum(z*z for z in digits))
assert maximum==M(3,3)==6
checks+=1
print(f'VERIFY_OK witness_and_projection_checks={checks} exhaustive_ternary_3x3_maximum={maximum}')
