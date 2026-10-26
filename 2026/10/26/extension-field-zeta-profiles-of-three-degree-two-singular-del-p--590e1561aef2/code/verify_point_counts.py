#!/usr/bin/env python3
"""Exhaustive point and Jacobian-gradient checks for three degree-two surfaces.

Only Python's standard library is required.  F_(2^m) is represented by binary
polynomials modulo a fixed irreducible polynomial.  Weighted-projective points
are uniquely represented by normalizing the first nonzero coordinate among
(x,y,z) to 1; (0,0,0,1) is not on any of these surfaces.
"""
from itertools import product

IRREDUCIBLE = {
    1: 0b11,
    2: 0b111,
    3: 0b1011,
    4: 0b10011,
    5: 0b100101,
    6: 0b1000011,
}
EXPECTED_TOTALS = {
    "A1": [1, 33, 25, 321, 961, 4545],
    "3A1": [3, 37, 57, 337, 993, 4417],
    "D4": [1, 33, 49, 321, 961, 4353],
}
EXPECTED_SMOOTH = {
    "A1": [0, 32, 24, 320, 960, 4544],
    "3A1": [0, 34, 54, 334, 990, 4414],
    "D4": [0, 32, 48, 320, 960, 4352],
}
EXPECTED_TRACES = {
    "A1": [-3, 3, -6, 3, -3, 6],
    "3A1": [-2, 4, -2, 4, -2, 4],
    "D4": [-3, 3, -3, 3, -3, 3],
}
EXPECTED_CHARPOLY = {
    "A1": [1, 3, 3, 2, 3, 3, 1],
    "3A1": [1, 2, 0, -2, -1],
    "D4": [1, 3, 3, 1],
}


def add(a, b):
    return a ^ b


def mul(a, b, m):
    out = 0
    modulus = IRREDUCIBLE[m]
    top = 1 << m
    while b:
        if b & 1:
            out ^= a
        b >>= 1
        a <<= 1
        if a & top:
            a ^= modulus
    return out


def power(a, n, m):
    out = 1
    while n:
        if n & 1:
            out = mul(out, a, m)
        a = mul(a, a, m)
        n >>= 1
    return out


def projective_base_points(q):
    for y, z in product(range(q), repeat=2):
        yield (1, y, z)
    for z in range(q):
        yield (0, 1, z)
    yield (0, 0, 1)


def equation_and_gradient(kind, x, y, z, w, m):
    x2, y2, z2 = power(x, 2, m), power(y, 2, m), power(z, 2, m)
    x4, y4, z4 = power(x, 4, m), power(y, 4, m), power(z, 4, m)
    if kind == "A1":
        g = add(add(y2, mul(y, z, m)), z2)
        f = add(power(w, 2, m), mul(w, g, m))
        for term in (mul(mul(x2, y, m), z, m),
                     mul(mul(x, y, m), z2, m), y4,
                     mul(y2, z2, m), z4):
            f = add(f, term)
        grad = (
            mul(y, z2, m),
            add(mul(w, z, m), add(mul(x2, z, m), mul(x, z2, m))),
            add(mul(w, y, m), mul(x2, y, m)),
            g,
        )
    elif kind == "3A1":
        f = add(power(w, 2, m), mul(w, x2, m))
        for term in (x4, mul(mul(x2, y, m), z, m),
                     mul(mul(x, y2, m), z, m),
                     mul(mul(x, y, m), z2, m), mul(y2, z2, m)):
            f = add(f, term)
        grad = (
            x2,
            add(mul(y2, z, m), mul(y, z2, m)),
            add(mul(x2, z, m), mul(x, z2, m)),
            add(mul(x2, y, m), mul(x, y2, m)),
        )
    elif kind == "D4":
        g = add(add(y2, mul(y, z, m)), z2)
        f = add(power(w, 2, m), mul(w, g, m))
        for term in (mul(mul(x, y2, m), z, m),
                     mul(mul(x, y, m), z2, m), y4,
                     mul(y2, z2, m), z4):
            f = add(f, term)
        grad = (
            add(mul(y2, z, m), mul(y, z2, m)),
            add(mul(w, z, m), mul(x, z2, m)),
            add(mul(w, y, m), mul(x, y2, m)),
            g,
        )
    else:
        raise ValueError(kind)
    return f, grad


def enumerate_surface(kind, m):
    q = 1 << m
    total = smooth = singular = 0
    for x, y, z in projective_base_points(q):
        for w in range(q):
            f, grad = equation_and_gradient(kind, x, y, z, w, m)
            if f == 0:
                total += 1
                if any(grad):
                    smooth += 1
                else:
                    singular += 1
    return total, smooth, singular


def newton_coefficients(power_sums):
    """Descending coefficients of the monic polynomial from its power sums."""
    rank = len(power_sums)
    elementary = [1]
    for k in range(1, rank + 1):
        numerator = sum(((-1) ** (i - 1)) * elementary[k - i] * power_sums[i - 1]
                        for i in range(1, k + 1))
        assert numerator % k == 0
        elementary.append(numerator // k)
    return [((-1) ** i) * elementary[i] for i in range(rank + 1)]


def main():
    ranks = {"A1": 6, "3A1": 4, "D4": 3}
    for kind in ("A1", "3A1", "D4"):
        totals, smooths, traces = [], [], []
        for m in range(1, 7):
            total, smooth, singular = enumerate_surface(kind, m)
            totals.append(total)
            smooths.append(smooth)
            q = 1 << m
            traces.append((total - (q * q + q + 1)) // q)
            assert (total - (q * q + q + 1)) % q == 0
            assert singular == (1 if kind in ("A1", "D4") else 3)
        assert totals == EXPECTED_TOTALS[kind], (kind, totals)
        assert smooths == EXPECTED_SMOOTH[kind], (kind, smooths)
        assert traces == EXPECTED_TRACES[kind], (kind, traces)
        coeffs = newton_coefficients(traces[:ranks[kind]])
        assert coeffs == EXPECTED_CHARPOLY[kind], (kind, coeffs)
        print(f"{kind}: totals q=2,4,8,16,32,64 = {totals}")
        print(f"{kind}: smooth counts q=2,4,8,16,32,64 = {smooths}")
        print(f"{kind}: trace powers = {traces}; characteristic coefficients = {coeffs}")
    print("ALL_EXHAUSTIVE_CHECKS_PASS")


if __name__ == "__main__":
    main()
