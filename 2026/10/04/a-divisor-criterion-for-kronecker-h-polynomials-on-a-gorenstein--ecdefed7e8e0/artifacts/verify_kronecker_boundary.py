#!/usr/bin/env python3
"""Exact regression checks for the Kronecker boundary factorization."""
from math import isqrt


def conv(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def geom(terms, step=1):
    out = [0] * ((terms - 1) * step + 1)
    for j in range(terms):
        out[j * step] = 1
    return out


def divisors(n):
    d = []
    for k in range(1, isqrt(n) + 1):
        if n % k == 0:
            d.append(k)
            if k * k != n:
                d.append(n // k)
    return sorted(d)


def hstar_floor(r, a, b):
    S = r + a + b
    coeff = [0] * (r + 2)
    for k in range(S):
        exponent = k - (k * a) // S - (k * b) // S
        assert 0 <= exponent <= r + 1
        coeff[exponent] += 1
    while coeff and coeff[-1] == 0:
        coeff.pop()
    return coeff


def kronecker_branch_formula(r, c):
    m = r // c
    return conv(geom(c, m), conv([1, 1], [1] * (m + 1)))


def odd_branch_formula(r, c):
    t = 2 * r // c
    assert t % 2 == 1
    assert c % 2 == 0
    p = c // 2
    m = (t + 1) // 2
    C = [1] + [2] * t + [1]
    C[m] += 2
    assert len(C) == 2 * m + 1
    assert C[-2] == (4 if m == 1 else 2)
    return conv(geom(p, t), C)


def main():
    for r in range(2, 241):
        div2 = divisors(2 * r)
        divr = divisors(r)
        assert len(div2) + 1 >= len(divr) + 1

        equal = hstar_floor(r, r, r)
        assert equal == conv([1] * r, [1, 1, 1])

        kronecker_count = 1
        for c in div2:
            H = hstar_floor(r, c, c + r)
            if r % c == 0:
                assert H == kronecker_branch_formula(r, c)
                kronecker_count += 1
            else:
                assert c % 2 == 0
                assert (2 * r // c) % 2 == 1
                assert H == odd_branch_formula(r, c)
        assert kronecker_count == len(divr) + 1
        assert len(div2) + 1 - kronecker_count == len(div2) - len(divr)

    print("VERIFY_OK")


if __name__ == "__main__":
    main()
