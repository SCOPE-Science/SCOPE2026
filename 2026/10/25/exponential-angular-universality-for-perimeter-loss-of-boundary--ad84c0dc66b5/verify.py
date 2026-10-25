#!/usr/bin/env python3
"""Arithmetic checks for polygon-boundary sampling perimeter identities."""
import math
import random
from bisect import bisect_right


def polygon_perimeter(points):
    return sum(math.dist(points[i], points[(i + 1) % len(points)]) for i in range(len(points)))


def convex_hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points
    def cross(o, a, b):
        return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lower=[]
    for p in points:
        while len(lower)>1 and cross(lower[-2],lower[-1],p)<=1e-12:
            lower.pop()
        lower.append(p)
    upper=[]
    for p in points[::-1]:
        while len(upper)>1 and cross(upper[-2],upper[-1],p)<=1e-12:
            upper.pop()
        upper.append(p)
    return lower[:-1]+upper[:-1]


def sample_polygon(vertices, samples):
    m=len(vertices)
    lengths=[math.dist(vertices[i],vertices[(i+1)%m]) for i in range(m)]
    cumulative=[0.0]
    for a in lengths:
        cumulative.append(cumulative[-1]+a)
    perimeter=cumulative[-1]
    points=[]
    edge_counts=[0]*m
    for s in samples:
        j=min(m-1,bisect_right(cumulative,s)-1)
        edge_counts[j]+=1
        p,q=vertices[j],vertices[(j+1)%m]
        r=(s-cumulative[j])/lengths[j]
        points.append((p[0]+r*(q[0]-p[0]),p[1]+r*(q[1]-p[1])))
    return points,cumulative,edge_counts


def deficit_from_gap_formula(vertices, samples):
    _,cumulative,edge_counts=sample_polygon(vertices,samples)
    m=len(vertices);perimeter=cumulative[-1]
    angles=[]
    for i in range(m):
        vx,vy=vertices[i]
        a=(vertices[i-1][0]-vx,vertices[i-1][1]-vy)
        b=(vertices[(i+1)%m][0]-vx,vertices[(i+1)%m][1]-vy)
        cosine=(a[0]*b[0]+a[1]*b[1])/(math.hypot(*a)*math.hypot(*b))
        angles.append(math.acos(max(-1.0,min(1.0,cosine))))
    samples=sorted(samples)
    loss=0.0
    for i in range(m):
        c=cumulative[i]
        at=bisect_right(samples,c)
        after=(samples[at] if at<len(samples) else samples[0]+perimeter)-c
        before=c-(samples[at-1] if at>0 else samples[-1]-perimeter)
        chord=math.sqrt(max(0.0,after*after+before*before-2*after*before*math.cos(angles[i])))
        loss+=before+after-chord
    return loss, all(edge_counts)


def phi(alpha):
    c=math.cos(alpha/2)
    return 1-(1-c*c)*math.atanh(c)/c


def test():
    rng=random.Random(431708)
    polygons=[[(0.,0.),(2.,0.),(2.,1.),(0.,1.)],[(0.,0.),(5.,0.),(0.,2.)],
              [(-2.,0.),(-1.,-1.),(2.,-1.),(3.,0.),(2.,2.),(-1.,3.)]]
    geom_checks=0
    for p in polygons:
        total=polygon_perimeter(p)
        for n in (30,60,120):
            for _ in range(60):
                s=[rng.uniform(0,total) for _ in range(n)]
                points,_,_=sample_polygon(p,s)
                proposed,allhit=deficit_from_gap_formula(p,s)
                if not allhit:
                    continue
                hull=convex_hull(points)
                actual=total-polygon_perimeter(hull)
                assert abs(actual-proposed)<3e-9*(1+total),(p,n,actual,proposed)
                geom_checks+=1
    integ_checks=0
    for j in range(1,99):
        a=j*math.pi/100.0
        q=2*(1+math.cos(a))
        N=12000
        g=[1-math.sqrt(max(0.0,1-q*((i+.5)/N)*(1-(i+.5)/N))) for i in range(N)]
        phi_integral=2*sum(g)/N
        v_integral=6*sum(t*t for t in g)/N-phi_integral**2
        c=math.cos(a/2)
        v_closed=6*phi(a)-4*c*c-phi(a)**2
        assert abs(phi_integral-phi(a))<2e-8,(j,phi_integral,phi(a))
        assert abs(v_integral-v_closed)<7e-8,(j,v_integral,v_closed)
        assert v_closed>0,(j,v_closed)
        integ_checks+=1
    # A Monte Carlo expectation check using actual hull perimeters of a rectangle.
    p=polygons[0]
    L=polygon_perimeter(p)
    n=80
    N=8000
    deficits=[]
    for _ in range(N):
        s=[rng.uniform(0,L) for _ in range(n)]
        points,_,_=sample_polygon(p,s)
        deficits.append(L-polygon_perimeter(convex_hull(points)))
    mean=sum(deficits)/N
    target=4*L*phi(math.pi/2)/(n+1)
    assert abs(mean-target)<.018*target,(mean,target)
    print('PASS',geom_checks,'full-hull perimeter identities;',integ_checks,'angle integral/variance identities; 8000 independent rectangle simulations')
    print('rectangle empirical_mean=',format(mean,'.9f'),'universal_prediction=',format(target,'.9f'))

if __name__=='__main__':
    test()
