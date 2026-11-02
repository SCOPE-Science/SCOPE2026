#!/usr/bin/env python3
"""Exact checks for prime-power Pascal-column valuation laws.

Standard library only. Finite tests corroborate, but do not replace, the proof.
"""
from fractions import Fraction
from math import comb


def prime_valuation_factorial(n, p):
    ans = 0
    while n:
        n //= p
        ans += n
    return ans


def observed_valuation(n, m, p):
    # Independent factorial valuation, not the p-adic floor quotient identity.
    return (prime_valuation_factorial(n - 1, p)
            - prime_valuation_factorial(m - 1, p)
            - prime_valuation_factorial(n - m, p))


def expected_mass(p, a, v):
    if v == 0:
        return Fraction(1, p ** a)
    return (Fraction(p - 1, p + 1)
            * Fraction(1, p ** abs(v - a))
            * (1 - Fraction(1, p ** (2 * min(v, a)))))


def test_case(p, a, levels):
    m = p ** a
    # Compare to direct exact integer binomial calculations at a separate sample.
    for n in range(m, m + 100):
        x = comb(n - 1, m - 1)
        k = 0
        while x % p == 0:
            x //= p
            k += 1
        assert k == observed_valuation(n, m, p)
    assert expected_mass(p, a, 0) == Fraction(1, m)
    for v in range(1, levels + 1):
        period = p ** (a + v - 1)
        sample_period = p ** (a + v)
        observed = sum(observed_valuation(n, m, p) == v
                       for n in range(m, m + sample_period))
        predicted = expected_mass(p, a, v) * sample_period
        assert predicted.denominator == 1, (p, a, v, predicted)
        assert observed == predicted, (p, a, v, observed, predicted)
        # Confirm the claimed period holds for the Boolean threshold.
        for n in range(m, m + 2 * period):
            assert ((observed_valuation(n, m, p) >= v)
                    == (observed_valuation(n + period, m, p) >= v)), (p,a,v,n)
        if v == 1:
            witness = m + (p - 1) * p ** (a - 1)
        else:
            witness = m * p ** (v - 1) + p ** (a - 1)
        assert observed_valuation(witness, m, p) >= v
        assert observed_valuation(witness + period // p, m, p) < v
    period0 = p ** (2 * a - 1)
    successes = sum(comb(n, m) % n == 0
                    for n in range(m, m + period0))
    expected_successes = (Fraction(p, p + 1)
                          * (1 - Fraction(1, p ** (2 * a))) * period0)
    assert expected_successes.denominator == 1
    assert successes == expected_successes, (p, a, successes, expected_successes)
    return successes, period0


def main():
    cases = [(2, a, 5) for a in range(1, 6)]
    cases += [(3, a, 4) for a in range(1, 4)]
    cases += [(5, a, 3) for a in range(1, 3)]
    cases += [(7, 1, 3)]
    for p, a, levels in cases:
        count, period = test_case(p, a, levels)
        print(f'FIELD_OK p={p} a={a} valuations=0..{levels} '
              f'zero_remainder={count}/{period}')
    print('VERIFY_OK independent_factorial_valuations=True '
          'exact_period_witnesses=True all_cases=11')


if __name__ == '__main__':
    main()
