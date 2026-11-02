#!/usr/bin/env python3
"""Independent numerical checks of exact orientation-dependent box exclusion-volume identities.

Dependencies: NumPy and SciPy. Deterministic seed; the analytical proof is independent
of these numerical diagnostics.
"""
import itertools
import numpy as np
from scipy.spatial import ConvexHull
from scipy.spatial.transform import Rotation

SEED = 901847
N = 240000
rng = np.random.default_rng(SEED)


def formula(lengths, rotation):
    a = np.asarray(lengths, dtype=float)
    weights = a[None, :] / a[:, None] + a[:, None] / a[None, :]
    return float(np.prod(a) * (2.0 + np.sum(weights * np.abs(rotation))))


def independent_convex_hull(lengths, rotation):
    a = np.asarray(lengths, dtype=float)
    corners = np.asarray(list(itertools.product((-0.5, 0.5), repeat=3)), dtype=float)
    first = corners * a
    second = first @ rotation.T
    pts = (first[:, None, :] + second[None, :, :]).reshape(-1, 3)
    return ConvexHull(pts).volume


def variance_formula(lengths):
    a = np.asarray(lengths, dtype=float)
    w = a[None, :] / a[:, None] + a[:, None] / a[None, :]
    t = float(w.sum())
    b = float((w*w).sum())
    s = float((w.sum(axis=1)**2).sum())
    p = np.pi
    ce = 1.0/12.0
    cs = 2.0/(3.0*p) - 1.0/4.0
    cd = 8.0/(3.0*p*p) - 1.0/4.0
    return float(np.prod(a)**2 * (cd*t*t + (ce-2*cs+cd)*b + (2*cs-2*cd)*s))


sample_rotation = Rotation.random(N, random_state=rng).as_matrix()
absr = np.abs(sample_rotation)
p = np.pi
for name, x, y, expected in (
    ('same element', (0,0), (0,0), 1.0/3.0),
    ('same row', (0,0), (0,1), 2.0/(3.0*p)),
    ('same column', (0,0), (1,0), 2.0/(3.0*p)),
    ('disjoint', (0,0), (1,1), 8.0/(3.0*p*p)),
):
    sample = float((absr[:,x[0],x[1]]*absr[:,y[0],y[1]]).mean())
    print(name, 'observed', round(sample,7), 'proved value', round(expected,7))
    assert abs(sample-expected)<0.003, name

for a in ((1,1,1),(2,1,1),(2,3,4)):
    means = np.prod(a)*(2+(sum(a)*sum(1.0/x for x in a)))
    w = np.asarray(a)[None,:]/np.asarray(a)[:,None] + np.asarray(a)[:,None]/np.asarray(a)[None,:]
    values = np.prod(a)*(2+np.einsum('ij,kij->k',w,absr))
    sm = float(values.mean())
    sv = float(values.var())
    exactv = variance_formula(a)
    print('box',a,'sample mean',round(sm,5),'exact',round(means,5),'sample variance',round(sv,5),'exact',round(exactv,5))
    assert abs(sm-means)<.008*means
    assert abs(sv-exactv)<.035*exactv
    for R in (np.eye(3),sample_rotation[101],sample_rotation[17201]):
        actual = independent_convex_hull(a,R)
        theoretical = formula(a,R)
        print('  hull vs determinant',round(actual,10),round(theoretical,10))
        assert abs(actual-theoretical)<1.e-9*max(1,actual)

c = -69 + 96/p +384/p**2
assert abs(variance_formula((1,1,1))-c)<1.e-12
assert c>0
assert (1/12+4*(2/(3*p)-.25)+4*(8/(3*p*p)-.25))>0
assert variance_formula((2,1,1))>c*4
print('ALL_EXCLUDED_VOLUME_CHECKS_PASSED')
