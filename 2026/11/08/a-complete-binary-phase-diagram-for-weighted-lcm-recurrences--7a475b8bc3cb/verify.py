"""Exact checks of the binary phase diagram for K-weighted LCM recurrences.

All recurrences are evaluated from integers using gcd, without assuming
prime-only increments. Separate implementations use unbounded integers and
modular residues to test the same claims.
"""
from math import gcd, lcm


def v2(n):
    assert n > 0
    return (n & -n).bit_length() - 1


def expected_even(K, n):
    if K % 2 == 0:
        t = v2(K + 2)
        e = n.bit_length() - 1
        return n == 1 << e and e >= 1 and (e - 1) % t == 0
    return n == 2 or (n == 4 and K % 12 in (1, 3, 11))


def expected_v2(K, n):
    t = v2(K + 2)
    r = n.bit_length() - 1
    return t * ((r + t - 1) // t)


def run_unbounded(K, N):
    A = 1
    for n in range(2, N + 1):
        c = n // gcd(n, A)
        assert (c % 2 == 0) == expected_even(K, n), (K, n, c)
        if c % 2 == 0:
            assert c == 2, (K, n, c)
        A *= K + c
        if K % 2 == 0:
            assert v2(A) == expected_v2(K, n), (K, n, v2(A))
        elif n >= 4:
            assert v2(A) >= n - 4, (K, n, v2(A))


def run_modular(K, N, mod):
    # Since n divides mod for 2 <= n <= N, gcd(n,A) == gcd(n,A mod mod).
    A = 1
    for n in range(2, N + 1):
        c = n // gcd(n, A)
        assert (c % 2 == 0) == expected_even(K, n), (K, n, c)
        if c % 2 == 0:
            assert c == 2, (K, n, c)
        A = (A * (K + c)) % mod
        if K % 2 == 0:
            # The modulus includes an extra 64 binary digits for an unambiguous valuation.
            assert v2(A) == expected_v2(K, n), (K, n, v2(A))


def main():
    for K in range(1, 321):
        run_unbounded(K, 700)
    print('UNBOUNDED_RECURRENCE_OK 320 coefficients x 699 steps')
    M = 1
    for n in range(2, 385):
        M = lcm(M, n)
    for K in range(1, 121):
        run_modular(K, 384, M << 64)
    print('MODULAR_INDEPENDENT_GCD_OK 120 coefficients x 383 steps')
    for t in range(1, 18):
        K = (1 << t) - 2
        if K == 0:
            K = 4
        run_unbounded(K, 2048)
    print('TARGETED_DYADIC_PHASES_OK t=1..17 x 2047 steps')
    for K in (1, 3, 5, 7, 11, 13, 17, 19, 23, 27, 31):
        run_unbounded(K, 4096)
    print('ODD_COEFFICIENT_PHASES_OK 11 coefficients x 4095 steps')
    print('VERIFY_OK finite_checks_only=True infinite_proof_separate=True independent_audit=False')

if __name__ == '__main__':
    main()
