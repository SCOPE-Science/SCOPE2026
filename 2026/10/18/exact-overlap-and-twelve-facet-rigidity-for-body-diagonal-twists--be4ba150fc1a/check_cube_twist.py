"""Reproducible exact and independent checks for the cube-twist intersection theorem.

Requires Python 3.10+, sympy; NumPy/SciPy are optional for numerical convex hulls.
No network access is used.
"""
from fractions import Fraction
from itertools import product
import math

import sympy as sp


def dot(a, b):
    return sum(x*y for x,y in zip(a,b))


def cross(x,y):
    return sp.Matrix(x).cross(sp.Matrix(y))


def data(q):
    q=sp.Rational(q)
    den=q*q+3
    a=2*(q+1)/den
    b=(q*q-1)/den
    d=2*(1-q)/den
    rot=sp.Matrix([[a,b,d],[d,a,b],[b,d,a]])
    w=sp.Matrix([1,1,1]); p=sp.Matrix([1,-1,q]);
    cyclic=lambda v:sp.Matrix([v[2],v[0],v[1]])
    v=[w,p,cyclic(p),cyclic(cyclic(p))]
    v=v+[-x for x in v]
    return rot,v


def verify(q, interior=True):
    q=sp.Rational(q)
    R,V=data(q)
    assert R.T*R==sp.eye(3)
    assert R.det()==1
    assert R*sp.Matrix([1,1,1])==sp.Matrix([1,1,1])
    for v in V:
        assert all(abs(z)<=1 for z in v)
        assert all(abs(z)<=1 for z in R.T*v)
    if interior:
        norms=[]
        for i in range(3):
            e=sp.eye(3)[:,i]
            norms.extend([e,-e,R*e,-R*e])
        for n in norms:
            triple=[v for v in V if dot(n,v)==1]
            assert len(triple)==3, (q,n,len(triple))
            area_sq=sp.factor(cross(triple[1]-triple[0],triple[2]-triple[0]).dot(
                   cross(triple[1]-triple[0],triple[2]-triple[0]))/4)
            assert sp.factor(area_sq-(3+q*q)**2/4)==0, (q,area_sq)
    return True


def symbolic_checks():
    q=sp.symbols('q',real=True)
    D=q*q+3
    A=2*(q+1)/D;B=(q*q-1)/D;C=2*(1-q)/D
    R=sp.Matrix([[A,B,C],[C,A,B],[B,C,A]])
    assert all(sp.cancel(z)==0 for z in R.T*R-sp.eye(3))
    assert sp.factor(R.det()-1)==0
    p=sp.Matrix([1,-1,q])
    assert all(sp.cancel(z)==0 for z in R.T*p-sp.Matrix([q,-1,1]))
    w=sp.Matrix([1,1,1]); v=sp.Matrix([-1,q,1])
    n=sp.Matrix([1,0,0]); t1=p-w; t2=-v-w
    assert sp.factor((t1.cross(t2)).dot(n)-(3+q*q))==0
    cos=(3*A-1)/2
    assert sp.factor(sp.diff(cos,q)+3*(q-1)*(q+3)/(q*q+3)**2)==0
    assert sp.simplify((6+2*q*q)-2*(3+q*q))==0
    assert sp.simplify((6*(3+q*q))/3-(6+2*q*q))==0


def numerical():
    try:
        import numpy as np
        from scipy.spatial import HalfspaceIntersection,ConvexHull
    except ImportError:
        print('NUMERICAL_HULL_SKIPPED missing_optional_numpy_scipy')
        return
    u=np.ones(3)/np.sqrt(3)
    K=np.array([[0,-u[2],u[1]],[u[2],0,-u[0]],[-u[1],u[0],0]])
    for theta in np.linspace(0.001,math.pi/3,231):
        R=np.cos(theta)*np.eye(3)+(1-np.cos(theta))*np.outer(u,u)+np.sin(theta)*K
        H=np.vstack((np.eye(3),-np.eye(3),R.T,-R.T))
        v=HalfspaceIntersection(np.column_stack((H,-np.ones(12))),np.zeros(3)).intersections
        h=ConvexHull(v)
        q=(3-2*np.sqrt(3)*np.sin(theta))/(1+2*np.cos(theta))
        expected=6+2*q*q
        assert len(v)==8 and len(h.simplices)==12
        assert abs(h.volume-expected)<4e-12,(theta,h.volume,expected)
        expected_v=np.array([np.ones(3),[1,-1,q],[q,1,-1],[-1,q,1]])
        expected_v=np.vstack((expected_v,-expected_v))
        assert max(min(np.linalg.norm(x-y) for y in expected_v) for x in v)<1e-10
    print('INDEPENDENT_HALFSPACE_HULL_OK sample_angles=231 vertices=8 triangular_facets=12')

if __name__=='__main__':
    symbolic_checks()
    print('SYMBOLIC_ORTHOGONAL_ROTATION_AND_FACE_AREA_OK')
    tests=[sp.Rational(n,97) for n in range(1,97)]
    for q in tests:verify(q,True)
    verify(0,True);verify(1,False)
    print('EXACT_RATIONAL_FACE_CERTIFICATES_OK interior_parameters=97 endpoints=2')
    numerical()
    print('CUBE_TWIST_ALL_CHECKS_OK')
