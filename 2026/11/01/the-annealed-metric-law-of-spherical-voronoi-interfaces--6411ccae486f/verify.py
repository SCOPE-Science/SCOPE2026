#!/usr/bin/env python3
"""Independent exact-moment and geometric-sampling checks for a spherical Voronoi metric law.

Python 3 standard library only. The random experiments are corroboration, not a proof.
"""
from fractions import Fraction
from math import comb, exp, gamma, lgamma, pi, sin, cos, sqrt, atan2
import random


def rising(q, k):
    out = Fraction(1)
    for j in range(k):
        out *= q + j
    return out


def moment(n, k):
    from math import factorial
    return (16**k * factorial(k) * rising(Fraction(2*n-1, 2), k)
            / rising(Fraction(n+1), 2*k))


def expected_length_over_pi(n):
    return Fraction(4*(n-1)*comb(2*n-2, n-1), 4**(n-1))


# Cross-check the closed form with an independently evaluated gamma/Beta integral.
for n in (2, 3, 4, 5, 6, 10, 100):
    exact = pi*float(expected_length_over_pi(n))
    beta = comb(n, 2)*16*exp(lgamma(n-.5)+lgamma(1.5)-lgamma(n+1))
    assert abs(exact/beta - 1) < 1e-12
assert expected_length_over_pi(2) == 2
assert expected_length_over_pi(3) == 3
assert expected_length_over_pi(4) == Fraction(15, 4)
for n in (2, 3, 4, 9):
    assert moment(n, 0) == 1
    assert moment(n, 1) == Fraction(8*(2*n-1), (n+1)*(n+2))
    for k in range(1, 5):
        u2 = rising(Fraction(2*n-1, 2), k)*rising(Fraction(3, 2), k)/rising(Fraction(n+1), 2*k)
        v = rising(Fraction(1), k)/rising(Fraction(3, 2), k)
        assert 16**k*u2*v == moment(n, k)
for k in (1, 2, 3):
    from math import factorial
    large_n = 40000
    scaled = Fraction(large_n**k, 16**k) * moment(large_n, k)
    assert abs(float(scaled)/factorial(k)-1) < 0.002


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])


def unit(a):
    norm = sqrt(dot(a, a))
    return tuple(x/norm for x in a)


def sample_point(rng):
    z, t = rng.uniform(-1, 1), rng.uniform(0, 2*pi)
    h = sqrt(1-z*z)
    return (h*cos(t), h*sin(t), z)


def edge_integrals(points):
    """Integrate all Voronoi interfaces directly by angular interval clipping.

    Unlike the coarea proof, this evaluates realized random tessellations.
    Returns length, integrated normalized height U, integrated squared chord Q.
    """
    n = len(points)
    length = u_integral = q_integral = 0.0
    for i in range(n):
        for j in range(i+1, n):
            a, b = points[i], points[j]
            normal = unit(tuple(x-y for x, y in zip(a, b)))
            axis = (0, 0, 1) if abs(normal[2]) < .9 else (0, 1, 0)
            e = unit(cross(normal, axis))
            f = cross(normal, e)
            endpoints = [0.0, 2*pi]
            inequalities = []
            for k in range(n):
                if k == i or k == j:
                    continue
                v = tuple(x-y for x, y in zip(a, points[k]))
                ve, vf = dot(e, v), dot(f, v)
                phase = atan2(vf, ve)
                endpoints.extend(((phase+pi/2)%(2*pi), (phase+3*pi/2)%(2*pi)))
                inequalities.append((ve, vf))
            endpoints.sort()
            for start, end in zip(endpoints[:-1], endpoints[1:]):
                midpoint = (start+end)/2
                if not all(x*cos(midpoint)+y*sin(midpoint) >= -1e-12
                           for x, y in inequalities):
                    continue
                delta = end-start
                length += delta
                ae, af = dot(a, e), dot(a, f)
                height_integral = (ae*(sin(end)-sin(start))
                                   + af*(cos(start)-cos(end)))
                u_integral += (delta+height_integral)/2
                q_integral += delta * sum((a[p]-b[p])**2 for p in range(3))
    return length, u_integral, q_integral


rng = random.Random(704217)
for n, reps in ((2, 1600), (3, 600), (4, 1500), (6, 1200)):
    totals = [0., 0., 0.]
    for _ in range(reps):
        three = edge_integrals([sample_point(rng) for _ in range(n)])
        for j in range(3):
            totals[j] += three[j]
    length = totals[0]/reps
    u = totals[1]/totals[0]
    q = totals[2]/totals[0]
    theoretical_length = float(expected_length_over_pi(n))*pi
    theoretical_u = (n-.5)/(n+1)
    theoretical_q = float(moment(n, 1))
    assert abs(length/theoretical_length-1) < .025, (n, 'length', length)
    assert abs(u-theoretical_u) < .025, (n, 'height', u)
    assert abs(q/theoretical_q-1) < .035, (n, 'chord', q)
    print(f'n={n} mean_total_length={length:.8f} theory={theoretical_length:.8f}'
          f' length_weighted_U={u:.7f} theory={theoretical_u:.7f}'
          f' length_weighted_Q={q:.7f} theory={theoretical_q:.7f}')
print('ALL_EXACT_MOMENT_AND_GEOMETRIC_CHECKS_PASSED')
