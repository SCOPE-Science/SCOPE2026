#!/usr/bin/env python3
"""Reproduce the spherical-cone formula for a symmetric skew octahedron."""
import math
import random

def probability(delta):
    assert delta>0
    L=math.hypot(1,2*delta)
    Y=3*math.sqrt(3)*delta
    omega_same=2*math.atan2(Y,L*(16*delta*delta-0.5))
    omega_mixed=2*math.atan2(Y,4.5*L+3*math.sqrt(3))
    return (2*omega_same+6*omega_mixed)/(4*math.pi)

def cross2(p,q,r):
    return (q[0]-p[0])*(r[1]-p[1])-(q[1]-p[1])*(r[0]-p[0])

def hull_size(points):
    pts=sorted(points)
    lo=[]
    for p in pts:
        while len(lo)>1 and cross2(lo[-2],lo[-1],p)<=1e-12:lo.pop()
        lo.append(p)
    hi=[]
    for p in reversed(pts):
        while len(hi)>1 and cross2(hi[-2],hi[-1],p)<=1e-12:hi.pop()
        hi.append(p)
    return len(lo)+len(hi)-2

def empirical(delta,n=20000,seed=2026):
    rng=random.Random(seed)
    W=((1.,0.),(-.5,math.sqrt(3)/2),(-.5,-math.sqrt(3)/2))
    V=[(p[0],p[1],delta) for p in W]
    count=0
    for _ in range(n):
        a,b,c=(rng.gauss(0,1) for i in range(3));norm=math.sqrt(a*a+b*b+c*c);u=(a/norm,b/norm,c/norm)
        # project onto orthonormal plane using e1 and u cross e1
        if abs(u[2]) <.9:
            e=(-u[1],u[0],0.)
        else:e=(0.,-u[2],u[1])
        t=math.sqrt(sum(x*x for x in e));e=tuple(x/t for x in e)
        f=(u[1]*e[2]-u[2]*e[1],u[2]*e[0]-u[0]*e[2],u[0]*e[1]-u[1]*e[0])
        pts=[(sum(v[i]*e[i] for i in range(3))*sgn,sum(v[i]*f[i] for i in range(3))*sgn) for v in V for sgn in (-1,1)]
        count+=(hull_size(pts)==6)
    return count/n

if __name__=='__main__':
    for d in (.08,.3,1/math.sqrt(2),1.,3.):
        theory=probability(d);obs=empirical(d)
        assert abs(theory-obs)<.019,(d,theory,obs)
        print('delta',d,'exact',theory,'empirical',obs)
    c=12*(math.sqrt(3)+3)/(math.pi*(3+2*math.sqrt(3)))
    for d in (.0001,.001):
        assert abs((1-probability(d))/d-c)<.001
    assert abs(probability(1/math.sqrt(2))-(4/math.pi)*math.atan(math.sqrt(2)/5))<1e-14
    print('VERIFY_OK',c)
