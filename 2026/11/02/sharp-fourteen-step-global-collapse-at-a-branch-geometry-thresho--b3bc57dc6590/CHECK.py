#!/usr/bin/env python3
"""Exact rational certificate for the global settling exponent of an absolute-value map.

Usage: python3 CHECK.py
No external dependencies. All inequalities, coordinates, and convex hulls use fractions.
"""
from fractions import Fraction as Q
from itertools import combinations

B=Q(1,4)
FIXED=(-B,2*B-1)

def F(z):
    x,y=z
    return abs(x)-y-1, x-abs(y)+B

def cross(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])

def hull(points):
    pts=sorted(set(points))
    if len(pts)<3:return tuple(pts)
    low=[]; high=[]
    for p in pts:
        while len(low)>1 and cross(low[-2],low[-1],p)<=0:low.pop()
        low.append(p)
    for p in reversed(pts):
        while len(high)>1 and cross(high[-2],high[-1],p)<=0:high.pop()
        high.append(p)
    return tuple(low[:-1]+high[:-1])

def clip(poly,axis,sgn):
    if not poly:return ()
    def h(p):return sgn*p[axis]
    if len(poly)==1:return poly if h(poly[0])>=0 else ()
    res=[]
    for j,p in enumerate(poly):
        q=poly[(j+1)%len(poly)]
        u,v=h(p),h(q)
        if u>=0:res.append(p)
        if (u<0<v) or (v<0<u):
            t=u/(u-v)
            res.append(tuple(p[i]+t*(q[i]-p[i]) for i in range(2)))
    return hull(res)

def image_polygons(polygons):
    images=set()
    for poly in polygons:
        for sx in (-1,1):
            p=clip(poly,0,sx)
            if not p:continue
            for sy in (-1,1):
                q=clip(p,1,sy)
                if not q:continue
                images.add(hull((sx*x-y-1,x-sy*y+B) for x,y in q))
    return images

def vertices(constraints):
    # Every itinerary cell is contained in a closed quadrant, hence pointed.
    cs=[]
    for a,b,c in constraints:
        if a==0 and b==0:
            if c<0:return ()
        else:cs.append((a,b,c))
    answer=set()
    for (a,b,c),(d,e,f) in combinations(cs,2):
        det=a*e-b*d
        if det==0:continue
        x=(b*f-c*e)/det
        y=(c*d-a*f)/det
        if all(g*x+h*y+k>=0 for g,h,k in cs):answer.add((x,y))
    return tuple(answer)

def global_image_at_five():
    ident=((Q(1),Q(0)),(Q(0),Q(1)))
    states=[(ident,(Q(0),Q(0)),())]
    feasible_counts=[]
    for step in range(1,6):
        following=[]
        for A,v,cs in states:
            for sx in (-1,1):
                for sy in (-1,1):
                    newcs=cs+((sx*A[0][0],sx*A[0][1],sx*v[0]),
                              (sy*A[1][0],sy*A[1][1],sy*v[1]))
                    if not vertices(newcs):continue
                    N=((sx*A[0][0]-A[1][0],sx*A[0][1]-A[1][1]),
                       (A[0][0]-sy*A[1][0],A[0][1]-sy*A[1][1]))
                    w=(sx*v[0]-v[1]-1,v[0]-sy*v[1]+B)
                    following.append((N,w,newcs))
        states=following
        feasible_counts.append(len(states))
    pieces=set()
    for A,v,cs in states:
        pts=vertices(cs)
        assert pts
        pieces.add(hull((A[0][0]*x+A[0][1]*y+v[0],
                         A[1][0]*x+A[1][1]*y+v[1]) for x,y in pts))
    return feasible_counts,pieces

def run():
    counts,P=global_image_at_five()
    assert counts==[4,13,25,45,75],counts
    assert len(P)==30,len(P)
    allvertices={v for polygon in P for v in polygon}
    assert len(allvertices)==13,len(allvertices)
    size_by_time={5:(len(P),len(allvertices))}
    for n in range(6,15):
        P=image_polygons(P)
        size_by_time[n]=(len(P),len({v for poly in P for v in poly}))
    expected={5:(30,13),6:(25,11),7:(20,9),8:(15,8),9:(12,7),
              10:(10,6),11:(8,5),12:(6,4),13:(3,2),14:(1,1)}
    assert size_by_time==expected,(size_by_time,expected)
    assert P=={(FIXED,)},P
    witness=(Q(-3),Q(1,4))
    orbit=[witness]
    for _ in range(14):orbit.append(F(orbit[-1]))
    assert orbit[13]==(Q(-3,4),Q(0)),orbit[13]
    assert orbit[14]==FIXED,orbit[14]
    assert F(FIXED)==FIXED
    print('PASS: global affine sign-cell paths:',counts)
    print('PASS: exact image polygon counts:',size_by_time)
    print('PASS: F^14(R^2) singleton:',FIXED)
    print('PASS: F^13 witness:',witness,'->',orbit[13])

if __name__=='__main__':run()
