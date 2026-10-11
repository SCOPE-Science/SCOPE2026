#!/usr/bin/env python3
import math

def build(n,a,b=None):
    if b is None:
        b=a
    pts=[(0.0,0.0)]
    x=y=0.0
    edges=[]
    for i in range(n):
        l=a if (n%2 or i%2==0) else b
        th=2*math.pi*i/n
        e=(l*math.cos(th),l*math.sin(th))
        edges.append(e)
        x+=e[0]; y+=e[1]
        pts.append((x,y))
    return pts,edges

def cross(u,v):
    return u[0]*v[1]-u[1]*v[0]

def area(pts):
    return abs(sum(pts[i][0]*pts[i+1][1]-pts[i+1][0]*pts[i][1]
                   for i in range(len(pts)-1))/2)

def formula(n,a,b):
    t=math.pi/n
    return n/16*((a+b)**2/math.tan(t)-math.tan(t)*(a-b)**2)

worst_close=0.0
worst_area=0.0
worst_tri=0.0

for n in range(5,61):
    if n%2:
        cases=[(1.0,1.0),(2.3,2.3)]
    else:
        cases=[(1.0,1.0),(2.0,1.0),(1.25,3.5),(7/5,11/7)]
    for a,b in cases:
        pts,edges=build(n,a,b)
        close=math.hypot(pts[-1][0],pts[-1][1])
        worst_close=max(worst_close,close)
        assert close<2e-12,(n,a,b,close)

        tri=[0.5*cross(edges[i],edges[(i+1)%n]) for i in range(n)]
        spread=max(tri)-min(tri)
        worst_tri=max(worst_tri,spread)
        assert spread<2e-12,(n,a,b,spread)

        if n%2==0:
            err=abs(area(pts)-formula(n,a,b))
            worst_area=max(worst_area,err)
            assert err<3e-11,(n,a,b,area(pts),formula(n,a,b))

            m=n//2
            opp=max(abs(edges[i+m][0]+edges[i][0])+abs(edges[i+m][1]+edges[i][1])
                    for i in range(m))
            if n%4==0:
                assert opp<2e-12,(n,a,b,opp)
            elif abs(a-b)>1e-12:
                assert opp>1e-4,(n,a,b,opp)

# Exact fixed-perimeter deficit check numerically.
for n in range(6,62,2):
    a,b=2.75,0.8
    A=formula(n,a,b)
    c=(a+b)/2
    Areg=n/4*c*c/math.tan(math.pi/n)
    deficit=n/16*math.tan(math.pi/n)*(a-b)**2
    assert abs((Areg-A)-deficit)<2e-13

print("VERIFY_OK")
print("n_range = 5..60")
print("max_closure_error = %.3e" % worst_close)
print("max_triangle_area_spread = %.3e" % worst_tri)
print("max_shoelace_formula_error = %.3e" % worst_area)
print("central_symmetry_parity = passed")
