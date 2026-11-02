"""Exact and independent numerical checks for the flat-Klein three-point theorem.
Run: python checks/verify.py (requires sympy and numpy).
All universal statements rely on the written analytic proof, not sampled tests.
"""
from fractions import Fraction as F
import math
import numpy as np
import sympy as sp


def check_symbolic():
    w, y = sp.symbols('w y', real=True)
    integrand0 = (y**2 - (y+w)**2)**2
    integrand1 = (y**2 - (y+w-1)**2)**2
    overlap = sp.integrate(integrand0, (y,-sp.Rational(1,2),sp.Rational(1,2)-w)) + sp.integrate(integrand1,(y,sp.Rational(1,2)-w,sp.Rational(1,2)))
    assert sp.simplify(overlap-w**2*(1-w)**2/3)==0
    q=w**2*(1-w)**2
    mean=sp.integrate(q,(w,0,1)); mean2=sp.integrate(q*q,(w,0,1))
    assert mean==sp.Rational(1,30)
    assert mean2==sp.Rational(1,630)
    assert sp.simplify(mean2-mean**2)==sp.Rational(1,2100)
    a,b=sp.symbols('a b',positive=True)
    assert sp.simplify((b**4/(12*a*a))**2*(mean2-mean**2)-b**8/(302400*a**4))==0
    print('EXACT_SECTION_CORRELATION_AND_BETA_MOMENTS_PASSED')


def conditional_direct(a,b,v,nx=450,ny=450):
    xx=((np.arange(nx)+.5)/nx*a)[:,None]
    yy=((np.arange(ny)+.5)/ny*b)[None,:]
    d0=np.mod(yy-v,b);d0=np.minimum(d0,b-d0)
    d1=np.mod(yy+v,b);d1=np.minimum(d1,b-d1)
    return float(np.minimum(xx*xx+d0*d0,(a-xx)**2+d1*d1).mean())


def conditional_formula(a,b,v):
    h=(2*v/b)%1.
    return (a*a+b*b)/12 - b**4/(12*a*a)*(h*(1-h))**2


def check_independent_grid():
    for a,b in [(1.,1.),(.5,1.),(1.7,1.),(2.4,.8)]:
        for v in [0.,b/12,b/8,b/4,b/3,b/2,3*b/4]:
            direct=conditional_direct(a,b,v)
            formula=conditional_formula(a,b,v)
            assert abs(direct-formula)<1.3e-5,(a,b,v,direct,formula)
    print('INDEPENDENT_DECK_MINIMUM_GRID_PASSED 28')


def check_three_point_covariance():
    a,b=1.,1.
    # Independent pairwise quotient-distance quadratures are assembled over
    # anchor positions, not obtained from the polynomial correlation formula.
    anchors=(np.arange(192)+.5)*b/192
    values=np.array([conditional_direct(a,b,v,nx=200,ny=200) for v in anchors])
    average=float(values.mean())
    observed=float(np.mean((values-average)**2))
    expected=b**8/(302400*a**4)
    assert abs(average-((a*a+b*b)/12-b**4/(360*a*a)))<5e-6,(average,expected)
    assert abs(observed-expected)<1.5e-7,(observed,expected)
    print('INDEPENDENT_SHARED_ANCHOR_COVARIANCE_GRID_PASSED 192')


def check_shared_edge_count_and_statistic():
    n = sp.symbols('n', integer=True, positive=True)
    m = n*(n-1)/2
    shared = 3*n*(n-1)*(n-2)/6  # unordered edge pairs sharing one vertex
    assert sp.simplify(2*shared/(m*m)-4*(n-2)/(n*(n-1)))==0
    rr = sp.symbols('rr',positive=True)
    k = rr**(-6)/sp.Integer(302400)
    assert sp.simplify((302400*k)**(-sp.Rational(1,6))-rr)==0
    print('EXACT_SHARED_EDGE_COUNT_AND_ASPECT_RECONSTRUCTION_PASSED')


def check_scaling_and_extrema():
    for a,b in [(1.,1.),(.5,1.),(3.,2.),(4.,1.)]:
        v_max=conditional_formula(a,b,0)
        v_min=conditional_formula(a,b,b/4)
        assert abs(v_max-v_min-b**4/(192*a*a))<1e-11
        norm=b**8/(302400*a**4)/(a*b)**2
        assert abs(norm-(b/a)**6/302400)<1e-13
    assert F(64,302400)==F(1,4725)
    print('EXACT_SHARP_ENDPOINTS_AND_SCALE_NORMALIZATION_PASSED')


if __name__=='__main__':
    check_symbolic()
    check_independent_grid()
    check_three_point_covariance()
    check_scaling_and_extrema()
    check_shared_edge_count_and_statistic()
    print('ALL_CHECKS_PASSED')
