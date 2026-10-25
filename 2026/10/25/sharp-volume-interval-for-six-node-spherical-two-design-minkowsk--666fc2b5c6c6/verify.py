#!/usr/bin/env python3
"""Independent finite-dimensional checks for six-normal isotropic polyhedra.

Requires numpy, scipy and sympy. Numerical sampling corroborates, but does not
replace, the analytic all-parameter proof in RESULT.md.
"""
import math
import numpy as np
import sympy as sp
from scipy.spatial import ConvexHull, HalfspaceIntersection

H = math.sqrt(2.0 / 3.0)

def nodes(phi):
    out = []
    for j in range(3):
        a = 2 * math.pi * j / 3
        out.append([H * math.cos(a), H * math.sin(a), 1 / math.sqrt(3)])
    for j in range(3):
        a = phi + 2 * math.pi * j / 3
        out.append([H * math.cos(a), H * math.sin(a), -1 / math.sqrt(3)])
    return np.array(out)

def exact_formulas(phi):
    t = 2 * math.cos(math.pi / 3 - phi)
    unit_facet_area = 18 * t / (1 + t) ** 2
    unit_volume = 36 * t / (1 + t) ** 2
    scale = math.sqrt(math.pi * (t + 1) ** 2 / (27 * t))
    minkowski_volume = (4 * math.pi ** 1.5 / (9 * math.sqrt(3))) * (t + 1) / math.sqrt(t)
    return t, unit_facet_area, unit_volume, scale, minkowski_volume

def independent_volume(phi):
    ns = nodes(phi)
    hs = np.column_stack([ns, -np.ones(6)])
    vertices = HalfspaceIntersection(hs, np.zeros(3)).intersections
    polytope = ConvexHull(vertices)
    return len(vertices), polytope.area, polytope.volume

def run():
    p = sp.symbols('p', positive=True)
    tt = sp.symbols('t', positive=True)
    r = 4 / (sp.sqrt(sp.Rational(2, 3)) * (tt + 1))
    facet = sp.factor(3 * r ** 2 * tt / 4)
    assert sp.simplify(facet - 18 * tt / (tt + 1) ** 2) == 0
    scale_sq = sp.pi * (tt + 1) ** 2 / (27 * tt)
    fixed_vol = sp.simplify((scale_sq ** sp.Rational(3, 2)) * 36 * tt / (tt + 1) ** 2)
    formula = 4 * sp.pi ** sp.Rational(3, 2) * (tt + 1) / (9 * sp.sqrt(3) * sp.sqrt(tt))
    assert sp.simplify(fixed_vol - formula) == 0
    assert sp.simplify(sp.diff((tt + 1) / sp.sqrt(tt), tt) - (tt - 1) / (2 * tt ** sp.Rational(3, 2))) == 0
    assert sp.simplify(formula.subs(tt, 1) - 8 * sp.pi ** sp.Rational(3, 2) / (9 * sp.sqrt(3))) == 0
    assert sp.simplify(formula.subs(tt, 2) - (2 * sp.pi / 3) ** sp.Rational(3, 2)) == 0

    angles = [0.0, 1e-5, math.pi / 12, math.pi / 6, 0.7, math.pi / 3]
    for phi in angles:
        ns = nodes(phi)
        assert np.max(np.abs(np.sum(ns, axis=0))) < 1e-11
        assert np.max(np.abs(ns.T @ ns - 2 * np.eye(3))) < 1e-11
        t, A, V, lam, VP = exact_formulas(phi)
        nv, area, vol = independent_volume(phi)
        assert nv == (5 if phi == 0 else 8), (phi, nv)
        assert abs(area - 6 * A) < 1e-8, (phi, area, 6 * A)
        assert abs(vol - V) < 1e-8, (phi, vol, V)
        assert abs(vol * lam ** 3 - VP) < 1e-8
        assert abs((6 * A) * lam ** 2 - 4 * math.pi) < 1e-8
    print('PASS: symbolic identities, endpoint bounds, design moments and 6 convex-hull checks')

if __name__ == '__main__':
    run()
