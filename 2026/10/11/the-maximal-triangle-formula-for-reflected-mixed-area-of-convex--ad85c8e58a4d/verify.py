"""Exact-rational regression checks for a quadrilateral mixed-area identity.

The universal statement is established by the accompanying mathematical proof.
This program checks canonical rational families and affine invariance independently.
"""
from fractions import Fraction as F
from itertools import combinations


def cross(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])


def hull(points):
    points=sorted(set(points))
    lower=[]
    for p in points:
        while len(lower)>1 and cross(lower[-2],lower[-1],p)<=0:
            lower.pop()
        lower.append(p)
    upper=[]
    for p in reversed(points):
        while len(upper)>1 and cross(upper[-2],upper[-1],p)<=0:
            upper.pop()
        upper.append(p)
    return lower[:-1]+upper[:-1]


def polygon_area(poly):
    return abs(sum(x*y2-x2*y for (x,y),(x2,y2) in zip(poly,poly[1:]+poly[:1])))/2


def check(vertices):
    S=polygon_area(hull(vertices))
    assert S>0
    D=hull([(x[0]-y[0],x[1]-y[1]) for x in vertices for y in vertices])
    AD=polygon_area(D)
    T=max(abs(cross(vertices[i],vertices[j],vertices[k]))/2 for i,j,k in combinations(range(4),3))
    assert AD == 2*S+4*T, (vertices,S,AD,T)
    assert (AD-2*S)/2==2*T
    return S,AD,T


def transform(poly, matrix, shift):
    (r,s),(t,u)=matrix
    return [(r*x+s*y+shift[0], t*x+u*y+shift[1]) for x,y in poly]


if __name__ == '__main__':
    checks=0
    for den in (7,11,13,17):
        for i in range(1,den):
            for j in range(1,den):
                a,b=F(i,den),F(j,den)
                poly=[(a,F(0)),(F(0),b),(a-1,F(0)),(F(0),b-1)]
                S,AD,T=check(poly)
                assert S==F(1,2)
                assert AD==3-2*min(a,1-a,b,1-b)
                checks+=1
                if (i+j)%5==0:
                    Q=transform(poly,((F(3),F(2)),(F(1),F(5))),(F(2),F(-3)))
                    s,d,t=check(Q)
                    assert (s,d,t)==tuple(F(13)*v for v in (S,AD,T))
                    checks+=1
    print('VERIFY_OK',checks,'exact-rational quadrilaterals')
