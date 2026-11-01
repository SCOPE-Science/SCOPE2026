#!/usr/bin/env python3
"""Exact-arithmetic regression checks for the alternating-level tree transform.

Uses the defining conditional-expectation matrices, not the closed-form
prefix-shell kernel, to construct every tested matrix entry.
"""
from fractions import Fraction
from itertools import product
from random import Random


def exact_norm(b, m):
    q = Fraction(-1, b)
    return Fraction(2 * (b - 1) * m, b + 1) + Fraction(2 * (b - 1), (b + 1) ** 2) * (1 - q ** m)


def kernel_entry(x, y, b, m):
    # x,y are length-m words over {0,...,b-1}.
    ans = 0
    for k in range(1, m + 1):
        same_k = x[:k] == y[:k]
        same_prior = x[:k-1] == y[:k-1]
        ans += (-1) ** (k-1) * (b ** k * int(same_k) - b ** (k-1) * int(same_prior))
    return ans


def direct_case(b, m, check_all_rows):
    words = list(product(range(b), repeat=m))
    n = len(words)
    target = exact_norm(b, m)
    rows = words if check_all_rows else words[:1]
    assertions = 0
    rng = Random(100000 * b + m)
    for x in rows:
        krow = [kernel_entry(x, y, b, m) for y in words]
        assert sum(krow) == 0
        assertions += 1
        assert Fraction(sum(abs(k) for k in krow), n) == target
        assertions += 1
        assert all(k != 0 for k in krow)
        assertions += 1
        # Choosing the signs of one row attains the norm.
        f = [1 if k > 0 else -1 for k in krow]
        assert Fraction(sum(k * z for k, z in zip(krow, f)), n) == target
        assertions += 1
        for _ in range(2):
            a = [rng.randrange(-4, 5) for _ in words]
            bound = max(abs(z) for z in a)
            assert abs(sum(k * z for k, z in zip(krow, a))) <= n * target * bound
            assertions += 1
    return assertions


def main():
    cases = [(b, m) for b in (2, 3, 4, 5) for m in range(1, 5) if b**m <= 125]
    cases += [(2, 7), (2, 8), (2, 9), (2, 10), (2, 11), (3, 5)]
    assertions = 0
    for b, m in cases:
        assertions += direct_case(b, m, b**m <= 64)
        exact = exact_norm(b, m)
        assert exact > 0
        assertions += 1
        # The exact depth increment is positive.
        if m > 1:
            increment = Fraction(2*(b-1), b+1) * (1 + Fraction((-1)**(m-1), b**m))
            assert exact - exact_norm(b, m-1) == increment
            assertions += 1
    print(f"PASS: {len(cases)} configurations, {assertions} exact rational assertions")
    print("sample b=2:", [str(exact_norm(2, m)) for m in range(1, 7)])
    print("sample b=3:", [str(exact_norm(3, m)) for m in range(1, 6)])


if __name__ == '__main__':
    main()
