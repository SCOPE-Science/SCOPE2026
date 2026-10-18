"""Finite exact checks for a record-jump coupling of parking-function deficits.

Run with Python 3: python verify.py.  The unrestricted proof is analytical.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, exp, lgamma, log, sqrt, pi


def exact_pmf(n, m):
    if not 1 <= m <= n:
        return Fraction(0)
    k = n + 1 - m
    return (Fraction(comb(n, k) * k ** k, n * (n + 1) ** (n - 1))
            * (Fraction(1, m) if m == 1 else m ** (m - 2)))


def direct_counts(n):
    out = Counter()
    for prefs in product(range(1, n + 1), repeat=n):
        slots = [False] * n
        final = None
        for pref in prefs:
            i = pref - 1
            while i < n and slots[i]:
                i += 1
            if i == n:
                break
            slots[i] = True
            final = i + 1
        else:
            out[n + 1 - final] += 1
    return out


def check():
    assertions = 0
    for n in range(1, 8):
        observed = direct_counts(n)
        assert sum(observed.values()) == (n + 1) ** (n - 1)
        assertions += 1
        for m in range(1, n + 1):
            assert Fraction(observed[m], (n + 1) ** (n - 1)) == exact_pmf(n, m)
            assertions += 1
    for n in range(1, 101):
        pn = [exact_pmf(n, m) for m in range(1, n + 1)]
        pn1 = [exact_pmf(n + 1, m) for m in range(1, n + 2)]
        assert sum(pn) == 1 and sum(pn1) == 1
        assertions += 2
        assert all(pn1[m - 1] < pn[m - 1] for m in range(1, n + 1))
        assertions += 1
        # All lost probability from old states moves to the newly exposed state n+1.
        assert sum(pn[m - 1] - pn1[m - 1] for m in range(1, n + 1)) == pn1[-1]
        assertions += 1
        # Increasing successive ratios across the old support (reverse likelihood order).
        ratios = [pn1[m - 1] / pn[m - 1] for m in range(1, n + 1)]
        assert all(ratios[m - 1] > ratios[m] for m in range(1, n))
        assertions += 1
        # Borel ratio and sharp TV: floating evidence only; exact statements proven in text.
        ratios_b = []
        for m in range(1, n + 1):
            b = exp(-m + (m - 1) * log(m) - lgamma(m + 1))
            ratios_b.append(float(pn[m - 1]) / b)
        assert min(ratios_b) > 1 - 1e-8
        assert all(ratios_b[m - 1] < ratios_b[m] + 1e-8 for m in range(1, n))
        assertions += 2
    print(f'VERIFY_OK {assertions} assertions, exhaustive n<=7; rational transitions n<=100')
    for n in [10, 100, 1000]:
        tail = 1 - sum(exp(-m + (m - 1) * log(m) - lgamma(m + 1))
                       for m in range(1, n + 1))
        print(f'n={n} sharp TV={tail:.12f}, sqrt(n)*TV={sqrt(n)*tail:.9f}')
    print(f'limiting sqrt(n)*TV={sqrt(2 / pi):.9f}')


if __name__ == '__main__':
    check()
