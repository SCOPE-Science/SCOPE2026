#!/usr/bin/env python3
"""Independent phase-eigenvalue and inverse-range checks for a two-mobility diffusion."""
import math
import random


def forward(delta, s):
    assert 0.0 < delta < 1.0 and s > 0.0
    mean = (1.0 + 2.0 * s) / (1.0 + 2.0 * s - delta * delta)
    cv2 = 1.0 + 2.0 * delta * delta / (1.0 + 2.0 * s) ** 2
    return mean, cv2


def inverse(mean, cv2):
    a = 1.0 - 1.0 / mean
    e = cv2 - 1.0
    assert mean > 1.0 and 2 * a * a < e < 2 * a
    return math.sqrt(2.0) * a / math.sqrt(e), a / e - 0.5


def spectral_moments(delta, s):
    # Diagonalize the symmetric 2x2 killed hidden-state generator.
    w = math.hypot(delta, s)
    rslow = 1.0 + s - w
    rfast = 1.0 + s + w
    assert rslow > 0.0
    weightslow = (1.0 + s / w) / 2.0
    weightfast = (1.0 - s / w) / 2.0
    assert 0.0 < weightfast < weightslow < 1.0
    mean = weightslow / rslow + weightfast / rfast
    second = 2.0 * (weightslow / (rslow * rslow) + weightfast / (rfast * rfast))
    return mean, second / (mean * mean) - 1.0


def close(x, y, tol=1e-9):
    assert math.isclose(x, y, rel_tol=tol, abs_tol=tol), (x, y)


def main():
    rng = random.Random(2431)
    # Independent diagonalization versus explicit inverse-matrix moment identities.
    for _ in range(1000):
        d = 0.025 + 0.95 * rng.random()
        s = math.exp(-3.0 + 6.0 * rng.random())
        m, c = forward(d, s)
        ms, cs = spectral_moments(d, s)
        close(m, ms)
        close(c, cs)
        d2, s2 = inverse(m, c)
        close(d, d2)
        close(s, s2)
    # Sample data directly inside the asserted exact moment region.
    for _ in range(1000):
        m = 1.025 + 15.0 * rng.random()
        a = 1.0 - 1.0 / m
        e = 2.0 * a * a + (2.0 * a - 2.0 * a * a) * (0.025 + 0.95 * rng.random())
        d, s = inverse(m, 1.0 + e)
        assert 0.0 < d < 1.0 and s > 0.0
        m2, c2 = forward(d, s)
        close(m, m2)
        close(1 + e, c2)
    print('CHECK_OK: 1000 spectral identities + 2000 forward/inverse comparisons')


if __name__ == '__main__':
    main()
