#!/usr/bin/env python3
"""Exact integer verification for a ternary-repunit cototient orbit theorem.
Finite tests supplement the symbolic proof; no external dependencies.
"""
from math import isqrt

def prime_factors(n):
    out = []
    d = 2
    while d*d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0: n //= d
        d = 3 if d == 2 else d+2
    if n > 1: out.append(n)
    return out

def phi(n):
    ans = n
    for p in prime_factors(n): ans -= ans//p
    return ans

def cototient(n):
    return n-phi(n)

def height(n):
    steps = 0
    while n > 1:
        nxt = cototient(n)
        assert 1 <= nxt < n, (n,nxt)
        n = nxt
        steps += 1
    return steps

def check(q,h,ar,br,cr):
    assert q > 3 and prime_factors(q)==[q]
    assert 2*q+1 == 3**h
    count=0
    for a in ar:
        for b in br:
            for c in cr:
                n = 2**a*3**b*q**c
                want = a+2*b+(2*h-1)*c
                assert height(n)==want,(q,a,b,c)
                x=n
                for j in range(c+1):
                    assert x == 2**a*3**(b+(h-1)*j)*q**(c-j)
                    if j<c:x=cototient(x)
                d=b+(h-1)*c
                for j in range(d+1):
                    assert x==2**(a+j)*3**(d-j)
                    if j<d:x=cototient(x)
                for j in range(a+d+1):
                    assert x==2**(a+d-j)
                    if j<a+d:x=cototient(x)
                assert x==1
                count+=1
    return count

if __name__ == '__main__':
    good=check(13,3,range(1,7),range(1,6),range(1,5))
    good2=check(1093,7,range(1,5),range(1,5),range(1,4))
    disallowed=0
    for q in range(5,300,2):
        if q==13 or prime_factors(q)!=[q]:continue
        y=cototient(2*3*q)
        assert any(p not in (2,3,q) for p in prime_factors(y)),(q,y)
        disallowed+=1
    assert height(2*3*13)==8
    assert height(4*3*13)==9
    print('VERIFY_OK')
    print('ternary_repunit_prime_13_exponent_triples='+str(good)+'_PASS')
    print('ternary_repunit_prime_1093_exponent_triples='+str(good2)+'_PASS')
    print('full_orbit_state_by_state_and_height=PASS')
    print('other_odd_primes_below_300_first_step_leak='+str(disallowed)+'_PASS')
    print('finite_computations_supplement_unrestricted_proof')
