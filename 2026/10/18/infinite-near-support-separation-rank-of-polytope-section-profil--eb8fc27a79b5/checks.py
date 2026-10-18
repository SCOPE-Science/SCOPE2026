"""Exact-rational checks for a polytope section-spline knot argument.

All calculations use the standard library and exact Fraction arithmetic.
"""
from fractions import Fraction as F
from itertools import combinations
from math import factorial


def dot(a,b):
    return sum((x*y for x,y in zip(a,b)),F(0))


def section_coeffs(vertices,triangulation,volumes,theta):
    d=len(theta)
    projected={v:dot(theta,v) for v in vertices}
    if len(set(projected.values()))!=len(vertices):
        raise ValueError('non-generic projected vertices')
    coefs={v:F(0) for v in vertices}
    for simplex,vol in zip(triangulation,volumes):
        for v in simplex:
            denom=F(1)
            for z in simplex:
                if z!=v:
                    denom*=projected[z]-projected[v]
            coefs[v]+=d*vol/denom
    return projected,coefs


def density(projections,coefs,t,d):
    return sum((c*max(F(0),t-projections[v])**(d-1) for v,c in coefs.items()),F(0))


def moments(projections,coefs,d):
    bounds=sorted(projections.values())
    z0=z1=F(0)
    for lo,hi in zip(bounds[:-1],bounds[1:]):
        for v,c in coefs.items():
            q=projections[v]
            if q>=hi:continue
            aa=max(F(0),lo-q);bb=hi-q
            z0+=c*(bb**d-aa**d)/d
            z1+=c*((bb**(d+1)-aa**(d+1))/(d+1)+q*(bb**d-aa**d)/d)
    return z0,z1


a,b,c,e=(F(0),F(0)),(F(1),F(0)),(F(1),F(1)),(F(0),F(1))
T=[(a,b,c),(a,c,e)]
V=[F(1,2),F(1,2)]
thetas=[(F(99,101),F(20,101)),(F(24,25),F(7,25)),(F(15,17),F(8,17))]
knots=[]
for theta in thetas:
    assert dot(theta,theta)==1
    pr,co=section_coeffs([a,b,c,e],T,V,theta)
    aa,bb=theta
    assert aa>bb>0
    assert co[b]==-1/(aa*bb)
    for t in [F(0),bb/2,bb,(aa+bb)/2,aa,aa+bb/2,aa+bb,(aa+bb)*2]:
        f = t/(aa*bb) if 0<t<bb else (F(1)/aa if bb<=t<=aa else ((aa+bb-t)/(aa*bb) if aa<t<aa+bb else F(0)))
        assert density(pr,co,t,2)==f,(theta,t,density(pr,co,t,2),f)
    assert moments(pr,co,2)==(F(1),(aa+bb)/2)
    assert F(17,20)<pr[b]<F(103,100) and pr[e]<F(17,20) and pr[c]>F(103,100)
    knots.append(pr[b])
assert len(set(knots))==len(knots)

v0=(F(0),F(0),F(0));v1=(F(1),F(0),F(0));v2=(F(0),F(1),F(0));v3=(F(0),F(0),F(1))
th=(F(36,49),F(24,49),F(23,49))
assert dot(th,th)==1
pr,co=section_coeffs([v0,v1,v2,v3],[(v0,v1,v2,v3)],[F(1,6)],th)
assert moments(pr,co,3)==(F(1,6),sum(th,F(0))/24)
assert len([z for z in co.values() if z!=0])==4
print('PASS exact two-dimensional square densities, knot coefficients, common interval, and third-dimensional tetrahedron moment integrals')
