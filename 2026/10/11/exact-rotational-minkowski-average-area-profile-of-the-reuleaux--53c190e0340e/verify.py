#!/usr/bin/env python3
"""Standalone symbolic and direct-geometric checks for the rotated Reuleaux mean area."""
import math
import sympy as sp

z,x=sp.symbols('z x', real=True)
F=(2*sp.pi-3*z-sp.sqrt(3)+3*sp.sin(z)-sp.sqrt(3)*sp.cos(z))/4
D=sp.pi/4-F.subs(z,x/3)
S=sp.pi*(sp.sqrt(3)*sp.cos(x/3)-3*sp.sin(x/3))/36
assert sp.simplify(sp.diff(D,x,2)+S/sp.pi)==0
assert sp.simplify(F.subs(z,0)-(sp.pi-sp.sqrt(3))/2)==0
assert sp.simplify(F.subs(z,sp.pi/3)-sp.pi/4)==0
assert sp.simplify(sp.diff(D,x).subs(x,0))==0
assert sp.trigsimp(F+F.subs(z,sp.pi/3-z)-(3*sp.pi-2*sp.sqrt(3))/4)==0
slope=sp.diff(F,z)
assert sp.trigsimp(slope-(2*sp.sqrt(3)*sp.cos(z-sp.pi/6)-3)/4)==0
assert sp.simplify(slope.subs(z,sp.pi/6)-(2*sp.sqrt(3)-3)/4)==0

# This is the cosine series of S. Direct exact coefficients verify the
# parity cancellation; the proof in RESULT.md gives the general formula.
assert sp.simplify(sp.integrate(S,(x,0,sp.pi)))==0
for k in range(1,10):
    coefficient=sp.simplify(2/sp.pi*sp.integrate(S*sp.cos(k*x),(x,0,sp.pi)))
    target=sp.Rational(1,9*k*k-1) if k%2 else sp.Integer(0)
    assert sp.simplify(coefficient-target)==0,(k,coefficient,target)

# Uniform tail control for the infinite Fourier series: the omitted
# terms decay as O(N^-3). Finite checks here only confirm implementation.
for angle in [0.0,0.04,0.16,0.39,math.pi/6,0.87,math.pi/3]:
    v=math.pi/4-math.fsum((1+math.cos(k*3*angle))/(math.pi*k*k*(9*k*k-1)) for k in range(1,20001,2))
    target=float(F.subs(z,angle).evalf(17))
    assert abs(v-target)<3e-12, (angle,v,target)

# Independent geometry: sample the actual exposed boundary points.
# Each of the three circular arcs has radius one and subtends pi/3.
vertices=[(math.cos(2*math.pi*j/3)/math.sqrt(3),
           math.sin(2*math.pi*j/3)/math.sqrt(3)) for j in range(3)]
def exposed(a):
    u=(math.cos(a),math.sin(a))
    candidates=list(vertices)
    for j,(cx,cy) in enumerate(vertices):
        arc_mid=math.pi+2*math.pi*j/3
        diff=(a-arc_mid+math.pi)%(2*math.pi)-math.pi
        if abs(diff)<=math.pi/6:
            candidates.append((cx+u[0],cy+u[1]))
    return max(candidates,key=lambda p:p[0]*u[0]+p[1]*u[1])
def estimate_area(angle,N=7000):
    points=[]
    c=math.cos(angle); s=math.sin(angle)
    for j in range(N):
        th=2*math.pi*j/N
        a=exposed(th)
        b=exposed(th-angle)
        rb=(c*b[0]-s*b[1],s*b[0]+c*b[1])
        points.append(((a[0]+rb[0])/2,(a[1]+rb[1])/2))
    doubled=0.0
    for p,q in zip(points,points[1:]+points[:1]):
        doubled+=p[0]*q[1]-p[1]*q[0]
    return abs(doubled)/2
max_err=0.0
for angle in [0.0,0.1,0.3,0.6,math.pi/3]:
    v=estimate_area(angle)
    target=float(F.subs(z,angle).evalf(17))
    err=abs(v-target)
    max_err=max(max_err,err)
    assert err<1.5e-6,(angle,v,target,err)
print('VERIFY_OK')
print('symbolic_second_derivative_endpoint_complement = PASS')
print('exact_cosine_coefficients_through_degree_9 = PASS')
print('series_vs_formula_at_7_angles = PASS')
print('direct_arc_support_areas_at_5_angles = PASS')
print('maximum_polygonal_sampling_error =',format(max_err,'.10g'))
