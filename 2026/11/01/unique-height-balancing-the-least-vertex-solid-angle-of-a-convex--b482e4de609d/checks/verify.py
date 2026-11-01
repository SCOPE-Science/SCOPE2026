"""Reproducible finite numerical checks for pyramid solid-angle balancing.

Mathematical proof is analytic; these checks sample special 3D examples.
No external data are required beyond numpy.
"""
import numpy as np
from math import pi,atan2,sqrt

def omega3(a,b,c):
    a,b,c=map(lambda v:np.array(v,dtype=float), (a,b,c))
    numerator=abs(float(np.linalg.det(np.column_stack([a,b,c]))))
    denominator=(np.linalg.norm(a)*np.linalg.norm(b)*np.linalg.norm(c)+
       np.dot(a,b)*np.linalg.norm(c)+np.dot(b,c)*np.linalg.norm(a)+
       np.dot(c,a)*np.linalg.norm(b))
    return 2*atan2(numerator,denominator)

def angles(poly,q,h):
    poly=np.array(poly,dtype=float);q=np.array(q,dtype=float);N=len(poly)
    a=np.array([0.,0.,h]); qq=np.r_[q,0.]
    apex=0.0
    for j in range(N):
        v=np.r_[poly[j],0.]; w=np.r_[poly[(j+1)%N],0.]
        apex+=omega3(v-a,w-a,qq-a)
    bases=[]
    for j in range(N):
        v=np.r_[poly[j],0.]
        w=np.r_[poly[(j-1)%N],0.]
        t=np.r_[poly[(j+1)%N],0.]
        bases.append(omega3(w-v,t-v,a-v))
    return np.array([apex]+bases)

def run():
    polygons=[(
        np.array([[np.cos(2*pi*j/3),np.sin(2*pi*j/3)] for j in range(3)]),
        np.array([0.,0.])),
        (np.array([[-1.,-1.],[2.,-1.],[2.,1.],[-1.,1.]]),np.array([0.3,0.2])),
        (np.array([[-2.,0.],[-1.,-1.],[1.,-1.],[2.,0.],[1.,2.],[-1.,2.]]),np.array([0.1,0.1]))]
    total=0
    for P,q in polygons:
        hs=np.geomspace(0.03,50,75)
        ang=np.array([angles(P,q,h) for h in hs]);total+=len(hs)*(len(P)+1)
        assert np.all(np.diff(ang[:,0])<-1e-11), 'apex angle monotonicity'
        assert np.all(np.diff(ang[:,1:],axis=0)>1e-11), 'base angle monotonicity'
        diff=ang[:,0]-np.min(ang[:,1:],axis=1)
        assert diff[0]>0 and diff[-1]<0
        assert np.count_nonzero(np.diff(np.sign(diff)))==1
    P=polygons[0][0];h=sqrt(2)
    v=angles(P,[0,0],h)
    assert np.max(abs(v-v[0]))<1e-12
    print('PASS:',total,'solid-angle evaluations, 3 polygon families, unique crossings and regular tetrahedron equality')
if __name__=='__main__': run()
