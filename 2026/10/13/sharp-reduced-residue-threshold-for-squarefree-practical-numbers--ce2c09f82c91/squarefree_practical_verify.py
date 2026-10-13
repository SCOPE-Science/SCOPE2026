"""Finite checks for a sharp reduced-progression threshold for squarefree practical integers.

Uses only the Python 3 standard library; finite tests supplement an unrestricted proof.
"""
from math import gcd, isqrt


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    return not any(n % p == 0 for p in range(3, isqrt(n) + 1, 2))


def next_prime(n):
    q = n + 1
    while not is_prime(q):
        q += 1
    return q


def factorization(n):
    factors = {}
    p = 2
    while p * p <= n:
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            factors[p] = e
        p = 3 if p == 2 else p + 2
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def sigma(n):
    product = 1
    for p, e in factorization(n).items():
        product *= (p ** (e + 1) - 1) // (p - 1)
    return product


def practical_squarefree(n):
    factors = factorization(n)
    if n == 1:
        return True
    if min(factors) != 2 or any(e != 1 for e in factors.values()):
        return False
    partial = 1
    for p in sorted(factors):
        if p > sigma(partial) + 1:
            return False
        partial *= p
    return True


checked = 0
for modulus in range(1, 5005):
    if gcd(modulus, 6) != 1:
        continue
    n = 6
    assert gcd(n, modulus) == 1 and practical_squarefree(n)
    p = 3
    for index in range(1, 11):
        q = next_prime(p)
        while modulus % q == 0:
            q = next_prime(q)
        assert q <= sigma(n) + 1
        n *= q
        assert gcd(n, modulus) == 1 and practical_squarefree(n)
        p = q
        checked += 1
print('greedy_extension_10_steps_each_modulus_below_5005=',checked,'PASS')

assert all(practical_squarefree(n) for n in [1, 2, 6, 30, 42, 66, 78, 210])
assert all(not practical_squarefree(n) for n in [3, 5, 10, 14, 18, 26])
for n in range(1, 100000):
    if practical_squarefree(n) and gcd(n, 5005) == 1:
        assert n in (1, 2, 6), n
print('direct_squarefree_practical_coprime_5005_under_100000=PASS')

for modulus in (5, 7, 11, 13, 35, 77, 385):
    n = 6
    p = 3
    while n < max(10000, 30 * modulus):
        q = next_prime(p)
        while modulus % q == 0:
            q = next_prime(q)
        n *= q
        p = q
    upper = sigma(n) + 1
    assert upper > 2 * p
    for b in range(modulus):
        if gcd(b, modulus) != 1:
            continue
        target = b * pow(n, -1, modulus) % modulus
        found = None
        for q in range(max(2, upper // 2), upper + 1):
            if q % modulus == target and is_prime(q):
                found = q
                break
        assert found is not None, (modulus, b, n, upper)
        assert practical_squarefree(n * found)
        assert n * found % modulus == b
print('finite_reduced_residue_witnesses_moduli_5_7_11_13_35_77_385=PASS')
print('VERIFY_OK')
