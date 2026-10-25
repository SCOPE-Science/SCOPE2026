#!/usr/bin/env python3
"""Independent numerical checks for the concentric-disk ball-illumination profile.

Python 3 standard library only. The radial integration checks the defining
intersection over enclosing disks, rather than relying on the arc-area formula.
"""
import math

PI = math.pi


def angles(R, r, t):
    assert 0 < r < R and r <= t <= 2*R-r
    k = R-r
    a = (t*t + k*k - R*R)/(2*t)
    h = math.sqrt(max(0., (k-a)*(k+a)))
    phi = math.atan2(h, -a)
    beta = math.atan2(h, t-a)
    return phi, beta


def excess(R, r, t):
    if t <= r: return 0.0
    assert t <= 2*R-r
    phi, beta = angles(R, r, t)
    delta = phi-beta
    return r*t*math.sin(phi) - r*r*phi + R*R*(delta-math.sin(delta))


def centres(R,r,t,N=250):
    k=R-r
    a=(t*t+k*k-R*R)/(2*t)
    A=math.acos(max(-1., min(1.,a/k)))
    for j in range(N+1):
        v=-A+2*A*j/N
        yield k*math.cos(v),k*math.sin(v)
    c=(k*k-t*t-R*R)/(2*t*R)
    B=math.acos(max(-1.,min(1.,c)))
    for j in range(1,N):
        v=B+(2*PI-2*B)*j/N
        yield t+R*math.cos(v),R*math.sin(v)


def numerical_excess(R,r,t,N=250):
    """Area by polar quadrature of the INTERSECTION of all enclosing R-disks.
    Centers sampled on both arcs of their lens, independently of proposed hull arcs.
    """
    cs=list(centres(R,r,t,N))
    sum_area=0.
    for j in range(N):
        v=2*PI*(j+.5)/N
        ux,uy=math.cos(v),math.sin(v)
        maxrad=1.e100
        for x,y in cs:
            proj=ux*x+uy*y
            q=R*R-x*x-y*y+proj*proj
            radius=proj+math.sqrt(max(0.,q))
            if radius<maxrad: maxrad=radius
        sum_area+=maxrad*maxrad
    return PI*sum_area/N-PI*r*r


def run():
    cases = [(2.,1.,1.3),(2.,1.,1.5),(2.,1.,2.3),
             (3.,1.,2.),(3.,1.,3.9),(1.5,1.,1.1)]
    for R,r,t in cases:
        ex=excess(R,r,t); num=numerical_excess(R,r,t)
        assert abs(ex-num)<0.011, (R,r,t,ex,num,ex-num)
        print('radial enclosure verified',R,r,t,'exact',round(ex,7),
              'independent quadrature',round(num,7),'difference',round(ex-num,7))
    for R,r in [(2.,1.),(3.,1.),(1.5,1.),(5.,2.)]:
        T=2*R-r
        xs=[r+(T-r)*i/200. for i in range(201)]
        ys=[excess(R,r,x) for x in xs]
        assert all(y2>y1 for y1,y2 in zip(ys[1:-1],ys[2:]))
        assert abs(ys[-1]-PI*(R*R-r*r))<1.e-10
        C0=(2*math.sqrt(2)/3)*math.sqrt(R*r/(R-r))
        C1=4*R*math.sqrt(2*R*(R-r)/T)
        a=excess(R,r,r+1.e-4)/(1.e-4**1.5)
        b=(PI*(R*R-r*r)-excess(R,r,T-1.e-4))/0.01
        assert abs(a/C0-1)<0.002,(R,r,a,C0)
        assert abs(b/C1-1)<0.002,(R,r,b,C1)
        print('endpoints verified',R,r,'small coeff',round(a,6),
              'limit',round(C0,6),'large coeff',round(b,6),'limit',round(C1,6))
    print('All independent numerical checks passed.')

if __name__=='__main__':run()
