#!/usr/bin/env python3
"""Reproducibility checks for the triangular-prism plane-section formulas."""
import math
import numpy as np
from numpy.polynomial.legendre import leggauss


def base_data(v):
    p = np.asarray(v, dtype=float)
    edge = np.roll(p, -1, axis=0)-p
    lengths = np.linalg.norm(edge, axis=1)
    assert p.shape == (3, 2) and abs(np.linalg.det(np.stack((p[1]-p[0],p[2]-p[0])))) > 1e-10
    return p, lengths, lengths.sum()


def exact_pentagon_quadrature(p, h, n=131072):
    theta=2*math.pi*np.arange(n)/n
    unit=np.column_stack((np.cos(theta),np.sin(theta)))
    q=np.sort(unit@p.T, axis=1)
    x=q[:,1]-q[:,0]; y=q[:,2]-q[:,1]
    f=(x+y)*np.arctan((x+y)/h)-x*np.arctan(x/h)-y*np.arctan(y/h)
    _,_,P=base_data(p)
    return 2*math.pi*f.mean()/(math.pi*(P+2*h))


def direct_edge_count(p, h, ntheta=720, nw=192):
    theta=2*math.pi*np.arange(ntheta)/ntheta
    w,weights=leggauss(nw)
    th=np.repeat(theta,nw)
    u=np.tile(w,ntheta)
    direction=np.column_stack((np.sqrt(1-u*u)*np.cos(th),np.sqrt(1-u*u)*np.sin(th)))
    base=direction@p.T
    vert=np.concatenate((base,base+h*u[:,None]),axis=1)
    levels=np.sort(vert,axis=1)
    mids=.5*(levels[:,1:]+levels[:,:-1])
    cuts=np.zeros(mids.shape,dtype=np.int8)
    edges=[(0,1),(1,2),(2,0),(3,4),(4,5),(5,3),(0,3),(1,4),(2,5)]
    for a,b in edges:
        cuts+=((vert[:,a,None]<mids)!=(vert[:,b,None]<mids))
    lengths=levels[:,1:]-levels[:,:-1]
    five=np.sum(np.where(cuts==5,lengths,0.0),axis=1).reshape(ntheta,nw)
    integral=2*math.pi*np.sum(five@weights)/ntheta
    _,_,P=base_data(p)
    return integral/(math.pi*(P+2*h)), int(cuts.min()),int(cuts.max())


def tall_coeff(p):
    _,lengths,_=base_data(p)
    s=0.0
    for j in range(3):
        a=p[(j+1)%3]-p[j];b=p[(j+2)%3]-p[j]
        alpha=math.acos(max(-1,min(1,float(np.dot(a,b)/np.linalg.norm(a)/np.linalg.norm(b)))))
        s+=np.linalg.norm(a)*np.linalg.norm(b)*(math.sin(alpha)-alpha*math.cos(alpha))
    return s/math.pi


def run():
    bases=[np.array([[0,0],[1,0],[.5,math.sqrt(3)/2]]),np.array([[0,0],[1,0],[0,1]]),np.array([[0,0],[1,0],[.3,.9]])]
    count=0
    for p in bases:
        _,lengths,P=base_data(p)
        for h in (.2,.7,1.4,4.0):
            analytic=exact_pentagon_quadrature(p,h)
            direct,lo,hi=direct_edge_count(p,h)
            assert lo>=0 and hi<=5,(lo,hi)
            assert abs(analytic-direct)<2e-4,(h,analytic,direct)
            assert 0<analytic<.5
            count+=1
        t=.002
        q=exact_pentagon_quadrature(p,t)
        thin=(2*t-t*t*sum(1/lengths))/(P+2*t)
        assert abs(q-thin)<2e-8,(q,thin)
        big=100.0
        q=exact_pentagon_quadrature(p,big)
        k=tall_coeff(p)
        predicted=k/(big*big)-k*P/(2*big**3)
        assert abs(q-predicted)<3e-8,(q,predicted)
    print('PRISM_CROFTON_CHECK_OK independent_edge_counts=',count,'thin_tall_checks=',2*len(bases))

if __name__=='__main__':run()
