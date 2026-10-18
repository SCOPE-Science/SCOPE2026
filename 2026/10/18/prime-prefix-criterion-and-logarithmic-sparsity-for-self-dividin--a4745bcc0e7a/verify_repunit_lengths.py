"""Exact finite checks accompanying a theorem on self-dividing decimal repunits.

Run with Python 3: python verify_repunit_lengths.py
The infinitude and asymptotic parts of the theorem require mathematical proofs.
"""

from functools import lru_cache


def smallest_factors_up_to(limit):
    least = list(range(limit + 1))
    for p in range(2, int(limit ** 0.5) + 1):
        if least[p] == p:
            for q in range(p * p, limit + 1, p):
                if least[q] == q:
                    least[q] = p
    return least


LEAST = smallest_factors_up_to(120000)


def factors(n):
    if n < len(LEAST):
        result = []
        while n > 1:
            p = LEAST[n]
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            result.append((p, e))
        return result
    result = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            result.append((p, e))
        p += 1 if p == 2 else 2
    if n > 1:
        result.append((n, 1))
    return result


@lru_cache(None)
def multiplicative_order_10(p):
    assert p > 5 and p % 2 and p % 5
    d = p - 1
    for r, _ in factors(p - 1):
        while d % r == 0 and pow(10, d // r, p) == 1:
            d //= r
    return d


def criterion(n):
    if n == 1:
        return True
    if n <= 0 or n % 2 == 0 or n % 5 == 0:
        return False
    fac = factors(n)
    if not fac or fac[0][0] != 3:
        return False
    prefix = 3 ** fac[0][1]
    for p, exponent in fac[1:]:
        if prefix % multiplicative_order_10(p):
            return False
        prefix *= p ** exponent
    return True


def direct(n):
    # Equivalent to 9n | 10**n - 1, without constructing huge repunits.
    return pow(10, n, 9 * n) == 1


def quadratic_character_10(p):
    assert p % 2 and p % 5
    return 1 if p % 40 in (1, 3, 9, 13, 27, 31, 37, 39) else -1


def regression():
    total = 0
    for n in range(1, 120001):
        value = criterion(n)
        assert value == direct(n), (n, value, direct(n))
        if value:
            total += 1
            if n > 1:
                assert n % 3 == 0
                for p, exponent in factors(n):
                    assert quadratic_character_10(p) == 1
    known = ((1, 37), (2, 333667), (3, 757), (4, 163))
    for a, q in known:
        assert factors(q) == [(q, 1)]
        assert multiplicative_order_10(q) == 3**a
        for e in range(1, 4):
            assert criterion((3**a) * q**e)
            assert direct((3**a) * q**e)
    print('SELF_DIVIDING_REPUNIT_EXACT_REGRESSION_OK',
          'range=1..120000', 'hits='+str(total), 'primitive_examples='+str(len(known)))


if __name__ == '__main__':
    regression()
