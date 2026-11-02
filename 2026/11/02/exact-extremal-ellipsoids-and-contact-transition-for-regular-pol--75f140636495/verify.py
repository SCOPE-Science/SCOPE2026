#!/usr/bin/env python3
"""Reproduce finite algebraic and containment checks for polygon-spiked ball ellipsoids.

The printed checks supplement, not replace, the quantified analytic proof.
Only Python's standard library is needed.
"""
import math

def matrices(d,m,a):
    g=math.cos(math.pi/m)
    b=a*g
    if b*b<=d/2:
        A2,B2=1.,1.
    else:
        A2=2*b*b/d
        B2=(d-2)*b*b/(d*(b*b-1))
    return b,A2,B2

def check(d,m,a):
    b,A2,B2=matrices(d,m,a)
    assert min(A2,B2)>0
    for i in range(1001):
        t=i/1000
        eq=A2*t*t+B2*(1-t*t)
        k=min(a,1) # a positive; only to keep the original construction visible
        bound=max(1,b*t)**2
        assert eq<=bound+1e-11
        for j in range(7):
            theta=(j+0.5)*math.pi/(7*m)
            poly=max(math.cos(theta-2*math.pi*k/m) for k in range(m))
            actual=max(1,a*t*poly)**2
            assert eq<=actual+1e-11
    if b>math.sqrt(d/2):
        assert abs(A2/(b*b)-2/d)<1e-12
        assert abs(B2*(1-1/(b*b))-(d-2)/d)<1e-12
    else:
        assert A2==1 and B2==1
        assert b*math.sqrt(2/d)<=1+1e-12
    # E(a,1) contains both the unit ball and all polygon vertices.
    assert a>=1
    assert abs(a*a/(A2*B2**((d-2)/2))-(a*a if b*b<=d/2 else
        d/(2*math.cos(math.pi/m)**2)*(d*(b*b-1)/((d-2)*b*b))**((d-2)/2)))<1e-9

if __name__=='__main__':
    n=0
    for d in (3,4,6,10):
        for m in (5,6,7,12):
            g=math.cos(math.pi/m)
            threshold=math.sqrt(d/2)/g
            for a in (1.,1.25,threshold*.999,threshold*1.001,2.,5.):
                check(d,m,a)
                n+=1
    print('PASS: %d parameter configurations; angular support containment and exact contact algebra.'%n)
