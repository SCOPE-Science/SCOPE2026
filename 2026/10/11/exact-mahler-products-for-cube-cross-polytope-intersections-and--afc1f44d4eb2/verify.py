"""Finite supplementary checks for exact cube--cross-polytope Mahler formulas.
The symbolic argument in RESULT.md, rather than these finite tests, proves the theorem.
Run: python3 verify.py (requires Python, SymPy, NumPy and SciPy).
"""
from fractions import Fraction
from itertools import combinations, permutations, product
from math import comb, factorial, isclose
import sympy as sp
import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import linprog


def primal_volume(d,t):
    t=Fraction(t)
    k=t.numerator//t.denominator
    s=sum((-1)**j*comb(d,j)*(t-j)**d for j in range(min(k,d)+1))
    return Fraction(2**d,factorial(d))*s


def polar_volume(d,t):
    t=Fraction(t)
    k=t.numerator//t.denominator
    return Fraction(2**d,factorial(k))*t**(-(d-k))


def vertices_primal(d,t):
    t=float(t);k=int(t)
    a=[1.0]*min(k,d)
    if k<d:a += [t-k]
    a += [0.0]*(d-len(a))
    arr=set(permutations(a))
    pts=set()
    for p in arr:
        for signs in product([-1,1],repeat=d):
            pts.add(tuple(signs[i]*p[i] for i in range(d)))
    return np.array(sorted(pts))


def vertices_polar(d,t):
    t=float(t)
    v=[]
    for i in range(d):
        e=np.eye(d)[i]
        v.extend([e,-e])
    v.extend([np.array(signs,dtype=float)/t for signs in product([-1,1],repeat=d)])
    return np.unique(np.array(v),axis=0)


def main():
    checks=0
    # Exact reciprocal-polynomial expressions for every rational sample.
    for d in range(2,7):
        for q in range(1,5):
            for p in range(q, d*q+1):
                t=Fraction(p,q)
                v=primal_volume(d,t); w=polar_volume(d,t)
                assert v>0 and w>0
                assert v*w>=Fraction(4**d,factorial(d)), (d,t,v,w)
                assert v<=2**d and Fraction(2**d,factorial(d))<=w<=2**d
                checks+=4
    # Independent half-space/vertex convex hulls for small dimensions.
    for d in range(2,6):
        for i in range(7):
            t=1+(d-1)*(i+1)/9
            points=vertices_primal(d,t)
            pol=vertices_polar(d,t)
            vu=ConvexHull(points).volume
            wu=ConvexHull(pol).volume
            assert isclose(vu,float(primal_volume(d,Fraction(t).limit_denominator(100000))),rel_tol=2e-8,abs_tol=2e-8),(d,t,vu)
            assert isclose(wu,float(polar_volume(d,Fraction(t).limit_denominator(100000))),rel_tol=2e-8,abs_tol=2e-8),(d,t,wu)
            checks+=2
    # Independently solve support maximization linear programs in sample directions.
    rng=np.random.default_rng(2004)
    for d in range(2,6):
        signs=np.array(list(product([-1.,1.],repeat=d)))
        for r in range(12):
            t=1+(d-1)*(r+0.5)/13
            y=rng.normal(size=d)
            sol=linprog(-y,A_ub=signs,b_ub=np.repeat(t,len(signs)),bounds=[(-1,1)]*d,method="highs")
            assert sol.success
            yy=sorted(np.abs(y),reverse=True)
            k=int(t)
            expected=sum(yy[:k])+(t-k)*yy[k]
            assert isclose(-sol.fun,expected,rel_tol=1e-9,abs_tol=1e-9)
            checks+=1
    x=sp.symbols('x',positive=True)
    P1=sp.Rational(32,3)*(x-3*(x-1)**3/x**2)
    P2=sp.Rational(16,3)/x*(6-(3-x)**3)
    assert sp.simplify(P1.subs(x,2)-P2.subs(x,2))==0
    assert sp.diff(P1,x).subs(x,2)==sp.Rational(-16,3)
    assert sp.diff(P2,x).subs(x,2)==sp.Rational(4,3)
    assert sp.simplify(sp.diff(P1,x,2)+192*(x-1)/x**4)==0
    roots_a=[float(sp.re(r)) for r in sp.nroots(2*x**3-9*x+6) if abs(float(sp.im(r)))<1e-8 and 1<float(sp.re(r))<2]
    roots_b=[float(sp.re(r)) for r in sp.nroots(2*x**3-9*x**2+21) if abs(float(sp.im(r)))<1e-8 and 2<float(sp.re(r))<3]
    assert len(roots_a)==len(roots_b)==1
    assert abs(float(P1.subs(x,roots_a[0]))-14.3750855157127)<1e-10
    assert abs(float(P2.subs(x,roots_b[0]))-13.38817407278678)<1e-10
    assert P1.subs(x,sp.Rational(3,2))==sp.Rational(128,9)
    checks+=10
    print('VERIFY_OK',checks,'local_peaks',roots_a[0],roots_b[0])


if __name__=='__main__':
    main()
