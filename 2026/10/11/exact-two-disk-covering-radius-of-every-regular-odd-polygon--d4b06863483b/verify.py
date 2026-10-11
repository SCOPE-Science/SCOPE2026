#!/usr/bin/env python3
"""Standalone reproducibility checks for the regular odd-polygon two-disk theorem."""
import math
import sympy as sp

t=sp.symbols('t', positive=True)
s=sp.sin(t)
c=sp.cos(t)
q=sp.cos(2*t)/c
assert sp.simplify(sp.trigsimp(c*c-(s*s+q*q)-sp.cos(2*t)*sp.tan(t)**2))==0
assert sp.simplify(sp.trigsimp(sp.sin(sp.pi/2-t)-sp.cos(t)))==0
assert sp.simplify(sp.trigsimp(sp.cos(t)**2+sp.sin(t)**2-1))==0

worst=0.0
checks=0
for n in range(3,202,2):
    tt=math.pi/(2*n)
    ss=math.sin(tt)
    rr=math.cos(tt)
    cuts=[(0.0,math.cos(2*tt)/rr),(0.0,-math.cos(2*tt)/rr)]
    vs=[(math.cos(2*math.pi*k/n),math.sin(2*math.pi*k/n)) for k in range(n)]
    def d2(v,x): return (v[0]-x)**2+v[1]**2
    for x,y in vs:
        center=ss if x>=0 else -ss
        err=d2((x,y),center)-rr**2
        worst=max(worst,err)
        assert err<5e-13,(n,x,y,err)
        assert abs(x)>=ss-5e-13
        checks+=1
    for pt in cuts:
        for center in [-ss,ss]:
            err=d2(pt,center)-rr**2
            worst=max(worst,err)
            assert err<5e-13,(n,pt,center,err)
            checks+=1
    # Independently find intersections of polygon sides with the axis x=0.
    inter=[]
    for j in range(n):
        x0,y0=vs[j]; x1,y1=vs[(j+1)%n]
        if x0*x1<0:
            lam=-x0/(x1-x0)
            inter.append(y0+lam*(y1-y0))
    assert len(inter)==2
    assert abs(max(inter)-cuts[0][1])<1e-12
    assert abs(min(inter)-cuts[1][1])<1e-12
    # Sample segments of the clipped half-polygons, not only original vertices.
    for j in range(n):
        v0=vs[j];v1=vs[(j+1)%n]
        for k in range(101):
            lam=k/100
            x=(1-lam)*v0[0]+lam*v1[0]
            y=(1-lam)*v0[1]+lam*v1[1]
            center=ss if x>=0 else -ss
            err=d2((x,y),center)-rr**2
            worst=max(worst,err)
            assert err<1e-12,(n,j,k,err)
            checks+=1
    # Algebraic chord endpoint verification and majority center circle radius.
    major=(n+1)//2
    x0,y0=vs[0]; x1,y1=vs[major-1]
    chord=math.hypot(x1-x0,y1-y0)
    mx,my=(x0+x1)/2,(y0+y1)/2
    assert abs(chord-2*rr)<1e-12
    assert abs(math.hypot(mx,my)-ss)<1e-12

print('VERIFY_OK')
print('odd_orders=3..201')
print('point_checks='+str(checks))
print('maximum_positive_squared_distance_defect='+format(worst,'.3e'))
print('symbolic_identities=passed')
