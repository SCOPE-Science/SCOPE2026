#!/usr/bin/env python3
from fractions import Fraction
from math import isqrt

def is_prime(n):
    if n<2: return False
    if n%2==0: return n==2
    d=3
    while d<=isqrt(n):
        if n%d==0: return False
        d+=2
    return True

def sigma_pow2(a):
    return 2**(a+1)-1

def sigma_two_prime(b,q):
    return (2**(b+1)-1)*(q+1)

def harmonious(a,b,q):
    return Fraction(2**a,sigma_pow2(a))+Fraction((2**b)*q,sigma_two_prime(b,q))==1

def main():
    known=[]
    for a in (2,3,5,7):
        q=2**a-1
        assert is_prime(q)
        assert harmonious(a,a,q)
        known.append((2**a,2**a*q))
    primes=[q for q in range(3,5000,2) if is_prime(q)]
    sols=[]
    for a in range(1,13):
        for b in range(1,13):
            for q in primes:
                if harmonious(a,b,q):
                    sols.append((a,b,q))
                    assert a==b
                    assert q==2**a-1
    expected=[(a,a,2**a-1) for a in range(1,13) if is_prime(2**a-1)]
    assert sols==expected
    print('VERIFY_OK')
    print('known_pairs='+repr(known))
    print('solutions='+repr(sols))
if __name__=='__main__': main()
