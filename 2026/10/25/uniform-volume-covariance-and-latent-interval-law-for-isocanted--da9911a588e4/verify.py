"""Reproducible independent checks for the uniform isocanted-cube law.

Python 3 standard library only. The deterministic polygon computation uses
convex-hull vertices and exact rational simplex integrals. The sampler
rejects against the original inequalities, not the polytope tiling.
"""
from fractions import Fraction as Q
from itertools import product
from math import atan2, factorial, sqrt, log
from random import Random


def theoretical(d, ell, a):
    delta = ell - a
    lp = (ell * ell + (d - 1) * a * a) / 12
    lt = delta * delta * (delta + (d + 2) * a) / (12 * (delta + d * a))
    return lp, lt


def polygon_exact(ell, a):
    delta = ell - a
    points = set()
    for e1, e2, e3 in product((-1, 1), repeat=3):
        points.add(((Q(e1) * delta + e3 * a) / 2,
                    (Q(e2) * delta + e3 * a) / 2))
    def cross(o, p, q):
        return (p[0] - o[0]) * (q[1] - o[1]) - (p[1] - o[1]) * (q[0] - o[0])
    pts = sorted(points)
    low = []
    for p in pts:
        while len(low) >= 2 and cross(low[-2], low[-1], p) <= 0:
            low.pop()
        low.append(p)
    up = []
    for p in reversed(pts):
        while len(up) >= 2 and cross(up[-2], up[-1], p) <= 0:
            up.pop()
        up.append(p)
    vertices = low[:-1] + up[:-1]
    # Exact raw second-moment integrals using triangles with apex origin.
    volume = Q(0)
    moment = [[Q(0), Q(0)], [Q(0), Q(0)]]
    for p, q in zip(vertices, vertices[1:] + vertices[:1]):
        area = (p[0] * q[1] - p[1] * q[0]) / 2
        assert area > 0
        volume += area
        for i in range(2):
            for j in range(2):
                avg = (2 * p[i] * p[j] + 2 * q[i] * q[j]
                       + p[i] * q[j] + q[i] * p[j]) / 12
                moment[i][j] += area * avg
    return len(vertices), volume, [[z / volume for z in row] for row in moment]


def rejection_covariance(d, ell, a, seed=99117, accepted=30000):
    rng = Random(seed + d)
    delta = ell - a
    target = accepted
    sums = [0.] * d
    secs = [[0.] * d for _ in range(d)]
    tries = 0
    while tries < 3500000 and accepted > 0:
        tries += 1
        x = [rng.uniform(-ell / 2, ell / 2) for _ in range(d)]
        if max(x) - min(x) > delta:
            continue
        accepted -= 1
        for i in range(d):
            sums[i] += x[i]
            for j in range(d):
                secs[i][j] += x[i] * x[j]
    assert accepted == 0, 'not enough accepted samples'
    n = target
    means = [z / n for z in sums]
    return tries, [[secs[i][j] / n - means[i] * means[j] for j in range(d)] for i in range(d)]


def main():
    count = 0
    for d in range(2, 21):
        for a in (Q(1, 10), Q(1, 3), Q(2, 3), Q(9, 10)):
            ell = Q(1)
            delta = ell - a
            # Independently recover from the disjoint tile mass and moments.
            vol = delta ** d + d * a * delta ** (d - 1)
            assert vol == delta ** (d - 1) * (delta + d * a)
            p0 = delta / (delta + d * a)
            pw = a / (delta + d * a)
            vdiag = (p0 * (delta ** 2 / 12 + a ** 2 / 4)
                     + pw * (delta ** 2 / 4 + a ** 2 / 12)
                     + (d - 1) * pw * (delta ** 2 / 12 + a ** 2 / 12))
            voff = p0 * a ** 2 / 4 + d * pw * a ** 2 / 12
            eig_p, eig_t = theoretical(d, ell, a)
            assert vdiag - voff == eig_t
            assert vdiag + (d - 1) * voff == eig_p
            ratio = (1 + 2 * a / (delta + d * a)) ** (d - 1)
            ratio *= (ell * ell + (d - 1) * a * a) / ((delta + d * a) ** 2)
            determinant = eig_p * eig_t ** (d - 1)
            assert abs(float(ratio - (Q(12) ** d) * determinant / vol ** 2)) < 1e-9
            count += 1
    for a in (Q(1, 10), Q(1, 3), Q(2, 3), Q(9, 10)):
        nverts, volume, M = polygon_exact(Q(1), a)
        ep, et = theoretical(2, Q(1), a)
        d = (ep + et) / 2
        off = (ep - et) / 2
        assert nverts == 6
        assert volume == (1-a) * (1+a)
        assert M == [[d, off], [off, d]]
    for d in (2, 3, 4):
        a = .22
        ell = 1.0
        tries, M = rejection_covariance(d, ell, a)
        ep, et = theoretical(d, ell, a)
        diag = et + (ep - et) / d
        off = (ep - et) / d
        assert max(abs(M[i][i] - diag) for i in range(d)) < .006
        assert max(abs(M[i][j] - off) for i in range(d) for j in range(d) if i!=j) < .006
        print('DIRECT_REJECTION',d,tries,'diag',round(M[0][0],6),'off',round(M[0][1],6))
    for d in (1000, 10000, 100000):
        a = .22
        delta = 1-a
        lr = (d-1)*log(1+2*a/(delta+d*a))
        lr += log(1+(d-1)*a*a)-2*log(delta+d*a)
        print('ASYMPTOTIC',d,round(lr+log(d),7))
    print('VERIFY_OK exact_profiles',count+4,'rejection_dimensions',3)


if __name__ == '__main__':
    main()
