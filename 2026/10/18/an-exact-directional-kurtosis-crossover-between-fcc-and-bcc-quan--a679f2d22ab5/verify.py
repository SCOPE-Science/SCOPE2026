"""Exact FCC/BCC Voronoi-cell moment verification; requires sympy, scipy, numpy.

Two separate integrations: a symmetry-chamber/simplex calculation, and a
vertex-hull/triangular-facet tetrahedral calculation with rational determinants.
"""
import itertools
import math
import sympy as S
import numpy as np
from scipy.spatial import ConvexHull

x, y, z = S.symbols('x y z')
t, u, v = S.symbols('t u v')
R2 = x*x + y*y + z*z
Q4 = x**4 + y**4 + z**4
Q22 = x*x*y*y + x*x*z*z + y*y*z*z


def integrate_simplex(poly, variables, scale=S.Integer(1)):
    result = S.Rational(0)
    for powers, coeff in S.Poly(S.expand(poly), *variables).terms():
        degree = sum(powers)
        result += coeff * S.prod(S.factorial(a) for a in powers) * scale**(degree + 3) / S.factorial(degree + 3)
    return S.factor(result)


def chamber(which, poly):
    if which == 'FCC':
        a = t + (u+v)/2
        b = (u+v)/2
        c = v/2
        return 12 * integrate_simplex(poly.subs({x:a, y:b, z:c}, simultaneous=True), (t,u,v))
    assert which == 'BCC'
    base = integrate_simplex(poly, (x,y,z), S.Rational(3,2))
    exc = integrate_simplex(poly.subs(x,x+1), (x,y,z), S.Rational(1,2))
    return 8 * (base - 3*exc)


def exact_vertices(which):
    if which == 'FCC':
        verts = list(itertools.product((-S.Rational(1,2),S.Rational(1,2)), repeat=3))
        for i in range(3):
            for sign in (-1,1):
                w = [S.Integer(0)]*3
                w[i] = S.Integer(sign)
                verts.append(tuple(w))
        return verts
    vertices = set()
    for p in set(itertools.permutations((S.Integer(1), S.Rational(1,2), S.Integer(0)))):
        for signs in itertools.product((-1,1), repeat=3):
            vertices.add(tuple(val*sign for val, sign in zip(p,signs)))
    return sorted(vertices)


def hull_integrals(which):
    vertices = exact_vertices(which)
    hull = ConvexHull(np.asarray(vertices,dtype=float))
    sums = [S.Rational(0)]*6
    for i,j,k in hull.simplices:
        mat = S.Matrix([vertices[int(i)],vertices[int(j)],vertices[int(k)]]).T
        det = abs(mat.det())
        assert det != 0
        a,b,c = mat*S.Matrix([t,u,v])
        r = a*a+b*b+c*c
        for index,poly in enumerate((S.Integer(1),r,r**2,r**3,a**4+b**4+c**4,a*a*b*b+a*a*c*c+b*b*c*c)):
            sums[index] += det * integrate_simplex(poly,(t,u,v))
    return tuple(S.factor(a) for a in sums), (len(vertices), len(hull.simplices))

expected = {
 'FCC': (S.Integer(2), S.Rational(3,8), S.Rational(41,240), S.Rational(1397,16128),S.Rational(3,80),S.Rational(7,720)),
 'BCC': (S.Integer(4), S.Rational(19,32), S.Rational(409,960), S.Rational(27217,80640),S.Rational(89,960),S.Rational(71,2880)),
}

for name in ('FCC','BCC'):
    volume, m2, m4, m6, a, c = expected[name]
    polynomials = (S.Integer(1),R2,R2**2,R2**3,Q4,Q22)
    expected_integrals = (volume, m2*volume, m4*volume,m6*volume,3*a*volume,3*c*volume)
    chamber_values = tuple(S.factor(chamber(name, p)) for p in polynomials)
    tetra_values, face_counts = hull_integrals(name)
    assert chamber_values == expected_integrals, (name,'chamber',chamber_values)
    assert tetra_values == expected_integrals, (name,'triangulation',tetra_values)
    print(f'{name}: vertices={face_counts[0]}, triangular facets={face_counts[1]}, volume={volume}, M2={m2}, M4={m4}, M6={m6}, A={a}, C={c}')

F2,F4,F6,FA,FC = expected['FCC'][1:]
B2,B4,B6,BA,BC = expected['BCC'][1:]
assert S.factor(F4/F2**2-B4/B2**2)==S.Rational(308,48735)
assert S.factor(F6/F2**3-B6/B2**3)==S.Rational(1758278,58335795)
w = S.symbols('w')
K_F=S.factor((3*FC+(FA-3*FC)*w)/(F2/3)**2)
K_B=S.factor((3*BC+(BA-3*BC)*w)/(B2/3)**2)
assert S.simplify(K_F-K_B-S.Rational(4,5415)*(74*w-29))==0
assert K_F.subs(w,S.Rational(1,3)) < K_B.subs(w,S.Rational(1,3))
assert K_F.subs(w,1)>K_B.subs(w,1)
print('FCC_BCC_DIRECTIONAL_KURTOSIS_CROSSOVER_OK threshold=29/74')
print('RADIAL_FOURTH_AND_SIXTH_COMPARISONS_OK')
