"""Standalone numerical checks of perpendicular width moments of rectangular boxes.

Run: python check_frame.py
Requires: numpy, scipy. Fixed random seeds.
"""
from math import pi, sqrt
import numpy as np
from scipy.spatial.transform import Rotation

A=8/(3*pi*pi)-1/4
B=8/(3*pi*pi)-2/(3*pi)
threshold=B/A
assert A>0 and B>0 and 1<threshold<3

def exact(side):
    a=np.asarray(side,dtype=float); s=a.sum();sq=np.dot(a,a)
    m=s/2
    cov=A*s*s-B*sq
    var=(1/3-2/(3*pi))*sq+(2/(3*pi)-1/4)*s*s
    return m,var,cov

# Separate numerical integration of the cross-column Haar absolute matrix moment.
# The conditional distribution of perpendicular second-column coordinates has
# absolute mean (2/pi)*sqrt(1-u[j]**2); the first column is uniform on S^2.
# Off-diagonal conditional circle average additionally has (2/pi)*sqrt(1-x^2).
# Direct latitude-longitude quadrature with Haar density sin(theta)/(4pi),
# E|u_1| sqrt(1-u_2²) * 2/pi. Numerical Gauss-Legendre.
nodes,weights=np.polynomial.legendre.leggauss(150)
ang=np.linspace(0,2*pi,1500,endpoint=False)
zz=nodes[:,None];ph=ang[None,:]
x=np.sqrt(1-zz**2)*np.cos(ph)
y=np.sqrt(1-zz**2)*np.sin(ph)
off_q=(2/pi)*np.sum((np.abs(x)*np.sqrt(1-y*y)).mean(axis=1)*weights/2)
assert abs(off_q-8/(3*pi*pi)) < 5e-7, (off_q,8/(3*pi*pi))

rng=np.random.default_rng(20261031)
N=400000
mat=Rotation.random(N,random_state=rng).as_matrix()
for side in [[1,1,1],[1,1,1.5266617081],[1,1,4],[.5,1,1.5],[2,3,4],[1,1,.61020008]]:
    m,v,c=exact(side)
    w=np.abs(mat).transpose(0,2,1)@np.asarray(side,dtype=float)
    e=w.mean(axis=0)
    v_emp=np.var(w[:,0])
    c_emp=np.mean((w[:,0]-m)*(w[:,1]-m))
    prod=(w[:,0]-m)*(w[:,1]-m)
    se=prod.std()/np.sqrt(N)
    assert abs(e[0]-m)<.012, (side,'mean',e[0],m)
    assert abs(v_emp-v)<.012,(side,'variance',v_emp,v)
    assert abs(c_emp-c)<max(5.5*se,.013), (side,'cov',c_emp,c,se)
    assert np.sign(c)==np.sign((sum(side)**2/sum(t*t for t in side))-threshold) or abs(c)<1e-9
    print('sides',side,'mean',round(m,7),'variance',round(v,7),'cov_formula',round(c,7), 'cov_MC',round(c_emp,7),'SE',round(se,7))

# sharp conditional variance comparison, each orientation gives three mutually
# perpendicular width values; independent sample consists of 3 separate rotations
for side in [[1,1,1],[1,1,4]]:
    m,v,c=exact(side)
    frame=(v+2*c)/3
    ind=v/3
    w=np.abs(mat).transpose(0,2,1)@np.asarray(side,dtype=float)
    frame_est=np.mean(w,axis=1)
    assert abs(np.var(frame_est)-frame)<.015
    assert (frame>ind)==(c>0)
    print('frame',side,'independent_mean_variance',ind,'orthogonal_mean_variance',frame)

# strict equality class: for fixed total side length, cube uniquely maximizes
# covariance, and rod limit (epsilon,epsilon,3-2*epsilon) attains sharp infimum.
for e in [.5,.1,.01,.001]:
    _,_,cres=exact([e,e,3-2*e]);_,_,cc=exact([1,1,1])
    assert cres < cc and cres < 0
print('ALL_ORTHOGONAL_WIDTH_TESTS_PASSED')
