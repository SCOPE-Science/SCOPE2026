#!/usr/bin/env python3
"""Independent numerical and exact-rational checks for the octahedral projection law.

Proof of the law is analytic and separate; finite checks are consistency tests.
Requires only Python 3 standard library.
"""
from fractions import Fraction as Q
from itertools import product
from math import acos, atan2, hypot, isclose, pi, sqrt
from random import Random


def dot(p, q):
    return sum(x*y for x, y in zip(p, q))


def det(p, q, r):
    return (p[0]*(q[1]*r[2]-q[2]*r[1])
            -p[1]*(q[0]*r[2]-q[2]*r[0])
            +p[2]*(q[0]*r[1]-q[1]*r[0]))


def solid_angle(p, q, r):
    lp, lq, lr = sqrt(dot(p,p)), sqrt(dot(q,q)), sqrt(dot(r,r))
    den = (lp*lq*lr+dot(p,q)*lr+dot(q,r)*lp+dot(r,p)*lq)
    return 2*atan2(abs(det(p,q,r)), den)


def spherical_cdf(s):
    assert 0 <= s <= 1
    v1 = ((1,0,0),(1,s,0),(2,s,s))
    v2 = ((1,1,1-s),(1,1,1),(1+s,1,1))
    return 12/pi*(solid_angle(*v1)+solid_angle(*v2))


def explicit_cdf(s):
    alpha=sqrt(3-2*s+s*s)
    beta=sqrt(3+2*s+s*s)
    d1=(1+sqrt(1+s*s))*sqrt(4+2*s*s)+2+s*s+2*sqrt(1+s*s)
    d2=sqrt(3)*alpha*beta+(3-s)*beta+(3+s)*alpha+3*sqrt(3)
    return 24/pi*(atan2(s*s,d1)+atan2(s*s,d2))


def radius_squared_analytic(a,b,c):
    assert a >= b >= c >= 0 and a > 0
    return 2+(((b+c)/a)**2 if a >= b+c else ((a-c)/b)**2)


def radius_squared_exact(a,b,c):
    assert a >= b >= c >= 0 and a > 0
    candidates=[]
    v=(a,b,c)
    for free in range(3):
        rest=[j for j in range(3) if j != free]
        for sg1,sg2 in product((-1,1),repeat=2):
            f=Q(-(v[rest[0]]*sg1+v[rest[1]]*sg2),v[free]) if v[free] else None
            if f is not None and -1 <= f <= 1:
                x=[None]*3
                x[rest[0]],x[rest[1]],x[free]=Q(sg1),Q(sg2),f
                candidates.append(sum(t*t for t in x))
    return max(candidates)


def projected_inradius_direct(u):
    # Construct an orthonormal basis in the plane perpendicular to u.
    un=sqrt(dot(u,u))
    u=[a/un for a in u]
    d=hypot(u[0],u[1])
    if d < 1e-12:
        p=(1.,0.,0.)
    else:
        p=(-u[1]/d,u[0]/d,0.)
    q=(u[1]*p[2]-u[2]*p[1],u[2]*p[0]-u[0]*p[2],u[0]*p[1]-u[1]*p[0])
    v=[(sign*p[i],sign*q[i]) for i in range(3) for sign in (-1.,1.)]
    supports=[]
    for i in range(6):
        for j in range(i+1,6):
            dx,dy=v[j][0]-v[i][0],v[j][1]-v[i][1]
            length=hypot(dx,dy)
            if length < 1e-12:
                continue
            nx,ny=dy/length,-dx/length
            h=nx*v[i][0]+ny*v[i][1]
            side=[nx*x+ny*y-h for x,y in v]
            if max(side) < 1e-10 or min(side) > -1e-10:
                supports.append(abs(h))
    assert supports, 'Failed to determine convex hull supporting edges'
    return min(supports)


def main():
    count=0
    for a in range(1,19):
        for b in range(a+1):
            for c in range(b+1):
                # Equality of rational-square formulas, not decimal approximations.
                target=Q(2)+((Q(b+c,a)**2) if a>=b+c else (Q(a-c,b)**2))
                got=radius_squared_exact(a,b,c)
                assert got==target,(a,b,c,target,got)
                count+=1
    for k in range(11):
        s=Q(k,10)
        r1=((Q(1),Q(0),Q(0)),(Q(1),s,Q(0)),(Q(2),s,s))
        r2=((Q(1),Q(1),Q(1)-s),(Q(1),Q(1),Q(1)),(Q(1)+s,Q(1),Q(1)))
        assert det(*r1)==s*s
        assert abs(det(*r2))==s*s
    assert isclose(spherical_cdf(0),0,abs_tol=1e-14)
    assert isclose(spherical_cdf(1),1,abs_tol=1e-13)
    for i in range(1,101):
        assert spherical_cdf((i-1)/100) <= spherical_cdf(i/100)+1e-13
        assert abs(explicit_cdf(i/100)-spherical_cdf(i/100))<1e-13
    assert abs(spherical_cdf(.5)-.30377752525699947)<1e-14
    rng=Random(28514)
    for i in range(500):
        u=(rng.gauss(0,1),rng.gauss(0,1),rng.gauss(0,1))
        a,b,c=sorted(map(abs,u),reverse=True)
        expected=1/sqrt(radius_squared_analytic(a,b,c))
        actual=projected_inradius_direct(u)
        assert abs(expected-actual)<2e-11,(i,actual,expected)
    trial=80000
    sgrid=(.25,.5,.75)
    counts=[0]*len(sgrid)
    for i in range(trial):
        a,b,c=sorted([abs(rng.gauss(0,1)) for j in range(3)],reverse=True)
        s=(b+c)/a if a>=b+c else (a-c)/b
        for k,t in enumerate(sgrid):
            if s<=t:counts[k]+=1
    for k,t in enumerate(sgrid):
        assert abs(counts[k]/trial-spherical_cdf(t))<.014
    print('VERIFY_OK',count,'exact-rational cube sections;',
          '500 independently projected planar hulls;',trial,'Haar directions')


if __name__=='__main__':main()
