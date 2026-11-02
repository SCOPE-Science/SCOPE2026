#!/usr/bin/env python3
"""Exact finite checks for the joint 2-adic binomial valuation spectrum.
All computations use integer arithmetic; they do not replace the infinite proof.
"""
from math import comb


def v2(z):
    assert z > 0
    return (z & -z).bit_length() - 1


def count_carries(n):
    """Count every outgoing binary carry in n+(2n), including terminal carry."""
    carry = 0
    count = 0
    i = 0
    while ((n >> i) or ((2 * n) >> i) or carry):
        digit_sum = ((n >> i) & 1) + (((2 * n) >> i) & 1) + carry
        carry = digit_sum >> 1
        count += carry
        i += 1
    return count


def A(n):
    return n.bit_count()


def B(n):
    return 2 * A(n) - (3*n).bit_count()


def even_seed(k):
    assert k >= 2
    return (2**(2*k-1) + 1)//3


def odd_seed(k):
    assert k >= 3
    return (2**(2*k-2) + 5)//3


def witness(k, b):
    assert k >= 1
    if b == 0:
        return (4**k - 1)//3
    if b % 2 == 0:
        base_k = b//2 + 1
        n = even_seed(base_k)
    else:
        assert b >= 3
        base_k = (b+3)//2
        n = odd_seed(base_k)
    assert base_k <= k
    for _ in range(k-base_k):
        n = 4*n + 1
    return n


def main():
    direct_exact = 0
    carry_tests = 0
    seen = {}
    # Independent factorial/binomial computations for moderate indices.
    for n in range(1, 1201):
        expected_A = v2(comb(2*n, n))
        expected_B = v2(comb(3*n, n))
        assert (A(n), B(n)) == (expected_A, expected_B), n
        assert B(n) == count_carries(n), n
        direct_exact += 2
        carry_tests += 1
    # Exhaustive bounded scan verifies obstructions and sample fibers.
    for n in range(1, 1 << 17):
        k = A(n)
        b = B(n)
        assert b == 0 or 2 <= b <= 2*k - 2, (n, k, b)
        seen.setdefault(k, set()).add(b)
    # Full constructive witness test for a much larger domain.
    construction_tests = 0
    for k in range(1, 61):
        permitted = [0] + list(range(2, 2*k-1))
        for b in permitted:
            n = witness(k, b)
            assert A(n) == k, (k, b, 'weight')
            assert B(n) == b, (k, b, 'value')
            assert B(n*2**13) == b and A(n*2**13) == k
            construction_tests += 1
    assert seen[1] == {0}
    for k in range(2, 10):
        # At 2^17 every weight k<=9 has enough witnesses to reach the complete spectrum.
        assert seen[k] == ({0} | set(range(2, 2*k-1))), (k, seen[k])
    print('VERIFY_OK',
          f'direct_integer_binomial_valuations={direct_exact}',
          f'carry_comparisons={carry_tests}',
          f'complete_scan_n={(1<<17)-1}',
          f'constructive_pairs={construction_tests}',
          f'full_scanned_weight_fibers=1..9')


if __name__ == '__main__':
    main()
