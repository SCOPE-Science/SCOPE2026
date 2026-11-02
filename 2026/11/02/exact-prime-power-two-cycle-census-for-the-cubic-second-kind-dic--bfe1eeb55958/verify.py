#!/usr/bin/env python3
"""Exact polynomial identity and independent finite checks of cubic-map two-cycles."""
from math import ceil


def mul(a, b):
    z = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            z[i + j] += ai * bj
    return z


def compose(a, b):
    out = [0]
    for coeff in reversed(a):
        out = mul(out, b)
        out[0] += coeff
    return out


def sub(a, b):
    n = max(len(a), len(b))
    return [(a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0)
            for i in range(n)]


def pred(p, k, x):
    if p != 2:
        h = (k + 2) // 3
        return (x - 1) % (p ** h) == 0 or (x + 1) % (p ** h) == 0
    if k == 1:
        return False
    if k <= 10:
        return x % 2 == 1
    r = (k + 1) // 3  # ceil((k-1)/3)
    mod = 2 ** (r - 1)
    return x % mod in (1, mod - 1)


def expected(p, k):
    if p != 2:
        return 2 * p ** (k - (k + 2) // 3)
    if k == 1:
        return 0
    if k <= 10:
        return 2 ** (k - 1)
    r = (k + 1) // 3
    return 2 ** (k - r + 2)


def fmod(x, modulus):
    return (x * x * x - 2 * x) % modulus


def main():
    f = [0, -2, 0, 1]
    f2_minus_x = sub(compose(f, f), [0, 1])
    fixed = mul([0, 1], [-3, 0, 1])
    cube = mul(mul([-1, 0, 1], [-1, 0, 1]), [-1, 0, 1])
    assert f2_minus_x[:len(mul(fixed, cube))] == mul(fixed, cube) and not any(f2_minus_x[len(mul(fixed, cube)):])
    assert sub(f, [0, 1]) == fixed
    configs = {2: 15, 3: 9, 5: 7, 7: 5, 11: 4, 13: 4, 17: 3, 19: 3}
    levels = 0
    residues = 0
    for p, top in configs.items():
        for k in range(1, top + 1):
            modulus = p ** k
            total = 0
            for x in range(modulus):
                y = fmod(x, modulus)
                z = fmod(y, modulus)
                direct = (z == x and y != x)
                predicted = pred(p, k, x)
                assert direct == predicted, (p, k, x, direct, predicted)
                total += direct
            assert total == expected(p, k), (p, k, total, expected(p, k))
            assert total % 2 == 0
            levels += 1
            residues += modulus
    print(f'VERIFY_OK prime_power_levels={levels} residue_classes={residues} identity=exact')


if __name__ == '__main__':
    main()
