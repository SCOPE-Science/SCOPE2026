#!/usr/bin/env python3
from fractions import Fraction
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

def sigma_pp(p, e):
    return (p ** (e + 1) - 1) // (p - 1)

def abundancy(factors):
    out = Fraction(1, 1)
    for p, e in factors:
        out *= Fraction(sigma_pp(p, e), p ** e)
    return out

def main():
    s = sigma_pp(31, 4)
    assert s == 954305
    assert s == 5 * 11 * 17351
    assert is_prime(17351)

    a = abundancy([(2,1),(5,2),(31,4),(11,2),(17351,2)])
    expected = Fraction(120128746647, 56859400510)
    assert a == expected
    assert a > Fraction(21, 10)
    assert a - Fraction(21, 10) == Fraction(362002788, 28429700255)

    primes = [p for p in range(2, 10001) if is_prime(p) and p % 3 == 1]
    checks = 0
    for p in primes:
        for e in range(2, 31, 2):
            lhs = sigma_pp(p, e) % 3 == 0
            rhs = e % 6 == 2
            assert lhs == rhs, (p, e, sigma_pp(p, e) % 3)
            checks += 1

    print('VERIFY_OK')
    print('sigma_31_4=' + str(s))
    print('sigma_31_4_factorization=5*11*17351')
    print('17351_prime=true')
    print('abundancy_forced_divisor=' + str(a))
    print('abundancy_excess=' + str(a - Fraction(21,10)))
    print('local_congruence_checks=' + str(checks))

if __name__ == '__main__':
    main()
