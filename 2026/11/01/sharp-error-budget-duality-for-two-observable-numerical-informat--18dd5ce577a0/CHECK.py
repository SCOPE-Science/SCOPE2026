"""Reproduce finite numerical comparisons for a two-Pauli robustness profile.

No numerical check in this file is used to prove the general theorem.
Requires only the Python standard library.
"""
import math
import random


def envelope(e):
    return e + math.sqrt(4.0 - e * e) if e <= math.sqrt(2.0) else 2 * math.sqrt(2.0)


def dual(t, e):
    return 2.0 * math.hypot(1.0 - t, 1.0) + e * abs(t)


def unit_vector(rng):
    z = rng.uniform(-1, 1)
    theta = rng.uniform(-math.pi, math.pi)
    u = math.sqrt(1 - z * z)
    return (u * math.cos(theta), u * math.sin(theta), z)


def test():
    count = 0
    rng = random.Random(182912)
    for e in (0.0, 0.1, 0.3, 0.5, 1.0, 1.4, math.sqrt(2), 1.6, 2.0, 3.0):
        t = 1.0 - e / math.sqrt(4.0 - e * e) if e < math.sqrt(2.0) else 0.0
        assert abs(dual(t, e) - envelope(e)) < 2e-12
        count += 1
        d_x = e if e <= math.sqrt(2.0) else math.sqrt(2.0)
        d_y = math.sqrt(4.0 - d_x * d_x)
        assert abs(math.hypot(d_x, d_y) - 2.0) < 1e-12
        assert d_x <= e + 1e-12
        assert abs(d_x + d_y - envelope(e)) < 1e-12
        count += 3
        for _ in range(250):
            z = rng.uniform(-1.0, 1.0)
            radius = math.sqrt(1.0 - z * z)
            theta1 = rng.uniform(-math.pi, math.pi)
            theta2 = rng.uniform(-math.pi, math.pi)
            x = (radius * math.cos(theta1), radius * math.sin(theta1), z)
            y = (radius * math.cos(theta2), radius * math.sin(theta2), z)
            if abs(x[0] - y[0]) <= e:
                assert abs((x[0] - y[0]) + (x[1] - y[1])) <= envelope(e) + 1e-12
            count += 1
    print(f"Finite diagnostic assertions completed: {count}")


if __name__ == "__main__":
    test()
