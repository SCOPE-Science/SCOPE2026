"""Independent exact-arithmetic checks for parity-restricted Pascal-row LCM formulas."""
from math import comb, lcm


def odd_prime_power_base(n):
    """The odd prime p if n=p**a (a>=1), otherwise 1."""
    p = 3
    while p * p <= n:
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            return p if n == 1 else 1
        p += 2
    return n if n > 1 and n % 2 else 1


def predicted(n):
    if n % 2:
        return 1, 1
    w = n // 2 + 1
    v2 = (w & -w).bit_length() - 1
    loss_even = 2 ** (1 + v2 - int(w & (w - 1) == 0))
    loss_odd = odd_prime_power_base(w)
    return loss_even, loss_odd


def direct(n):
    all_lcm = even_lcm = odd_lcm = 1
    for k in range(n + 1):
        b = comb(n, k)
        all_lcm = lcm(all_lcm, b)
        if k & 1:
            odd_lcm = lcm(odd_lcm, b)
        else:
            even_lcm = lcm(even_lcm, b)
    assert all_lcm % even_lcm == 0 and all_lcm % odd_lcm == 0
    return all_lcm // even_lcm, all_lcm // odd_lcm


def main():
    for n in range(1, 801):
        expected = predicted(n)
        observed = direct(n)
        assert observed == expected, (n, observed, expected)
    for m in range(1, 151):
        for j in range(m + 1):
            # Check the claimed local 2-adic valuation reduction independently.
            a, b = comb(2 * m, 2 * j), comb(m, j)
            va = (a & -a).bit_length() - 1
            vb = (b & -b).bit_length() - 1
            assert va == vb, (m, j, va, vb)
    print('VERIFY_OK exact_row_lcms=800 doubled_index_checks=11475')


if __name__ == '__main__':
    main()
