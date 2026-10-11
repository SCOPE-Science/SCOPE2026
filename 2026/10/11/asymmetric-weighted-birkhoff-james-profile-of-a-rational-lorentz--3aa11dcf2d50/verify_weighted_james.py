#!/usr/bin/env python3
"""Exact rational certificate for the weighted orthogonal James profile.

The exhaustive reduction is described in RESULT.md. Requires Python 3
standard library only. Tests every real weight, not a finite parameter grid:
the feasible-status partition is cut at every exact algebraic breakpoint.
"""
from fractions import Fraction as F
from math import isqrt

Z = F(0)
H = F(1,2)
K = F(3,4)
R = F(2,3)

def dot(a,b):
    return a[0]*b[0]+a[1]*b[1]

def add(a,b):
    return tuple(a[i]+b[i] for i in range(2))

def sub(a,b):
    return tuple(a[i]-b[i] for i in range(2))

def lin(c0,c1):
    return (c0,c1)

def trim(c):
    c = list(c)
    while len(c)>1 and c[-1]==0:
        c.pop()
    return tuple(c)

def mul(u,v):
    c=[Z]*(len(u)+len(v)-1)
    for i,a in enumerate(u):
        for j,b in enumerate(v):
            c[i+j]+=a*b
    return trim(c)

def poly_sub(u,v):
    m=max(len(u),len(v))
    return trim(tuple((u[i] if i<len(u) else Z)-(v[i] if i<len(v) else Z) for i in range(m)))

def sqrt_rational(q):
    if q<0:
        return None
    n,d=isqrt(q.numerator),isqrt(q.denominator)
    if n*n==q.numerator and d*d==q.denominator:
        return F(n,d)
    raise AssertionError('Unexpected irrational critical root; exact isolation required')

def roots(p):
    p=trim(p)
    if len(p)==1: return ()
    if len(p)==2:
        return (-p[0]/p[1],)
    assert len(p)==3
    a,b,c=p[2],p[1],p[0]
    disc=b*b-4*a*c
    if disc<0:return ()
    rad=sqrt_rational(disc)
    return ((-b-rad)/(2*a),(-b+rad)/(2*a))

def val(p,a):
    v=Z
    for c in reversed(p):v=v*a+c
    return v

def feasible_at(a,p0,p1,q0,q1):
    p0,p1,q0,q1=(val(z,a) for z in (p0,p1,q0,q1))
    def both(u):
        p=p0+(p1-p0)*u
        q=q0+(q1-q0)*u
        return min(p,q)>0
    if both(Z) or both(F(1)):
        return True
    d=(p1-p0)-(q1-q0)
    if d:
        u=(q0-p0)/d
        if Z<u<F(1) and both(u):
            return True
    return False

FACETS=[(F(1),Z),(-F(1),Z),(Z,F(1)),(Z,-F(1))]
FACETS.extend((i*R,j*R) for i in (F(1),-F(1)) for j in (F(1),-F(1)))

# Endpoint pairs ((x(0),x(1)),(y(0),y(1))). Each path is affine in u.
CASES=[
    (((F(1),Z),(F(1),H)),((Z,F(1)),(Z,F(1)))),
    (((F(1),H),(K,K)),((-K,K),(-K,K))),
    (((F(1),H),(F(1),H)),((Z,F(1)),(-H,F(1)))),
    (((F(1),H),(F(1),H)),((-H,F(1)),(-K,K))),
]

BRANCHES=[
    (F(0),F(3,8),(F(1),-R)),
    (F(3,8),F(7,12),(K,Z)),
    (F(7,12),F(1),(F(2,5),F(3,5))),
]

def facet_polynomial(f,x,y,sign,profile):
    # dot(f,a*x+(1-a)*sign*y)-profile(a)
    # Coefficients of a^0 and a^1, with rational exact arithmetic.
    y=tuple(sign*z for z in y)
    return (dot(f,y)-profile[0],dot(f,sub(x,y))-profile[1])

def check_upper():
    checks=0
    polynomials=0
    for (cx,cy) in CASES:
        for lo,hi,profile in BRANCHES:
            for f in FACETS:
                p0=facet_polynomial(f,cx[0],cy[0],F(1),profile)
                p1=facet_polynomial(f,cx[1],cy[1],F(1),profile)
                for g in FACETS:
                    q0=facet_polynomial(g,cx[0],cy[0],F(-1),profile)
                    q1=facet_polynomial(g,cx[1],cy[1],F(-1),profile)
                    det=poly_sub(mul(p0,q1),mul(p1,q0))
                    # All possible feasibility changes are roots of these
                    # endpoint inequalities and their 2x2 determinant.
                    critical={lo,hi}
                    for pol in (p0,p1,q0,q1,det):
                        polynomials+=1
                        for r in roots(pol):
                            if lo<r<hi:critical.add(r)
                    critical=sorted(critical)
                    witnesses=set(critical)
                    for l,r in zip(critical,critical[1:]):
                        witnesses.add((l+r)/2)
                    for a in witnesses:
                        checks+=1
                        assert not feasible_at(a,p0,p1,q0,q1), (
                            'UNBOUNDED', cx,cy,lo,hi,f,g,a)
    return checks,polynomials

def norm(x):
    return max(abs(x[0]),abs(x[1]),R*(abs(x[0])+abs(x[1])))

def check_lower():
    # Three exact lower-bound families. The displayed facets attain each
    # branch as a lower bound for both weighted signs, at all a in [0,1].
    witnesses=[((F(1),H),(-H,F(1)),(F(1),-R)),
               ((K,K),(-K,K),(K,Z)),
               ((F(1),H),(-F(2,5),F(1)),(F(2,5),F(3,5)))]
    supports=[((Z,F(1)),(R,-R)),((Z,F(1)),(F(1),Z)),((R,R),(F(1),Z))]
    for (x,y,profile),(fp,fq) in zip(witnesses,supports):
        assert norm(x)==norm(y)==1
        # For x corner (1,1/2): two active supporting normals span a cone
        # whose zero values are achieved for either witness y.
        # For x=(3/4,3/4): the diagonal supporting normal annihilates y.
        if x==(K,K):assert y[0]+y[1]==0
        else:assert y[0]<=0<=y[0]+y[1]
        for a in (F(0),F(1)):
            z1=add(tuple(a*q for q in x),tuple((1-a)*q for q in y))
            z2=sub(tuple(a*q for q in x),tuple((1-a)*q for q in y))
            target=profile[0]+profile[1]*a
            assert dot(fp,z1)>=target and dot(fq,z2)>=target, (
                'LOWER_FAIL',x,y,a)
    assert K-(F(2,5)+F(3,5)*F(5,8)) == -F(1,40)
    return len(witnesses)

if __name__=='__main__':
    a,b=check_upper()
    c=check_lower()
    print('WEIGHTED_JAMES_OCTAGON_ALL_PARAMETERS_EXACT_OK',
          'test_points=',a,'critical_polynomials=',b,'lower_families=',c)
