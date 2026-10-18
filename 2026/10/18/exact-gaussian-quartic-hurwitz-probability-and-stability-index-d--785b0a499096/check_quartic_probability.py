#!/usr/bin/env python3
"""Independent elementary quadrature diagnostic for a Gaussian quartic stability probability."""
import math

def simpson(n):
    assert n > 0 and n % 2 == 0
    step = (math.pi / 2.0) / n
    total = 0.0
    for j in range(n + 1):
        t = j * step
        if j == n:
            v = math.pi / 2.0
        else:
            v = math.atan(math.sin(t) ** 2 / math.cos(t))
        total += v * (1 if j in (0, n) else 4 if j % 2 else 2)
    return step * total / 3.0

if __name__ == '__main__':
    a, b = simpson(8192), simpson(16384)
    assert abs(a - b) < 1e-10, (a, b)
    h = 1 / 16 - b / (2 * math.pi**2)
    assert 0 < h < 1 / 32
    assert abs(h - 0.009283844724298119) < 1e-10
    probs = [h, 0.25, 0.5 - 2*h, 0.25, h]
    assert abs(sum(probs) - 1) < 1e-14
    assert min(probs) > 0
    assert probs == probs[::-1]
    print('I =', repr(b))
    print('h =', repr(h))
    print('P(N_-=0..4) =', probs)
