#!/usr/bin/env python3
"""Finite numerical sanity checks for the exact barycentric triangle formula.

The mathematical proof, not the direction grid, establishes the continuum claim.
"""
import math
import random


def free_p_cost(s, t, b, c, a, p):
    """Three spanning-tree costs of molecule (-s-t,s,t)."""
    return min(
        (abs(s) * b) ** p + (abs(t) * c) ** p,
        (abs(s + t) * b) ** p + (abs(t) * a) ** p,
        (abs(s + t) * c) ** p + (abs(s) * a) ** p,
    ) ** (1.0 / p)


def run():
    rnd = random.Random(6)
    cases = 0
    directions = 720
    for _ in range(100):
        # A=(0,0), B=(1,0), C=(u,v), v>0.
        x, y = rnd.uniform(-1.8, 1.8), rnd.uniform(0.1, 1.8)
        b, c, a = 1.0, math.hypot(x, y), math.hypot(x - 1.0, y)
        costheta_a = max(-1.0, min(1.0, (b*b+c*c-a*a)/(2*b*c)))
        costheta_b = max(-1.0, min(1.0, (b*b+a*a-c*c)/(2*b*a)))
        costheta_c = max(-1.0, min(1.0, (c*c+a*a-b*b)/(2*c*a)))
        angles = tuple(math.acos(z) for z in (costheta_a, costheta_b, costheta_c))
        for p in (0.28, 0.55, 0.84, 1.0):
            predicted = 2 ** (1/p-1) / math.cos(max(angles)/2)
            sampled = 0.0
            for k in range(directions):
                angle = 2 * math.pi * k / directions
                ux, uy = math.cos(angle), math.sin(angle)
                t = uy/y
                s = ux - x*t
                sampled = max(sampled, free_p_cost(s,t,b,c,a,p))
            # Finite angular mesh only approaches the true norm.
            assert sampled <= predicted*(1+2e-11), (sampled,predicted)
            assert sampled >= predicted*(1-0.003), (sampled,predicted)
            cases += 1
    print(f'VERIFIED sampled_triangles=100 exponent_cases={cases} directions={directions}; proof_is_analytic=True')


if __name__ == '__main__':
    run()
