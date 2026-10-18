"""Exact certificate for the least squarefree-semiprime Egyptian rank of 1/2.

No prime tables, floating point arithmetic, or search bounds on the final
pair are assumed. Python 3.9+ standard library suffices.
"""
from fractions import Fraction
from itertools import combinations
from math import isqrt

WITNESS = (6, 10, 15, 21, 26, 35, 39, 65, 91)


def prime(n):
    if n < 2:
        return False
    return all(n % d != 0 for d in range(2, isqrt(n) + 1))


def sqfree_semiprime(n):
    if n < 6:
        return False
    for p in range(2, isqrt(n) + 1):
        if n % p == 0:
            q = n // p
            return p != q and prime(p) and prime(q)
    return False


def semiprimes_to(bound):
    return tuple(n for n in range(6, bound + 1) if sqfree_semiprime(n))


def square_divisors(b):
    # Complete prime factorization of b by trial division, then divisors of b^2.
    factors = []
    residual = b
    p = 2
    while p * p <= residual:
        if residual % p:
            p += 1
            continue
        e = 0
        while residual % p == 0:
            residual //= p
            e += 1
        factors.append((p, 2 * e))
        p += 1
    if residual > 1:
        factors.append((residual, 2))
    result = [1]
    for p, e in factors:
        result = [old * p ** j for old in result for j in range(e + 1)]
    assert len(result) == len(set(result))
    assert all(b * b % divisor == 0 for divisor in result)
    return tuple(result)


def last_pair(residual, threshold):
    """All x<y, both squarefree semiprimes > threshold, with 1/x+1/y=residual."""
    a, b = residual.numerator, residual.denominator
    answer = []
    for t in square_divisors(b):
        if (b + t) % a:
            continue
        x = (b + t) // a
        if x <= threshold:
            continue
        partner_t = b * b // t
        if (b + partner_t) % a:
            continue
        y = (b + partner_t) // a
        if not (x < y and sqfree_semiprime(x) and sqfree_semiprime(y)):
            continue
        assert Fraction(1, x) + Fraction(1, y) == residual
        answer.append((x, y))
    return tuple(answer)


def check(k, bound, expected_pool, expected_prefixes, expected_live):
    pool = semiprimes_to(bound)
    assert pool == expected_pool
    prefixes = 0
    positive = 0
    live = 0
    solutions = []
    for prefix in combinations(pool, k - 2):
        prefixes += 1
        residual = Fraction(1, 2) - sum((Fraction(1, x) for x in prefix), Fraction(0))
        if residual <= 0:
            continue
        positive += 1
        # The two remaining reciprocals are strictly smaller than 1/prefix[-1].
        if residual >= Fraction(2, prefix[-1]):
            continue
        live += 1
        for x, y in last_pair(residual, prefix[-1]):
            solutions.append(prefix + (x, y))
    assert prefixes == expected_prefixes
    assert live == expected_live
    assert positive == prefixes
    assert solutions == [], solutions
    print('k=', k, 'pool=', len(pool), 'prefixes=', prefixes,
          'positive=', positive, 'live=', live, 'completions=', len(solutions))


def main():
    assert len(WITNESS) == 9 and len(set(WITNESS)) == 9
    assert all(sqfree_semiprime(x) for x in WITNESS)
    assert sum((Fraction(1, x) for x in WITNESS), Fraction(0)) == Fraction(1, 2)
    first_six = semiprimes_to(22)
    assert first_six == (6, 10, 14, 15, 21, 22)
    assert sum((Fraction(1, x) for x in first_six), Fraction(0)) == Fraction(115, 231) < Fraction(1, 2)
    assert sum((Fraction(1, x) for x in first_six[:4]), Fraction(0)) == Fraction(17, 42)
    assert sum((Fraction(1, x) for x in first_six[:5]), Fraction(0)) == Fraction(19, 42)
    check(7, 31, (6, 10, 14, 15, 21, 22, 26), 21, 6)
    check(8, 63, (6, 10, 14, 15, 21, 22, 26, 33, 34, 35, 38, 39, 46, 51, 55, 57, 58, 62), 18564, 74)
    print('Nine-term witness verified:', WITNESS)


if __name__ == '__main__':
    main()
