"""Finite numerical sanity checks for the elementary Blaschke norm profile.

The analytic theorem is proved separately; sampling never certifies a
continuous supremum or a global minimax statement.
"""
import cmath
import math
import random


def factor(z, a):
    return (z - a) / (1 - a.conjugate() * z)


def parameters(a, b):
    delta = abs((b - a) / (1 - a.conjugate() * b))
    omega = (1 - a * b.conjugate()) / (1 - a.conjugate() * b)
    return delta, omega


def predicted_norm(a, b, u, v):
    if u == 0 or v == 0:
        return abs(u) + abs(v)
    delta, omega = parameters(a, b)
    alpha = 2 * math.asin(delta)
    orientation = u * omega * v.conjugate() / (abs(u) * abs(v))
    phase = abs(cmath.phase(orientation))
    gap = max(0.0, phase - alpha)
    return math.sqrt(max(0.0, abs(u)**2 + abs(v)**2
                              + 2 * abs(u) * abs(v) * math.cos(gap)))


def predicted_projection(a, b):
    delta, omega = parameters(a, b)
    scalar = omega * max(0.0, 1 - 2 * delta**2)
    distance = (2 * delta * math.sqrt(1 - delta**2)
                if delta <= 1 / math.sqrt(2) else 1.0)
    return scalar, distance


def sampled_norm(a, b, u, v, mesh=8192):
    return max(abs(u * factor(cmath.exp(2j * math.pi * j / mesh), a)
                   + v * factor(cmath.exp(2j * math.pi * j / mesh), b))
               for j in range(mesh))


def main():
    rng = random.Random(1137)
    pairs = [(0j, 0j), (0j, 0.1), (0j, 1 / math.sqrt(2)),
             (0j, 0.92), (0.2+0.3j, -0.4+0.25j),
             (0.6+0.1j, 0.8+0.05j), (-0.9+0.01j, 0.75-0.15j)]
    for _ in range(17):
        a = complex(rng.uniform(-0.8, 0.8), rng.uniform(-0.4, 0.4))
        b = complex(rng.uniform(-0.8, 0.8), rng.uniform(-0.4, 0.4))
        pairs.append((a, b))
    checked = 0
    largest_error = 0.0
    for a, b in pairs:
        coeffs = [(1+0j, 0j), (0j, 1+0j), (1+0j, -1+0j),
                  (0.2+0.4j, 0.7-0.3j), (1+0j, 1j)]
        scalar, distance = predicted_projection(a, b)
        coeffs.append((1+0j, -scalar))
        for u, v in coeffs:
            calculated = predicted_norm(a, b, u, v)
            sampled = sampled_norm(a, b, u, v)
            error = abs(calculated - sampled)
            largest_error = max(largest_error, error)
            assert sampled <= calculated + 1e-10, (a, b, u, v, sampled, calculated)
            assert error < 0.001, (a, b, u, v, sampled, calculated)
            checked += 1
        assert abs(predicted_norm(a, b, 1, -scalar) - distance) < 1e-12
    print('PASS: %d boundary-sampling checks; largest mesh discrepancy %.8g' %
          (checked, largest_error))
    print('Sampling is illustrative, not proof of the continuum theorem.')


if __name__ == '__main__':
    main()
