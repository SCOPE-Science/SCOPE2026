#!/usr/bin/env python3
from math import isqrt

LIMIT = 200000

def spf_sieve(n):
    spf = list(range(n + 1))
    if n >= 1:
        spf[1] = 1
    for p in range(2, isqrt(n) + 1):
        if spf[p] == p:
            for m in range(p * p, n + 1, p):
                if spf[m] == m:
                    spf[m] = p
    return spf

SPF = spf_sieve(LIMIT)

def factorint(n):
    f = {}
    while n > 1:
        p = SPF[n]
        f[p] = f.get(p, 0) + 1
        n //= p
    return f

def divisors_from_factorization(f):
    ds = [1]
    for p, a in f.items():
        old = list(ds)
        mul = 1
        add = []
        for _ in range(a):
            mul *= p
            add.extend(d * mul for d in old)
        ds.extend(add)
    return sorted(ds, reverse=True)

def chi(n):
    ds = divisors_from_factorization(factorint(n))
    return sum(d if i % 2 == 0 else -d for i, d in enumerate(ds))

def phi(n):
    if n == 1:
        return 1
    out = n
    for p in factorint(n):
        out -= out // p
    return out

def is_prime(n):
    return n >= 2 and SPF[n] == n

def is_prime_square(n):
    r = isqrt(n)
    return r * r == n and is_prime(r)

def zero_expected(n):
    return n == 1 or is_prime(n)

def one_expected(n):
    return n == 8 or is_prime_square(n)

def two_expected(n):
    if n == 27:
        return True
    if n % 2:
        return False
    q = n // 2
    return q % 2 == 1 and is_prime(q)

def main():
    anchor = [
        0,0,0,1,0,2,0,1,1,2,0,4,0,2,4,3,0,7,0,4,4,2,0,8,1,2,2,6,0,14
    ]
    got_anchor = []
    counts = {0: 0, 1: 0, 2: 0}
    for n in range(1, LIMIT + 1):
        d = chi(n) - phi(n)
        assert d >= 0, (n, d)
        assert (d == 0) == zero_expected(n), (n, d, "zero")
        assert (d == 1) == one_expected(n), (n, d, "one")
        assert (d == 2) == two_expected(n), (n, d, "two")
        if d in counts:
            counts[d] += 1
        if n <= len(anchor):
            got_anchor.append(d)
    assert got_anchor == anchor, (got_anchor, anchor)
    print("VERIFY_OK")
    print("checked_n_max=" + str(LIMIT))
    print("oeis_a382545_first_30_match=true")
    print("zero_fiber_count_through_limit=" + str(counts[0]))
    print("one_fiber_count_through_limit=" + str(counts[1]))
    print("two_fiber_count_through_limit=" + str(counts[2]))

if __name__ == "__main__":
    main()
