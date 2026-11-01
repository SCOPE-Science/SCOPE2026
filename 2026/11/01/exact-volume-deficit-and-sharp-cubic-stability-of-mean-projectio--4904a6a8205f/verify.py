#!/usr/bin/env python3
"""Independent finite checks of the orthotope mean-section-body volume identity.

All-dimensional quantifiers and mixed-volume identities are proved analytically
in RESULT.md. The tests here corroborate their constants and algebra, rather
than inferring a theorem from finite samples.
"""
from fractions import Fraction
from itertools import product
from math import cos, sin, pi, sqrt, exp, log


def ordered_pairs_sum(r):
    return sum(r[i]**2*r[j] for i in range(3) for j in range(3) if i != j)


def deficit_pairs(a, b, c):
    return (a-b)**2/(a*b) + (b-c)**2/(b*c) + (c-a)**2/(c*a)


def check_exact_identites():
    tests = 0
    for x, y, z in product((1, 2, 3, 5, 8), repeat=3):
        a, b, c = map(Fraction, (x, y, z))
        r = (b*c, a*c, a*b)
        t = (a*b*c)**2
        assert ordered_pairs_sum(r) - 6*t == t*deficit_pairs(a,b,c)
        assert deficit_pairs(a,b,c) >= 0
        assert (deficit_pairs(a,b,c) == 0) == (a==b==c)
        tests+=1
    print('exact-rational triples:', tests)


def volume_triple_constant_quadrature(m):
    # C = (1/2) int_0^{2pi} int_0^{2pi} sqrt(cos²(a) sin²(b) + sin²(a) cos²(b)) da db.
    h = 2*pi/m
    vals = [(cos((k+.5)*h)**2, sin((k+.5)*h)**2) for k in range(m)]
    total = 0.0
    for ca2, sa2 in vals:
        total += sum(sqrt(ca2*sb2 + sa2*cb2) for cb2, sb2 in vals)
    return total*h*h/2


def independently_check_convex_hull(C):
    # Samples exposed points of three planar disks; the convex hull is an
    # *inscribed approximation*. Testing this numerical convergence is not proof.
    try:
        import numpy as np
        from scipy.spatial import ConvexHull
    except ImportError:
        print('optional SciPy convex-hull cross-check unavailable')
        return
    rng = np.random.default_rng(43121)
    u = rng.normal(size=(16000,3))
    u /= np.linalg.norm(u, axis=1)[:,None]
    for radii in ((1,1,1), (.4,1.2,2.3), (.1,2,5)):
        pts = np.zeros_like(u)
        for i in range(3):
            w = u.copy();w[:,i] = 0
            pts += radii[i] * w/np.linalg.norm(w,axis=1)[:,None]
        hull_vol = ConvexHull(pts).volume
        exact_vol = 2*pi*ordered_pairs_sum(radii) + C*np.prod(radii)
        assert 0 < (exact_vol-hull_vol)/exact_vol < 0.002, (radii,hull_vol,exact_vol)
        print('sample hull:',radii,'analytic:',round(exact_vol,8),
              'inscribed:',round(hull_vol,8))


def check_sharp_log_stability():
    # The universal proof uses 2(cosh t-1) >= t².
    # This finite check verifies the claimed normalization and approach to 1.
    for t in (1e-2, 5e-2, .1, .4, 1.0, 2.0):
        a,b,c=exp(t),1.0,exp(-t)
        gap=deficit_pairs(a,b,c)
        sq=(log(a)-log(b))**2+(log(b)-log(c))**2+(log(a)-log(c))**2
        assert gap>=sq*(1-1e-12)
    t=1e-4
    a,b,c=exp(t),1.0,exp(-t)
    ratio=deficit_pairs(a,b,c)/(6*t*t)
    assert abs(ratio-1)<1e-6
    print('small-aspect log-stability ratio:',ratio)


if __name__=='__main__':
    check_exact_identites()
    C1=volume_triple_constant_quadrature(300)
    C2=volume_triple_constant_quadrature(600)
    assert abs(C1-C2)<1e-3
    assert abs(C2-13.372779524499367)<1e-3
    print('universal triple-disk coefficient C:',C2,
          '(midpoint quadrature)')
    independently_check_convex_hull(C2)
    check_sharp_log_stability()
    print('All finite checks PASS; analytic proof establishes universal assertion.')
