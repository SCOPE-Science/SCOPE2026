"""Exact verification of the arithmetic primitive-row Fourier frame-potential identity.

No dependencies outside the Python standard library. Computational tests are finite;
the manuscript's local-prime-power proof establishes the general theorem.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import gcd


def prime_powers(n):
    assert n >= 2
    result = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            k = 0
            while n % p == 0:
                n //= p
                k += 1
            result.append((p, k))
        p += 1
    if n > 1:
        result.append((n, 1))
    return result


def weights(n):
    terms = [(1, Fraction(1))]
    for p, k in prime_powers(n):
        beta = Fraction(1, (p - 1) ** 2)
        terms = ([(d * p ** (k - 1), w * beta) for d, w in terms] +
                 [(d * p ** k, w * (1 - beta)) for d, w in terms])
    return [(d, w) for d, w in terms if w]


def mobius(n):
    if n == 1:
        return 1
    sign = 1
    for p, k in prime_powers(n):
        if k > 1:
            return 0
        sign *= -1
    return sign


def ramanujan(n, t):
    # Ramanujan's integer-valued divisor sum, independent of the weights formula.
    return sum(d * mobius(n // d) for d in range(1, n + 1)
               if n % d == 0 and t % d == 0)


def direct(n, a):
    phi = sum(gcd(u, n) == 1 for u in range(n))
    return Fraction(sum(ramanujan(n, x - y) ** 2 for x in a for y in a),
                    phi ** 2)


def weighted(n, a):
    return sum((w * sum(count * count for count in
                            Counter(x % d for x in a).values())
                for d, w in weights(n)), Fraction(0))


def sharp(n, s):
    result = Fraction(0)
    for d, w in weights(n):
        q, r = divmod(s, d)
        result += w * (d * q * q + r * (2 * q + 1))
    return result


def deficit(n, a):
    s = len(a)
    out = Fraction(0)
    for d, w in weights(n):
        q, _ = divmod(s, d)
        count = Counter(x % d for x in a)
        out += w * sum((count.get(r, 0) - q) *
                       (count.get(r, 0) - q - 1) for r in range(d))
    return out


def verify():
    cases = 0
    exhaust = 0
    nonoptimal = 0
    for n in (2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 21, 25, 27, 30, 35, 45):
        for s in range(1, min(n, 8) + 1):
            a = tuple(range(s))
            assert direct(n, a) == weighted(n, a) == sharp(n, s)
            assert deficit(n, a) == 0
            cases += 1
            if n <= 18 and s <= 4:
                for b in combinations(range(n), s):
                    fp = direct(n, b)
                    assert fp == weighted(n, b)
                    assert fp - sharp(n, s) == deficit(n, b) >= 0
                    is_balanced = all(
                        all(v in divmod(s, d)[0:1] + (divmod(s, d)[0] + 1,)
                            for v in (Counter(x % d for x in b).get(r, 0)
                                      for r in range(d)))
                        for d, w in weights(n) if w > 0
                    )
                    assert (fp == sharp(n, s)) == is_balanced
                    nonoptimal += fp > sharp(n, s)
                    exhaust += 1
    assert sharp(9, 4) == Fraction(9, 2)
    assert direct(9, (0, 1, 2, 3)) == Fraction(9, 2)
    assert direct(9, (0, 1, 3, 6)) == Fraction(11, 2)
    assert nonoptimal > 0
    print(f'VERIFY_OK moduli=18 consecutive_cases={cases} exhaustive_sets={exhaust} '
          f'nonoptimal_sets={nonoptimal} exact_rational_identity=PASS equality=PASS')


if __name__ == '__main__':
    verify()
