"""Finite numerical checks of the radial Gaussian window-design asymptotics.

This checks identities and finite samples only; the continuum/global theorem
requires the analytical proof in RESULT.md.
"""
import math


def q(a, d):
    return math.cos(d) ** 2 / a + a * math.sin(d) ** 2


def circle_min(t, a, angles, samples=12000):
    m = len(angles)
    best = float('inf')
    for k in range(samples):
        phi = math.pi * k / samples
        val = sum(math.exp(-t * q(a, phi - z)) for z in angles) / m
        best = min(best, val)
    return best


def check():
    checked = 0
    for m in (3, 4, 5, 8):
        d = math.pi / (2 * m)
        a = 1 / math.tan(d)
        s = math.sin(math.pi / m)
        assert abs(q(a, d) - s) < 1.e-13
        checked += 1
        angles = [j * math.pi / m for j in range(m)]
        for t in (12., 24., 48.):
            val = circle_min(t, a, angles)
            asym = (2 / m) * math.exp(-t * s)
            # Finite t can have exponentially small positive corrections.
            assert 0.999 < val / asym < 1.02, (m, t, val / asym)
            checked += 1
    # Two windows: unsqueezed equal weights are globally best, for all radii.
    for t in (1., 10., 30.):
        val = circle_min(t, 1., [0., .37])
        assert abs(val / math.exp(-t) - 1) < 1.e-10
        checked += 1
    # Perturbation profile with (three distinct) angular offsets and squeeze.
    m = 3
    u = [0., .5, -.3]
    v = .7
    d = math.pi / 6
    h = math.sin(d) ** 3 / math.cos(d)
    increments = [u[(j + 1) % 3] - u[j] for j in range(3)]
    prediction = math.exp(-h*v*v - .5*max(increments))
    for t, tol in ((40., .06), (120., .04), (300., .03)):
        ang = [j*math.pi/3 + u[j]/t for j in range(3)]
        value = circle_min(t, math.sqrt(3) + v/math.sqrt(t), ang)
        ratio = (3/2) * value * math.exp(t*math.sqrt(3)/2)
        assert abs(ratio - prediction) < tol, (t, ratio, prediction)
        checked += 1
    # Strict convexity of squeeze penalty and strictly positive angular slope.
    for m in range(3, 19):
        d = math.pi / (2*m)
        a = 1/math.tan(d)
        slope = (a-1/a)*math.sin(2*d)
        penalty = math.cos(d)**2/a**3
        assert abs(slope-2*math.cos(math.pi/m)) < 1.e-12
        assert abs(penalty-math.sin(d)**3/math.cos(d)) < 1.e-12
        assert slope>0 and penalty>0
        checked += 4
    print(f'PASS: {checked} finite analytic-identity and numerical assertions.')
    print('Finite sampling is not proof of global optimality or the limiting law.')

if __name__ == '__main__':
    check()
