"""Independent finite checks for a local denominator theorem of a reciprocal-gcd sum.

All calculations are exact apart from the separately labelled numerical Euler-product
approximation. Finite checks are not a proof of the asymptotic.
"""
from fractions import Fraction
from math import gcd, gamma, log, pi, sqrt


def v3(t):
    k = 0
    while t % 3 == 0:
        t //= 3
        k += 1
    return k


def factor(n):
    result = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            result.append((p, e))
        p += 1
    if n > 1:
        result.append((n, 1))
    return result


def predicted(n):
    a = 0
    k = 0
    h = 1
    for p, e in factor(n):
        h *= (p ** (2 * e + 1) + 1) // (p + 1)
        if p == 3:
            a = e
        elif p % 3 == 2:
            k += v3(2 * e + 1)
    return Fraction(h, n), a > k


for n in range(1, 1001):
    direct = sum((Fraction(1, gcd(n, j)) for j in range(1, n + 1)), Fraction())
    product_value, pred = predicted(n)
    assert product_value == direct
    assert (direct.denominator % 3 == 0) == pred
print('EXACT_RATIONAL_N_1_TO_1000 PASS')


def spf_sieve(N):
    spf = list(range(N + 1))
    for p in range(2, int(N**0.5) + 1):
        if spf[p] == p:
            for k in range(p * p, N + 1, p):
                if spf[k] == k:
                    spf[k] = p
    return spf


N = 500_000
spf = spf_sieve(N)
v_exp = bytearray(N + 1)
a3 = bytearray(N + 1)
k3 = bytearray(N + 1)
count = 0
for n in range(2, N + 1):
    p = spf[n]
    m = n // p
    v_exp[n] = v_exp[m] + 1 if m % p == 0 else 1
    a3[n] = a3[m] + (p == 3)
    if p % 3 == 2:
        k3[n] = k3[m] + v3(2 * v_exp[n] + 1) - (v3(2 * v_exp[m] + 1) if m % p == 0 else 0)
    else:
        k3[n] = k3[m]
    if a3[n] > k3[n]:
        count += 1
    if n in (10000, 100000, 500000):
        print('COUNT', n, count, 'SCALED', round(count * log(n)**(1 / 3) / n, 9))
assert count == 64093
print('SIEVE_COUNT_N_500000 PASS')


def primes_below(N):
    sieve = bytearray(b'\x01') * N
    sieve[:2] = b'\x00\x00'
    for p in range(2, int(N**0.5) + 1):
        if sieve[p]:
            sieve[p*p:N:p] = b'\x00' * (((N - 1 - p*p)//p) + 1)
    return (p for p in range(2, N) if sieve[p])


def approx_constant(prime_bound):
    lp = 0.0
    for p in primes_below(prime_bound):
        if p % 3 != 2:
            continue
        e, pe, z = 1, p, 1.0
        while pe <= 10**13:
            z += 3.0 ** (-v3(2 * e + 1)) / pe
            e += 1
            pe *= p
        local = (1 - 1/p)**(2/3) * (1 + 1/p)**(1/3) * z
        lp += log(local)
    return (2/3)**(2/3) / (2 * gamma(2/3)) * (pi/(3 * sqrt(3)))**(1/3) * __import__('math').exp(lp)


val = approx_constant(20000)
assert 0.2840 < val < 0.2842
print('EULER_PRODUCT_PRIMES_BELOW_20000', round(val, 12))
print('FINITE_CHECKS_ALL_PASS (asymptotic follows from proof, not enumeration)')
