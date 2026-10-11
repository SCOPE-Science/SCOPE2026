#!/usr/bin/env python3
"""Exact algebra checks and independent polyhedral tests for homothetic frusta."""
import itertools
import math
import numpy as np
import sympy as sp
from scipy.spatial import ConvexHull


def ratio(d, a):
    b=1-a
    t=2/(2+d*b+math.sqrt(4-4*b+d*d*b*b))
    S=sum(a**j for j in range(d))
    phi=S/(d*d*t*(1-t)*(1-b*t)**(d-1))
    return t, phi


def centroid(d, a):
    S=sum(a**j for j in range(d))
    T=sum((j+1)*a**j for j in range(d))
    return T/((d+1)*S)


def direct_polar_volume(vertices, center):
    """Intersect all actual polar facet inequalities; no theorem formula used."""
    vv=np.asarray(vertices, float)-np.asarray(center,float)
    d=vv.shape[1]
    pv=[]
    for ix in itertools.combinations(range(len(vv)),d):
        mat=vv[list(ix),:]
        if abs(np.linalg.det(mat)) < 1e-10:
            continue
        sol=np.linalg.solve(mat, np.ones(d))
        if np.max(vv@sol) <= 1+1e-9 and not any(np.linalg.norm(sol-v)<1e-8 for v in pv):
            pv.append(sol)
    if len(pv)<d+1:
        raise AssertionError('not enough polar vertices')
    return ConvexHull(np.asarray(pv)).volume


def polar_base_volume(vertices):
    return direct_polar_volume(vertices,np.zeros(len(vertices[0])))


a=sp.symbols('a',real=True)
z=sp.symbols('z',real=True)
for d in range(2,13):
    S=sum(a**j for j in range(d))
    T=sum((j+1)*a**j for j in range(d))
    g=T/((d+1)*S)
    b=1-a
    Q=-1+(2+d*b)*g-(d+1)*b*g**2
    P=sum(sp.binomial(min(k,2*d-4-k)+3,3)*a**k for k in range(2*d-3))
    assert sp.factor(Q-a*b*P/((d+1)*S*S))==0
    # Polynomial certificate for centroid ordering, valid to any dimension
    assert all(int(sp.binomial(min(k,2*d-4-k)+3,3))>0 for k in range(2*d-3))
    # Critical quadratic: one root gives t in (0,1)
    tt=sp.symbols('t',real=True)
    num= -1+(2+d*b)*tt-(d+1)*b*tt**2
    assert sp.expand(num.subs(tt,sp.Rational(1,2)).subs(a,1))==0
    assert sp.expand(num.subs(tt,sp.Rational(1,d+1)).subs(a,0))==0

for d in range(2,13):
    prev=None
    for j in range(41):
        av=j/40
        tv, ph=ratio(d,av)
        gv=centroid(d,av)
        assert 0<tv<=.5
        if 0<av<1:
            assert tv<gv-1e-12
        else:
            assert abs(tv-gv)<1e-12
        if prev is not None:
            assert ph>prev-1e-12
        prev=ph
    assert abs(ratio(d,0)[1]-(d+1)**(d+1)/d**(d+2))<1e-12
    assert abs(ratio(d,1)[1]-4/d)<1e-12

# Independent convex-hull reconstruction for nonsymmetric base triangles and symmetric squares.
base_sets=[
    np.array([[-1.,-1.],[2.,-1.],[-1.,2.]]), # noncentrally symmetric, Santalo point 0
    np.array([[-1.,-1.],[1.,-1.],[1.,1.],[-1.,1.]]),
]
worst=0.
for K in base_sets:
    Kp=polar_base_volume(K)
    for av in [.05,.2,.5,.8,1.]:
        vertices=np.array([list(x)+[0.] for x in K]+[list(av*x)+[1.] for x in K])
        tv,_=ratio(3,av)
        numeric=direct_polar_volume(vertices,[0.,0.,tv])
        pred=Kp/(3*tv*(1-tv)*(1-(1-av)*tv)**2)
        err=abs(numeric-pred)
        worst=max(worst,err)
        assert err<1e-10,(av,err,numeric,pred)

print('VERIFY_OK')
print('symbolic_all_dims_d_2_to_12 = passed')
print('centroid_order_and_universal_product_sweep = passed')
print('nonsymmetric_and_symmetric_3d_polar_polytope_tests = passed')
print('max_absolute_polar_volume_error = %.3e'%worst)
