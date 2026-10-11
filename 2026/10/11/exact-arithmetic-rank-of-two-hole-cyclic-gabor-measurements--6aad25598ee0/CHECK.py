"""Exact cyclotomic check for two-hole cyclic Gabor ambiguity zeros.

Run: python3 CHECK.py
Only uses the Python standard library. Every Fourier value is reduced in
Z[X]/Phi_n(X), so this is not a floating-point zero test.
"""
from functools import lru_cache
from math import gcd


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def monic_division(num, den):
    a = num[:]
    m = len(den) - 1
    assert den[-1] == 1
    quo = [0] * (len(num) - m)
    for k in range(len(num) - m - 1, -1, -1):
        c = a[k + m]
        quo[k] = c
        for j in range(m + 1):
            a[k + j] -= c * den[j]
    assert all(v == 0 for v in a)
    return quo


@lru_cache(None)
def cyclotomic(n):
    p = [-1] + [0] * (n - 1) + [1]
    for d in divisors(n):
        if d < n:
            p = monic_division(p, cyclotomic(d))
    assert p[-1] == 1
    return p


def powers_mod_cyclotomic(n):
    phi = cyclotomic(n)
    degree = len(phi) - 1
    cur = [1] + [0] * (degree - 1)
    powers = []
    for j in range(n):
        powers.append(tuple(cur))
        high = cur[-1]
        cur = [0] + cur[:-1]
        for i in range(degree):
            cur[i] -= high * phi[i]
    assert cur == [1] + [0] * (degree - 1)
    return powers


def predicted_zeros(n, a):
    d = gcd(n, a)
    q = n // d
    two_torsion = (
        sum(gcd(ell, n) for ell in range(1, n)
            if (n % 2 == 0 and (n // 2) % gcd(ell, n) == 0))
    )
    even_order = 0
    if q % 2 == 0:
        j = sum(gcd(2 * t + 1, d) for t in range(d))
        even_order = d * (n - 2) + (2 * d if q == 2 else 0) - (q // 2) * j
    return two_torsion + even_order + (4 * d if q % 3 == 0 else 0)


def direct_exact_zeros(n, a):
    powers = powers_mod_cyclotomic(n)
    degree = len(powers[0])
    retained = set(range(n)) - {0, a}
    zeros = 0
    for lag in range(n):
        products = [t for t in retained if (t - lag) % n in retained]
        for freq in range(n):
            coeff = [0] * degree
            for t in products:
                for i, value in enumerate(powers[(freq * t) % n]):
                    coeff[i] += value
            zeros += not any(coeff)
    return zeros


def main():
    checked = 0
    for n in range(5, 36):
        for a in range(1, n):
            predicted = predicted_zeros(n, a)
            exact = direct_exact_zeros(n, a)
            assert exact == predicted, (n, a, predicted, exact)
            checked += 1
    assert predicted_zeros(15, 1) == 4
    assert predicted_zeros(15, 3) == 0
    assert predicted_zeros(15, 5) == 20
    print(f'EXACT_CHECK_OK: {checked} pairs (5 <= n <= 35, 1 <= a < n)')


if __name__ == '__main__':
    main()
