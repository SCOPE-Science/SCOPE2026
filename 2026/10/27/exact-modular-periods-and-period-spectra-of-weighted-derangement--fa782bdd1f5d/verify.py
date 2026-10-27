"""Exact modular checks for weighted-fixed-point permutation counts.

Run: python3 verify.py   (standard library only).
Finite checks corroborate but cannot prove universal period claims.
"""
from math import gcd, lcm
from itertools import permutations


def modular_order(u, m):
    assert m >= 2 and gcd(u, m) == 1
    x = 1
    for order in range(1, m + 1):  # Euler's totient <= m
        x = x * u % m
        if x == 1:
            return order
    raise AssertionError('modular order not found')


def recurrence_sequence(u, m, nmax):
    a = 1
    result = [a]
    for n in range(1, nmax + 1):
        a = (n * a + pow(u, n, m)) % m
        result.append(a)
    return result


def unit_order_spectrum(m):
    return {lcm(m, modular_order(u, m)) for u in range(m) if gcd(u, m) == 1}


def all_divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def carmichael_by_orders(m):
    value = 1
    for u in range(m):
        if gcd(u, m) == 1:
            value = lcm(value, modular_order(u, m))
    return value


def run():
    pairs = 0
    upper_comparisons = 0
    proper_divisor_tests = 0
    max_period = 0
    spectrum_checks = 0
    for m in range(2, 51):
        exponent = carmichael_by_orders(m)
        q = exponent // gcd(exponent, m)
        predicted_spectrum = {m * e for e in all_divisors(q)}
        assert unit_order_spectrum(m) == predicted_spectrum, (m, 'spectrum')
        spectrum_checks += 1
        for u in range(m):
            if gcd(u, m) != 1:
                continue
            period = lcm(m, modular_order(u, m))
            # Independent recurrence, not evaluation of a shifted congruence.
            seq = recurrence_sequence(u, m, 2 * period)
            for i in range(period):
                assert seq[i] == seq[i + period], (m, u, period, i)
                upper_comparisons += 1
            for d in all_divisors(period):
                if d == period:
                    continue
                # Exclude every proper divisor of the proposed least period.
                assert any(seq[i] != seq[i + d] for i in range(period)), (
                    m, u, d, 'shorter period')
                proper_divisor_tests += 1
            pairs += 1
            max_period = max(max_period, period)
    permutation_tests = 0
    for n in range(0, 8):
        for u in (-3, -2, -1, 0, 1, 2, 3):
            direct = sum((1 + u) ** sum(perm[i] == i for i in range(n))
                         for perm in permutations(range(n)))
            rec = 1
            for j in range(1, n + 1):
                rec = j * rec + u ** j
            assert direct == rec, (n, u, direct, rec)
            permutation_tests += 1
    print('VERIFY_OK:', pairs, 'coprime parameter/modulus combinations;',
          upper_comparisons, 'shift comparisons;',
          proper_divisor_tests, 'proper-divisor obstructions;',
          spectrum_checks, 'full modular period spectra;',
          permutation_tests, 'direct weighted-permutation sums;',
          'maximum checked least period', max_period)


if __name__ == '__main__':
    run()
