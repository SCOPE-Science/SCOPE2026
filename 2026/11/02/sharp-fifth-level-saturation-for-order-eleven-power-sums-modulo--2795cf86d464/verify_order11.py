"""Exact finite certificate for order-eleven power zero sums.

Run with Python 3.9+ (standard library only): python verify_order11.py
Mathematical reduction to these finite checks is proved separately.
"""

from itertools import combinations_with_replacement
from math import comb, isqrt


def prime(n):
    if n < 2:
        return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return False
    return True


def root_of_order_11(p, k):
    modulus = p ** k
    assert prime(p) and p % 11 == 1 and k >= 1
    # Euler's theorem ensures that each candidate has eleventh power one.
    exponent = (p - 1) * p ** (k - 1) // 11
    for base in range(2, p):
        residue = pow(base, exponent, modulus)
        if residue != 1:
            assert pow(residue, 11, modulus) == 1
            assert residue % p != 1
            return residue
    raise AssertionError("Failed to find an eleventh root")


def enumerate_zero_sums(p, k):
    modulus = p ** k
    root = root_of_order_11(p, k)
    powers = [pow(root, i, modulus) for i in range(11)]
    assert len(set(powers)) == 11
    coeffs = [0] * 11
    zeros = [0] * 11
    first_witness = [None] * 11
    checked = 0

    def visit(position, remaining, residue, total):
        nonlocal checked
        if position == 10:
            coeffs[10] = remaining
            checked += 1
            if (residue + remaining * powers[10]) % modulus == 0:
                zeros[total] += 1
                if first_witness[total] is None:
                    first_witness[total] = tuple(coeffs)
            return
        for number in range(remaining + 1):
            coeffs[position] = number
            visit(position + 1, remaining - number,
                  (residue + number * powers[position]) % modulus, total)

    for total in range(1, 11):
        visit(0, total, 0, total)
    assert checked == comb(21, 11) - 1 == 352715
    minimal = next((t for t in range(1, 11) if zeros[t]), 11)
    return minimal, zeros, first_witness, root, checked


def independent_small_length_check(p, k, bound=4):
    modulus = p ** k
    root = root_of_order_11(p, k)
    powers = [pow(root, i, modulus) for i in range(11)]
    for t in range(1, bound + 1):
        count = sum(sum(powers[i] for i in indices) % modulus == 0
                    for indices in combinations_with_replacement(range(11), t))
        if count:
            return t
    return 11


def main():
    # 2155**3 > 10**10; this is the precise threshold from the
    # ten-dimensional cyclotomic resultant norm bound.
    assert 2154 ** 3 < 10 ** 10 < 2155 ** 3
    small_primes = [p for p in range(2, 2155)
                    if p % 11 == 1 and prime(p)]
    expected = [23, 67, 89, 199, 331, 353, 397, 419, 463,
                617, 661, 683, 727, 859, 881, 947, 991,
                1013, 1123, 1277, 1321, 1409, 1453, 1607,
                1783, 1871, 2003, 2069, 2113]
    assert small_primes == expected and len(small_primes) == 29
    levels = 0
    checked_total = 0
    exceptions = []
    for p in small_primes:
        minimum, zeros, witnesses, root, checked = enumerate_zero_sums(p, 3)
        checked_total += checked
        levels += 1
        assert minimum == (9 if p == 23 else 11), (p, minimum, zeros)
        if p == 23:
            assert zeros[9] > 0
            assert not any(zeros[1:9])
            exceptions.append((p, 3, minimum, root, witnesses[9]))
        else:
            assert not any(zeros[1:11])
    for k, desired in [(4, 9), (5, 11)]:
        minimum, zeros, witnesses, root, checked = enumerate_zero_sums(23, k)
        checked_total += checked
        levels += 1
        assert minimum == desired
        if k == 4:
            assert zeros[9] > 0 and not any(zeros[1:9])
            exceptions.append((23, 4, minimum, root, witnesses[9]))
        else:
            assert not any(zeros[1:11])
    # Independent combinatorial enumeration of all length <= 4 multisets.
    for p in (23, 67, 89, 199):
        assert independent_small_length_check(p, 3) == 11
    assert checked_total == 31 * 352715
    print('VERIFY_OK primes=29 levels=31 coefficient_vectors=10934165 '
          'k3_exception=23:9 k4_exception=23:9 k5_all=11')
    for item in exceptions:
        p, k, minimum, root, witness = item
        print('WITNESS p={} k={} length={} q={} counts={}'.format(
            p, k, minimum, root, ','.join(map(str, witness))))


if __name__ == '__main__':
    main()
