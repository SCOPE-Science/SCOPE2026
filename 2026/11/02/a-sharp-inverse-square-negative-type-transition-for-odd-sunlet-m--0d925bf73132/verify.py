#!/usr/bin/env python3
"""Standalone finite checks for the odd-sunlet negative-type asymptotic theorem.

This program illustrates finite cases. The proof for all odd orders is analytic.
Requires Python 3 standard library only.
"""
import math


def fourier_blocks(n, p):
    assert n >= 5 and n % 2 == 1 and p >= 1
    d = [min(r, n - r) for r in range(n)]
    a = [x ** p for x in d]
    b = [(x + 1) ** p for x in d]
    c = [(x + 2) ** p if r else 0.0 for r, x in enumerate(d)]
    scalar = sum(a) + sum(c) - 2 * sum(b)
    blocks = []
    for k in range(1, (n + 1) // 2):
        cosine = [math.cos(2 * math.pi * k * r / n) for r in range(n)]
        ak = sum(x * y for x, y in zip(a, cosine))
        bk = sum(x * y for x, y in zip(b, cosine))
        ck = sum(x * y for x, y in zip(c, cosine))
        eigen = (ak + ck) / 2 + math.hypot((ak - ck) / 2, bk)
        blocks.append((k, eigen, ak, bk, ck))
    return scalar, blocks


def critical_exponent(n):
    low, high = 1.0, 1.6
    for _ in range(49):
        p = (low + high) / 2
        scalar, blocks = fourier_blocks(n, p)
        if scalar > 0 or max(v[1] for v in blocks) > 0:
            high = p
        else:
            low = p
    return (low + high) / 2


def simpson(f, a, b, steps=40000):
    assert steps % 2 == 0
    h = (b - a) / steps
    s = f(a) + f(b)
    for j in range(1, steps):
        s += (4 if j % 2 else 2) * f(a + j * h)
    return s * h / 3


def main():
    checks = 0
    for n in range(5, 102, 2):
        scalar, blocks = fourier_blocks(n, 1.0)
        assert abs(scalar + 2) < 4e-9
        checks += 1
        for k, eigen, ak, bk, ck in blocks:
            angle = math.pi * k / (2 * n)
            expected = -1 / (4 * (math.cos(angle) ** 2 if k % 2 == 0
                                 else math.sin(angle) ** 2))
            assert abs(ak - expected) < 1e-8
            assert abs(bk - ak) < 1e-8
            assert abs(ck - (ak - 2)) < 1e-8
            assert eigen < 0
            checks += 4
    for n in range(5, 102, 2):
        p = critical_exponent(n)
        scalar, blocks = fourier_blocks(n, p)
        top = max(blocks, key=lambda item: item[1])
        assert top[0] == 2, (n, top)
        assert abs(top[1]) < 2e-9
        assert scalar < 0
        checks += 3
    I = simpson(lambda u: (1 - math.cos(u)) / u if u else 0.0,
                0.0, 2 * math.pi)
    target = 2 * math.pi ** 2 / I
    assert abs(target - 8.097627356866537) < 1e-8
    checks += 1
    for n, bound in [(21, .25), (41, .10), (61, .06), (101, .03)]:
        scaled = n * n * (critical_exponent(n) - 1)
        assert abs(scaled - target) < bound
        checks += 1
    for n in [5, 7, 11]:
        p = 1.07
        _, blocks = fourier_blocks(n, p)
        for k, _, a, b, c in blocks:
            # Real cosine-mode test: one amplitude on the core, another on leaves.
            z = [math.cos(2 * math.pi * k * j / n) for j in range(n)]
            for scale in [0.0, 0.3, -0.7, 1.0]:
                x = z + [scale * t for t in z]
                nodes = [(j, layer) for layer in (0, 1) for j in range(n)]
                direct = 0.0
                for i, (ri, li) in enumerate(nodes):
                    for j, (rj, lj) in enumerate(nodes):
                        dist = min((ri - rj) % n, (rj - ri) % n)
                        if li == lj == 1 and ri == rj:
                            dist = 0
                        else:
                            dist += li + lj
                        direct += x[i] * x[j] * (dist ** p)
                expected = n / 2 * (a + 2 * scale * b + scale ** 2 * c)
                assert abs(direct - expected) < 1e-8
                checks += 1
    print(f'CHECK_OK checks={checks} asymptotic_constant={target:.12f}')
    for n in [5, 9, 21, 41, 101]:
        p = critical_exponent(n)
        print(f'n={n} p={p:.12f} scaled_excess={n*n*(p-1):.9f}')


if __name__ == '__main__':
    main()
