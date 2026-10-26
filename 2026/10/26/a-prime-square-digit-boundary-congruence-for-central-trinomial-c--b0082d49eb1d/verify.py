#!/usr/bin/env python3
"""Exact-integer sanity checks for a central-trinomial prime-square congruence."""

PRIMES = (5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43)
MULTIPLIER_MAX = 31


def central_trinomial_list(limit):
    values = [1, 1]
    for n in range(2, limit + 1):
        numerator = (2*n-1)*values[-1] + 3*(n-1)*values[-2]
        assert numerator % n == 0
        values.append(numerator // n)
    return values


def main():
    limit = max(p*MULTIPLIER_MAX - 1 for p in PRIMES)
    values = central_trinomial_list(limit)
    count = 0
    for p in PRIMES:
        eps = 1 if p % 3 == 1 else -1
        modulus = p*p
        for m in range(1, MULTIPLIER_MAX + 1):
            lhs = values[p*m - 1] % modulus
            first_order = (eps + m*(values[p-1]-eps))*values[m-1] % modulus
            explicit = eps*pow(3, m*(p-1), modulus)*values[m-1] % modulus
            assert lhs == first_order == explicit, (p, m, lhs, first_order, explicit)
            count += 1
        for r in range(1, 5):
            n = p**r - 1
            if n > limit:
                break
            expected = (eps**r)*pow(3, n, modulus) % modulus
            assert values[n] % modulus == expected, (p, r)
    assert count == len(PRIMES)*MULTIPLIER_MAX == 372
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
