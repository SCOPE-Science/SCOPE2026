"""Finite exact checks of Farey-indexed Sturmian beta gap formulas.

Requires only Python 3 standard library. The infinite claims are proved in RESULT.md;
these checks test finite word identities and numerical manifestations only.
"""
from decimal import Decimal, localcontext
from fractions import Fraction
from math import gcd


def ceil_fraction(x):
    return -(-x.numerator // x.denominator)


def digits(alpha, n):
    return [ceil_fraction((j + 1) * alpha) - ceil_fraction(j * alpha)
            for j in range(n)]


def period(p, q):
    return digits(Fraction(p, q), q)


def evaluate_period(u, t):
    return sum((a * t ** (j + 1) for j, a in enumerate(u)), Fraction(0))


def totient(q):
    return sum(gcd(p, q) == 1 for p in range(1, q + 1))


def check_farey_prefixes():
    for n in range(1, 20):
        fractions = [Fraction(0), Fraction(1)]
        fractions += [Fraction(p, q) for q in range(2, n + 1)
                      for p in range(1, q) if gcd(p, q) == 1]
        fractions.sort()
        words = {tuple(digits((a + b) / 2, n))
                 for a, b in zip(fractions, fractions[1:])}
        assert len(words) == sum(totient(q) for q in range(1, n + 1)), n
    return 19


def check_rational_formulas():
    checked = 0
    for q in range(2, 15):
        for p in range(1, q):
            if gcd(p, q) != 1:
                continue
            u = period(p, q)
            assert u[0] == 1 and sum(u) == p
            N = 8 * q
            midpoint = Fraction(p, q)
            delta = Fraction(1, 1000 * q * N)
            below = digits(midpoint - delta, N)
            above = digits(midpoint + delta, N)
            assert below == [u[j % q] for j in range(N)]
            expected = [u[j % q] + int(j % q == q - 1)
                        - int(j >= q and j % q == 0) for j in range(N)]
            assert above == expected
            assert all(a in (0, 1) for a in expected)
            for t in (Fraction(1, 2), Fraction(2, 3), Fraction(3, 4)):
                P = evaluate_period(u, t)
                left = P / (1 - t ** q)
                right = left + (1 - t) * t ** q / (1 - t ** q)
                assert (right - left) == (1 - t) * t ** q / (1 - t ** q)
                assert right == (P + (1 - t) * t ** q) / (1 - t ** q)
            checked += 1
    return checked


def decimal_ceil(x):
    return int(x.to_integral_value(rounding='ROUND_CEILING'))


def beta_from_period(p, q, plus=False, precision=83):
    u = period(p, q)
    with localcontext() as ctx:
        ctx.prec = precision

        def f(b):
            inv = Decimal(1) / b
            power = inv
            P = Decimal(0)
            for digit in u:
                P += digit * power
                power *= inv
            tail = inv ** q
            left = P / (1 - tail)
            if plus:
                left += (1 - inv) * tail / (1 - tail)
            return left - 1

        lower, upper = Decimal(1), Decimal(2)
        for _ in range(290):
            mid = (lower + upper) / 2
            if f(mid) > 0:
                lower = mid
            else:
                upper = mid
        return +(lower + upper) / 2


def irrational_base_and_constant(precision=83):
    with localcontext() as ctx:
        ctx.prec = precision
        alpha = Decimal(2).sqrt() - 1
        a = [decimal_ceil((j + 1) * alpha) - decimal_ceil(j * alpha)
             for j in range(400)]

        def f(b):
            inv = Decimal(1) / b
            power = inv
            total = Decimal(0)
            for d in a:
                total += d * power
                power *= inv
            return total - 1

        l, r = Decimal('1.2'), Decimal(2)
        for _ in range(290):
            mid = (l + r) / 2
            if f(mid) > 0:
                l = mid
            else:
                r = mid
        b = (l + r) / 2
        D = sum((Decimal(j + 1) * Decimal(d) / (b ** (j + 2))
                 for j, d in enumerate(a)), Decimal(0))
        return +b, +(1 - 1 / b) / D


def check_normalized_gap():
    B, K = irrational_base_and_constant()
    assert abs(B - Decimal('1.600326070040330228')) < Decimal('1e-17')
    assert abs(K - Decimal('0.277914863057636969')) < Decimal('1e-17')
    records = []
    for p, q in [(1, 2), (2, 5), (5, 12), (12, 29), (29, 70)]:
        left = beta_from_period(p, q)
        right = beta_from_period(p, q, plus=True)
        assert Decimal(1) < left < right < Decimal(2)
        value = (right - left) * left ** q
        records.append((p, q, value))
    assert abs(records[-1][2] - K) < Decimal('1e-11')
    return B, K, records


if __name__ == '__main__':
    print('Farey length levels checked:', check_farey_prefixes())
    print('Reduced rational slopes checked:', check_rational_formulas())
    B, K, records = check_normalized_gap()
    print('Irrational target beta:', B)
    print('Exact asymptotic constant (numeric):', K)
    for p, q, value in records:
        print('slope={}/{} normalized_gap={}'.format(p, q, value))
    print('VERIFY_OK')
