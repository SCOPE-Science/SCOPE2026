#!/usr/bin/env python3
"""Exact rational checks for a parallelogram equal-endpoint-distance radius theorem.
No external dependencies. The analytical proof, not this finite test, covers all shapes.
"""
from fractions import Fraction as Q
from math import sqrt

def dot(a,b): return a[0]*b[0]+a[1]*b[1]
def plus(a,b): return (a[0]+b[0], a[1]+b[1])
def minus(a,b): return (a[0]-b[0], a[1]-b[1])
def times(q,a): return (q*a[0], q*a[1])
def sq(a): return dot(a,a)

def bisector_boundary_reach_sq(a,b,poly):
    """Independent oracle: intersect a perpendicular bisector with polygon edges."""
    half=Q(1,2);mid=times(half,plus(a,b)); d=minus(b,a)
    hits=[]
    for i,p in enumerate(poly):
        z=poly[(i+1)%len(poly)]
        v=dot(minus(p,mid),d);w=dot(minus(z,mid),d)
        if v==0:hits.append(p)
        if w==0:hits.append(z)
        if v*w<0:
            t=-v/(w-v)
            hits.append(plus(p,times(t,minus(z,p))))
    assert hits
    return max(sq(minus(p,a)) for p in hits)

def predicted(x,y):
    # Vertices 0,(1,0),(1+x,y),(x,y) ; y>0 ; x,y rational.
    b2=x*x+y*y;q=abs(x)
    beta=min(Q(1),Q(1,2)/q) if q else Q(1)
    alpha=min(Q(1),b2/(2*q)) if q else Q(1)
    return Q(1,4)+y*y*beta*beta, b2/Q(4)+y*y/b2*alpha*alpha

count=0
for i in range(-25,26):
    for j in range(1,31):
        x=Q(i,10); y=Q(j,10)
        z=(Q(0),Q(0));u=(Q(1),Q(0));v=(x,y)
        poly=[z,u,plus(u,v),v]
        ru=bisector_boundary_reach_sq(z,u,poly)
        rv=bisector_boundary_reach_sq(z,v,poly)
        pu,pv=predicted(x,y)
        assert ru==pu and rv==pv,(x,y,ru,rv,pu,pv)
        b2=x*x+y*y
        possible=min(ru,rv)>=max(Q(1),b2)/4
        simple=abs(x)<=min(Q(1),b2)
        assert possible==simple,(x,y,possible,simple)
        count+=1
print('INDEPENDENT_EXACT_BISECTOR_INTERSECTION_AND_SHEAR_THRESHOLD_PASSED',count)

# Exact polynomial identity, attained by every rectangle scaled to the larger-side far reach.
for j in range(1,41):
    t=Q(j,40); ell2=Q(1,4)+t*t
    perimeter_sq=4*(1+t)**2
    right=Q(64,5)*ell2+Q(4,5)*(1-t)*(1+11*t)
    assert perimeter_sq==right
    # Under length ordering, the other side is able to witness this common radius.
    assert t*t/4+1>=ell2
print('SHARP_SIDE_DISPARITY_FAMILY_PASSED')

# Exact rhombic equality family and optimal quadratic angular deviation.
for j in range(0,30):
    c=Q(j,60)  # 0 <= c < 1/2, opposite-edge witness is nonvertex
    ell2=Q(5,4)-c*c
    perimeter_sq=Q(16)
    right=Q(64,5)*ell2+Q(64,5)*c*c
    assert perimeter_sq==right
    assert 2*c<1
print('SHARP_SHEAR_FAMILY_PASSED')

# Independent floating-point asymptotic order checks, not a proof of the exponents.
Pstar=8/sqrt(5)
rect=[];rhomb=[]
for eps in [1e-2,1e-3,1e-4,1e-5]:
    t=1-eps
    aa=1/sqrt(.25+t*t);bb=t*aa
    Pre=2*(aa+bb)
    rect.append((Pre-Pstar)/(aa-bb))
    c=eps
    ar=1/sqrt(1.25-c*c)
    Prh=4*ar
    rhomb.append((Prh-Pstar)/(c*c))
assert max(rect)-min(rect)<.05
assert max(rhomb)-min(rhomb)<.02
print('INDEPENDENT_NEAR_SQUARE_RATE_CHECKS_PASSED')

# Nonvertex endpoint convention: when the bisector reaches a vertex, the
# largest radius of that side is a missing endpoint, not an attainable strut.
for u,v,which in [((Q(1),Q(0)),(Q(1,2),Q(1)),0),
                  ((Q(1),Q(0)),(Q(1),Q(1)),1)]:
    z=(Q(0),Q(0));poly=[z,u,plus(u,v),v]
    endpoint=bisector_boundary_reach_sq(z,(u,v)[which],poly)
    a=(u,v)[which];mid=times(Q(1,2),a)
    d=a
    hits=[]
    for i,p in enumerate(poly):
        q=poly[(i+1)%4];s=dot(minus(p,mid),d);t=dot(minus(q,mid),d)
        if s==0:hits.append(p)
        if t==0:hits.append(q)
        if s*t<0:hits.append(plus(p,times(-s/(t-s),minus(q,p))))
    far=[h for h in hits if sq(minus(h,z))==endpoint]
    assert far and all(h in poly for h in far)
print('VERTEX_ONLY_TERMINAL_EXCLUSIONS_PASSED')

print('ALL_CHECKS_PASSED')
