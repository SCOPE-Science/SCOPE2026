#!/usr/bin/env python3
"""Exact-rational regression checks for symmetric conservative MPRK22(1/2)."""
from fractions import Fraction as Q


def direct_step(t, x):
    """Solve the conservative stage and endpoint flux balance exactly."""
    v = (2*x + t/Q(2)) / (t + 2)
    u = x/v
    w = (1-x)/(1-v)
    xn = (x + (t/Q(2))*w)/(1+(t/Q(2))*(u+w))
    return v, xn


def m(t, d):
    k = t**3 + 5*t**2 + 8*t + 4
    z = 2*t**2 + 4*t + 4
    return -(4*d + t**3+t**2-4*t-4)/(k-z*d)


def endpoint(t):
    c = (2-t)/(2+t)
    b = (4-t-t*t)/(t*t+3*t+4)
    return b,c


def q(t):
    b,c = endpoint(t)
    return max(c,-b)


def assert_derivative_identity(t, d1, d2):
    k = t**3+5*t**2+8*t+4
    z = 2*t*t+4*t+4
    secant = (m(t,d2)-m(t,d1))/(d2-d1)
    expected = -(2*t**3*(t+1)*(t+2))/((k-z*d1)*(k-z*d2))
    assert secant == expected


def main():
    checks=0
    ts=[Q(i,j) for i,j in [(1,100),(1,10),(1,2),(1,1),(3,2),(2,1),(5,2),(3,1),(4,1),(10,1),(100,1)]]
    for t in ts:
        b,c=endpoint(t)
        assert Q(-1)<b<c<Q(1)
        assert q(t)<1
        assert c-b==2*t*t/((t+2)*(t*t+3*t+4))
        checks+=3
        for j in range(1,200):
            x=Q(j,200)
            v,xn=direct_step(t,x)
            d=2*x-1
            assert 0<v<1 and 0<xn<1
            assert 2*xn-1==d*m(t,d*d)
            assert abs(2*xn-1)<=q(t)*abs(d)
            checks+=3
            if t==2:
                assert 2*xn-1==-d**3/(12-5*d*d)
                assert abs(2*xn-1)<=abs(d)**3/7
                checks+=2
        for j in range(15):
            d1=Q(j,16); d2=Q(j+1,16)
            assert_derivative_identity(t,d1,d2)
            checks+=1
    f=lambda z:z**3+2*z*z-2*z-8
    left=Q(1751100,1000000); right=Q(1751101,1000000)
    assert f(left)<0<f(right)
    assert ((Q(1561552,1000000)**2+Q(1561552,1000000)-4)<0)
    assert ((Q(1561553,1000000)**2+Q(1561553,1000000)-4)>0)
    checks+=3
    for t in [Q(1,10),Q(1),Q(3,2),Q(2),Q(3),Q(5),Q(50)]:
        x=Q(99,100)
        d=2*x-1
        for i in range(4):
            _,x=direct_step(t,x)
            nd=2*x-1
            assert abs(nd)<=q(t)*abs(d)
            d=nd
            checks+=1
    print(f'PASS: {checks} exact-rational assertions')


if __name__ == '__main__':
    main()
