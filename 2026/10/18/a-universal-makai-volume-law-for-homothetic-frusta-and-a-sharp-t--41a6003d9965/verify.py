"""Independent finite checks for the universal difference-body polar law.

Requires Python 3, NumPy, SciPy, and SymPy. Execute: python verify.py
The infinite-dimensional statement is proved in RESULT.md, not by these tests.
"""
from fractions import Fraction
from itertools import product
from math import factorial
import numpy as np
from scipy.spatial import ConvexHull, HalfspaceIntersection
import sympy as sp


def polar_volume_from_differences(vertices):
    vv = np.asarray(vertices, dtype=float)
    differences = np.array([a - b for a in vv for b in vv if np.linalg.norm(a - b) > 1e-12])
    # Q={y: differences @ y <=1}; origin is strictly feasible.
    H = np.hstack([differences, -np.ones((len(differences),1))])
    verts = HalfspaceIntersection(H, np.zeros(vv.shape[1])).intersections
    return ConvexHull(verts).volume


def check_base(base, t):
    base = np.asarray(base, dtype=float)
    d = base.shape[1] + 1
    vertices = np.vstack([
        np.column_stack([base,np.ones(len(base))]),
        np.column_stack([t*base,t*np.ones(len(base))])
    ])
    real_vol = ConvexHull(vertices).volume
    real_polar = polar_volume_from_differences(vertices)
    base_vol = ConvexHull(base).volume
    base_polar = polar_volume_from_differences(base)
    pred_vol = base_vol*(1-t**d)/d
    pred_polar = base_polar*(d+1-(d-1)*t)/(d*(1-t))
    tolerance=2e-8
    assert abs(real_vol/pred_vol-1)<tolerance,(real_vol,pred_vol)
    assert abs(real_polar/pred_polar-1)<tolerance,(real_polar,pred_polar)
    return d,t,real_vol,real_polar


def check_exact_polynomials():
    x=sp.symbols('x')
    for d in range(2,40):
        sd=sum(x**i for i in range(d))
        f=sp.expand(sd*(d+1-(d-1)*x))
        h=sum((j+1)*(d-1-j)*x**j for j in range(d-1))
        der=sum(sp.binomial(j+2,2)*x**j for j in range(d-1))
        assert sp.expand(2*d-f-(1-x)**2*h)==0
        assert sp.expand(sp.diff(f,x)-2*(1-x)*der)==0
        assert sp.expand(2*d-sp.expand(f.subs(x,1)))==0
        for numerator,denominator in ((0,1),(1,3),(3,5),(9,10)):
            q=Fraction(numerator,denominator)
            F=Fraction(d+1,1)+2*sum((q**j for j in range(1,d)),Fraction(0,1))-(d-1)*q**d
            D=(1-q)**2*sum(((j+1)*(d-1-j)*q**j for j in range(d-1)),Fraction(0,1))
            assert F+ D == 2*d
    return 38


def main():
    count=check_exact_polynomials()
    tests=[]
    bases=[
        [[0,0],[2,0],[.25,1.9]], # nonsymmetric triangle
        [[-.4,.2],[2.1,-.3],[1.8,1.8],[-.7,1.1]], # skew quadrilateral
        [[-.9,.1],[.8,-.7],[2,.2],[1.1,2.1],[-.6,1.8]], # pentagon
        [[0,0,0],[1.4,0,0],[.2,1.6,0],[.4,.3,2]], # tetrahedral base in 4D
    ]
    for b in bases:
        for t in [0.0,.2,.61,.92]:
            tests.append(check_base(b,t))
    print('VERIFY_OK symbolic_dimensions=2..39 numeric_cases=',len(tests))
    print('last_sample:',tests[-1])

if __name__=='__main__':
    main()
