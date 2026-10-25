#!/usr/bin/env python3
"""Numerical finite-sample cross-check, not an infinite mathematical proof.
Requires only the Python standard library. Run: python verify_halving.py
"""
import math

def polygon_area(points):
    return abs(sum(p[0]*q[1]-p[1]*q[0] for p,q in zip(points,points[1:]+points[:1])))*0.5 if len(points)>2 else 0.0

def clip(points,nx,ny,t):
    inside=[];hits=[]
    for p,q in zip(points,points[1:]+points[:1]):
        a=p[0]*nx+p[1]*ny-t
        b=q[0]*nx+q[1]*ny-t
        if a<=0: inside.append(p)
        if a*b<0:
            lam=a/(a-b)
            z=(p[0]+lam*(q[0]-p[0]),p[1]+lam*(q[1]-p[1]))
            inside.append(z);hits.append(z)
    return polygon_area(inside),hits

def test_n(n):
    vertices=[(math.cos(2*math.pi*j/n),math.sin(2*math.pi*j/n)) for j in range(n)]
    area=polygon_area(vertices)
    delta=math.pi/(2*n)
    worst=0.0
    for j in range(37):
        phi=delta*j/36
        nx,ny=math.cos(phi),math.sin(phi)
        lo,hi=-1.1,1.1
        for _ in range(90):
            mid=(lo+hi)*0.5
            if clip(vertices,nx,ny,mid)[0]<area*0.5: lo=mid
            else: hi=mid
        _,hits=clip(vertices,nx,ny,(lo+hi)*0.5)
        assert len(hits)==2,(n,j,hits)
        observed=math.hypot(hits[0][0]-hits[1][0],hits[0][1]-hits[1][1])
        expected=2*math.cos(delta)*math.sqrt(math.cos(2*delta))/math.sqrt(math.cos(phi)**2-math.tan(delta)**2*math.sin(phi)**2)
        worst=max(worst,abs(observed-expected))
    return worst

if __name__=='__main__':
    for n in (3,5,7,9,11,13,19,31,51):
        worst=test_n(n)
        print('n=',n,'max_abs_error=',format(worst,'.3g'))
        assert worst<4e-13
    print('All finite numerical comparisons passed; not a proof.')
