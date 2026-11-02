#!/usr/bin/env python3
"""Exact-arithmetic reproducibility checks for the prime-power binomial gcd claim."""
from math import comb,gcd

def digit_sum(n,p):
    ans=0
    while n:
        ans+=n%p
        n//=p
    return ans

def vp_factorial(n,p):
    ans=0
    while n:
        n//=p
        ans+=n
    return ans

def vp_integer(n,p):
    assert n>0
    ans=0
    while n%p==0:
        n//=p
        ans+=1
    return ans


def run():
    count=0
    direct=0
    cases=0
    for p in (2,3,5,7,11,13,17):
        exponent=1
        while p**exponent<=243:
            N=p**exponent
            if N>=3:
                k=N-1
                for q in range(2,N+1):
                    top=q*k
                    from_factorials=(vp_factorial(top,p)-vp_factorial(k,p)-vp_factorial(top-k,p))
                    from_digits=(digit_sum(k,p)+digit_sum(top-k,p)-digit_sum(top,p))//(p-1)
                    assert from_factorials==from_digits==exponent, (p,exponent,q)
                    assert digit_sum(top,p)==digit_sum(top-k,p)==exponent*(p-1)
                    if N<=32:
                        assert vp_integer(comb(top,k),p)==exponent,(p,exponent,q,'direct')
                        direct+=1
                    count+=1
                if N<=32:
                    g=0
                    for q in range(2,N+1):
                        g=gcd(g,comb(q*k,k))
                    assert g==N,(p,exponent,g)
                cases+=1
            exponent+=1
    print(f'VERIFY_OK prime_powers={cases} binomial_valuations={count} direct_binomials={direct}')

if __name__=='__main__':
    run()
