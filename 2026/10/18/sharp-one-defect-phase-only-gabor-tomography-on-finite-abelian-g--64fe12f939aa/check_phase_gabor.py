#!/usr/bin/env python3
"""Finite arithmetic spot checks of the stated Weyl ambiguity spectrum.
This is supplemental testing, not proof over all groups or phases.
Uses only Python's standard library.
"""
import cmath
import itertools
import math

def check(moduli):
    points = list(itertools.product(*(range(k) for k in moduli)))
    lookup = {x: i for i, x in enumerate(points)}
    n = len(points)
    exponent = math.lcm(*moduli)
    t = math.pi if exponent % 2 else math.pi - math.pi / exponent
    z = cmath.exp(1j * t)
    g = [z if i == 0 else 1 for i in range(n)]
    goal = (4 * math.sin(math.pi / (2 * exponent)) if exponent % 2
            else 2 * math.sin(math.pi / exponent))
    mags = []
    forced = 0
    for a in points:
        for dual in points:
            value = 0j
            for x in points:
                xp = tuple((x[i] + a[i]) % moduli[i] for i in range(len(moduli)))
                angle = -2 * math.pi * sum(x[i] * dual[i] / moduli[i]
                                           for i in range(len(moduli)))
                value += g[lookup[xp]] * g[lookup[x]].conjugate() * cmath.exp(1j * angle)
            if not any(a) and any(dual):
                assert abs(value) < 1e-8
                forced += 1
            else:
                assert abs(value) > 1e-8
                mags.append(abs(value))
    assert forced == n - 1
    assert len(mags) == n * n - n + 1
    assert abs(min(mags) - goal) < 1e-8
    assert abs(max(mags) - n) < 1e-8
    # A dense numerical phase scan is a stress test, not an optimality proof.
    for j in range(1001):
        w = cmath.exp(2j * math.pi * j / 1000)
        scalar = abs(n - 2 + 2 * w.real)
        distances = [abs(w-1) * abs(w-cmath.exp(2j*math.pi*k/exponent))
                     for k in range(1, exponent)]
        visible = min(scalar, *distances)
        assert visible <= goal + 2e-8
    print('PASS', moduli, 'order', n, 'exponent', exponent,
          'rank', len(mags), 'minimum', round(min(mags), 10))

if __name__ == '__main__':
    for mods in [(6,), (7,), (8,), (9,), (10,), (12,),
                 (2,2,2), (4,2), (3,3), (3,2,2), (2,2,2,2), (3,3,3)]:
        check(mods)
