"""Finite numerical sanity checks of a prime-cycle positive Fourier support theorem.

Run: python CHECK.py. Standard-library only. This is not an infinite proof.
"""
import cmath
import math


def constructed_values(p, k, D, epsilon=0.5):
    t = p - k
    d = (t + 1) // 2
    assert d <= D <= (p - 1) // 2
    result = []
    for x in range(p):
        angle = 2.0 * math.pi * x / p
        value = 1.0
        for r in range(t // 2):
            value *= math.cos(math.pi / p) - math.cos(
                2.0 * math.pi * (x - 2 * r - 0.5) / p
            )
        if t % 2:
            value *= 1.0 - math.cos(2.0 * math.pi * (x - (t - 1)) / p)
        value *= (1.0 + epsilon * math.cos(angle)) ** (D - d)
        result.append(value)
    return result


def discrete_fourier(values):
    p = len(values)
    return [
        sum(values[x] * cmath.exp(-2j * math.pi * x * y / p)
            for x in range(p))
        for y in range(p)
    ]


def check():
    checked = 0
    for p in (3, 5, 7, 11, 13):
        for k in range(1, p + 1):
            t = p - k
            d = (t + 1) // 2
            for D in range(d, (p - 1) // 2 + 1):
                v = constructed_values(p, k, D)
                scale = max(abs(z) for z in v)
                assert scale > 0
                for x, z in enumerate(v):
                    if x < t:
                        assert abs(z) < scale * 1e-8, (p, k, D, x, z)
                    else:
                        assert z > scale * 1e-10, (p, k, D, x, z)
                spectrum = discrete_fourier(v)
                sscale = max(abs(z) for z in spectrum)
                target = {j % p for j in range(-D, D + 1)}
                for j, z in enumerate(spectrum):
                    if j in target:
                        assert abs(z) > sscale * 1e-7, (p, k, D, j, z)
                    else:
                        assert abs(z) < sscale * 1e-8, (p, k, D, j, z)
                checked += 1
        print(f"p={p}: all admissible pairs checked")
    print(f"PASS: {checked} nonnegative support-pair witnesses")


if __name__ == "__main__":
    check()
