"""Reproduce finite sanity checks for binary antipalindrome quotient obstructions.

Uses only Python 3's standard library. This is not a replacement for
 the all-length normalization and shell-counting proof.
"""
from fractions import Fraction


def antipalindromes(half_length):
    for head in range(1 << (half_length - 1), 1 << half_length):
        s = format(head, '0%db' % half_length)
        mirrored_complement = ''.join('1' if bit == '0' else '0'
                                      for bit in reversed(s))
        yield int(s + mirrored_complement, 2)


def valuation2(n):
    return (n & -n).bit_length() - 1


def shell_ok(n):
    for d in range(20):
        t = 4 ** d
        if n % 2 == 0 and t < n < 2 * t:
            return True
        if n % 2 == 1 and 3 * n > 2 * t and 2 * n < 3 * t:
            return True
    return False


def forbidden_set(x):
    out = set()
    t = 1
    while 2 * t <= x:
        out.update(range(2 * t, min(x, 4 * t) + 1, 2))
        t *= 4
    t = 1
    while 3 * t < 2 * x:
        lo = 3 * t // 2
        hi = min(x, (8 * t - 1) // 3)
        for n in range(lo + 1, hi + 1):
            if n % 2 == 1 and 2 * n > 3 * t and 3 * n < 8 * t:
                out.add(n)
        t *= 4
    return out


def formula_at_boundary(k):
    q = 4 ** k
    return Fraction(19 * q, 36) + Fraction(2 * k, 3) - Fraction(7, 9)


def main():
    vals = sorted({a for h in range(1, 9) for a in antipalindromes(h)})
    assert len(vals) == 255
    for a in vals:
        bits = format(a, 'b')
        leading_ones = len(bits) - len(bits.lstrip('1'))
        assert valuation2(a) == leading_ones
    quotients = {a // b for a in vals for b in vals if a % b == 0}
    assert quotients
    for n in quotients:
        assert shell_ok(n), ('violates quotient shell', n)
    print('antipalindromes_checked=%d' % len(vals))
    print('ordered_pairs_checked=%d' % (len(vals) ** 2))
    print('distinct_integer_quotients=%d' % len(quotients))
    print('quotient_shell_violations=0')
    for k in range(1, 9):
        x = 3 * (4 ** k) // 2
        count = len(forbidden_set(x))
        expect = formula_at_boundary(k)
        assert expect.denominator == 1
        assert count == expect.numerator
        print('k=%d x=%d forbidden=%d ratio=%s' % (k, x, count, Fraction(count, x)))
    print('all_finite_checks_passed')


if __name__ == '__main__':
    main()
