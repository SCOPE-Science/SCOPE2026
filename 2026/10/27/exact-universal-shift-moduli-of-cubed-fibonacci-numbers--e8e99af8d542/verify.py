#!/usr/bin/env python3
"""Integer-only independent checks of universal Fibonacci-cube shift moduli."""
from math import gcd
from itertools import permutations
MAXK = 500
F = [0, 1]
for _ in range(MAXK + 20):
    F.append(F[-1] + F[-2])
def L(m):
    return 2 if m == 0 else F[m-1] + F[m+1]
def expected(k):
    if k % 2:
        return 2 if k % 6 == 3 else 1
    m = k//2
    return L(m) if m%2 else (F[m] if m%4==2 else 3*F[m])
A=[[0,0,0,1],[1,1,1,1],[1,2,4,8],[8,12,18,27]]
det=0
for perm in permutations(range(4)):
    inversions=sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
    product=1
    for i,j in enumerate(perm):product*=A[i][j]
    det+=(-1 if inversions%2 else 1)*product
assert abs(det)==2,det
for n in range(0,MAXK):
    u=lambda i:F[i]**3
    assert u(n+4)==3*u(n+3)+6*u(n+2)-3*u(n+1)-u(n)
for k in range(1,MAXK+1):
    a,b=F[k-1],F[k]
    c=0
    for z in [a**3-1,3*a*a*b,3*a*b*b,b**3]:c=gcd(c,z)
    d=0
    for n in range(4):d=gcd(d,F[n+k]**3-F[n]**3)
    value=expected(k)
    assert (c,d)==(value,value),(k,c,d,value)
    for n in range(4,12):
        assert (F[n+k]**3-F[n]**3)%value==0,(k,n)
assert expected(8)==9
print('VERIFY_OK k=1..500, four-shift gcd and coefficient content agree with formula')
