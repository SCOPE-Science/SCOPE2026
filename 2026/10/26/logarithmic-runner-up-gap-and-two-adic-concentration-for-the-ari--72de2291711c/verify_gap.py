#!/usr/bin/env python3
"""Independent finite checks for the dyadic arithmetic-derivative runner-up theorem.

Python >=3.11, standard library only. This is not an infinite proof.
"""
from decimal import Decimal, localcontext


def check():
    max_k = 20
    size = 1 << max_k
    least = list(range(size))
    for p in range(2, int(size ** .5) + 1):
        if least[p] == p:
            for q in range(p * p, size, p):
                if least[q] == q:
                    least[q] = p
    derivative = [0] * size
    for n in range(2, size):
        p = least[n]
        q = n // p
        derivative[n] = q + p * derivative[q]

    with localcontext() as ctx:
        ctx.prec = 70
        L2 = Decimal(2).ln()
        b = L2 / (3 * Decimal(3).ln())
        c = Decimal(1) / 2 - b
        gamma = c / L2 + c * ((b * L2 / c).ln() / L2)
        for k in range(2, max_k + 1):
            top = max(range(1, 1 << k), key=derivative.__getitem__)
            mval = derivative[top]
            gap = k * (1 << (k - 1)) - mval
            scale = Decimal(1 << k)
            logk = Decimal(k).ln() / L2
            assert scale * (c * logk + gamma) <= Decimal(gap)
            assert Decimal(gap) <= scale * (logk + 2) / 2
            t = k - ((top & -top).bit_length() - 1)
            assert Decimal(t) <= (logk + 2) / (2 * c)
            assert Decimal(t) >= (2 * b * k / (logk + 2)).ln() / L2
            assert Decimal(0) < Decimal(1) - Decimal(top) / scale
            assert Decimal(1) - Decimal(top) / scale <= (logk + 2) / Decimal(k)
    print('VERIFY_OK exhaustive_dyadic_prefixes k=2..20 max_n=1048575')


if __name__ == '__main__':
    check()
