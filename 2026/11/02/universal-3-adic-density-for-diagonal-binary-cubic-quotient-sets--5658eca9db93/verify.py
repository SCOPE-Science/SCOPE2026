#!/usr/bin/env python3
"""Finite consistency tests of the 3-adic diagonal cubic density theorem.

Does not prove the infinite Hensel lifting or density claims.
"""
from itertools import product


def units(q):
    return {i for i in range(q) if i % 3}


def values(a, b, q):
    x3 = {pow(x, 3, q) for x in range(q)}
    return {(a * x + b * y) % q for x, y in product(x3, repeat=2)}


def check_unit_cube_classes():
    for k in range(2, 6):
        q = 3 ** k
        cubes = {pow(x, 3, q) for x in range(q) if x % 3}
        expected = {x for x in range(q) if x % 9 in (1, 8)}
        assert cubes == expected, (k, cubes, expected)


def check_one_factor_forms():
    count = 0
    for alpha in range(1, 9):
        if alpha % 3 == 0:
            continue
        for beta in range(1, 9):
            if beta % 3 == 0:
                continue
            for k in (2, 3, 4):
                q = 3 ** k
                v = values(alpha, 3 * beta, q)
                assert units(q).issubset(v), (alpha, beta, k)
                count += 1
    return count


def check_equal_unit_forms():
    count = 0
    for alpha, beta in product((1, 2, 4, 5, 7, 8), repeat=2):
        gamma = (-beta * pow(alpha, -1, 9)) % 9
        q = 3 ** 5
        v = values(alpha, beta, q)
        if gamma in (1, 8):
            assert {9 * j for j in range(q // 9)} <= v, (alpha, beta, "cube")
        else:
            assert {3 * j for j in range(q // 3) if j % 3} <= v, (alpha, beta, "noncube")
        count += 1
    return count


def check_normalization():
    checks = 0
    for a, b in product((-729, -243, -81, -27, -9, -3, -2, -1, 1, 2, 3, 9, 27, 81, 243, 729), repeat=2):
        if a == 0 or b == 0:
            continue
        if abs(a) % 3 == 0:
            A = 0
            z = a
            while z % 3 == 0:
                A += 1
                z //= 3
        else:
            A = 0
        if abs(b) % 3 == 0:
            B = 0
            z = b
            while z % 3 == 0:
                B += 1
                z //= 3
        else:
            B = 0
        if A > B:
            a, b, A, B = b, a, B, A
        alpha, beta = a // (3 ** A), b // (3 ** B)
        t, r = divmod(B - A, 3)
        assert r in (0, 1, 2)
        for x, y in product((-2, -1, 0, 1, 2), repeat=2):
            if r != 2:
                lhs = a * (3 ** t * x) ** 3 + b * y ** 3
                rhs = 3 ** (A + 3 * t) * (alpha * x ** 3 + 3 ** r * beta * y ** 3)
            else:
                lhs = a * (3 ** (t + 1) * x) ** 3 + b * y ** 3
                rhs = 3 ** (A + 3 * t + 2) * (3 * alpha * x ** 3 + beta * y ** 3)
            assert lhs == rhs
            checks += 1
    return checks



if __name__ == "__main__":
    check_unit_cube_classes()
    n1 = check_one_factor_forms()
    n2 = check_equal_unit_forms()
    n3 = check_normalization()
    # The final check above operates over a large finite modulus; avoid
    # conflating its numerical scale with a certificate for infinite claims.
    print(f"VERIFY_OK cube_class_levels=2..5 one_factor_cases={n1} equal_unit_cases={n2} normalization_pairs={n3}")
