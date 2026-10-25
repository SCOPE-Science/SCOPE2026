"""Reproducible checks for affine least-squares projection on regular polygons.
Uses only the Python standard library. Exact checks use rational coordinates after a fixed vertical rescaling.
"""
from fractions import Fraction as F
from math import cos, sin, pi, acos, sqrt


def area_moment(poly):
    twice_area = poly[0][0]*0
    six_moment = poly[0][0]*0
    for (x,y),(xx,yy) in zip(poly, poly[1:]+poly[:1]):
        cross=x*yy-xx*y
        twice_area +=cross
        six_moment += (x+xx)*cross
    return twice_area/2, six_moment/6


def clip_left(poly,h):
    out=[]
    for (x,y),(xx,yy) in zip(poly,poly[1:]+poly[:1]):
        inside=x<=h
        nextinside=xx<=h
        if inside: out.append((x,y))
        if inside!=nextinside:
            lam=(h-x)/(xx-x)
            out.append((h,y+lam*(yy-y)))
    return out


def norm_polygon(poly,c):
    A,_=area_moment(poly)
    cap=clip_left(poly,-1/c)
    C,M=area_moment(cap)
    return 1+2*(-C-c*M)/A


def regular_poly(n):
    return [(cos(2*pi*j/n),sin(2*pi*j/n)) for j in range(n)]


def norm_n(n):
    theta=2*pi/n
    return norm_polygon(regular_poly(n),12/(2+cos(theta)))


def triangle_quadrature(n,N=130):
    theta=2*pi/n
    c=12/(2+cos(theta))
    total=0.
    for j in range(n):
        a=cos(theta*j);b=cos(theta*(j+1))
        for k in range(N):
            u=(k+.5)/N
            for l in range(N):
                s=(l+.5)/N
                x=u*a+(1-u)*s*b
                total+=2*(1-u)*abs(1+c*x)/(N*N*n)
    return total


def rational_vertices(n):
    if n==3:
        # y-coordinates divided by sqrt(3), preserving all area ratios.
        return [(F(1),F(0)), (F(-1,2),F(1,2)), (F(-1,2),F(-1,2))]
    if n==4:
        return [(F(1),F(0)), (F(0),F(1)), (F(-1),F(0)), (F(0),F(-1))]
    if n==6:
        return [(F(1),F(0)), (F(1,2),F(1,2)), (F(-1,2),F(1,2)),(F(-1),F(0)),(F(-1,2),F(-1,2)),(F(1,2),F(-1,2))]
    raise ValueError(n)

def test():
    n_checks=0
    for n,c,expected in [(3,F(8),F(19,8)),(4,F(6),F(233,108)),(6,F(24,5),F(361,180))]:
        val=norm_polygon(rational_vertices(n),c)
        assert val==expected,(n,val,expected)
        n_checks+=1
        assert abs(norm_n(n)-float(expected))<1e-12
        n_checks+=1
        print('EXACT',n,val)
    for n in (5,7,9,12):
        a=norm_n(n); b=triangle_quadrature(n,180)
        assert abs(a-b)<8e-5,(n,a,b)
        n_checks+=1
        print('QUADRATURE',n,a,b,abs(a-b))
    lim=1-2*acos(F(1,4))/pi+11*sqrt(15)/(8*pi)
    C=5*pi*sqrt(15)/12
    for n in (80,120,200,320,500):
        value=norm_n(n)
        scaled=n*n*(value-lim)
        assert abs(scaled-C)<.04,(n,scaled,C)
        n_checks+=1
        print('SECOND_ORDER',n,scaled,'limit_coefficient',C)
    print('ALL PASSED',n_checks,'sets of checks')

if __name__=='__main__':
    test()
