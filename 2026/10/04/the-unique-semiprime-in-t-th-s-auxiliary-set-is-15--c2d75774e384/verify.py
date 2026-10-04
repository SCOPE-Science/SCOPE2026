#!/usr/bin/env python3
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d <= isqrt(n):
        if n % d == 0:
            return False
        d += 2
    return True

def sigma_semiprime(p,q):
    if p == q:
        return p*p+p+1
    return (p+1)*(q+1)

def in_S_semiprime(p,q):
    n = p*q
    s = sigma_semiprime(p,q)
    d = 2*n-s
    return d > 0 and s % d == 0, (s//d if d > 0 and s % d == 0 else None)

def divisors(n):
    out=[]
    for d in range(1,isqrt(n)+1):
        if n%d==0:
            out.append(d)
            if d*d!=n:
                out.append(n//d)
    return sorted(out)

def main():
    # Exact factorization branches for distinct primes.
    sol2=[]
    for u in divisors(12):
        v=12//u
        if u < v and u%2==0 and v%2==0:
            p,q=u+3,v+3
            if is_prime(p) and is_prime(q):
                sol2.append((p,q))
    assert sol2 == []

    # x=3: both factors would be odd but their product would be 6.
    assert all(not (u%2==1 and (6//u)%2==1) for u in divisors(6) if 6%u==0)

    sol4=[]
    for u in divisors(40):
        v=40//u
        if u < v and u%3==1 and v%3==1 and (u+5)%3==0 and (v+5)%3==0:
            p,q=(u+5)//3,(v+5)//3
            if p%2 and q%2 and is_prime(p) and is_prime(q):
                sol4.append((p,q))
    assert sol4 == [(3,5)]

    ok,x=in_S_semiprime(3,5)
    assert ok and x==4

    # Prime-square branch.
    assert sigma_semiprime(3,3) == 13
    assert 2*9-13 == 5
    for p in range(5,500,2):
        if is_prime(p):
            s=p*p+p+1
            d=p*p-p-1
            assert d < s < 2*d

    # Bounded regression only.
    limit=200000
    primes=[p for p in range(3,limit+1,2) if is_prime(p)]
    found=set()
    for i,p in enumerate(primes):
        if p*p>limit:
            break
        for q in primes[i:]:
            if p*q>limit:
                break
            ok,x=in_S_semiprime(p,q)
            if ok:
                found.add((p*q,p,q,x))
    assert found == {(15,3,5,4)}

    print("VERIFY_OK")
    print("classification=[15]")
    print("witness_x=4")
    print("regression_limit=200000")

if __name__ == "__main__":
    main()
