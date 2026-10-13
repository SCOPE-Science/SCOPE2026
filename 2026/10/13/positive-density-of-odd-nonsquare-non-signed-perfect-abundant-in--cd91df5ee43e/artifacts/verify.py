#!/usr/bin/env python3
"""Exact finite checks for the odd-abundant-square density theorem."""
from math import gcd, isqrt, prod
from fractions import Fraction

def primes_upto(n):
    a = bytearray(b'\x01') * (n + 1)
    a[0:2] = b'\x00\x00'
    for p in range(2, isqrt(n) + 1):
        if a[p]:
            a[p*p:n+1:p] = b'\x00' * ((n-p*p)//p + 1)
    return [p for p in range(2,n+1) if a[p]]

def factor(n):
    f=[]
    d=2
    while d*d<=n:
        if n%d==0:
            e=0
            while n%d==0:
                n//=d;e+=1
            f.append((d,e))
        d+=1
    if n>1:f.append((n,1))
    return f

def sigma(n):
    return prod((p**(e+1)-1)//(p-1) for p,e in factor(n))

a=11025
C=sigma(a)
assert factor(a)==[(3,2),(5,2),(7,2)]
assert C==22971 and C-2*a==921 and (C-2*a)//2==460
Y=50000
assert Y>C+1 and Y>7
P=primes_upto(Y+100)
assert len([p for p in P if p<=Y])==5133
rho=prod((p-1)/p for p in P if p<=Y)
lower=rho*(1-Fraction(C+1,Y))/a
assert lower>0

def witness(m):
    assert m>1 and gcd(m,a)==1 and m%2==1
    assert isqrt(m)**2!=m
    sm=sigma(m)-m
    b=C*sm
    assert b<m
    n=a*m
    assert sigma(n)==C*sigma(m)>2*n
    H=(sigma(n)-2*n)//2
    h=(C-2*a-1)//2
    assert (sigma(n)-2*n)%2==0
    assert h*m+b < H < (h+1)*m
    return n
p1=next(p for p in P if p>Y)
p2=next(p for p in P if p>p1)
n1=witness(p1)
n2=witness(p1*p2)
# The density proof is analytic and follows the exact inequality sum_{k>Y} 1/[k(k-1)]=1/Y.
assert Fraction(1,Y)==Fraction(1,Y+1)+Fraction(1,Y*(Y+1))
print(f'VERIFY_OK anchor={a} sigma={C} delta=921 h=460 piY=5133 '
      f'Y={Y} n_prime={n1} n_composite={n2} '
      f'rho_approx={rho:.12g} lower_density_approx={lower:.12g} '
      'interval_checks=yes analytic_density_proof=separate')
