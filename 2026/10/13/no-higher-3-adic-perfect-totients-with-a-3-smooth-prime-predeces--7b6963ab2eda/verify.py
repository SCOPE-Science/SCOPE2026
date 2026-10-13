#!/usr/bin/env python3
from math import isqrt


def factor(n):
    f={}
    d=2
    while d*d<=n:
        while n%d==0:
            f[d]=f.get(d,0)+1
            n//=d
        d=3 if d==2 else d+2
    if n>1:
        f[n]=f.get(n,0)+1
    return f


def phi(n):
    r=n
    for p in factor(n):
        r=r//p*(p-1)
    return r


def isprime(n):
    if n<2:
        return False
    if n%2==0:
        return n==2
    d=3
    while d*d<=n:
        if n%d==0:
            return False
        d+=2
    return True


def tail_sum_from(n):
    s=0
    while True:
        s+=n
        if n==1:
            return s
        n=phi(n)


def perfect_totient(n):
    return tail_sum_from(phi(n))==n

formula_checks=0
for A in range(1,11):
    for B in range(0,9):
        m=(2**A)*(3**B)
        got=tail_sum_from(m)
        want=(2**(A-1))*(3**(B+1)+1)-1
        assert got==want,(A,B,got,want)
        formula_checks+=1

parameter_checks=0
perfect_hits=[]
for a in range(1,9):
    for b in range(0,7):
        p=(2**a)*(3**b)+1
        if not isprime(p) or p<=3:
            continue
        for k in range(1,7):
            n=(3**k)*p
            got=perfect_totient(n)
            expected=(k==1 and a==2)
            assert got==expected,(a,b,k,p,n,got,expected)
            parameter_checks+=1
            if got:
                perfect_hits.append((a,b,k,p))

reduced=[]
for a in range(1,80):
    for k in range(1,80):
        if 2**a==3**k+1:
            reduced.append((a,k))
assert reduced==[(2,1)],reduced

assert perfect_totient(15)
assert perfect_totient(39)
assert perfect_totient(111)
assert perfect_totient(327)
assert perfect_totient(8751)

print(
    'VERIFY_OK',
    f'formula_checks={formula_checks}',
    f'parameter_checks={parameter_checks}',
    f'perfect_hits={perfect_hits}',
    f'reduced_solutions={reduced}',
)
