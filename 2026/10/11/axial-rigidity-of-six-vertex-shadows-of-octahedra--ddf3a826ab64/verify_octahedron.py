"""Standalone numerical and symbolic diagnostics for affine-octahedron shadows.

Run: python verify_octahedron.py
Requirements: Python 3 with numpy, scipy, sympy. Numerical checks are
supplementary to the analytic proof in RESULT.md.
"""
import itertools
import math
import numpy as np
import sympy as sp
from scipy.spatial import ConvexHull


def omega(p, q, r):
    p, q, r = (np.asarray(z, dtype=float) for z in (p, q, r))
    V = abs(np.linalg.det(np.column_stack((p, q, r))))
    D = (np.linalg.norm(p) * np.linalg.norm(q) * np.linalg.norm(r)
         + np.dot(p, q)*np.linalg.norm(r)
         + np.dot(p, r)*np.linalg.norm(q)
         + np.dot(q, r)*np.linalg.norm(p))
    return 2*math.atan2(V, D)


def spherical_formula(A):
    A = np.asarray(A, dtype=float)
    assert A.shape == (3,3) and abs(np.linalg.det(A)) > 1.e-10
    total = 0.0
    for i in range(3):
        j, k = [x for x in range(3) if x != i]
        for s, t in itertools.product((-1, 1), repeat=2):
            total += omega(A[:, i], A[:, i]+s*A[:, j], A[:, i]+t*A[:, k])
    return total/(2*math.pi)


def axial_formula(lam):
    a = math.sqrt(2)-1
    h = math.hypot(1, lam)
    return 4/math.pi*(2*math.atan(a*lam/(1+h))
                      + math.atan((h-lam)**2))


def hull_vertices(A, normal):
    w = np.asarray(normal, dtype=float)
    w /= np.linalg.norm(w)
    p = np.array([1., 0., 0.])
    if abs(np.dot(p, w)) > 0.8:
        p = np.array([0., 1., 0.])
    p -= np.dot(p, w)*w
    p /= np.linalg.norm(p)
    q = np.cross(w, p)
    vertices = np.vstack([A.T, -A.T])
    polygon = np.column_stack([vertices @ p, vertices @ q])
    return len(ConvexHull(polygon).vertices)


def run():
    t = sp.symbols('t', positive=True)
    a = sp.sqrt(2)-1
    F = (a-1)+(6*a-a*a+1)*t*t+(a+a*a)*t**4
    assert sp.simplify(F.subs(t, a)) == 0
    assert sp.simplify(F - (2-sp.sqrt(2))*(t*t-a*a)*(t*t+3+2*sp.sqrt(2))) == 0
    print('SYMBOLIC_DERIVATIVE_FACTOR_OK')
    lambdas = [0.02,0.1,0.3,0.5,0.9,1.,1.1,2.,4.,10.,50.]
    worst = 0.0
    for lam in lambdas:
        P = spherical_formula(np.diag([1.,1.,lam]))
        Q = axial_formula(lam)
        worst = max(worst, abs(P-Q))
        assert abs(P-Q) < 1.e-12
        assert P >= axial_formula(1)-1.e-12
    print('AXIAL_SOLID_ANGLE_AGREEMENT_OK',format(worst,'.3g'))
    rng = np.random.default_rng(12657)
    max_hull_fail = 0
    N=2500
    matrices=[np.eye(3), np.diag([1.,1.,0.2]),np.diag([1.,1.,4.])]
    for _ in range(5):
        A = rng.normal(size=(3,3))
        if abs(np.linalg.det(A))>0.05:
            matrices.append(A)
    for index,A in enumerate(matrices):
        u=rng.normal(size=(N,3));u/=np.linalg.norm(u,axis=1)[:,None]
        c=np.linalg.solve(A,u.T).T
        abs_c=np.abs(c)
        dominance=np.max(abs_c,axis=1) > (np.sum(abs_c,axis=1)-np.max(abs_c,axis=1))
        mc=dominance.mean()
        exact=spherical_formula(A)
        # Standard error <= 1/(2 sqrt(N)); six-sigma conservative with fixed seed.
        assert abs(mc-exact) < 0.06,(index,mc,exact)
        # Convex hull check against a completely different projected-geometry pathway.
        for u0,pred in zip(u[:120], dominance[:120]):
            n=hull_vertices(A,u0)
            if n != (4 if pred else 6):
                max_hull_fail+=1
        print('MATRIX',index,'solid_angle',format(exact,'.12f'),
              'random_sample',format(mc,'.12f'), 'samples',N)
    assert max_hull_fail==0
    print('HULL_INDEPENDENT_CHECK_OK',len(matrices)*120)
    print('VERIFY_OK')

if __name__=='__main__':
    run()
