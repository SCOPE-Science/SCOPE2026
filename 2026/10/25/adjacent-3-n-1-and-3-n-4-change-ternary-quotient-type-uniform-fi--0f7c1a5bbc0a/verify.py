#!/usr/bin/env python3
"""Exact finite checks accompanying the theorem on local ternary quotients.

These tests are illustrative; the symbolic carry identity in the proof
establishes the statement for all n >= 5.
"""


def exponents(n):
    assert isinstance(n, int) and n >= 5
    numerator = (0, 1, 2, 3, n - 1, n + 3, 2*n - 1, 2*n, 2*n + 1)
    denominator = (0, 2, n - 1, n, n + 1)
    assert len(numerator) == len(set(numerator)) == 9
    assert len(denominator) == len(set(denominator)) == 5
    assert numerator[0] == denominator[0] == 0
    return numerator, denominator


def at3(support):
    return sum(3**e for e in support)


def polynomial_mul(a, b):
    out = {}
    for i, ai in a.items():
        for j, bj in b.items():
            out[i + j] = out.get(i + j, 0) + ai*bj
    return {e:c for e,c in out.items() if c}


def compressed_carry(n):
    # Check the full pre-carry product has its claimed generic coefficient pattern.
    _, qs = exponents(n)
    product = polynomial_mul({0: 1, 1: 1, n: 1}, {j: 1 for j in qs})
    expected = {0:1, 1:1, 2:1, 3:1, n - 1:1, n:3,
                n + 1:2, n + 2:2, 2*n - 1:1, 2*n:1, 2*n + 1:1}
    assert product == expected


def run():
    for n in range(5, 205):
        ps, qs = exponents(n)
        compressed_carry(n)
        assert at3(ps) == (3**n + 4)*at3(qs), n
        assert len(ps) == 9 and len(qs) == 5
        # A polynomial multiple would make P(1)/Q(1) integral.
        assert len(ps) % len(qs) != 0
    print('VERIFIED: 200 exact support, carry, integer-identity, and localness checks')


if __name__ == '__main__':
    run()
