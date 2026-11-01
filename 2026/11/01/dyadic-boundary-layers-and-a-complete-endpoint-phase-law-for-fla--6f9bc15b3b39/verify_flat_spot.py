"""Exact rational finite checks for flat-spot density endpoint decomposition.

These tests verify finite identities only; the uniform asymptotics are proved in RESULT.md.
"""
from fractions import Fraction
from math import gcd, floor


def mechanical_parameter(p, k):
    num = 0
    for i in range(1, k + 1):
        bit = ((i + 1) * p) // k - (i * p) // k
        assert bit in (0, 1)
        num += bit * (1 << (k - i))
    return Fraction(num, 1 << k)


def first_support(k):
    t = Fraction(1, 1 << (k - 1))
    return (1 - t) / k, (2 - t) / k


def leading_k(z):
    for k in range(4, 250):
        if first_support(k)[0] <= z:
            return k
    raise ValueError("increase search cap")


def finite_density(z, maxden):
    value = Fraction(0)
    first = Fraction(0)
    others = Fraction(0)
    min_other = None
    for k in range(2, maxden + 1):
        for p in range(1, k):
            if gcd(p, k) != 1:
                continue
            t = mechanical_parameter(p, k)
            if (p - t) <= k * z <= (p - t + 1):
                term = Fraction(k, (1 << k) - 1)
                value += term
                if p == 1:
                    first += term
                else:
                    others += term
                    min_other = k if min_other is None else min(k, min_other)
    return value, first, others, min_other


def test():
    n = 0
    for k in range(3, 51):
        assert mechanical_parameter(1, k) == Fraction(1, 1 << (k - 1))
        n += 1
    for q in range(10, 28):
        layer = Fraction(q, (1 << (q - 1)) - 1)
        probes = [Fraction(q, 1), Fraction(q, 1) + layer / 2,
                  Fraction(q, 1) + (layer + Fraction(1)) / 2,
                  Fraction(q, 1) + Fraction(1, 2)]
        for u in probes:
            z = 1 / u
            K = leading_k(z)
            expected = q if u <= q + layer else q + 1
            assert K == expected, (q, u, K, expected)
            n += 1
    for z in [Fraction(1, 8), Fraction(2, 17), Fraction(1, 9),
              Fraction(1, 10), Fraction(2, 21), Fraction(1, 12),
              Fraction(1, 20), Fraction(2, 41), Fraction(100000, 2000001)]:
        u = 1 / z
        K = leading_k(z)
        total, first, others, min_other = finite_density(z, 78)
        assert total == first + others
        assert min_other is None or 2 * min_other * z >= 3
        expected_first = sum((Fraction(k, (1 << k) - 1)
                              for k in range(K, 79)
                              if first_support(k)[0] <= z <= first_support(k)[1]), Fraction(0))
        assert first == expected_first
        assert all(first_support(k)[0] <= z <= first_support(k)[1]
                   for k in range(K, min(78, (3 * u) // 2) + 1))
        approx = Fraction(K + 1, 1 << (K - 1))
        if u >= 10:
            assert abs(total - approx) < approx / 100
        n += 5
    print(f"PASS: {n} exact-rational finite checks")


if __name__ == "__main__":
    test()
