"""Self-contained exact and finite numerical checks of a three-node feedback stability theorem.

Run: python3 verify.py
Fractions check fixed certificates; bisection checks only illustrative finite parameter values.
"""
from fractions import Fraction as F
from math import sqrt


def coeff(a,t,rho):
    b = 1 + 3*a*a - F(3,4)*t*t
    c = a*a*a + a*(1-F(3,4)*t*t) + rho - t - t*t*t/4
    h = 3*a*b - c
    return b,c,h


def determinant3(m):
    return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
            -m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
            +m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))


def char_direct(a,t,rho,x):
    return determinant3([[x+a+t/2,F(-1),F(0)],
                         [F(1),x+a+t/2,F(-1)],
                         [rho,F(0),x+a-t]])


def char_formula(a,t,rho,x):
    b,c,_ = coeff(a,t,rho)
    return x**3+3*a*x*x+b*x+c

for a,t,rho in [(F(1,4),F(3,4),F(1)),(F(1,4),F(0),F(1)),
                (F(1,8),F(1,2),F(4,5)),(F(2,3),F(1,3),F(11,7))]:
    for x in [F(-3,2),F(0),F(1,3),F(2)]:
        assert char_direct(a,t,rho,x)==char_formula(a,t,rho,x)

assert coeff(F(1,4),F(3,4),F(1)) == (F(49,64),F(39,128),F(69,256))
assert coeff(F(1,4),F(0),F(1)) == (F(19,16),F(81,64),-F(3,8))


def bisect(fn,low,high):
    assert fn(low)*fn(high)<0
    for _ in range(100):
        mid=(low+high)/2
        if fn(mid)*fn(low)>0:
            low=mid
        else:
            high=mid
    return (low+high)/2

rho_star = 8/(3*sqrt(3))
t_star = 2/sqrt(3)
for rho in [1.0,rho_star,1.7]:
    t0=bisect(lambda t:t+t**3/4-rho,0.0,3.0)
    v=1-.75*t0*t0
    s=1+.75*t0*t0
    for a in [0.02,0.01]:
        c=lambda t:a**3+a*(1-.75*t*t)+rho-t-t**3/4
        h=lambda t:8*a**3+2*a*(1-.75*t*t)-rho+t+t**3/4
        tH=bisect(h,0.0,3.0)
        tZ=bisect(c,0.0,3.0)
        if rho<rho_star-1e-8:
            assert tH<t0<tZ
            assert abs((tZ-tH)/a-3*v/s)<0.04
        elif rho>rho_star+1e-8:
            assert tH>tZ
        else:
            assert tH<t_star<tZ
            assert abs((tZ-tH)/a**3-4.5)<0.15
            assert 3*a*a+1-.75*tH*tH>0
print('VERIFIED: exact determinant and Hurwitz certificates; sample root ordering and asymptotics')
