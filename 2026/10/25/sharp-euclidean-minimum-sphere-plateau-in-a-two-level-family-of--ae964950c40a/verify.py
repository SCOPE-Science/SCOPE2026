"""Independent finite checks of an enclosing-ball theorem for two-level marked poset polytopes.

Run: python3 verify.py
Requires Python's standard library plus NumPy/SciPy for the independent
small-dimensional vertex enumeration and convex epigraph optimization.
Finite checks supplement rather than replace the proof for all parameters.
"""
from fractions import Fraction as Q
from itertools import product, combinations
import numpy as np
from scipy.optimize import minimize


def candidate_vertices(p, q, t):
    zero = (Q(0),)
    one = (Q(1),)
    va = [tuple(Q(0) for _ in range(p)) + tuple(map(Q, e))
          for e in product((0, 1), repeat=q)]
    vb = [tuple(map(Q, e)) + (1-t,)*q
          for e in product((0, 1), repeat=p) if any(e)]
    return va, vb


def center_and_radius(p, q, t):
    u = t * (1-t)
    excess = max(Q(0), Q(p)-q*u)
    alpha = excess / (2*p)
    c = (alpha,)*p + (Q(1,2),)*q
    r2 = Q(q,4) + excess**2 / (4*p)
    return alpha, c, r2


def brute_vertices(p, q, t):
    d = p+q
    A, b = [], []
    for i in range(p):
        v = np.zeros(d); v[i] = -1.; A.append(v); b.append(0.)
        for j in range(q):
            v = np.zeros(d); v[i] = 1-float(t); v[p+j] = -1.
            A.append(v); b.append(0.)
            v = np.zeros(d); v[i] = float(t); v[p+j] = 1.
            A.append(v); b.append(1.)
    A, b = np.array(A), np.array(b)
    verts = {}
    for s in combinations(range(len(b)), d):
        mat = A[list(s)]
        if np.linalg.matrix_rank(mat, tol=1e-9) < d:
            continue
        x = np.linalg.solve(mat, b[list(s)])
        if max(A@x-b) > 1e-8:
            continue
        verts[tuple(np.rint(x*1e8).astype(int))] = x
    return list(verts.values())


counts = {'exact_profiles':0, 'vertices_checked':0, 'brute_profiles':0,
          'optimizer_profiles':0}
for p in (2, 3, 4):
    for q in (2, 3, 4, 5, 6, 8, 12):
        for t in (Q(0), Q(1,5), Q(2,5), Q(1,2), Q(4,5), Q(1)):
            va, vb = candidate_vertices(p,q,t)
            alpha, c, r2 = center_and_radius(p,q,t)
            av = [sum((z-c_i)**2 for z,c_i in zip(v,c)) for v in va]
            bv = [sum((z-c_i)**2 for z,c_i in zip(v,c)) for v in vb]
            assert all(z == r2 for z in av)
            assert all(z <= r2 for z in bv)
            assert max(av+bv) == r2
            u = t*(1-t)
            if u == 0:
                expected = 2**q+2**p-1
            elif q*u <= p:
                expected = 2**q+1
            else:
                expected = 2**q
            assert sum(z == r2 for z in av+bv) == expected
            # Contact mean certificate: mix all first-group corners with one full-cube vertex.
            weight = alpha  # positive only in the nonsaturated phase
            theta = (Q(1,2)-weight*(1-t))/(1-weight)
            assert Q(0) <= theta <= Q(1)
            assert weight*Q(1)+(1-weight)*Q(0) == alpha
            assert (1-weight)*theta+weight*(1-t) == Q(1,2)
            if weight > 0:
                assert bv[-1] == r2
            counts['exact_profiles'] += 1
            counts['vertices_checked'] += len(va)+len(vb)

for p,q in ((1,1),(1,2),(2,1),(2,2),(2,3),(3,2)):
    for t in (Q(0), Q(1,5), Q(1,2), Q(1)):
        va, vb = candidate_vertices(p,q,t)
        expected = np.array([list(map(float,v)) for v in va+vb])
        actual = np.array(brute_vertices(p,q,t))
        assert len(actual) == len(expected), (p,q,t,len(actual),len(expected))
        assert all(np.min(np.linalg.norm(actual-v,axis=1)) < 1e-7 for v in expected)
        counts['brute_profiles'] += 1

for p,q,t in ((2,3,Q(1,5)),(2,2,Q(1,2)),(2,9,Q(1,2)),(1,5,Q(1,2)),(2,10,Q(2,5))):
    va, vb = candidate_vertices(p,q,t)
    vertices = np.array([list(map(float,v)) for v in va+vb])
    alpha,c,r2 = center_and_radius(p,q,t)
    c = np.array(list(map(float,c)))
    r2 = float(r2)
    constraints = [dict(type='ineq',fun=lambda z,v=v:z[-1]-np.dot(z[:-1]-v,z[:-1]-v))
                   for v in vertices]
    solution = minimize(lambda z:z[-1], list(c)+[r2+.25],
                        method='SLSQP', constraints=constraints,
                        options={'maxiter':400,'ftol':2e-11})
    assert solution.success, (p,q,t,solution.message)
    assert abs(solution.fun-r2)<1e-7, (p,q,t,solution.fun,r2)
    assert np.linalg.norm(solution.x[:-1]-c)<3e-5
    counts['optimizer_profiles'] += 1

print('CHECK_OK', counts)
