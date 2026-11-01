#!/usr/bin/env python3
"""Numerically check the claimed five eigenvalues using raw spherical harmonics.
Run with Python 3 standard library only: python verify_quadrupole.py.
Numerical comparisons corroborate, but do not replace, the exact proof.
"""
from cmath import exp
from math import pi, sqrt, cos, sin


def points(m, h, offset):
    r = sqrt(1-h*h)
    out = []
    for j in range(m):
        t = 2*pi*j/m
        out.append((r*cos(t),r*sin(t),h))
    for j in range(m):
        t = 2*pi*j/m + offset
        out.append((r*cos(t),r*sin(t),-h))
    return out


def harmonics2(p):
    x,y,z=p
    w=complex(x,y)
    wm=w.conjugate()
    a=sqrt(15/(32*pi))
    b=sqrt(15/(8*pi))
    c=sqrt(5/(16*pi))
    # In increasing order of the magnetic index -2,-1,0,1,2.
    return (a*wm*wm,b*z*wm,c*(3*z*z-1),-b*z*w,a*w*w)


def gram(m,u,offset):
    rows=[harmonics2(p) for p in points(m,sqrt(u),offset)]
    G=[[sum(row[j].conjugate()*row[k] for row in rows)
        for k in range(5)] for j in range(5)]
    return G


def expected(m,u):
    scale=(2*m*5)/(16*pi)
    a=(3*u-1)**2
    b=6*u*(1-u)
    c=1.5*(1-u)**2
    return [scale*c,scale*b,scale*a,scale*b,scale*c]


def test():
    cases=0
    us=[0.001,.02,.07,(6-sqrt(21))/15,.14,.2,1/3,.4,.7,.95]
    for m in (5,6,7,11,16,29):
        for off in (0,pi/m,0.617):
            for u in us:
                G=gram(m,u,off); goal=expected(m,u)
                for j in range(5):
                    for k in range(5):
                        target=goal[j] if j==k else 0
                        assert abs(G[j][k]-target)<2e-11,(m,off,u,j,k,G[j][k],target)
                cases+=1
    star=(6-sqrt(21))/15
    rho=(5+sqrt(21))/4
    a=(3*star-1)**2; b=6*star*(1-star); c=1.5*(1-star)**2
    assert abs(a-b)<1e-14
    assert abs(c/a-rho)<1e-12
    assert a>0 and c>a
    for k in range(1,10000):
        u=k/10000
        levels=((3*u-1)**2,6*u*(1-u),1.5*(1-u)**2)
        assert max(levels)/min(levels)>rho-2e-8
    print('PASS:',cases,'independent raw harmonic Gram identities; 9999 height comparisons')
    print('Optimal u=',format(star,'.16f'),'optimal squared condition number=',format(rho,'.16f'))

if __name__=='__main__':
    test()
