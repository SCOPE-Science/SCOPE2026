#!/usr/bin/env python3
import math
import sympy as sp

t = sp.symbols("t", real=True)
ax, ay, bx, by = sp.symbols("ax ay bx by", real=True)
f = (ax+t*bx)**2 + (ay+t*by)**2
assert sp.expand(sp.diff(f,t) - (2*(ax*bx+ay*by) + 2*t*(bx*bx+by*by))) == 0

def dot(a,b):
    return a[0]*b[0] + a[1]*b[1]

def norm2(a):
    return dot(a,a)

def sub(a,b):
    return (a[0]-b[0], a[1]-b[1])

def add(a,b):
    return (a[0]+b[0], a[1]+b[1])

def mul(s,a):
    return (s*a[0],s*a[1])

def edge_roots(P,A,B,r):
    d=sub(B,A)
    x=sub(A,P)
    aa=norm2(d)
    bb=2*dot(x,d)
    cc=norm2(x)-r*r
    disc=bb*bb-4*aa*cc
    if disc < -1e-11:
        return []
    if disc < 0:
        disc=0.0
    sq=math.sqrt(disc)
    vals=[(-bb-sq)/(2*aa),(-bb+sq)/(2*aa)]
    out=[]
    for u in vals:
        if -1e-10 <= u <= 1+1e-10:
            u=min(1.0,max(0.0,u))
            p=add(A,mul(u,d))
            if not any(norm2(sub(p,q))<1e-16 for q in out):
                out.append(p)
    return out

def count_boundary(P,V,r):
    pts=[]
    for i in range(4):
        for q in edge_roots(P,V[i],V[(i+1)%4],r):
            if not any(norm2(sub(q,z))<1e-14 for z in pts):
                pts.append(q)
    return len(pts)

cases=[
    ((3.0,0.0),(1.0,2.0)),   # acute
    ((4.0,0.0),(0.0,1.0)),   # rectangle
    ((5.0,0.0),(0.2,2.5)),   # strongly anisotropic acute
    ((1.0,0.0),(3.0,0.2)),   # thin acute
]
for a,b in cases:
    assert dot(a,b) >= -1e-14
    P=(0.0,0.0)
    V=[P,a,add(a,b),b]

    # Collect all radii at which combinatorics can change:
    # vertex distances and perpendicular distances to edge interiors.
    crit={0.0}
    for A in V:
        crit.add(math.sqrt(norm2(sub(A,P))))
    for i in range(4):
        A,B=V[i],V[(i+1)%4]
        d=sub(B,A)
        u=-dot(sub(A,P),d)/norm2(d)
        if 0 < u < 1:
            q=add(A,mul(u,d))
            crit.add(math.sqrt(norm2(sub(q,P))))
    crit=sorted(crit)

    sample=[]
    for x,y in zip(crit,crit[1:]):
        if y-x>1e-9:
            sample.append((x+y)/2)
    sample.extend(crit)
    for r in sample:
        assert count_boundary(P,V,r) <= 2, (a,b,r,count_boundary(P,V,r))

print("VERIFY_OK")
print("symbolic_derivative = exact")
print("critical_radius_sweeps = passed")
