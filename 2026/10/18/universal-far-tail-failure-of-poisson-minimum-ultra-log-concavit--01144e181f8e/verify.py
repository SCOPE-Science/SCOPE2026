#!/usr/bin/env python3
"""Standalone, standard-library reproduction of finite checks for a Poisson minimum law.

These are numerical diagnostics. The theorem's universal range is proved analytically.
"""
from decimal import Decimal, localcontext
from fractions import Fraction


def rational_identity():
    p = [Fraction(1, 5), Fraction(2, 5), Fraction(2, 5)]
    survival = [sum(p[j:], Fraction(0)) for j in range(3)] + [Fraction(0)]
    weights = {1: Fraction(1, 4), 2: Fraction(1, 4), 5: Fraction(1, 2)}
    for k in range(3):
        direct = sum((weight * (survival[k]**n - survival[k + 1]**n)
                      for n, weight in weights.items()), Fraction(0))
        factored = p[k] * sum(
            (weight * sum((survival[k]**(n-1-j) * survival[k+1]**j
                           for j in range(n)), Fraction(0))
             for n, weight in weights.items()), Fraction(0))
        assert direct == factored, (k, direct, factored)


def poisson_case(rate, weights, indices):
    with localcontext() as ctx:
        ctx.prec = 120
        lam = Decimal(rate)
        size_weights = {n: Decimal(str(q)) for n, q in weights.items()}
        assert sum(size_weights.values()) == 1
        assert size_weights[1] > 0 and size_weights[2] > 0
        M = 190
        p = [(-lam).exp()]
        for k in range(M):
            p.append(p[-1] * lam / Decimal(k+1))
        S = [Decimal(0)] * (M+2)
        for k in range(M, -1, -1):
            S[k] = S[k+1] + p[k]
        # Replacing the tiny tail beyond M gives negligible high-precision error.
        for k in indices:
            assert k+1 <= M
            h = []
            for j in [k-1, k, k+1]:
                h_j = sum((weight * sum((S[j]**(n-1-m)*S[j+1]**m
                                       for m in range(n)), Decimal(0))
                           for n, weight in size_weights.items()), Decimal(0))
                h.append(h_j)
            defect = h[0]*h[2]/h[1]**2 - 1
            asymp = size_weights[2] / size_weights[1] * p[k-1]
            ratio = defect/asymp
            assert defect > 0, (rate, weights, k, defect)
            assert Decimal('0.85') < ratio < Decimal('1.05'), (rate, k, ratio)
            left = p[k] * h[1]
            assert left > 0
        return len(indices)


if __name__ == '__main__':
    rational_identity()
    total = 0
    total += poisson_case('0.3', {1: '0.5', 2: '0.5'}, [10, 20, 30])
    total += poisson_case('3', {1: '0.0001', 2: '0.9999'}, [20, 30, 40])
    total += poisson_case('5', {1: '0.4', 2: '0.3', 6: '0.3'}, [25, 35, 45])
    print('verification: PASS (rational identity and %d high-precision tail checks)' % total)
