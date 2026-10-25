"""Independent exact-rational checks for reflected mixed volumes of vertex-cut tetrahedra.
Run: python verify.py. Requires numpy and scipy for candidate facet triangulations.
All facet half-space tests and volume sums are carried out in fractions.Fraction.
"""
from fractions import Fraction as F
from itertools import product
from math import comb
import numpy as np
from scipy.spatial import ConvexHull

Z=F(0); O=F(1)
E=[(O,Z,Z),(Z,O,Z),(Z,Z,O)]

def vecadd(u,v):return tuple(x+y for x,y in zip(u,v))
def vecsub(u,v):return tuple(x-y for x,y in zip(u,v))
def mul(t,u):return tuple(t*x for x in u)
def cross(u,v):return (u[1]*v[2]-u[2]*v[1], u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0])
def dot(u,v):return sum((x*y for x,y in zip(u,v)),Z)
def det(u,v,w):return dot(u,cross(v,w))

def vertices(depths):
    pts={(Z,Z,Z)}
    for i,a in enumerate(depths):
        if a==0:
            pts.add(E[i]);continue
        pts.add(mul(1-a,E[i]))
        for j in range(3):
            if i!=j:pts.add(vecadd(mul(1-a,E[i]),mul(a,E[j])))
    return sorted(pts)

def hull_volume(pts,centroid):
    hull=ConvexHull(np.asarray(pts,dtype=float),qhull_options='Qt')
    out=Z;triangles=0
    for indices in hull.simplices:
        x,y,z=[pts[int(i)] for i in indices]
        normal=cross(vecsub(y,x),vecsub(z,x))
        signs={1 if v>0 else -1 for p in pts if (v:=dot(normal,vecsub(p,x)))!=0}
        assert len(signs)==1,('Invalid floating-hull facet', x,y,z)
        vol=abs(det(vecsub(x,centroid),vecsub(y,centroid),vecsub(z,centroid)))/6
        assert vol>0
        out+=vol;triangles+=1
    return out,triangles

def exact_values(a,b,c):
    x=(a,b,c);s=sum(x,Z);S2=sum((t*t for t in x),Z);S3=sum((t*t*t for t in x),Z)
    assert 0<=s<1
    vol=(1-S3)/6
    mix=(3-s-(2-s)*S2-S3)/6
    deficit=s+(2-s)*(S2-S3)/(1-S3)
    ratio=2+6*mix/vol
    assert ratio==20-6*deficit
    return vol,mix,ratio,deficit

def check(a,b,c):
    x=(a,b,c);v=vertices(x)
    centroid=mul(F(1,len(v)),tuple(sum((p[i] for p in v),Z) for i in range(3)))
    va,fa=hull_volume(v,centroid)
    dv=sorted({vecsub(p,q) for p in v for q in v})
    vb,fb=hull_volume(dv,(Z,Z,Z))
    expected_vol,mix,ratio,deficit=exact_values(*x)
    assert va==expected_vol,(x,va,expected_vol)
    assert vb/va==ratio,(x,vb/va,ratio)
    # General Minkowski degree-three identity and normalized Godbersen deficit.
    assert vb==2*va+6*mix
    return fa,fb

def sharp_bounds(s):
    concentrated=s*(1+3*s)/(1+s+s*s)
    balanced=s*(9+6*s-5*s*s)/(9-s*s*s)
    assert concentrated>=balanced
    return 20-6*concentrated,20-6*balanced

def run():
    count=0;facet_count=0
    for aa,bb,cc in product((0,1,2,4,7),repeat=3):
        a,b,c=(F(aa,15),F(bb,15),F(cc,15))
        if a+b+c>=1:continue
        fa,fb=check(a,b,c);count+=1;facet_count+=fa+fb
        s=a+b+c
        lower,upper=sharp_bounds(s)
        _,_,ratio,_=exact_values(a,b,c)
        assert lower<=ratio<=upper,(a,b,c,lower,ratio,upper)
        if a==b==c and s>0: assert ratio==upper
        if sum(t>0 for t in (a,b,c))==1:assert ratio==lower
    # Algebraic identity for pair-mixing derivative: x+y=v, third cut c.
    # H(p)=[v²-v³+c²-c³+(3v-2)p]/[1-v³-c³+3vp], p=xy.
    # Its derivative is -B/[denominator²], B=2-3v+v³+3vc²-2c³.
    derivative_checks=0
    for v_num in range(1,11):
        v=F(v_num,13)
        for c_num in range(0,13-v_num):
            c=F(c_num,13)
            B=2-3*v+v**3+3*v*c*c-2*c**3
            assert B>0
            N0=v*v-v**3+c*c-c**3;D0=1-v**3-c**3
            assert (3*v-2)*D0-3*v*N0 == -B
            assert 0<=c and 0<v and v+c<1
            derivative_checks+=1
    print('VERIFY_OK exact_hulls=',count,'rational_triangles=',facet_count,'mixing_derivative_checks=',derivative_checks)

if __name__=='__main__':run()
