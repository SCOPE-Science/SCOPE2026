"""Independent numerical consistency checks for a dodecahedral directional-width law.

Run with Python 3.9+ and no third-party packages. The proof is geometric;
quadrature and finite spherical grids are not substitutes for that proof.
"""
import math

PHI = (1.0 + math.sqrt(5.0)) / 2.0
Q = (3.0 - math.sqrt(5.0)) / 2.0
R = math.sqrt(3.0)
S_MIN = 1.0 / math.sqrt(1.0 + 4.0 * Q * Q)
S_BREAK = 1.0 / math.sqrt(1.0 + Q * Q)
W_MIN, W_BREAK, W_MAX = (2.0 * R * x for x in (S_MIN, S_BREAK, 1.0))


def vertices():
    vs = [(a, b, c) for a in (-1.0, 1.0)
          for b in (-1.0, 1.0) for c in (-1.0, 1.0)]
    for a in (-1.0, 1.0):
        for b in (-1.0, 1.0):
            vs.extend([(0.0, a / PHI, b * PHI),
                       (a / PHI, b * PHI, 0.0),
                       (a * PHI, 0.0, b / PHI)])
    return vs


def beta(s):
    z = Q * s / math.sqrt(1.0 - s * s)
    return math.acos(min(1.0, max(-1.0, z)))


def density(w):
    s = w / (2.0 * R)
    if s < S_MIN or s > 1.0:
        return 0.0
    if s >= S_BREAK:
        return 5.0 / R
    return 5.0 / R * (1.0 - 3.0 * beta(s) / math.pi)


def cdf(w):
    s = w / (2.0 * R)
    if s <= S_MIN:
        return 0.0
    if s >= 1.0:
        return 1.0
    if s >= S_BREAK:
        return 10.0 * s - 9.0
    z = math.sqrt(max(0.0, 1.0 - (1.0 + Q * Q) * s * s))
    return 10.0 * s - 9.0 + 30.0 / math.pi * (math.atan(z / Q) - s * beta(s))


def simpson(f, a, b, n=40000):
    assert n % 2 == 0
    h = (b - a) / n
    acc = f(a) + f(b)
    for i in range(1, n):
        acc += (4 if i % 2 else 2) * f(a + i * h)
    return acc * h / 3


def check():
    verts = vertices()
    assert len(verts) == 20 and len(set(verts)) == 20
    for v in verts:
        assert abs(sum(a*a for a in v) - 3.0) < 5e-15
        near = [w for w in verts if
                abs(sum((a-b)**2 for a,b in zip(v,w)) - (2/PHI)**2) < 1e-9]
        assert len(near) == 3
        for w in near:
            assert abs(sum(a*b for a,b in zip(v,w)) - math.sqrt(5)) < 1e-12

    assert abs(Q - PHI**(-2)) < 1e-15
    assert S_MIN < S_BREAK < 1.0
    assert abs(cdf(W_MIN)) < 1e-13
    assert abs(cdf(W_BREAK) - (10*S_BREAK-9)) < 1e-13
    assert abs(cdf(W_MAX) - 1) < 1e-13
    assert abs(density(W_BREAK) - 5/R) < 1e-13

    # Direct quadrature of the proposed density, not of the CDF formula.
    for j in (0, 1, 2):
        mom = (simpson(lambda w: w**j * density(w), W_MIN, W_BREAK, 48000)
               + simpson(lambda w: w**j * density(w), W_BREAK, W_MAX, 48000))
        if j == 0:
            assert abs(mom - 1.0) < 2e-7, mom
        if j == 2:
            unit_edge = mom * (PHI / 2.0)**2
            known = ((3+math.sqrt(5))/2
                     + 10/math.pi * math.sqrt(1+2/math.sqrt(5)))
            assert abs(unit_edge - known) < 2e-7, (unit_edge, known)

    # Check the analytic derivative of the explicit CDF in both regimes.
    for j in range(1, 200):
        w = W_MIN + (W_BREAK-W_MIN) * j / 200
        h = 1e-6
        assert abs((cdf(w+h)-cdf(w-h))/(2*h)-density(w)) < 8e-7
    for j in range(1, 200):
        w = W_BREAK + (W_MAX-W_BREAK) * j / 200
        h = 1e-6
        assert abs((cdf(w+h)-cdf(w-h))/(2*h)-density(w)) < 2e-9

    # Independently compute support values at a deterministic Fibonacci sphere grid.
    n = 120000
    tallies = [0] * 11
    query = [W_MIN + (W_MAX-W_MIN) * i/12 for i in range(1, 12)]
    mean = 0.0
    for i in range(n):
        z = 1.0 - 2.0 * (i + 0.5) / n
        theta = 2.0 * math.pi * i / ((1.0+math.sqrt(5.0))/2.0)
        radial = math.sqrt(1-z*z)
        u = (radial*math.cos(theta), radial*math.sin(theta), z)
        w = 2.0 * max(sum(a*b for a,b in zip(v,u)) for v in verts)
        assert W_MIN - 5e-8 <= w <= W_MAX + 5e-8
        mean += w
        for j,t in enumerate(query):
            tallies[j] += (w <= t)
    for j,t in enumerate(query):
        assert abs(tallies[j]/n - cdf(t)) < 0.0015, (j, tallies[j]/n, cdf(t))
    direct_mean = mean/n
    predicted_mean = (simpson(lambda w:w*density(w), W_MIN,W_BREAK,48000)
                      +simpson(lambda w:w*density(w),W_BREAK,W_MAX,48000))
    assert abs(direct_mean - predicted_mean) < 0.0002
    print('VERIFY_OK', 'vertices=20', 'fibonacci_directions=120000',
          'cdf_samples=11', 'normalization=1',
          'second_moment_unit_edge=%.12f' % known,
          'constant_tail_mass=%.12f' % (10*(1-S_BREAK)))

if __name__ == '__main__':
    check()
