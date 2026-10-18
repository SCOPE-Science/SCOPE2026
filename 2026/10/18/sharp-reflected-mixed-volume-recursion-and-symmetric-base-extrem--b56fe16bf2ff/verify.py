"""Exact regression tests for reflected mixed volumes of homothetic frusta.

Run: python verify.py
Only the Python standard library is needed.
"""
from fractions import Fraction as F
from math import comb
from itertools import combinations


def psi(k,t):
    return sum(t**a for a in range(k))


def area_hull(points):
    pts = sorted(set(tuple(map(F,p)) for p in points))
    def cross(o,a,b):
        return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lower=[]
    for p in pts:
        while len(lower)>1 and cross(lower[-2],lower[-1],p)<=0:
            lower.pop()
        lower.append(p)
    upper=[]
    for p in reversed(pts):
        while len(upper)>1 and cross(upper[-2],upper[-1],p)<=0:
            upper.pop()
        upper.append(p)
    hull=lower[:-1]+upper[:-1]
    return abs(sum(hull[i][0]*hull[(i+1)%len(hull)][1]-hull[(i+1)%len(hull)][0]*hull[i][1] for i in range(len(hull))))/2


def mixed_area(a,b,base):
    return area_hull([(a*x[0]-b*y[0],a*x[1]-b*y[1]) for x in base for y in base])


def integrate_quadratic(g,left,right):
    mid=(left+right)/2
    return (right-left)*(g(left)+4*g(mid)+g(right))/6


def test_polygons():
    polygons=[[(F(0),F(0)),(F(1),F(0)),(F(0),F(1))],
              [(F(-1),F(-1)),(F(1),F(-1)),(F(1),F(1)),(F(-1),F(1))],
              [(F(0),F(0)),(F(3),F(0)),(F(4),F(1)),(F(1),F(3)),(F(-1),F(1))]]
    tests=0
    for base in polygons:
        v=area_hull(base)
        m1=(mixed_area(F(1),F(1),base)-2*v)/2
        assert mixed_area(F(1),F(2),base)==v+4*m1+4*v
        for t in (F(0),F(1,4),F(1,2),F(1)):
            for s in (F(1,4),F(1),F(7,3)):
                q=1-t
                integral=integrate_quadratic(lambda z:mixed_area(1-q*z,s,base),F(0),F(1))
                integral+=integrate_quadratic(lambda z:mixed_area(1,s+q*z,base),-s,F(0))
                vol=v*psi(3,t)/3
                c1=(psi(2,t)*m1+psi(1,t)*v)/3
                c2=(psi(1,t)*v+psi(2,t)*m1)/3
                predicted=vol+3*c1*s+3*c2*s*s+vol*s*s*s
                assert integral==predicted,(base,t,s,integral,predicted)
                if base==polygons[1]:
                    assert m1==v
                else:
                    assert m1>v
                tests+=1
    return tests


def coefficient_checks():
    checks=0
    for n in range(2,22):
        for t in (F(0),F(1,7),F(1,3),F(2,3),F(1)):
            for j in range(1,n):
                # Central-symmetry specialization: all base mixed volumes equal.
                x=(psi(n-j,t)+psi(j,t))/psi(n,t)
                if t<1:
                    y=(2-t**j-t**(n-j))/(1-t**n)
                    assert x==y
                    gap=(1-t**j)*(1-t**(n-j))/(1-t**n)
                    assert x==1+gap
                else:
                    assert x==1
                if n>=3 and t<1:
                    assert 1<x<=2
                checks+=1
    return checks

if __name__=='__main__':
    a=test_polygons()
    b=coefficient_checks()
    print('VERIFY_OK',a,'exact planar Minkowski integrals',b,'exact coefficient identities')
