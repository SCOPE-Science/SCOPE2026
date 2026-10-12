"""Reproducible exact checks for the modular-energy complete-period moment law.

Run with Python >=3.9: python verification.py
Only the Python standard library is required.
"""
from fractions import Fraction
from math import gcd, lcm


def j2(n):
    # Jordan totient of order 2, calculated by its prime factorization.
    value = n * n
    x = n
    p = 2
    while p * p <= x:
        if x % p == 0:
            value = value // (p * p) * (p * p - 1)
            while x % p == 0:
                x //= p
        p += 1
    if x > 1:
        value = value // (x * x) * (x * x - 1)
    return value


def energy(m, n):
    return sum(n % k for k in range(1, m + 1))


def moment_gcd(m):
    return Fraction(sum(gcd(k, ell)**2 - 1 for k in range(1, m+1)
                        for ell in range(1, m+1)), 12)


def moment_jordan(m):
    return Fraction(sum(j2(d) * (m // d)**2 for d in range(1, m+1)) - m*m, 12)


def brute_moment(m):
    period = lcm(*range(1, m+1))
    mean = Fraction(m * (m-1), 4)
    return sum((Fraction(energy(m, n)) - mean)**2 for n in range(period)) / period


def brute_covariance(k, ell):
    period = lcm(k, ell)
    a = Fraction(k-1, 2)
    b = Fraction(ell-1, 2)
    return sum((Fraction(n % k) - a) * (Fraction(n % ell) - b)
               for n in range(period)) / period


if __name__ == '__main__':
    for k in range(1, 21):
        for ell in range(1, 21):
            assert brute_covariance(k, ell) == Fraction(gcd(k,ell)**2-1, 12), (k,ell)
    print('PASS: 400 exact covariance identities for moduli 1..20')

    for m in range(1, 10):
        a = brute_moment(m)
        b = moment_gcd(m)
        c = moment_jordan(m)
        assert a == b == c, (m,a,b,c)
        print(f'PASS: m={m}: complete-period variance = {a}')

    for m in range(1, 151):
        assert moment_gcd(m) == moment_jordan(m), m
    print('PASS: 150 exact gcd/Jordan-formula comparisons, m=1..150')
    print('The limiting cubic constant and infinite claims are established by proof, not finite checking.')
