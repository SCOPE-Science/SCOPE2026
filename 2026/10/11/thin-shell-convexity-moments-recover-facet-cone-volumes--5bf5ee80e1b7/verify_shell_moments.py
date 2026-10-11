#!/usr/bin/env python3
"""Deterministic finite diagnostics for visibility in planar homothetic shells.

The exact limiting theorem is proved analytically; these tests are finite checks.
Standard-library Python 3 only.
"""
from __future__ import annotations

import math
import random


def cross(a,b):
    return a[0]*b[1]-a[1]*b[0]


def polygon_weights(v):
    # Convex, counterclockwise, and with origin strictly inside.
    z=[cross(v[i],v[(i+1)%len(v)]) for i in range(len(v))]
    assert min(z)>0
    s=sum(z)
    return [e/s for e in z]


def sample_shell(v,weights,t,rng):
    u=rng.random(); e=0
    while e<len(weights)-1 and u>=weights[e]:
        u-=weights[e]; e+=1
    a,b=v[e],v[(e+1)%len(v)]
    s=rng.random()
    y=(a[0]*(1-s)+b[0]*s,a[1]*(1-s)+b[1]*s)
    r=math.sqrt(t*t+(1-t*t)*rng.random())
    return (r*y[0],r*y[1]),e


def segment_hits_inner_interior(x,y,v,t):
    # Clip the segment to convex polygon tP using determinant inequalities.
    lo,hi=0.,1.
    for i,a in enumerate(v):
        b=v[(i+1)%len(v)]
        edge=(b[0]-a[0],b[1]-a[1])
        ax=(x[0]-t*a[0],x[1]-t*a[1])
        dy=(y[0]-x[0],y[1]-x[1])
        c=cross(edge,ax); m=cross(edge,dy)
        if abs(m)<1.e-13:
            if c < -1.e-13: return False
        elif m>0:
            lo=max(lo,-c/m)
        else:
            hi=min(hi,-c/m)
        if lo>hi: return False
    if hi-lo<1.e-12: return False
    z=(x[0]+0.5*(lo+hi)*(y[0]-x[0]),
       x[1]+0.5*(lo+hi)*(y[1]-x[1]))
    return all(cross((v[(i+1)%len(v)][0]-v[i][0],
                      v[(i+1)%len(v)][1]-v[i][1]),
                     (z[0]-t*v[i][0],z[1]-t*v[i][1]))>1.e-13
               for i in range(len(v)))


def diagnostic(v,t,seed,N=45000):
    rng=random.Random(seed)
    w=polygon_weights(v)
    visible=0; same=0
    for _ in range(N):
        x,ex=sample_shell(v,w,t,rng)
        y,ey=sample_shell(v,w,t,rng)
        s=ex==ey
        same+=s
        hit=segment_hits_inner_interior(x,y,v,t)
        if s:
            assert not hit, 'Same-facet chord unexpectedly enters the inner homothet'
        visible+=not hit
    target=sum(p*p for p in w)
    obs=visible/N
    assert same<=visible
    assert abs(same/N-target)<0.015
    return target,same/N,obs


def main():
    examples=[
      ('square',[(-1.,-1.),(1.,-1.),(1.,1.),(-1.,1.)]),
      ('triangle',[ (2.,0.),(-1.,2.),(-1.,-2.)]),
      ('offcenter-triangle',[ (2.2,0.3),(-0.8,2.3),(-0.8,-1.7)]),
    ]
    for idx,(name,v) in enumerate(examples):
        for t in (0.92,0.98,0.997):
            target,same,obs=diagnostic(v,t,123000+idx*100+int(1000*t))
            # The finite-thickness value can only exceed the same-facet probability.
            assert obs>=same-1.e-10
            print(f'{name} t={t:.3f} limit={target:.6f} same={same:.6f} visible={obs:.6f}')
    print('VERIFY_OK')

if __name__=='__main__':
    main()
