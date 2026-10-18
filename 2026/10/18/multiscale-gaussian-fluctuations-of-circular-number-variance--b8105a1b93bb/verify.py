"""Finite checks of circular number-variance identities (Python standard library)."""
from math import pi, sin
from random import Random


def covariance_kernel(s, t):
    a, b = min(s, 1-s), min(t, 1-t)
    u, v = min(a, b), max(a, b)
    return (2.0 / 3.0) * u*u * (3*v*(1-v)-u)


def spectral_covariance(s, t, modes=4000):
    return sum((2*sin(pi*k*s)**2/(pi*k)**2) *
               (2*sin(pi*k*t)**2/(pi*k)**2)
               for k in range(1, modes+1))


def circular_overlap(s, d):
    d %= 1.0
    return max(0., s-d)+max(0., s-(1-d))-s*s


def count_variance(points, s):
    n = len(points)
    cuts = sorted({0., 1.} | set(points) | {(x-s) % 1. for x in points})
    result = 0.
    for lo, hi in zip(cuts[:-1], cuts[1:]):
        mid = (lo+hi)/2.
        number = sum(((p-mid) % 1.) <= s for p in points)
        result += (hi-lo)*(number-n*s)**2
    return result


def pair_representation(points, s):
    n = len(points)
    return (n*s*(1-s) +
            2*sum(circular_overlap(s, points[i]-points[j])
                  for i in range(n) for j in range(i)))


def verify():
    rng = Random(20261008)
    checks = 0
    for n in range(1, 11):
        for _ in range(45):
            pts = [rng.random() for __ in range(n)]
            s = rng.random()
            assert abs(count_variance(pts,s)-pair_representation(pts,s)) < 2.e-10
            checks += 1
    for _ in range(120):
        s, t = rng.random(), rng.random()
        assert abs(covariance_kernel(s,t)-spectral_covariance(s,t)) < 1.e-9
        checks += 1
    for _ in range(100):
        r, t = sorted([rng.random()*3, rng.random()*3])
        delta = 0.01
        predicted = 2./3*r*r*(3*t-r)-2*delta*r*r*t*t
        actual = covariance_kernel(delta*r, delta*t)/delta**3
        assert abs(predicted-actual)<1.e-9
        checks += 1
    for _ in range(100):
        r, t = sorted([rng.random()*3,rng.random()*3])
        increment = (2./3*t*t*(3*t-t)+2./3*r*r*(3*r-r)
                     - 2*(2./3*r*r*(3*t-r)))
        expected = 4*r*(t-r)**2+(4./3.)*(t-r)**3
        assert abs(increment-expected)<5.e-13
        checks += 1
    return checks


if __name__ == '__main__':
    print(f'PASS: {verify()} finite identities and consistency checks')
