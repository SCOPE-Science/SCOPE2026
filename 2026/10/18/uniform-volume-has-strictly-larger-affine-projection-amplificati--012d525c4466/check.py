#!/usr/bin/env python3
"""Finite independent consistency checks for affine volume/cone stability formulas.

This is a numerical and exact-formula companion; the universal comparison is
proved analytically in RESULT.md.
"""
from math import pi, sqrt, asin, cos, sin, isclose

checks = 0

def near(a, b, tol=5e-8):
    global checks
    checks += 1
    assert abs(a-b) <= tol * (1 + abs(a) + abs(b)), (a,b)

def positive(x):
    global checks
    checks += 1
    assert x > 0, x

def simpson(fun, left, right, steps=4000):
    assert steps % 2 == 0
    h = (right-left)/steps
    s = fun(left)+fun(right)
    for k in range(1, steps):
        s += (4 if k % 2 else 2)*fun(left+k*h)
    return h*s/3

def G(d, s):
    if s <= d/(d+2):
        return 0.0
    return (d+2)*s/(d+1)-1+(d/((d+2)*s))**d/(d+1)

# The conditional positive-part identity is independently integrated.
for d in (1,2,3,5,11):
    a = (d+2)/d
    cut = d/(d+2)
    for s in (0,cut/2,cut,cut*1.01,1,2,5):
        direct = simpson(lambda r:d*r**(d-1)*max(a*s*r-1,0),0,1,24000)
        near(direct,G(d,s),2e-8)
        positive(1+max(0,G(d,s)-max(0,s-1)))
        assert G(d,s)+1e-12 >= max(0,s-1)

# On an interval the cone law is uniform on the endpoints and the
# volume law is uniform interior; affine projector norms are 1 and 5/3.
near((abs(1+1)+abs(1-1))/2, 1)
near(simpson(lambda y:abs(1+3*y)/2,-1,1,24000), 5/3)

# The Euclidean disk has angular-uniform cone measure, radius density 2r.
N_cone = 1/3 + 2*sqrt(3)/pi
N_area = 11*sqrt(15)/(8*pi) + 2*asin(1/4)/pi
ang = simpson(lambda th:abs(1+2*cos(th))/(2*pi),0,2*pi,24000)
cutoff=-asin(1/4)
radial = sum(simpson(lambda th:abs(1+4*sin(th))*2/pi*cos(th)**2,a,b,12000)
             for a,b in ((-pi/2,cutoff),(cutoff,pi/2)))
near(ang,N_cone,2e-8)
near(radial,N_area,2e-8)
positive(N_area-N_cone)

# Independent perimeter and interior radial-kernel quadrature for regular
# polygons, including the non-centrally-symmetric triangle.
for n in (3,4,5,6,7,8,12,19):
    angle = 2*pi/n
    v = [(cos(j*angle),sin(j*angle)) for j in range(n)]
    cov = (2+cos(angle))/6
    ss = []
    for j in range(n):
        p,q = v[j],v[(j+1)%n]
        for k in range(1200):
            t = (k+0.5)/1200
            z0 = (1-t)*p[0]+t*q[0]
            ss.append(z0/cov)
    Lc = sum(abs(1+s) for s in ss)/len(ss)
    Lv = sum(1+2*G(2,max(0,-s)) for s in ss)/len(ss)
    near(Lv-Lc, 2*sum(G(2,max(0,-s))-max(0,-s-1) for s in ss)/len(ss), 3e-8)
    positive(Lv-Lc)
print(f"PASS: {checks} analytical-formula consistency assertions")
