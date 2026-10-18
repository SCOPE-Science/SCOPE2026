"""Exact rational checks of local 3-adic square-value densities.

No numerical approximation enters the formula evaluation.  Finite
congruence tests illustrate rather than prove the infinite statement.
"""
from collections import Counter
from fractions import Fraction as F


def valuation(m):
    if m == 0:
        return None, None
    k = 0
    while m % 3 == 0:
        m //= 3
        k += 1
    return k, m % 3


def q(c):
    if c == 0:
        return F(1, 2)
    k, u = valuation(c)
    if k % 2:
        return (1 - F(1, 3 ** (k + 1))) / 2
    if u == 1:
        return F(1, 2) - F(1, 3 ** (k + 1))
    return F(1, 2)


def h(m):
    if m == 0:
        return F(5, 16)
    k, u = valuation(m)
    weights = [F(4 * (j + 1), 9 * 3**j) for j in range(k + 1)]
    subtotal = sum((weights[j] for j in range(k) if j % 2 == 0), F(0)) / 2
    if k % 2 == 0 and u == 1:
        subtotal += 1 - sum(weights)
    if k % 2:
        subtotal += weights[k] * F(3, 16)
    else:
        subtotal += weights[k] * (F(1, 16) + (F(1, 2) if u == 2 else 0))
    return subtotal


def delta(n):
    if n % 3 == 1:
        return F(8, 9)
    if n % 9 in (2, 5):
        return F(0)
    if n % 9 == 8:
        return q((64 * n + 1) // 9) / 9
    if n % 9 in (3, 6):
        return F(1, 6)
    return F(1, 6) + F(4, 9) * h(n // 9)


def finite_counts(n, k):
    mod = 3**k
    vals = Counter((a * (a + 1) // 2) % mod for a in range(mod))
    residues = {j * j % mod for j in range(mod)}
    numerator = sum(ca * cb for a, ca in vals.items() for b, cb in vals.items()
                    if ((a * b + n) % mod) in residues)
    return F(numerator, mod * mod)


def main():
    expected = {0: F(11,36), 1: F(8,9), 2: F(0), 3: F(1,6),
                5: F(0), 8: F(4,81), 9: F(23,54),
                12: F(1,6), 18: F(5,18)}
    for n, value in expected.items():
        assert delta(n) == value, (n, delta(n), value)
    assert h(0) == F(5,16)
    assert q(0) == F(1,2)
    for n in range(-40, 41):
        target = delta(n)
        last = F(1)
        for k in range(1, 6):
            upper = finite_counts(n, k)
            assert upper >= target, (n, k, upper, target)
            assert upper <= last, (n, k, upper, last)
            last = upper
        assert last - target < F(1, 10), (n, last, target)
    print('PASS: 9 exact reference densities, 81 parameters, 405 nested finite-ring checks.')
    for n in (0, 1, 2, 3, 5, 8, 9, 12, 18):
        print(f'n={n}, predicted={delta(n)}, modulo 3^5={finite_counts(n,5)}')


if __name__ == '__main__':
    main()
