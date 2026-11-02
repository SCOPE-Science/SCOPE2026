"""Standalone numerical checks of rectangular flat Klein-bottle distance moments.

Run with Python 3 (standard library only): python verify.py
The analytical theorem does not rely on Monte Carlo or quadrature.
"""

import math
import random
from fractions import Fraction


def expectation_formula(a, b):
    if not (a > 0 and b > 0):
        raise ValueError("a and b must be positive")
    p = a * a / 3 + b * b / 12 - 2 * a**4 / (45 * b * b)
    if a <= b:
        return p
    h = math.sqrt((a - b) * (a + b))
    expression = (
        a * h * (8 * a**4 - 26 * a*a*b*b + 33 * b**4)
        - 15 * b**6 * math.acosh(a / b)
    )
    return p + expression / (180 * b*b*a*a)


def simpson_integral_correction(a, b, n=8192):
    if a <= b:
        return 0.0
    if n % 2:
        raise ValueError("even n required")
    dx = (a - b) / n
    f = lambda u: max(0.0, (u - b) * (u + b)) ** 2.5
    acc = f(b) + f(a)
    for i in range(1, n):
        acc += (4 if i % 2 else 2) * f(b + i * dx)
    return (4 / (15 * b*b*a*a)) * dx * acc / 3


def torus_expectation(a, b):
    return a*a / 3 + b*b / 12


def reduced_distance_sq(x, y, xp, yp, a, b):
    def horizontal_distance(z):
        return abs((z + a) % (2 * a) - a)
    u = horizontal_distance(x - xp)
    v = horizontal_distance(x + xp)
    t = abs(y - yp)
    return min(u*u + t*t, v*v + (b - t)**2)


def deck_distance_sq(x, y, xp, yp, a, b):
    best = float("inf")
    for k in range(-2, 3):
        for j in range(-2, 3):
            best = min(
                best,
                (x - xp - 2*k*a)**2 + (y - yp - 2*j*b)**2,
                (x + xp - 2*k*a)**2 + (y - yp - (2*j+1)*b)**2,
            )
    return best


def run():
    # Exact rational checks in the polynomial regime, including the crossover.
    q1 = Fraction(1, 3) + Fraction(1, 12) - Fraction(2, 45)
    q2 = Fraction(1, 3) + Fraction(4, 12) - Fraction(2, 45*4)
    assert q1 == Fraction(67, 180)
    assert q2 == Fraction(59, 90)
    assert math.isclose(expectation_formula(1.0, 1.0), float(q1), abs_tol=1e-14)
    assert math.isclose(expectation_formula(1.0, 2.0), float(q2), abs_tol=1e-14)

    # Independently integrate the positive-part correction for all regimes.
    for a, b in [(0.5, 2.0), (1.0, 1.0), (1.0, 2.0),
                 (2.0, 1.0), (3.0, 1.0), (1.5, 1.0), (5.0, 1.0)]:
        p = a*a/3 + b*b/12 - 2*a**4/(45*b*b)
        numerical = p + simpson_integral_correction(a, b)
        closed = expectation_formula(a, b)
        assert abs(numerical - closed) < 2e-9 * max(1, closed), (a, b, numerical, closed)
        assert closed < torus_expectation(a, b), (a, b, closed)

    # Deck-orbit formula checked without using the reduced probabilistic law.
    rng = random.Random(321321)
    largest_deck_residual = 0.0
    for a, b in [(1.0, 1.0), (1.0, 2.0), (2.0, 1.0), (4.0, 0.6)]:
        for _ in range(3000):
            x, xp = 2*a*rng.random(), 2*a*rng.random()
            y, yp = b*rng.random(), b*rng.random()
            residual = abs(reduced_distance_sq(x, y, xp, yp, a, b)
                           - deck_distance_sq(x, y, xp, yp, a, b))
            largest_deck_residual = max(largest_deck_residual, residual)
            assert residual < 1e-11 * max(1, a*a+b*b), (a, b, residual)

    # Fresh independent Monte Carlo cross-check of the second moment.
    for a, b in [(1.0, 1.0), (1.0, 2.0), (2.0, 1.0), (3.0, 1.0)]:
        count = 150000
        total, total2 = 0.0, 0.0
        for _ in range(count):
            x, xp = 2*a*rng.random(), 2*a*rng.random()
            y, yp = b*rng.random(), b*rng.random()
            z = reduced_distance_sq(x, y, xp, yp, a, b)
            total += z
            total2 += z*z
        mean = total / count
        variance = max(0.0, total2 / count - mean*mean)
        se = math.sqrt(variance / count)
        target = expectation_formula(a, b)
        assert abs(mean - target) < 6*se + 0.0005, (a, b, mean, target, se)
        print(f"a={a:g}, b={b:g}, observed={mean:.8f}, theorem={target:.8f}, SE={se:.7f}")
    print(f"deck residual maximum: {largest_deck_residual:.3e}")
    print("PASS: exact-rational, independent quadrature, deck-orbit and Monte Carlo checks")


if __name__ == "__main__":
    run()
