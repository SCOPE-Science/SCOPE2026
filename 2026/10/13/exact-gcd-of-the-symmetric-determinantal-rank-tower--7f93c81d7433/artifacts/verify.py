from fractions import Fraction
from math import comb, gcd

def degree(n, q):
    x = Fraction(1, 1)
    for j in range(q):
        x *= Fraction(comb(n+j, q-j), comb(2*j+1, j))
    assert x.denominator == 1
    return x.numerator

def vp(x, p):
    e = 0
    while x % p == 0:
        x //= p
        e += 1
    return e

def primes_of(n):
    out = []
    p = 2
    m = n
    while p*p <= m:
        if m % p == 0:
            out.append(p)
            while m % p == 0:
                m //= p
        p += 1
    if m > 1:
        out.append(m)
    return out

def s2(n):
    return n.bit_count()

tower_cases = 0
witness_checks = 0
for n in range(2, 121):
    g = 0
    for q in range(1, n):
        g = gcd(g, degree(n, q))
        tower_cases += 1

    if n == 2:
        expected = 2
    elif n & (n - 1) == 0:
        expected = n // 2
    else:
        expected = 1
    assert g == expected, (n, g, expected)

    if n >= 3 and n & (n - 1):
        for p in primes_of(n):
            e = 0
            m = n
            while m % p == 0:
                m //= p
                e += 1
            q = p ** e
            if q < n:
                assert vp(degree(n, q), p) == 0
            else:
                assert p % 2 == 1
                assert degree(n, n - 1) == 2 ** (n - 1)
                assert vp(degree(n, n - 1), p) == 0
            witness_checks += 1

valuation_checks = 0
for e in range(2, 9):
    n = 2 ** e
    for m in range(1, n // 2):
        even_q = 2 * m
        even_v = vp(degree(n, even_q), 2)
        closed = m * (e - 1) - 2 * sum(s2(u) for u in range(m))
        assert even_v == closed
        assert even_v >= e - 1
        valuation_checks += 1

        odd_q = 2 * m - 1
        assert vp(degree(n, odd_q), 2) == even_v + (2 * m - 1)
        valuation_checks += 1

    assert vp(degree(n, 2), 2) == e - 1

print("VERIFY_OK", tower_cases, witness_checks, valuation_checks)
