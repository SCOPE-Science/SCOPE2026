#!/usr/bin/env python3
"""Exact-rational diagnostic for the farthest-projection four-cycle theorem.

No third-party modules; checks concrete finite sets, not the continuum proof.
"""
from fractions import Fraction as F
from itertools import product

def add(x,y): return (x[0]+y[0],x[1]+y[1])
def sub(x,y): return (x[0]-y[0],x[1]-y[1])
def scale(c,x): return (c*x[0],c*x[1])
def dot(x,y): return x[0]*y[0]+x[1]*y[1]
def cross(x,y): return x[0]*y[1]-x[1]*y[0]
def proj(x,p,q):
    d=sub(q,p)
    return add(p,scale(dot(sub(x,p),d)/dot(d,d),d))
def sqdist(x,p,q):
    h=sub(x,proj(x,p,q))
    return dot(h,h)

def construct(a,b,c):
    # Cyclically ordered triangle: apex lies to the left of the oriented side.
    d=sub(b,a); L=dot(d,d); cma=sub(c,a)
    u=dot(cma,d)/L; v=cross(d,cma)/L
    assert v>0
    s=u*u+v*v; t=(1-u)**2+v*v; E=u*u+(1-u)**2+v*v
    conditions=[s*t>(1-u)**4, u*u*t>(E-u)**2,
                s*t>u**4, (1-u)**2*s>(E-1+u)**2]
    raw=[(s/E,F(0)),(u*u/E,u*v/E),(u*u/E,F(0)),(s/E,(1-u)*v/E)]
    perp=(-d[1],d[0])
    candidates=[add(a,add(scale(x,d),scale(y,perp))) for x,y in raw]
    return all(conditions),candidates,conditions

def direct_map(x,source,lines):
    targets=[j for j in range(3) if j!=source]
    ds=[sqdist(x,*lines[j]) for j in targets]
    if ds[0]==ds[1]:return x,None
    which=targets[0 if ds[0]>ds[1] else 1]
    return proj(x,*lines[which]),which

def all_four_cycles(points):
    a,b,c=points
    lines=[(a,b),(a,c),(b,c)]
    found={}
    for labels in product(range(3),repeat=4):
        if any(labels[j]==labels[(j+1)%4] for j in range(4)):continue
        # Compose four prescribed projections restricted to starting line.
        A,B=lines[labels[0]];d=sub(B,A)
        def cycle_return(x):
            for label in labels[1:]+(labels[0],):x=proj(x,*lines[label])
            return x
        f0=cycle_return(A);f1=cycle_return(B)
        alpha=dot(sub(f1,f0),d)/dot(d,d)
        assert abs(alpha)<1
        beta=dot(sub(f0,A),d)/dot(d,d)
        x=add(A,scale(beta/(1-alpha),d))
        orbit=[x]
        for k in range(4):
            y,chosen=direct_map(orbit[-1],labels[k],lines)
            if chosen!=labels[(k+1)%4]:break
            orbit.append(y)
        else:
            if orbit[-1]==orbit[0] and len(set(orbit[:-1]))==4:
                found[tuple(sorted(orbit[:-1]))]=labels
    return set(found)

def examine(u,v):
    a=(F(0),F(0));b=(F(1),F(0));c=(u,v)
    pts=(a,b,c)
    predicted=set()
    for side in [(a,b,c),(b,c,a),(c,a,b)]:
        valid,poly,tests=construct(*side)
        if valid:
            assert len(set(poly))==4
            lines=[(side[0],side[1]),(side[0],side[2]),(side[1],side[2])]
            for i,target in enumerate((1,0,2,0)):
                q,j=direct_map(poly[i],(0,1,0,2)[i],lines)
                assert q==poly[(i+1)%4] and j==target
            predicted.add(tuple(sorted(poly)))
    exact=all_four_cycles(pts)
    assert predicted==exact,(u,v,len(predicted),len(exact))
    assert len(exact)<=1
    return len(exact)

def main():
    tests=0; histogram=[0,0]
    for numerator in range(-4,13):
        for ynum in range(1,13):
            u=F(numerator,8);v=F(ynum,12)
            histogram[examine(u,v)]+=1
            tests+=1
    # Isosceles boundary comparison without irrational numerical approximation:
    for numerator in range(1,33):
        v=F(numerator,40);q=v*v
        predicted=16*q*q-4*q-1<0
        found=bool(examine(F(1,2),v))
        assert found==predicted
        tests+=1
    assert histogram[1]>0 and histogram[0]>0
    print(f'CHECK_OK exact rational triangles: {tests}; grid cycles zero/one: {histogram}')

if __name__=='__main__': main()
