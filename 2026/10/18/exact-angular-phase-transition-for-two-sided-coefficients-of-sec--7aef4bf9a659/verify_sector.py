"""Reproduce numerical consistency tests for the sector-valued harmonic Hardy coefficient profile.

Only Python standard-library modules are used. This is a finite numerical check,
not a substitute for the analytic proof.
"""
import cmath
import math
import random

TAU = 2 * math.pi
N = 8192


def cone_projection(z, beta):
    phase = cmath.phase(z)
    clamped = max(-beta, min(beta, phase))
    direction = cmath.exp(1j * clamped)
    length = max(0.0, (z / direction).real)
    return length * direction


def ratio(trace, order):
    N = len(trace)
    norm = math.sqrt(sum(abs(x)**2 for x in trace) / N)
    cn = sum(x * cmath.exp(-1j * order * TAU * (j + 0.5) / N)
             for j, x in enumerate(trace)) / N
    cm = sum(x * cmath.exp(1j * order * TAU * (j + 0.5) / N)
             for j, x in enumerate(trace)) / N
    return (abs(cn) + abs(cm)) / norm


def test():
    cases = [
        (0.0, 0.0),
        (math.pi / 9, -0.11),
        (math.pi / 6, 0.2),
        (math.pi / 4, -0.3),
        (math.pi / 4, 0.7),
        (math.pi / 4, 1.5),
        (0.30 * math.pi, math.pi / 2),
        (math.pi / 3, -math.pi / 2),
        (0.4 * math.pi, math.pi / 2),
        (math.pi / 2, math.pi / 2),
    ]
    for beta, theta in cases:
        for order in [1, 3, 7]:
            trace = [cone_projection(2*cmath.exp(-1j*theta)*math.cos(order*TAU*(j+0.5)/N+0.271), beta)
                     for j in range(N)]
            observed = ratio(trace, order)
            expected = max(1.0, math.sqrt(2)*math.sin(beta))
            assert abs(observed-expected) < 2.0e-6, (beta, theta, order, observed, expected)
    rng = random.Random(27092026)
    for beta in [0.01, math.pi/6, math.pi/4, math.pi/3, math.pi/2]:
        for order in [1, 5]:
            trace = [rng.random()*cmath.exp(1j*rng.uniform(-beta,beta)) for _ in range(2048)]
            assert ratio(trace, order) <= max(1.0, math.sqrt(2)*math.sin(beta)) + 1.0e-12
    for beta in [0.1, math.pi/4, 0.4*math.pi]:
        for theta in [0.0, 0.5, 1.2]:
            left = math.cos(theta-beta)**2 + math.cos(theta+beta)**2
            right = 1.0+math.cos(2*theta)*math.cos(2*beta)
            assert abs(left-right) < 1.0e-12
    print('PASS: 30 sampled sharpness configurations, 10 random-cone inequality tests, and 9 trigonometric checks')


if __name__ == '__main__':
    test()
