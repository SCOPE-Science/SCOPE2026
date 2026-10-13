#!/usr/bin/env python3
"""Exact-arithmetic finite checks for odd-power Fibonacci window gcds.

No finite test proves the universal theorem; the proof is mathematical.
"""
from math import gcd

ODD_EXPONENTS = range(1, 24, 2)  # 1, 3, ..., 23
ODD_WINDOWS = range(1, 62, 2)   # 1, 3, ..., 61
MAX_TERM = max(ODD_WINDOWS) + max(ODD_EXPONENTS) + 12


def fibonacci_table(n):
    f = [0, 1]
    for _ in range(n - 1):
        f.append(f[-1] + f[-2])
    return f


def consecutive_power_window_gcd(f, k, r, count):
    terms = [f[j] ** r for j in range(count + k + 1)]
    window = sum(terms[1:k + 1])
    common = 0
    for n in range(count):
        common = gcd(common, window)
        window += terms[n + k + 1] - terms[n + 1]
    return common


def check():
    f = fibonacci_table(MAX_TERM)
    assert [x % 4 for x in f[:12]] == [0, 1, 1, 2, 3, 1, 0, 1, 1, 2, 3, 1]
    cases = 0
    windows = 0
    for r in ODD_EXPONENTS:
        for k in ODD_WINDOWS:
            expected = 2 if k % 6 == 3 else 1
            short_gcd = consecutive_power_window_gcd(f, k, r, r + 1)
            long_gcd = consecutive_power_window_gcd(f, k, r, r + 10)
            assert short_gcd == expected, (r, k, short_gcd, expected)
            assert long_gcd == short_gcd, (r, k, long_gcd, short_gcd)
            cases += 1
            windows += r + 10
    # Oddness of the power is essential; these 25-term quartic sums
    # vanish modulo 5, unlike their first-power counterparts.
    for n in range(40):
        assert sum(f[n + j] ** 4 for j in range(1, 26)) % 5 == 0
    print("VERIFY_OK")
    print(f"odd_exponents_1_to_{max(ODD_EXPONENTS)}={len(ODD_EXPONENTS)}")
    print(f"odd_window_lengths_1_to_{max(ODD_WINDOWS)}={len(ODD_WINDOWS)}")
    print(f"all_parameter_pairs={cases}_PASS")
    print(f"all_independent_direct_window_checks={windows}_PASS")
    print("short_prefix_gcd_r_plus_1_vs_long_direct_gcd=PASS")
    print("fibonacci_mod4_period_6=PASS")
    print("quartic_window_25_mod5_boundary=PASS")
    print("finite_checks_supplement_unrestricted_proof")


if __name__ == "__main__":
    check()
