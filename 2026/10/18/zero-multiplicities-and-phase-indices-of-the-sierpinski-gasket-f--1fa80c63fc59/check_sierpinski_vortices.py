"""Reproduce independent finite checks for the Sierpinski Fourier zero divisor.

This checker is supplementary; finite computations are not the proof of the
unrestricted statements. Run with Python 3 and the standard library only.
"""
from __future__ import annotations
import cmath
import math

TAU = 2 * math.pi


def zero_order(u: int, v: int) -> int:
    if (u % 3, v % 3) not in ((1, 2), (2, 1)):
        return 0
    ans = 1
    while u % (2 ** ans) == 0 and v % (2 ** ans) == 0:
        ans += 1
    return ans


def transform(x: float, y: float, depth: int = 42) -> complex:
    product = 1 + 0j
    for j in range(1, depth + 1):
        scale = 2.0 ** j
        product *= (1 + cmath.exp(-1j * TAU * x / scale)
                    + cmath.exp(-1j * TAU * y / scale)) / 3
    return product


def winding(u: int, v: int, radius: float = 0.09, samples: int = 1024) -> int:
    # Calculate the winding using a small frequency-space circle around a zero.
    x0, y0 = 2 * u / 3, 2 * v / 3
    z = [transform(x0 + radius * math.cos(TAU * k / samples),
                   y0 + radius * math.sin(TAU * k / samples))
         for k in range(samples)]
    assert min(abs(w) for w in z) > 1e-14
    theta = sum(cmath.phase(z[(k + 1) % samples] / z[k])
                for k in range(samples))
    return round(theta / TAU)


def count_ball(radius: int):
    bound = (3 * radius + 1) // 2 + 1
    multiplicity = {}
    charged = {-1: 0, 0: 0, 1: 0}
    for u in range(-bound, bound + 1):
        for v in range(-bound, bound + 1):
            if 4 * (u * u + v * v) > 9 * radius * radius:
                continue
            order = zero_order(u, v)
            if not order:
                continue
            multiplicity[order] = multiplicity.get(order, 0) + 1
            orient = -1 if (u % 3, v % 3) == (1, 2) else 1
            charged[orient if order % 2 else 0] += 1
    return multiplicity, charged


def main():
    examples = [(1, -1), (-1, 1), (2, -2), (-2, 2),
                (4, -4), (-4, 4), (8, -8), (-8, 8)]
    for u, v in examples:
        order = zero_order(u, v)
        w = winding(u, v)
        expected = 0 if order % 2 == 0 else (-1 if u % 3 == 1 else 1)
        assert w == expected, (u, v, order, w, expected)
        assert abs(transform(2 * u / 3, 2 * v / 3)) < 1e-10
    for radius in (9, 27, 90, 180):
        multiplicity, charged = count_ball(radius)
        total = sum(multiplicity.values())
        assert charged[1] == charged[-1]
        for level in range(1, 5):
            # The exact scaling identity for nodes of multiplicity >= level.
            tail = sum(ct for order, ct in multiplicity.items() if order >= level)
            smaller, _ = count_ball_integer_scaled(radius, 2 ** (level - 1))
            assert tail == smaller, (radius, level, tail, smaller)
        print(f'R={radius}, zeros={total}, winding={charged}, first_orders={dict(sorted(multiplicity.items())[:5])}')
    print('All independently enumerated zero orders, exact scaling counts, and local phase windings passed.')


def count_ball_integer_scaled(radius: int, scale: int):
    # Count base zeros of Euclidean radius <= radius / scale with exact integers.
    bound = (3 * radius + 2 * scale - 1) // (2 * scale) + 1
    count = 0
    for u in range(-bound, bound + 1):
        for v in range(-bound, bound + 1):
            if (u % 3, v % 3) not in ((1, 2), (2, 1)):
                continue
            if 4 * scale * scale * (u * u + v * v) <= 9 * radius * radius:
                count += 1
    return count, None

if __name__ == '__main__':
    main()
