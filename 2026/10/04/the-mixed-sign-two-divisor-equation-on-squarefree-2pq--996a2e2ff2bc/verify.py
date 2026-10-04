#!/usr/bin/env python3
from itertools import combinations
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

def divisors_2pq(p, q):
    return sorted({1,2,p,2*p,q,2*q,p*q,2*p*q})

def sigma_2pq(p, q):
    return 3*(p+1)*(q+1)

EXPECTED = {
    (3,5):(15,3),
    (3,7):(14,2),
    (5,7):(5,1),
    (3,13):(13,1),
    (5,11):(1,5),
    (5,13):(2,10),
    (7,11):(2,22),
    (5,17):(1,17),
}

def direct_pairs(p, q):
    n = 2*p*q
    target = sigma_2pq(p,q) - 2*n
    ds = divisors_2pq(p,q)
    return [(d1,d2) for d1 in ds for d2 in ds if d1 != d2 and d1-d2 == target]

def symbolic_small_cases():
    # p=3: tq-s=12, s,t in {1,2,3,6}.
    A = [1,2,3,6]
    qs3 = set()
    for t in A:
        for s in A:
            if (12+s) % t == 0:
                q = (12+s)//t
                if q > 3 and is_prime(q):
                    qs3.add(q)
    assert qs3 == {5,7,13}

    # p=5: q=7 is the positive-D case. For q>=11,
    # same-block differences force q<=13; mixed block obeys (t-2)q=s-18.
    qs5 = {7}
    for q in (11,13):
        E = 2*q-18
        A = [1,2,5,10]
        if any(b-a == E for a in A for b in A if a != b):
            qs5.add(q)
    for t in [1,2,5,10]:
        for s in [1,2,5,10]:
            den = t-2
            num = s-18
            if den != 0 and num % den == 0:
                q = num//den
                if q > 5 and is_prime(q):
                    qs5.add(q)
    assert qs5 == {7,11,13,17}

    # p=7: (t-4)q=s-24.
    qs7 = set()
    for t in [1,2,7,14]:
        for s in [1,2,7,14]:
            den = t-4
            num = s-24
            if den != 0 and num % den == 0:
                q = num//den
                if q > 7 and is_prime(q):
                    qs7.add(q)
    assert qs7 == {11}

def check_large_prime_inequalities():
    # Algebraic boundary check used in the p>=11 proof.
    p, q = 11, 13
    assert q*(p-3)-5*p-2 == 47 > 0
    # For larger p,q with q>p, the expression increases in each variable.
    assert p*(p-4) >= 7*p > 3*p+2
    assert p*(p-5) >= 6*p > 3*p+2

def main():
    symbolic_small_cases()
    check_large_prime_inequalities()

    for (p,q), witness in EXPECTED.items():
        n = 2*p*q
        d1,d2 = witness
        assert d1 in divisors_2pq(p,q)
        assert d2 in divisors_2pq(p,q)
        assert d1 != d2
        assert sigma_2pq(p,q) == 2*n + d1 - d2
        assert witness in direct_pairs(p,q)

    # Independent bounded regression only.
    primes = [x for x in range(3,2000,2) if is_prime(x)]
    found = {}
    for i,p in enumerate(primes):
        for q in primes[i+1:]:
            pairs = direct_pairs(p,q)
            if pairs:
                found[(p,q)] = pairs
    assert set(found) == set(EXPECTED)

    values = sorted(2*p*q for p,q in EXPECTED)
    assert values == [30,42,70,78,110,130,154,170]

    print("VERIFY_OK")
    print("values=" + repr(values))
    print("prime_pairs=" + repr(sorted(EXPECTED)))
    print("regression_prime_bound=2000")

if __name__ == "__main__":
    main()
