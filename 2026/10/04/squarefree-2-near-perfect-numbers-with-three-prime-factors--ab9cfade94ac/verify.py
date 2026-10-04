#!/usr/bin/env python3
from math import isqrt
from itertools import combinations

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

def divisors(n):
    out = []
    for d in range(1, isqrt(n)+1):
        if n % d == 0:
            out.append(d)
            if d*d != n:
                out.append(n//d)
    return sorted(out)

def sigma_2pq(p,q):
    return 3*(p+1)*(q+1)

def is_two_near_2pq(p,q):
    n = 2*p*q
    D = sigma_2pq(p,q) - 2*n
    ds = divisors(n)
    pairs = [(a,b) for a,b in combinations(ds,2) if a+b == D]
    return pairs

def main():
    # Algebraic formula and the uniform large-p exclusion.
    for p in [7,11,13,17,19]:
        assert 36 - 8*p < 0
    assert 3*(3+1)*(5+1) - 4*3*5 == 12
    assert 3*(3+1)*(11+1) - 4*3*11 == 12
    assert 3*(5+1)*(7+1) - 4*5*7 == 4

    assert (2,10) in is_two_near_2pq(3,5)
    assert is_two_near_2pq(3,7) == []
    assert (1,11) in is_two_near_2pq(3,11)
    assert is_two_near_2pq(5,7) == []

    # For p=3 and q>=13, every divisor below 12 is in {1,2,3,6}.
    for q in [13,17,19,23,29,31,37]:
        small = [d for d in divisors(6*q) if d < 12]
        assert small == [1,2,3,6]
        assert max(a+b for a,b in combinations(small,2)) == 9

    # Bounded regression, not used as proof of exhaustiveness.
    primes = [x for x in range(3,1000,2) if is_prime(x)]
    found = []
    for i,p in enumerate(primes):
        for q in primes[i+1:]:
            if is_two_near_2pq(p,q):
                found.append((p,q,2*p*q))
    assert found == [(3,5,30),(3,11,66)]

    print("VERIFY_OK")
    print("classification=[30, 66]")
    print("pairs=[(3,5),(3,11)]")
    print("witnesses=30:(2,10);66:(1,11)")

if __name__ == "__main__":
    main()
