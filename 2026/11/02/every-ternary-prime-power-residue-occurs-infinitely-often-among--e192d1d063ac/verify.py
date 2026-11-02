#!/usr/bin/env python3
"""Exact 3-adic factorial-unit checks for sparse-index Catalan congruences.

No finite test is used as proof of the unbounded-exponent theorem.
"""
from math import comb


def make_oracle(k):
    modulus = 3 ** k
    partial = [1] * modulus
    for j in range(1, modulus):
        partial[j] = partial[j - 1] * (j if j % 3 else 1) % modulus

    def factorial_unit(n):
        result = 1
        while n:
            q, r = divmod(n, modulus)
            result = result * (-1 if q % 2 else 1) * partial[r] % modulus
            n //= 3
        return result

    def factorial_valuation(n):
        result = 0
        while n:
            n //= 3
            result += n
        return result

    def central(n):
        value = factorial_valuation(2 * n) - 2 * factorial_valuation(n)
        base = factorial_unit(n)
        unit = factorial_unit(2 * n) * pow(base, -2, modulus) % modulus
        return value, unit

    def catalan(n):
        value, unit = central(n)
        d = n + 1
        while d % 3 == 0:
            value -= 1
            d //= 3
        assert value >= 0
        return 3 ** value * unit * pow(d, -1, modulus) % modulus

    return central, catalan


def sparse_index(v, t, L):
    return sum(2 * 3 ** (i * L) for i in range(1, v + 1)) + sum(
        3 ** (i * L) for i in range(v + 1, v + t + 1))


def verify():
    tested = 0
    all_residues = 0
    for k in range(1, 8):
        modulus = 3 ** k
        central, catalan = make_oracle(k)
        for n in range(400):
            assert catalan(n) == comb(2 * n, n) // (n + 1) % modulus
        for L in (k + 2, k + 3):
            c = central(3 ** L)[1]
            valuation_d, d = central(2 * 3 ** L)
            assert valuation_d == 1
            if k >= 2:
                assert c % 9 == 2
            else:
                assert c % 3 == 2
            order = 2 * 3 ** (k - 1)
            assert pow(c, order, modulus) == 1
            assert pow(c, order // 2, modulus) != 1
            if k >= 2:
                assert pow(c, order // 3, modulus) != 1
            for v in range(k + 2):
                for t in range(12):
                    n = sparse_index(v, t, L)
                    valuation, unit = central(n)
                    assert valuation == v
                    assert unit == pow(d, v, modulus) * pow(c, t, modulus) % modulus
                    assert catalan(n) == (3 ** v * pow(d, v, modulus) * pow(c, t, modulus)) % modulus
                    tested += 1
        if k <= 5:
            L = k + 2
            seen = set()
            for v in range(k + 1):
                for t in range(2 * 3 ** (k - 1)):
                    n = sparse_index(v, t, L)
                    seen.add(catalan(n))
            assert seen == set(range(modulus))
            all_residues += len(seen)
    print(f"VERIFY_OK prime_power_levels=1..7 separated_block_checks={tested} "
          f"direct_Catalan_checks=2800 full_residue_levels=1..5 "
          f"total_residue_targets={all_residues}")


if __name__ == '__main__':
    verify()
