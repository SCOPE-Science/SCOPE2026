"""Independent volume and exact-arithmetic checks for simplex segment extrusions.
Run: python verify.py. Requires numpy and scipy (see requirements.txt).
"""
from fractions import Fraction as F
from itertools import product
import random
import numpy as np
from scipy.spatial import ConvexHull

VERT = ((0,0,0),(1,0,0),(0,1,0),(0,0,1))


def closed_forms(v,t):
    v=tuple(F(x) for x in v)
    t=F(t)
    w=(-sum(v),)+v
    T=sum(abs(x) for x in w)/2
    H=sum(abs(w[0]+w[i]) for i in (1,2,3))
    q=3*t*T
    vk=(1+q)/6
    vdiff=F(10,3)+2*t*(T+H)
    ratio=vdiff/vk
    god=(ratio-2)/6
    assert F(20+4*q*(1+H/T),1+q)==ratio
    assert (3+t*(T+2*H))/(1+3*t*T)==god
    assert F(20+8*q,1+q)<=ratio<=F(20+12*q,1+q)
    assert F(3+q,1+q)<=god<=F(3+F(5,3)*q,1+q)
    return vk,vdiff,ratio,god,T,H


def calc_polytope_volume(points):
    ps=np.asarray(points,dtype=float)
    return ConvexHull(ps).volume


def geometric_primitive(v,t):
    vv=np.asarray(v,dtype=float)*float(t)
    vertices=np.asarray(VERT,dtype=float)
    k=np.concatenate((vertices,vertices+vv))
    diffs=(k[:,None,:]-k[None,:,:]).reshape(-1,3)
    return calc_polytope_volume(k),calc_polytope_volume(diffs)


def check():
    rng=random.Random(726)
    count=0
    for v in [(1,0,0),(1,1,-1),(1,1,1),(1,-1,0),(1,1,0),(-3,2,-5),(2,-3,4)]:
        for t in [F(1,7),F(2,3),F(1),F(3,2)]:
            vk,vd,r,_,T,H=closed_forms(v,t)
            gk,gd=geometric_primitive(v,t)
            assert abs(gk-float(vk))<1e-9,(v,t,gk,vk)
            assert abs(gd-float(vd))<1e-8,(v,t,gd,vd)
            count+=1
    for z in range(250):
        v=tuple(rng.randint(-9,9) for _ in range(3))
        if v==(0,0,0):continue
        t=F(rng.randint(1,9),rng.randint(1,9))
        vk,vd,r,_,T,H=closed_forms(v,t)
        gk,gd=geometric_primitive(v,t)
        assert abs(gk-float(vk))<2e-8,(v,t,gk,vk)
        assert abs(gd-float(vd))<3e-8,(v,t,gd,vd)
        count+=1
    # The volume of the general Minkowski combination uses the same
    # facet formula but is checked independently from explicit 4x4
    # tetrahedral vertex differences.
    for i in range(175):
        v=tuple(rng.randint(-5,5) for _ in range(3))
        if v==(0,0,0): continue
        a=F(rng.randint(1,7),rng.randint(1,6))
        b=F(rng.randint(1,7),rng.randint(1,6))
        t=F(rng.randint(1,7),rng.randint(1,6))
        T=F(sum(abs(x) for x in (-sum(v),)+v),2)
        H=F(sum(abs(sum(v)-x) for x in v))
        f3=(a*a*a+9*a*a*b+9*a*b*b+b*b*b)/6
        G=T*(a*a+b*b)/2+a*b*H
        exact=f3+t*(a+b)*G
        xs=np.asarray(VERT,dtype=float)
        v=np.asarray(v,dtype=float)
        verts=(float(a)*xs[:,None,:]-float(b)*xs[None,:,:]).reshape(-1,3)
        verts=np.concatenate([verts,verts+float(t*(a+b))*v])
        numerical=calc_polytope_volume(verts)
        assert abs(numerical-float(exact))<5e-8,(v,a,b,t,numerical,exact)
        count+=1
    # Sharp orientations. Barycentric velocity vectors have sum zero.
    for q in (F(1,100),F(1),F(100)):
        for w in ((-3,1,1,1),(-1,1,0,0),(-1,1,1,-1),(1,1,-1,-1)):
            v=w[1:]
            t=q/(3*F(sum(map(abs,w)),2))
            _,_,R,_,T,H=closed_forms(v,t)
            if H==T:assert R==F(20+8*q,1+q)
            if H==2*T:assert R==F(20+12*q,1+q)
            count+=1
    # Every intermediate directional ratio is attained explicitly.
    for u in (F(i,20) for i in range(21)):
        w=(F(1),F(1),-u,-(2-u))
        assert sum(w)==0
        T=F(sum(abs(x) for x in w),2)
        H=sum(abs(w[0]+w[i]) for i in (1,2,3))
        assert H/T==2-u
        count+=1
    print('PASS:',count,'independent polytope-volume / exact-rational / equality checks')

if __name__ == '__main__': check()
