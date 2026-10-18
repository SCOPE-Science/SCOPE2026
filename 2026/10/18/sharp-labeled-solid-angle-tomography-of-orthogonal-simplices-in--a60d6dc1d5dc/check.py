#!/usr/bin/env python3
"""Independent numerical checks for inverse solid-angle tomography of orthogonal simplices.
Requires NumPy and SciPy. Deterministic quadrature and geometric formulas; numerical checks are not a proof.
"""
import math
import numpy as np
from scipy.special import ndtr
from numpy.polynomial.legendre import leggauss
from scipy.optimize import root


def probabilities(a, order=65):
    """Independent half-normal tensor quadrature over [0,10]."""
    a = np.asarray(a, dtype=float)
    n = len(a)
    z, w = leggauss(order)
    h = 5.0 * (z + 1.0)
    w = 5.0 * w * math.sqrt(2 / math.pi) * np.exp(-h * h / 2)
    out=[]
    for i in range(n):
        args = [(a[i]/a[j])*h for j in range(n) if j != i]
        u = np.zeros((order,)*(n-1), dtype=float)
        weights = np.ones_like(u)
        for k,v in enumerate(args):
            sh=[1]*(n-1); sh[k]=order
            u = u + v.reshape(sh)
            weights = weights * w.reshape(sh)
        out.append((0.5**(n-1))*np.sum(weights*ndtr(-u)))
    return np.asarray(out)


def trihedron_solid_angle(a, i):
    a=np.asarray(a,float)
    n=len(a)
    assert n==3
    origin=np.zeros(3)
    verts=[origin]+[a[j]*np.eye(3)[j] for j in range(3)]
    v=[verts[j]-verts[i+1] for j in range(4) if j!=i+1]
    u,vv,w=v
    det=abs(np.linalg.det(np.array([u,vv,w])))
    denom=(np.linalg.norm(u)*np.linalg.norm(vv)*np.linalg.norm(w)
      +np.dot(u,vv)*np.linalg.norm(w)
      +np.dot(vv,w)*np.linalg.norm(u)
      +np.dot(w,u)*np.linalg.norm(vv))
    return 2*math.atan2(det,denom)


def test():
    a=np.array([1.0,2.3]); p=probabilities(a,105)
    expected=np.array([math.atan(a[1]/a[0]),math.atan(a[0]/a[1])])/(2*math.pi)
    assert np.max(abs(p-expected))<2e-11,(p,expected)
    print('PASS 2D exact planar-angle normalization')
    for a in (np.array([1.,1.,1.]),np.array([.65,1.2,2.4]),np.array([2.1,.55,1.6])):
        p=probabilities(a,75)
        direct=np.array([trihedron_solid_angle(a,i)/(4*math.pi) for i in range(3)])
        assert np.max(abs(p-direct))<2e-9,(a,p,direct)
        assert np.all(np.diff(p[np.argsort(a)])<1e-10),(a,p)
        if len(np.unique(a))==3:
            assert np.all(np.diff(p[np.argsort(a)]) < -1e-7),(a,p)
    print('PASS 3D exact independent trihedral-angle formula and reverse leg order')
    for a in ([.7,1.4,1.], [1.5,.7,1.], [1.2,1.8,1.]):
        a=np.asarray(a,float)
        t=np.log(a[:-1]); base=probabilities(a,55)[:-1]
        J=np.zeros((2,2))
        step=1e-5
        for j in range(2):
            e=np.eye(2)[j]*step
            J[:,j]=(probabilities(np.exp(np.r_[t+e,0.]),55)[:-1]-probabilities(np.exp(np.r_[t-e,0.]),55)[:-1])/(2*step)
        for i in range(2):
            assert J[i,i]<0
            assert J[i,1-i]>0
            assert -J[i,i]>J[i,1-i]
        sol=root(lambda s: probabilities(np.exp(np.r_[s,0.]),55)[:-1]-base,[0.,0.],tol=1e-9)
        assert np.max(abs(sol.x-t))<1e-7,(sol.x,t)
    print('PASS negative grounded-Laplacian sign/strict dominance and inverse recovery')


if __name__=='__main__':
    test()
