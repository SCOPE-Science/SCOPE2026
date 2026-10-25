"""Finite corroboration of the square-avoidance theorem for relatively prime subsets.

The proof for all n is in RESULT.md; this script checks exact finite cases only.
Run: python verify.py
"""
from math import gcd, isqrt


def primes_dividing(n):
    ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            ans.append(d)
            while n % d == 0:
                n //= d
        d = 3 if d == 2 else d + 2
    if n > 1:
        ans.append(n)
    return ans


def mobius_value(n):
    ans = 1
    d = 2
    while d * d <= n:
        if n % d == 0:
            n //= d
            if n % d == 0:
                return 0
            ans = -ans
        d += 1
    return -ans if n > 1 else ans


def phi_exact(n):
    return sum(mobius_value(d) * (2 ** (n // d) - 1)
               for d in range(1, n + 1) if n % d == 0)


def phi_exhaustive(n):
    result = 0
    for mask in range(1, 1 << n):
        g = n
        for a in range(1, n + 1):
            if mask & (1 << (a - 1)):
                g = gcd(g, a)
                if g == 1:
                    break
        if g == 1:
            result += 1
    return result


for n in range(1, 16):
    assert phi_exact(n) == phi_exhaustive(n), (n, phi_exact(n))

for n in range(2, 1001):
    val = phi_exact(n)
    assert val > 0 and isqrt(val) ** 2 != val, n
    if n % 2:
        rad = 1
        for p in primes_dividing(n):
            rad *= p
        t = n // rad
        assert t % 2 == 1
        assert val % (2 ** t) == 0
        assert (val // (2 ** t)) % 2 == 1
    else:
        m = n // 2
        assert (2 ** m - 1) ** 2 < val < (2 ** m) ** 2
        r = sum(1 for p in primes_dividing(m) if p > 2)
        if m >= 3:
            # Finite exact check of the estimate used in the proof.
            assert r * 2 ** (2 * m // 3) < 2 ** m - 1
print('VERIFY_OK: 15 exhaustive and 999 exact Möbius cases')
