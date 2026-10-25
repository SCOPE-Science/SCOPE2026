#!/usr/bin/env python3
"""Independent finite-case checks of the exact Yule–Simon concavity index.

Requires only Python >=3.11 standard library. The infinite theorem is analytic.
"""
from decimal import Decimal, localcontext


def root(r):
    A = (Decimal(r + 3) / 2).ln()
    B = Decimal(r + 2).ln()
    def f(a):
        return (a * A).exp() + (-a * B).exp() - 2
    low = Decimal('1e-50')
    high = Decimal(1)
    for _ in range(235):
        mid = (low + high) / 2
        if f(mid) > 0:
            high = mid
        else:
            low = mid
    return (low + high) / 2


def difference(r, k, a):
    # Divide the centered second difference by h_a(k) > 0.
    pos = (Decimal(k + r + 1) / Decimal(k)).ln()
    neg = (Decimal(k - 1) / Decimal(k + r)).ln()
    return (a * pos).exp() + (a * neg).exp() - 2


with localcontext() as ctx:
    ctx.prec = 74
    for r in [1, 2, 3, 4, 5, 10, 20, 100, 1000, 10000]:
        a = root(r)
        assert a > Decimal(1) / Decimal(r + 1)
        if r <= 1000:
            H1 = sum((Decimal(1) / Decimal(j) for j in range(1, r + 2)), Decimal(0))
            H2 = sum((Decimal(1) / Decimal(j*j) for j in range(1, r + 2)), Decimal(0))
            assert a < H2 / (H1 * H1)
        assert abs(difference(r, 2, a)) < Decimal('1e-65')
        assert difference(r, 2, a * Decimal('0.99999')) < 0
        assert difference(r, 2, a * Decimal('1.00001')) > 0
        if r <= 100:
            for k in range(3, 251):
                assert difference(r, k, a) >= -Decimal('1e-65')
        print(f'r={r}: a={a:.17f}')
print('All finite-case numerical checks passed.')
