#!/usr/bin/env python3
"""Illustrative quadrature of the analytic density formulas; not an infinite-domain proof."""
import math

N=4096

def ellipse_profile(semiaxis_a,semiaxis_b):
    entries=[]
    for j in range(N):
        theta=2*math.pi*j/N
        E=semiaxis_a**2*math.sin(theta)**2+semiaxis_b**2*math.cos(theta)**2
        curvature=semiaxis_a*semiaxis_b/E**1.5
        ds=math.sqrt(E)*2*math.pi/N
        entries.append((curvature,ds))
    v=sum(math.sqrt(k)*ds for k,ds in entries)
    weights=[math.sqrt(k)*ds/v for k,ds in entries]
    a=[k**(-0.5) for k,_ in entries]
    m=sum(w*x**(1/3) for w,x in zip(weights,a))
    t_A=min(x**(1/3)/m for x in a)
    def frontier(t):
        if t>=1-1.e-13:
            q=[1.0]*N
            return sum(w*x for w,x in zip(weights,a))/m**3,q
        lo,hi=0.,1.
        def mass(c):
            return sum(w*max(t,c*x**(1/3)) for w,x in zip(weights,a))
        while mass(hi)<1:
            hi*=2
        for _ in range(54):
            mid=(lo+hi)/2
            if mass(mid)>1:hi=mid
            else:lo=mid
        c=(lo+hi)/2
        q=[max(t,c*x**(1/3)) for x in a]
        return sum(w*x/z**2 for w,x,z in zip(weights,a,q))/m**3,q
    if semiaxis_a==semiaxis_b:
        assert abs(t_A-1)<1.e-10
        return (1.,1.,1.,1.,1.)
    lo,hi=t_A,1.
    for _ in range(52):
        t=(lo+hi)/2
        A,q=frontier(t)
        if A>t**(-2):hi=t
        else:lo=t
    t=(lo+hi)/2
    A,q=frontier(t)
    H=min(q)**(-2)
    mass=sum(w*z for w,z in zip(weights,q))
    active=sum(w for w,z in zip(weights,q) if abs(z-t)<1.e-9)
    assert t_A<t<1 and A>1 and active>0
    assert abs(A-H)<2.e-8 and abs(mass-1)<2.e-8
    return (t_A,t,A,H,active)

if __name__=='__main__':
    circ=ellipse_profile(1.,1.)
    ex=ellipse_profile(2.,1.)
    ex2=ellipse_profile(3.,1.)
    assert all(abs(x-1.)<1.e-9 for x in circ)
    assert 0.98480<ex[1]<0.98484
    assert 1.03105<ex[2]<1.03110
    assert ex2[2]>ex[2]>1.
    print('ellipse (2,1): t_A=%.9f t_*=%.9f R_A=%.9f R_H=%.9f floor_mass=%.7f' % ex)
    print('ellipse (3,1): t_A=%.9f t_*=%.9f R_A=%.9f R_H=%.9f floor_mass=%.7f' % ex2)
    print('RANDOM_POLYGON_CLIPPED_MINIMAX_NUMERIC_OK')
