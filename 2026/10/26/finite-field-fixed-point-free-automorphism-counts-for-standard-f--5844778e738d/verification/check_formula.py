"""Arithmetic cross-check for the fixed-point-free count formula.

This script checks the divisor-sum identity by an independent enumeration of
pairs of exponents in a cyclic group of order q-1. It does not prove the Lie
algebra automorphism classification or the universal theorem.
"""
from math import gcd


def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def is_prime_power(q):
    for p in range(2, q + 1):
        if is_prime(p):
            r = q
            while r % p == 0:
                r //= p
            if r == 1:
                return True
    return False


def divisors(m):
    return [d for d in range(1, m + 1) if m % d == 0]


def euler_phi(d):
    return sum(1 for k in range(1, d + 1) if gcd(k, d) == 1)


def divisor_sum_pairs(q, n):
    m = q - 1
    return sum(euler_phi(d) * (m - min(d, n - 1)) for d in divisors(m) if d > 1)


def direct_pairs(q, n):
    """Count admissible (a,b) using exponents in a cyclic group of order q-1."""
    m = q - 1
    total = 0
    for i in range(m):
        if i == 0:  # a = 1 is forbidden
            continue
        for j in range(m):
            if all((j + k * i) % m != 0 for k in range(n - 1)):
                total += 1
    return total


def is_composite(n):
    return n > 1 and any(n % d == 0 for d in range(2, n))


def fixed_point_free_count(q, n):
    if n < 4 or not is_prime_power(q):
        raise ValueError("Require n >= 4 and q a prime power")
    return q ** (2 * n - 3) * divisor_sum_pairs(q, n)


def main():
    qs = [q for q in range(2, 65) if is_prime_power(q)]
    tests = 0
    for q in qs:
        for n in range(4, 13):
            assert divisor_sum_pairs(q, n) == direct_pairs(q, n), (q, n)
            count = fixed_point_free_count(q, n)
            assert (count > 0) == (n < q or is_composite(q - 1)), (q, n, count)
            tests += 1
        n = 4
        expected = q ** 5 * ((q - 3) ** 2 if q % 2 else (q - 2) * (q - 4))
        assert fixed_point_free_count(q, n) == expected, (q, n, expected)
    print(f"CHECK_OK: {tests} divisor-sum/direct-count and existence-cutoff cases; n=4 simplification checked for {len(qs)} prime powers")


if __name__ == "__main__":
    main()
