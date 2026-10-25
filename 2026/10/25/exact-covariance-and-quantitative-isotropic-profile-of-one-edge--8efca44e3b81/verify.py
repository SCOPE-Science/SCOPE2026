#!/usr/bin/env python3
"""Independent finite polytope integrations and exact symbolic checks for a cube plus a diagonal segment.

Requires numpy, scipy and sympy. Run: python verify.py
"""
import itertools,math
import numpy as np
import sympy as sp
from scipy.spatial import ConvexHull

def expected(d, t):
    t=float(t)
    a=(1+(d+2)*t)/(12*(1+d*t))
    b=(1+2*t+d*t*t)/12
    J=np.ones((d,d))/d
    return 1+d*t,a*(np.eye(d)-J)+b*J

def independent_hull_integration(d,t):
    points=np.array([[float(z)/2+float(s)*t/2 for z in v]
        for (*v,s) in itertools.product((-1,1),repeat=d+1)])
    points=np.unique(points,axis=0)
    hull=ConvexHull(points)
    volume=0.0
    raw=np.zeros((d,d))
    for face in hull.simplices:
        vertices=points[face]
        size=abs(np.linalg.det(vertices))/math.factorial(d)
        total=vertices.sum(axis=0)
        raw+=size*(vertices.T@vertices+np.outer(total,total))/((d+1)*(d+2))
        volume+=size
    return volume,raw/volume

if __name__=='__main__':
    d,t=sp.symbols('d t',positive=True)
    R=(1+(d+2)*t)**(d-1)*(1+2*t+d*t*t)/(1+d*t)**(d+1)
    log_derivative=(d-1)*(d+2)/(1+(d+2)*t)+(2+2*d*t)/(1+2*t+d*t*t)-(d+1)*d/(1+d*t)
    target=2*d*(d-1)*t*(t-1)/((1+d*t)*(1+(d+2)*t)*(1+2*t+d*t*t))
    assert sp.factor(log_derivative-target)==0
    assert sp.factor(sp.diff(target,t).subs(t,1)-2*d*(d-1)/((d+1)*(d+3)**2))==0
    cases=0
    for dim in range(2,5):
        for weight in (.25,1.,3.):
            volume,cov=independent_hull_integration(dim,weight)
            vol_target,cov_target=expected(dim,weight)
            assert abs(volume-vol_target)<1e-9
            assert np.max(np.abs(cov-cov_target))<1e-9
            cases+=1
    print('VERIFY_OK symbolic_profile=1 symbolic_curvature=1 independent_polytope_integrations=',cases)
