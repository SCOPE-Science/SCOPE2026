#!/usr/bin/env python3
"""Exact-integer orbit checks for the even-degree secant-model escape theorem.

Finite checks are illustrations and algebraic consistency tests; the proof is analytic.
"""
import math


def orbit(a, d, seed, steps=5):
    x, y = seed
    states = [(x, y)]
    for _ in range(steps):
        s = x + y
        x, y = y - a * s**d, y - 2*a * s**d
        states.append((x, y))
    return states


def checks():
    for d in (2, 4):
        for a in (-2, -1, 1, 2):
            states = orbit(a, d, (1, 0), steps=6 if d == 2 else 5)
            if a < 0:
                other = orbit(-a, d, (-1, 0), steps=len(states)-1)
                assert states == [(-u, -v) for u, v in other]
            for n in range(1, len(states)-1):
                x, y = states[n]
                xp, yp = states[n+1]
                z = x-y
                r = abs(x+y)
                assert z == a*(states[n-1][0]+states[n-1][1])**d
                if a > 0 and x < 0 and y < 0:
                    assert -(xp+yp) == r+z+3*a*r**d
            # Explicit leading-direction tests use exact integer cross-products.
            x, y = states[-1]
            assert a*x < 0 and a*y < 0
            assert abs(2*x-y)*10000 < abs(y)  # x/y approaches 1/2.
            h = [(math.log(abs(u+v)) + math.log(3*abs(a))/(d-1))/d**n for n, (u, v) in enumerate(states) if u+v]
            assert h[-1] > 0
            assert abs(h[-1]-h[-2]) < 1.0e-2
    print('EXACT_ORBIT_CHECK_OK')

if __name__ == '__main__':
    checks()
