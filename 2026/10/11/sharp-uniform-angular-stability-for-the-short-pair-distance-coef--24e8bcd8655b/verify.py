#!/usr/bin/env python3
"""Finite, reproducible numerical checks for a convex-polygon short-pair theorem.
Python standard library only. The manuscript contains the infinite proof.
"""
from math import pi, sin, cos, sqrt, atan2, tan


def cross(a,b): return a[0]*b[1]-a[1]*b[0]
def sub(a,b): return (a[0]-b[0], a[1]-b[1])
def dot(a,b): return a[0]*b[0]+a[1]*b[1]
def add(a,b): return (a[0]+b[0], a[1]+b[1])
def mul(k,a): return (k*a[0], k*a[1])

def area(v):
    return sum(cross(v[i],v[(i+1)%len(v)]) for i in range(len(v)))/2

def clip(poly, a, b):
    # CCW polygon, keep the half-plane left of oriented edge a->b.
    out=[]
    if not poly: return out
    edge=sub(b,a)
    old=poly[-1]
    vo=cross(edge,sub(old,a))
    for new in poly:
        vn=cross(edge,sub(new,a))
        if (vo<-1.e-13 and vn>1.e-13) or (vo>1.e-13 and vn<-1.e-13):
            lam=vo/(vo-vn)
            out.append(add(old,mul(lam,sub(new,old))))
        if vn>=-1.e-13: out.append(new)
        old,vo=new,vn
    return out

def overlap(v,z):
    poly=[add(p,z) for p in v]
    for i in range(len(v)):
        poly=clip(poly,v[i],v[(i+1)%len(v)])
        if not poly: return 0.0
    return max(0.0,area(poly))

def data(v):
    assert len(v)>=3 and area(v)>0
    n=len(v)
    edges=[sub(v[(i+1)%n],v[i]) for i in range(n)]
    le=[sqrt(dot(e,e)) for e in edges]
    assert min(le)>1.e-7
    assert min(cross(edges[i-1],edges[i]) for i in range(n))>1.e-8
    normals=[(e[1]/le[i],-e[0]/le[i]) for i,e in enumerate(edges)]
    alphas=[pi-atan2(cross(edges[i-1],edges[i]),dot(edges[i-1],edges[i])) for i in range(n)]
    assert all(0<a<pi for a in alphas)
    assert abs(sum(alphas)-(n-2)*pi)<1.e-10
    return le,normals,alphas

def q(u,normals,alphas):
    n=len(alphas)
    d=[max(0.,-dot(u,normal)) for normal in normals]
    return sum(.5/tan(alphas[i])*(d[i-1]**2+d[i]**2)+d[i-1]*d[i]/sin(alphas[i]) for i in range(n))

def vertex_f(alpha):
    beta=pi-alpha
    return 1-beta/tan(beta)

def inspect(v):
    le,no,al=data(v)
    A=area(v); n=len(v)
    p=sum(le)
    coeff=sum(vertex_f(a) for a in al)/(8*pi*pi)
    mean=(n-2)*pi/n
    B=n*vertex_f(mean)/(8*pi*pi)
    variance=sum((a-mean)**2 for a in al)
    assert coeff+1.e-11>=B+variance/(24*pi*pi)
    for j in range(128):
        theta=2*pi*(j+0.234)/128
        u=(cos(theta),sin(theta)); t=0.0008
        d=[max(0.,-dot(u,normal)) for normal in no]
        predicted=A-t*sum(le[i]*d[i] for i in range(n))+t*t*q(u,no,al)
        actual=overlap(v,mul(t,u))
        assert abs(predicted-actual)<3.e-10,(n,j,predicted,actual)
    m=8000
    val=2*pi*sum(q((cos(2*pi*(j+0.189)/m),sin(2*pi*(j+0.189)/m)),no,al) for j in range(m))/m
    expected=sum(vertex_f(a) for a in al)/2
    assert abs(val-expected)<4.e-6,(n,val,expected)
    # The integral probability is exact to order four, for sufficiently small r.
    return n,coeff,B,variance


def regular(n): return [(cos(2*pi*j/n),sin(2*pi*j/n)) for j in range(n)]

def deformed(n):
    return [((1+0.04*cos(4*pi*j/n)+0.025*sin(6*pi*j/n))*cos(2*pi*j/n),
             (1+0.04*cos(4*pi*j/n)+0.025*sin(6*pi*j/n))*sin(2*pi*j/n)) for j in range(n)]

shapes=[[(0.,0.),(1.,0.),(1.,1.),(0.,1.)],
        [(0.,0.),(2.,0.),(0.45,1.6)],
        [(0.,0.),(2.,0.),(3.,1.),(0.5,1.8)],
        [(0.,0.),(2.,0.),(2.,0.75),(0.,0.75)]]
shapes += [regular(n) for n in (3,5,6,7,10)]
shapes += [deformed(n) for n in (5,7,10)]
for poly in shapes:
    n,coeff,B,var=inspect(poly)
    print('N=%d, c4=%.10f, baseline=%.10f, angle_variance=%.10g' % (n,coeff,B,var))
# Global sharpness: small balanced exterior-angle perturbations in high even N.
for n in (100,200,400):
    beta=2*pi/n
    eps=0.2/n
    # Two repeated +/- pairs preserve each half-turn total.
    ds=[eps,-eps,eps,-eps]
    angles=[pi-beta-d for d in ds]+[pi-beta]*(n-4)
    c4=sum(vertex_f(a) for a in angles)/(8*pi*pi)
    baseline=n*vertex_f(pi-beta)/(8*pi*pi)
    ratio=(c4-baseline)/sum(d*d for d in ds)
    target=1/(24*pi*pi)
    assert ratio>=target*(1-1.e-5) and ratio<=target*1.2,(ratio,target)
    print('N=%d, sharpness ratio %.12f versus %.12f' % (n,ratio,target))
print('VERIFY_OK')
