"""Finite checks for cap-conditioned spherical right-angle graph expansions.

This is a Monte Carlo consistency check, not a proof of an asymptotic theorem.
The radial beta law and the sequential tangent-Gram sampling formula are exact.
"""

from itertools import combinations, product
from math import exp, pi, sqrt

import numpy as np
from scipy.special import betaincc, betainccinv, ndtr


def phi(x):
    return exp(-0.5*x*x)/sqrt(2*pi)


def motif_terms(k, signs, p):
    edges = list(combinations(range(k), 2))
    statuses = dict(zip(edges, signs))
    q = {e: (p if statuses[e] == 1 else 1-p) for e in edges}
    base = np.prod(list(q.values()))
    lin = sum(statuses[e]*np.prod([q[f] for f in edges if f != e]) for e in edges)
    tri = 0.0
    for i, j, l in combinations(range(k), 3):
        tri_edges = {(i,j), (i,l), (j,l)}
        tri += (statuses[i,j]*statuses[i,l]*statuses[j,l]
                *np.prod([q[f] for f in edges if f not in tri_edges]))
    return float(base), float(lin), float(tri)


def predicted(k, signs, d, *, lam=None, a=None):
    assert (lam is None) != (a is None)
    if lam is not None:
        assert lam > 0
        p, v, b = ndtr(lam*lam), phi(lam*lam), 2+lam**4
    else:
        assert a >= 0
        p, v, b = 0.5, phi(0), (phi(a)/(1-ndtr(a)))**2
    base, lin, tri = motif_terms(k, signs, p)
    return base + (b*v*lin + v**3*tri)/sqrt(d)


def spherical_coordinate(D, n, gen):
    t = gen.standard_normal(n)
    return t / np.sqrt(t*t + gen.chisquare(D-1, size=n))


def cap_radial(d, h, n, gen):
    # If S is the positive first coordinate, then S^2 is a beta variate
    # conditioned to exceed h^2.  Survival inversion avoids rare rejection.
    tail = betaincc(0.5, (d-1)/2, h*h)
    if not 0 < tail <= 1:
        raise ValueError('Cap too small for stable numerical inverse sampling')
    return np.sqrt(betainccinv(0.5, (d-1)/2,
                              gen.uniform(0, tail, size=n)))


def triangle_sample(d, h, n, gen):
    s = [cap_radial(d, h, n, gen) for _ in range(3)]
    # Choose U1 at the first tangent coordinate; the relative Gram entries
    # have this exact independent-coordinate construction.
    x = spherical_coordinate(d-1, n, gen)
    y = spherical_coordinate(d-1, n, gen)
    z = x*y + np.sqrt((1-x*x)*(1-y*y))*spherical_coordinate(d-2, n, gen)
    g = (x, y, z)
    out = []
    for (i,j), v in zip(((0,1),(0,2),(1,2)), g):
        dot = s[i]*s[j] + np.sqrt((1-s[i]**2)*(1-s[j]**2))*v
        out.append(dot >= 0)
    return np.stack(out, axis=1)


def check():
    # All labelled patterns in a four-point graph have total probability one
    # separately at leading and first orders.
    for k in (3,4):
        for lam, a in ((0.8, None), (None, 0.0), (None, 1.5)):
            m = k*(k-1)//2
            if lam is not None:
                p,v,b = ndtr(lam*lam), phi(lam*lam), 2+lam**4
            else:
                p,v,b = .5, phi(0), (phi(a)/(1-ndtr(a)))**2
            bases, corrections = [], []
            for signs in product((-1,1), repeat=m):
                base, lin, tri = motif_terms(k, signs, p)
                bases.append(base)
                corrections.append(b*v*lin + v**3*tri)
            assert abs(sum(bases)-1) < 1e-12
            assert abs(sum(corrections)) < 1e-12

    gen = np.random.default_rng(624973)
    report = []
    for d in (500, 3000):
        for lam, a in ((0.7,None), (1.0,None), (None,0.0), (None,2.0)):
            h = lam*d**(-.25) if lam is not None else a/sqrt(d)
            draws = triangle_sample(d, h, 280000, gen)
            for signs in ((1,1,1),(1,1,-1),(1,-1,-1),(-1,-1,-1)):
                target = np.array([v==1 for v in signs])
                actual = float(np.mean(np.all(draws==target, axis=1)))
                estimate = predicted(3, signs, d, lam=lam, a=a)
                # A coarse, independent finite-sample corroboration tolerance;
                # omitted second-order terms can be visible at these dimensions.
                tol = 0.026 if d == 500 else 0.007
                assert abs(actual-estimate) <= tol, (d,lam,a,signs,actual,estimate)
                report.append(abs(actual-estimate))
    print('CAP_GRAPH_PATTERN_EXPANSION_CHECKS_OK',
          len(report), round(max(report),6))


if __name__ == '__main__':
    check()
