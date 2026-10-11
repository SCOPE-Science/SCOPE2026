#!/usr/bin/env python3
import math

TOL = 3e-9

def dot(a,b):
    return a[0]*b[0]+a[1]*b[1]

def sub(a,b):
    return (a[0]-b[0],a[1]-b[1])

def add(a,b):
    return (a[0]+b[0],a[1]+b[1])

def mul(s,a):
    return (s*a[0],s*a[1])

def vertex(th):
    return (math.cos(th),math.sin(th))

def normal(th):
    return (math.cos(th),math.sin(th))

def det(a,b):
    return a[0]*b[1]-a[1]*b[0]

def line_intersection(n1,r1,n2,r2):
    D=det(n1,n2)
    if abs(D)<1e-14:
        return None
    return ((r1*n2[1]-n1[1]*r2)/D,
            (n1[0]*r2-r1*n2[0])/D)

def ratio_from_definition(N,t):
    a=math.pi/N
    c=math.cos(a)
    v0=vertex(0)
    v1=vertex(2*a)
    d=add(mul(1-t,v0),mul(t,v1))
    n=(-d[1],d[0])

    cons=[]
    for j in range(N):
        uj=normal((2*j+1)*a)
        cons.append((uj,c))
        cons.append((uj,c-dot(uj,d)))

    pts=[]
    for i in range(len(cons)):
        for j in range(i+1,len(cons)):
            p=line_intersection(cons[i][0],cons[i][1],cons[j][0],cons[j][1])
            if p is None:
                continue
            if all(dot(nn,p)<=rr+2e-10 for nn,rr in cons):
                pts.append(p)
    assert pts

    h=max(dot(n,vertex(2*j*a)) for j in range(N))
    return max(dot(n,p)/h for p in pts)

def closed_ratio(N):
    a=math.pi/N
    if N%12==10:
        th=math.pi/6+a/3
    elif N%12==2:
        th=math.pi/6-a/3
    else:
        raise ValueError(N)
    return 1/math.cos(th)-math.tan(th)/(2*math.cos(a))

def switch(N):
    a=math.pi/N
    if N%12==10:
        return ((math.cos(a)-2*math.sin(math.pi/6+a/3))/
                (math.cos(math.pi/3+5*a/3)-math.sin(math.pi/6+a/3)))
    else:
        return ((math.cos(a)-2*math.cos(math.pi/3+a/3))/
                (math.sin(math.pi/6+5*a/3)-math.cos(math.pi/3+a/3)))

tested=[10,14,22,26,34,38,46,50,58,62,70,74,94,98,118,122,190,194]
worst=0.0
for N in tested:
    R=closed_ratio(N)
    ts=[0.0,switch(N),0.5]
    ts += [k/40 for k in range(1,20)]
    vals=[ratio_from_definition(N,t) for t in ts]
    err=abs(max(vals)-R)
    worst=max(worst,err)
    assert err<TOL,(N,err,max(vals),R)
    assert all(v<=R+TOL for v in vals),(N,max(vals)-R)

m10=1-closed_ratio(10)
target=(7-3*math.sqrt(5))/2
assert abs(m10-target)<2e-14

ball=1-math.sqrt(3)/2
for N in (122,194):
    assert abs((1-closed_ratio(N))-ball)<0.002

print("VERIFY_OK")
print("tested_polygon_counts =", tested)
print("max_definition_formula_error = %.3e" % worst)
print("decagon_specialization = passed")
print("ball_limit_stress = passed")
