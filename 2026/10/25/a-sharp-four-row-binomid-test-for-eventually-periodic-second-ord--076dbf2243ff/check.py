#!/usr/bin/env python3
"""Finite checks supporting an exact criterion for binomid recurrences.

This checker is illustrative; the theorem is proved for all indices in RESULT.md.
"""
from math import gcd


def fnomial(f, n, k):
    if k in (0, n):
        return 1, 1
    num = 1
    den = 1
    for j in range(n-k+1, n+1):
        num *= f(j)
    for j in range(1, k+1):
        den *= f(j)
    return num, den


def is_binomid_to(f, N):
    return all((num % den == 0)
               for n in range(1, N+1)
               for k in range(n+1)
               for num, den in [fnomial(f,n,k)])


def periodic(pattern):
    return lambda n: pattern[(n-1)%len(pattern)]


def exceptional_transient(a,b,sign):
    return lambda n: a if n==1 else b*sign**(n-2)


def is_divisible_to(f,N):
    return all(f(j)%f(i)==0
               for i in range(1,N+1)
               for j in range(i,N+1,i))


def is_strong_to(f,N):
    return all(gcd(abs(f(i)),abs(f(j)))==abs(f(gcd(i,j)))
               for i in range(1,N+1) for j in range(1,N+1))


def test_family(a,b):
    if b%a:
        return
    patterns=[(a,b),(a,b,-a,-b),(a,a,-2*a),
              (a,-a,-2*a,-a,a,2*a)]
    for pattern in patterns:
        f=periodic(pattern)
        assert is_binomid_to(f,30),(a,b,pattern)
        assert is_divisible_to(f,30)
        assert is_strong_to(f,30)
    for sign in [-1,1]:
        f=exceptional_transient(a,b,sign)
        assert is_binomid_to(f,30)
        assert is_divisible_to(f,30)


def test_necessity():
    # All nonzero periodic solutions of second-order cyclotomic recurrences
    # are covered by these symbolic patterns. Exhaust finite parameter samples.
    forms=[lambda a,b: (a,b),lambda a,b:(a,b,-a,-b),
           lambda a,b:(a,b,-a-b),
           lambda a,b:(a,b,b-a,-a,-b,a-b)]
    checks=0
    for a in range(-6,7):
        for b in range(-7,8):
            if a==0 or b==0:continue
            for form in forms:
                p=form(a,b)
                if 0 in p:continue
                f=periodic(p)
                two=(b%a==0 and (f(3)*f(4))%(a*b)==0)
                actual=is_binomid_to(f,24)
                assert two==actual,(a,b,p,two,actual)
                checks+=1
            for s in (-1,1):
                f=exceptional_transient(a,b,s)
                two=(b%a==0 and (f(3)*f(4))%(a*b)==0)
                assert two==is_binomid_to(f,24)
                checks+=1
    return checks


def witness():
    f=periodic((1,2,-3))
    assert is_binomid_to(f,3)
    assert fnomial(f,4,2)==(-3,2)
    return 'rows <= 3 integral but [4,2] = -3/2'


if __name__=='__main__':
    for a in (-5,-2,-1,1,2,5):
        for t in (-6,-3,-1,1,4):
            test_family(a,a*t)
    print('PASS: all six positive/negative signed families through n=30')
    print('PASS:',test_necessity(),'second-order periodic/transient parameter cases through n=24')
    print('PASS: sharpness witness:',witness())
