"""Self-contained numerical cross-checks for clique-windmill volume and hub limits.
Uses SciPy only; finite checks do not substitute for analytical proofs.
"""
import math
from fractions import Fraction
from itertools import combinations, product
from scipy.integrate import quad
from scipy.special import gamma, gammainc
from scipy.spatial import ConvexHull
import numpy as np


def c_of(r):
    return 2.0 ** (1-r)


def fiber(r, t):
    if t < 0 or t > 1:
        return 0.
    if t <= 0.5:
        return c_of(r)-t**r
    return (1-t)**r


def vol_poly_exact(r, m):
    c = Fraction(1, 2**(r-1))
    s = sum((math.comb(m,j) * (-1)**j * c**(m-j) * Fraction(1,2**(r*j+1)) / (r*j+1)
             for j in range(m+1)), Fraction(0))
    return s + Fraction(1,2**(r*m+1)) / (r*m+1)


def scaled_volume(r, m):
    c=c_of(r)
    integral = quad(lambda t: (max(0,1-t**r/c))**m, 0, 0.5, epsabs=2e-13)[0]
    return integral + 2.0**(-m-1)/(r*m+1)


def cdf_scaled(r,m,s):
    t=min(s/m**(1/r),1)
    c=c_of(r)
    top=quad(lambda v: (max(0,1-v**r/c))**m,0,min(t,.5),epsabs=1e-12)[0]
    if t>.5:
        top+=quad(lambda v: ((1-v)**r/c)**m,.5,t,epsabs=1e-12)[0]
    return top/scaled_volume(r,m)


def test():
    # Independently integrate original 1D section and verify exact rational coefficient formula.
    count=0
    for r in range(2,6):
        for m in range(1,7):
            integral=quad(lambda t: fiber(r,t)**m,0,1,epsabs=2e-13,points=[.5])[0]
            exact=float(vol_poly_exact(r,m))
            assert abs(integral-exact)<2e-13,(r,m,integral,exact)
            count+=1
    # One-clique case is a complete graph: convex hull of 0, e_i and all-half vertex.
    for d in range(3,7):
        # All extreme points of the edge relaxation of a clique:
        # origin, unit vectors, and half-vectors on subsets of size >= 3.
        halfs=[]
        for k in range(3,d+1):
            for I in combinations(range(d),k):
                v=np.zeros(d)
                v[list(I)]=.5
                halfs.append(v)
        vertices=np.vstack([np.zeros(d),np.eye(d),*halfs])
        volume=ConvexHull(vertices).volume
        assert abs(volume-2.0**(1-d))<1e-12,(d,volume)
    # Completely separate geometric reconstruction: enumerate all half-integral
    # feasible points for small windmills, then compute their convex-hull volumes.
    # Half-integrality for fractional stable-set polytopes is classical.
    for m, r in ((1,2), (1,3), (2,2), (2,3)):
        n=1+m*r
        edges=[(0,j) for j in range(1,n)]
        for b in range(m):
            I=range(1+b*r,1+(b+1)*r)
            edges.extend((i,j) for i in I for j in I if i<j)
        pts=[v for v in product((0., .5, 1.), repeat=n)
             if all(v[i]+v[j]<=1. for i,j in edges)]
        assert abs(ConvexHull(pts).volume-float(vol_poly_exact(r,m)))<1e-10, (m,r)
    # At high dimension the renormalized Laplace integral approaches its gamma constant.
    for r in (2,3,4):
        c=c_of(r)
        goal=c**(1/r)*gamma(1+1/r)
        prev=100.
        for m in (25,100,400,1600):
            observed=scaled_volume(r,m)*m**(1/r)
            err=abs(observed/goal-1)
            assert err < prev and err <.06, (r,m,observed,goal,err)
            prev=err
        for s in (.35, .8, 1.5):
            empirical=cdf_scaled(r,1600,s)
            limit=gammainc(1/r, s**r/c)
            assert abs(empirical-limit)<.002,(r,s,empirical,limit)
    print('PASS: 24 rational/exact-quadrature comparisons, 8 independent convex-hull comparisons,')
    print('      12 asymptotic convergence comparisons, 9 hub CDF approximations.')
    print('Friendship r=2: ratio / sqrt(m) ->', 2*c_of(2)**.5*gamma(1.5))
    for r in (2,3,4):
        print('r=',r,'large-m scaled volume factor=',c_of(r)**(1/r)*gamma(1+1/r))

if __name__=='__main__':
    test()
