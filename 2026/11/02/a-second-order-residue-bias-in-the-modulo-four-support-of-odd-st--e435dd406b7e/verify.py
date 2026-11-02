"""Finite, exact checks for the arithmetic-support classification and mod-8 splitting.

No floating-point claims and no inference of asymptotics from this test.
Run: python3 verify.py
"""
from math import isqrt

MAX_COEFFICIENT = 1400
MAX_INDEX = 40000


def sieve_spf(n):
    spf = list(range(n + 1))
    for p in range(2, isqrt(n) + 1):
        if spf[p] == p:
            for j in range(p * p, n + 1, p):
                if spf[j] == j:
                    spf[j] = p
    return spf


def factor(n, spf):
    out = {}
    while n > 1:
        p = spf[n]
        out[p] = out.get(p, 0) + 1
        n //= p
    return out


def from_factorization(n, spf):
    """Directly test the two independent prime/square support conditions."""
    t = 3 * n - 1
    if isqrt(2 * t) ** 2 == 2 * t:
        return 1  # odd coefficient
    for epsilon in (1, 2):
        if t % epsilon:
            continue
        f = factor(t // epsilon, spf)
        exceptional = [p for p, v in f.items() if v % 2]
        if len(exceptional) == 1:
            p = exceptional[0]
            if p % 8 in (5, 7) and f[p] % 4 == 1:
                return 2
    return 0


def coefficient_mod4(limit):
    """Expand OU*(q) = sum_{j>=0} q^(2j+1) prod_{h<j}(1+q^(2h+1))^2."""
    poly = [0] * (limit + 1)
    poly[0] = 1
    result = [0] * (limit + 1)
    for j in range((limit + 1) // 2):
        if j:
            part = 2 * j - 1
            for _ in range(2):
                for i in range(limit, part - 1, -1):
                    poly[i] = (poly[i] + poly[i - part]) % 4
        base = 2 * j + 1
        for i in range(limit - base + 1):
            result[base + i] = (result[base + i] + poly[i]) % 4
    return result


def from_prime_square_parametrization(x, spf):
    """Enumerate the two mutually exclusive forms for M=(3n-1)/2."""
    result = {1: set(), 3: set(), 5: set(), 7: set()}
    maximum_m = (3 * x - 1) // 2
    for p in range(5, maximum_m + 1, 2):
        if spf[p] != p:
            continue
        if p % 24 in (7, 13):
            scale = 1
        elif p % 24 in (5, 23):
            scale = 2
        else:
            continue
        power = p
        while scale * power <= maximum_m:
            bound = isqrt(maximum_m // (scale * power))
            for u in range(1, bound + 1):
                if u % 3 == 0 or u % p == 0:
                    continue
                m = scale * power * u * u
                assert m % 3 == 1
                n = (2 * m + 1) // 3
                assert n % 2 == 1 and n <= x
                assert n not in result[n % 8], 'duplicate representation'
                result[n % 8].add(n)
            power *= p ** 4
    return result


def main():
    spf = sieve_spf(3 * MAX_INDEX)
    coefficients = coefficient_mod4(MAX_COEFFICIENT)
    for n in range(1, MAX_COEFFICIENT + 1, 2):
        v = from_factorization(n, spf)
        if v == 1:
            assert coefficients[n] % 2 == 1, (n, v, coefficients[n])
        else:
            assert coefficients[n] == v, (n, v, coefficients[n])
    by_factor = {r: set() for r in (1, 3, 5, 7)}
    for n in range(1, MAX_INDEX + 1, 2):
        if from_factorization(n, spf) == 2:
            by_factor[n % 8].add(n)
    by_param = from_prime_square_parametrization(MAX_INDEX, spf)
    assert by_factor == by_param, {
        r: (sorted(by_factor[r] - by_param[r])[:3], sorted(by_param[r] - by_factor[r])[:3])
        for r in (1, 3, 5, 7)
    }
    counts = {r: len(by_factor[r]) for r in (1, 3, 5, 7)}
    print(f'VERIFY_OK coeffs_odd_n={len(range(1, MAX_COEFFICIENT+1, 2))} '
          f'direct_indices={len(range(1, MAX_INDEX+1, 2))} '
          f'index_limit={MAX_INDEX} residues={counts}')


if __name__ == '__main__':
    main()
