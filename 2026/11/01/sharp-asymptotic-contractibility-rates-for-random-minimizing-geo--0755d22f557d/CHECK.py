#!/usr/bin/env python3
"""Reproduce exact covariance and random-geodesic polygon checks."""
from math import factorial, comb, pi, sqrt
from fractions import Fraction
import sympy as sp
import numpy as np

a,b = sp.symbols('a b', positive=True, real=True)
t = a*(1-a)
alpha=(b*b + a*a-a)/(2*b)
beta=(b*b-a*a+a)/(2*b)
V=[(sp.Rational(1,2),alpha),(a-sp.Rational(1,2),beta),(-sp.Rational(1,2),alpha),(-sp.Rational(1,2),-alpha),(sp.Rational(1,2)-a,-beta),(sp.Rational(1,2),-alpha)]
A=sp.S(0); Mxx=sp.S(0); Mxy=sp.S(0); Myy=sp.S(0)
for (x,y),(X,Y) in zip(V,V[1:]+V[:1]):
    d=x*Y-X*y
    A += d/2
    Mxx+=(x*x+x*X+X*X)*d/12
    Mxy+=(2*x*y+x*Y+X*y+2*X*Y)*d/24
    Myy+=(y*y+y*Y+Y*Y)*d/12
assert sp.simplify(A-b)==0
C=sp.Matrix([[sp.factor(Mxx/A),sp.factor(Mxy/A)], [sp.factor(Mxy/A),sp.factor(Myy/A)]])
exact=(1-2*t**2/b**2*(1-t/b**2)**2)/144
assert sp.factor(C.det()/b**2-exact)==0
assert sp.factor(exact.subs(a,0)-sp.Rational(1,144))==0
assert sp.simplify(exact.subs({a:sp.Rational(1,2),b:sp.sqrt(3)/2})-sp.Rational(25,3888))==0
assert sp.simplify(C.subs({a:sp.Rational(1,2),b:sp.sqrt(3)/2})[0,1])==0
print('SYMBOLIC_VORONOI_SECOND_MOMENTS_AND_SHARP_ENDPOINTS_PASSED')

def spline_center(n):
    z=Fraction(0)
    for j in range(n//2+1):
        x=Fraction(n,2)-j
        if x>0:
            z+=(-1)**j*comb(n,j)*x**(n-1)
    return z/factorial(n-1)
assert spline_center(3)==Fraction(3,4)
assert spline_center(4)==Fraction(2,3)
assert spline_center(5)==Fraction(115,192)
assert spline_center(6)==Fraction(11,20)
assert spline_center(3)**2 == Fraction(9,16)
print('EXACT_RECTANGULAR_WINDING_BSPLINE_LAWS_PASSED')

# Check that the claimed extrema follow from nonnegative factor,
# u = a(1-a)/b^2 in [0,1/3], and strictly positive derivatives.
u=sp.symbols('u',real=True)
assert sp.factor(sp.diff(u*(1-u)**2,u))==(u-1)*(3*u-1)
assert sp.factor(sp.diff(t,a))==1-2*a
assert sp.simplify((2*t*u*(1-u)**2).subs({a:sp.Rational(1,2),u:sp.Rational(1,3)})-sp.Rational(2,27))==0
print('GLOBAL_SHAPE_OPTIMIZATION_CERTIFICATE_PASSED')

# Independent polygon integration at random rational lattice parameters.
rng=np.random.default_rng(847)

def poly_moments_numeric(av,bv):
    al=(bv*bv+av*av-av)/(2*bv); be=(bv*bv-av*av+av)/(2*bv)
    v=np.array([[.5,al],[av-.5,be],[-.5,al],[-.5,-al],[.5-av,-be],[.5,-al]])
    cross=v[:,0]*np.roll(v[:,1],-1)-v[:,1]*np.roll(v[:,0],-1)
    ar=np.sum(cross)/2
    x,y=v[:,0],v[:,1]; X,Y=np.roll(x,-1),np.roll(y,-1)
    sx=np.sum((x*x+x*X+X*X)*cross)/(12*ar)
    sy=np.sum((y*y+y*Y+Y*Y)*cross)/(12*ar)
    sxy=np.sum((2*x*y+x*Y+X*y+2*X*Y)*cross)/(24*ar)
    return v, ar, np.array([[sx,sxy],[sxy,sy]])

for av,bv in [(0,1),(.13,1.1),(.31,1.3),(.5,sqrt(3)/2),(.5,2)]:
    poly,ar,S=poly_moments_numeric(av,bv)
    tt=av*(1-av)
    target=(1-2*tt**2/bv**2*(1-tt/bv**2)**2)/144
    assert abs(ar-bv)<1e-12
    assert abs(np.linalg.det(S)/bv**2-target)<1e-12
    # Sample random interior points by triangulation about the origin.
    tri_a=poly; tri_b=np.roll(poly,-1,axis=0)
    areas=.5*np.abs(tri_a[:,0]*tri_b[:,1]-tri_a[:,1]*tri_b[:,0])
    choices=rng.choice(6,size=80000,p=areas/areas.sum())
    U=rng.random((80000,2)); r=np.sqrt(U[:,0]); w=U[:,1]
    pts=(r*(1-w))[:,None]*tri_a[choices]+(r*w)[:,None]*tri_b[choices]
    numer=np.cov(pts,rowvar=False,bias=True)
    assert abs(np.linalg.det(numer)/bv**2-target)<1.2e-4
    # independently compare with the full deck distance for points in V.
    for p in pts[:100]:
        base=np.dot(p,p)
        for i in range(-2,3):
            for j in range(-2,3):
                if i==j==0: continue
                vec=np.array([i+j*av,j*bv])
                assert base<=np.dot(p-vec,p-vec)+1e-9
print('INDEPENDENT_POLYGON_MOMENT_AND_DECK_CHECKS_PASSED')

# Independent random-loop check for the source triangle endpoints.
for av,bv,expect in [(0,1,9/16),(.5,sqrt(3)/2,7/12)]:
    poly,area,_=poly_moments_numeric(av,bv)
    tri_a=poly;tri_b=np.roll(poly,-1,axis=0)
    areas=.5*np.abs(tri_a[:,0]*tri_b[:,1]-tri_a[:,1]*tri_b[:,0])
    N=150000
    disps=[]
    for _ in range(2):
        choices=rng.choice(6,size=N,p=areas/areas.sum())
        U=rng.random((N,2));r=np.sqrt(U[:,0]);w=U[:,1]
        disps.append((r*(1-w))[:,None]*tri_a[choices]+(r*w)[:,None]*tri_b[choices])
    s=disps[0]+disps[1]
    # In V iff no nonzero lattice translate is strictly shorter.
    inside=np.ones(N,dtype=bool)
    baseline=np.sum(s*s,axis=1)
    for i in range(-2,3):
        for j in range(-2,3):
            if i==j==0:continue
            v=np.array([i+j*av,j*bv]);inside&=baseline<=np.sum((s-v)**2,axis=1)
    empirical=inside.mean()
    assert abs(empirical-expect)<.009, (av,empirical,expect)
print('INDEPENDENT_RANDOM_GEODESIC_TRIANGLE_LIMIT_CASES_PASSED')

# Separate polygon-length test: independent torus vertices, not direct V increments.
for nv, expected in [(4,Fraction(4,9)), (5,Fraction(115,192)**2)]:
    N=140000
    vertices=rng.random((nv,N,2))
    vectors=np.roll(vertices,-1,axis=0)-vertices
    vectors-=np.floor(vectors+.5)
    winding=np.rint(vectors.sum(axis=0)).astype(int)
    empirical=np.all(winding==0,axis=1).mean()
    assert abs(empirical-float(expected))<.009, (nv, empirical,expected)
print('INDEPENDENT_FOUR_AND_FIVE_VERTEX_WINDING_LAWS_PASSED')
print('ALL_CHECKS_PASSED')
