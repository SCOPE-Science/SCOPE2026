"""Alternative computational checks for the central-binomial character-parity theorem.

No external dependencies. Run: python verify.py
"""
from math import comb, isqrt
from collections import Counter


def isprime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def chi(a, p):
    a %= p
    return 0 if not a else (1 if pow(a, (p - 1) // 2, p) == 1 else -1)


def first_failure(p):
    for m in range(1, 6):
        c = comb(2 * m, m)
        if c % p and chi(c, p) != (-1) ** m:
            return m
    return None


def predicted_first(p):
    if p in (3, 5):
        return None
    if chi(2, p) == 1:
        return 1
    if chi(3, p) == 1:
        return 2
    if chi(5, p) == 1:
        return 3
    if chi(7, p) == -1:
        return 4
    return 5


def lucas_central(n, p):
    res = 1
    while n:
        d = n % p
        if 2 * d >= p:
            return 0
        res = res * comb(2 * d, d) % p
        n //= p
    return res


def count_class(L):
    # Assesses the actual shifted central-binomial sequence.
    cnt = Counter(lucas_central(2 * n + 1, 5) for n in range((5 ** L - 1) // 2))
    assert set(cnt) <= {0, 2, 3}
    # Integer arithmetic avoids rounding in the claim's closed form.
    real, imag = 1, 0
    for _ in range(L):
        real, imag = 2 * real - imag, real + 2 * imag
    c2 = (3 ** L - 1 + 2 * imag) // 4
    c3 = (3 ** L - 1 - 2 * imag) // 4
    c0 = (5 ** L - 3 ** L) // 2
    assert (3 ** L - 1 + 2 * imag) % 4 == 0
    assert (3 ** L - 1 - 2 * imag) % 4 == 0
    assert [cnt[x] for x in (0, 2, 3)] == [c0, c2, c3], (L, cnt, c0, c2, c3)
    return cnt


def verify():
    primes = [p for p in range(3, 5000, 2) if isprime(p)]
    cs = Counter()
    for p in primes:
        got = first_failure(p)
        want = predicted_first(p)
        assert got == want, (p, got, want)
        cs[got] += 1
    # Independent whole-binomial test (not Lucas) on exceptions.
    for p in (3, 5):
        for m in range(1, 701):
            c = comb(2 * m, m)
            if c % p:
                assert chi(c, p) == (-1) ** m, (p, m)
    # Each of 16 Legendre sign patterns occurs exactly 12 times
    # in units modulo lcm(8,12,5,7)=840.
    signs = Counter()
    for u in range(1, 840):
        if __import__('math').gcd(u, 840) == 1:
            # Evaluate Dirichlet character signs using small prime
            # representatives with the same residue mod 840.
            pp = u + 840
            while not isprime(pp):
                pp += 840
            signs[tuple(chi(a, pp) for a in (2, 3, 5, 7))] += 1
    assert len(signs) == 16 and set(signs.values()) == {12}, signs
    digit_results = {L: dict(count_class(L)) for L in range(1, 7)}
    print('VERIFY_OK primes_tested=', len(primes), 'first_failure_counts=', dict(cs),
          'exceptional_indices=', 2 * 700, 'dirichlet_patterns=', len(signs),
          'digit_levels=', len(digit_results), 'max_shifted_terms=', (5 ** 6 - 1) // 2)
    print('digit_counts=', digit_results)


if __name__ == '__main__':
    verify()
