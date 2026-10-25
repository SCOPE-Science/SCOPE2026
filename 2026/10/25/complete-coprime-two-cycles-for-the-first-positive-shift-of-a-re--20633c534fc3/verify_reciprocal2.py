"""Exact arithmetic consistency tests for the reciprocal quadratic classification.

Finite tests support the proof and are not a proof of its infinite quantifiers.
"""
from math import gcd, isqrt


def f(n):
    return n * n - n + 2


def expected(d):
    return (d * d - d + 2) // 2, (d * d + d + 2) // 2


def divisors(n):
    for k in range(1, isqrt(n) + 1):
        if n % k == 0:
            yield k
            if k * k != n:
                yield n // k


checked = 0
for a in range(1, 3000):
    for b in divisors(f(a)):
        if b <= a or gcd(a, b) != 1:
            continue
        if f(b) % a:
            continue
        checked += 1
        d = b - a
        assert (a, b) == expected(d)
        assert d % 2 == 1 or d % 4 == 0

for d in range(1, 8000):
    a, b = expected(d)
    assert b - a == d
    assert f(b) % a == 0
    assert f(a) % b == 0
    assert (gcd(a, b) == 1) == (d % 2 == 1 or d % 4 == 0)

# The first four simultaneous prime examples are arithmetically valid.
for a,b in [(7,11),(29,37),(67,79),(191,211)]:
    assert f(a)%b==f(b)%a==0
    assert all(a%k and b%k for k in range(2,isqrt(b)+1))
print(f'VERIFY_OK coprime_pairs={checked} parameter_cases=7999 prime_examples=4')
