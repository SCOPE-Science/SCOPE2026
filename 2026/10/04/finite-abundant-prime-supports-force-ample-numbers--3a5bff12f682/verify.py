#!/usr/bin/env python3
from functools import lru_cache
from itertools import product
from fractions import Fraction
import math

Q = (3, 5, 7, 11, 13)
EXPS = (9, 5, 2, 1, 1)

@lru_cache(None)
def recursive_divisors(exps):
    if all(e == 0 for e in exps):
        return 1
    total = 1
    ranges = [range(e + 1) for e in exps]
    for sub in product(*ranges):
        if sub != exps:
            total += recursive_divisors(sub)
    return total

def value(primes, exps):
    n = 1
    for p, e in zip(primes, exps):
        n *= p ** e
    return n

def Z(s):
    z = 1.0
    for q in Q:
        z /= 1.0 - q ** (-s)
    return z

def main():
    prod_q = Fraction(1, 1)
    for q in Q:
        prod_q *= Fraction(q, q - 1)
    assert prod_q == Fraction(1001, 384)
    assert prod_q > 2

    n = value(Q, EXPS)
    a = recursive_divisors(EXPS)
    assert n == 430996190625
    assert a == 436791402496
    assert a > n

    lo, hi = 1.0, 3.0
    assert Z(lo) > 2.0 and Z(hi) < 2.0
    for _ in range(100):
        mid = (lo + hi) / 2.0
        if Z(mid) > 2.0:
            lo = mid
        else:
            hi = mid
    alpha = (lo + hi) / 2.0
    assert 1.18 < alpha < 1.19
    assert abs(Z(alpha) - 2.0) < 1e-12

    s = alpha + 0.001
    restricted_series = Z(s) / (2.0 - Z(s))
    hypothetical_bound = Z(s - 1.0)
    assert restricted_series > hypothetical_bound

    print("VERIFY_OK")
    print("support_product=" + str(prod_q))
    print("witness_n=" + str(n))
    print("witness_a=" + str(a))
    print("alpha_Q=" + repr(alpha))
    print("near_pole_ratio=" + repr(restricted_series))
    print("hypothetical_bound=" + repr(hypothetical_bound))

if __name__ == "__main__":
    main()
