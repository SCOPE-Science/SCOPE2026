"""Supplementary numerical diagnostics for two conditional Cartesian-radius envelopes.
Run with Python 3, no external packages. Finite tests are not the analytic proof.
"""
import math
import random

PI = math.pi


def profiles(u):
    phi = math.acos(u)
    s = math.sqrt(max(0.0, 1.0-u*u))
    return (u*u + ((1-2*u*u)*phi+u*s)/PI,
            1 - (phi-u*s)/PI)


def h_bounds(u, theta):
    c = abs(math.cos(theta))
    s = abs(math.sin(theta))
    low = max(u, s)
    high = 1.0 if c <= u else u*c+math.sqrt(max(0, 1-u*u))*s
    return low, high


def mean_square(f, count=32768):
    return sum(f(2*PI*j/count)**2 for j in range(count))/count


def test():
    assertions = 0
    for u in [0.0, 0.01, 0.08, 0.2, 0.5, 0.73, 0.9, 0.99, 1.0]:
        low, high = profiles(u)
        value_low = mean_square(lambda t: h_bounds(u,t)[0])
        value_high = mean_square(lambda t: h_bounds(u,t)[1])
        assert abs(value_low-low) < 4e-8
        assert abs(value_high-high) < 4e-8
        assertions += 2
        assert abs((high-low)-2*(1-u*u)*math.asin(u)/PI) < 1e-12
        assertions += 1
        for weight in [0.0, 0.25, 0.5, 0.75, 1.0]:
            val = mean_square(lambda t: (1-weight)*h_bounds(u,t)[0] + weight*h_bounds(u,t)[1],4096)
            assert low-2e-6 <= val <= high+2e-6
            assertions += 1
    rng = random.Random(108351)
    for _ in range(160):
        points = [rng.uniform(0.2,1.7)*complex(math.cos(a),math.sin(a))
                  for a in [rng.uniform(0,2*PI) for _ in range(12)]]
        count = 8192
        h = [max(abs(z.real*math.cos(2*PI*j/count)+z.imag*math.sin(2*PI*j/count))
                 for z in points) for j in range(count)]
        u = min(h)/max(h)
        q = sum(x*x for x in h)/count/max(h)**2
        a,b = profiles(u)
        assert a-1e-6 <= q <= b+1e-6
        assertions += 1
    for u in [0.001, 0.0005, 0.0001]:
        low, _ = profiles(u)
        assert abs((low-0.5)/(u**3)-4/(3*PI)) < 3e-4
        assertions += 1
    print('PASS:', assertions, 'supplementary profile and finite-spectrum assertions')

if __name__ == '__main__':
    test()
