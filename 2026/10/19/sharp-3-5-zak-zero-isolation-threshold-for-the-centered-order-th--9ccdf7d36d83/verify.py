"""Exact-rational checks for the order-three centered B-spline Zak-zero theorem.

Run: python3 verify_order_three_zak.py
Finite tests support; they do not replace the proof in RESULT.md.
"""
from fractions import Fraction as F
from math import pi, sin, cos


def B(u):
    u = abs(u)
    if u <= F(1,2):
        return F(3,4)-u*u
    if u <= F(3,2):
        return (F(3,2)-u)**2/2
    return F(0)


def h(u):
    if u <= F(1,2):
        return 2*u
    if u <= F(3,2):
        return F(3,2)-u
    return F(0)


def S(q, x):
    return sum((1 if k%2==0 else -1)*B(q*(x-k)) for k in range(-8,9))


def H(q, x):
    return h(q*(1-x))+h(q*(1+x))-2*h(q*(2-x))-2*h(q*(2+x))


def finite_zero(q,x,v):
    theta=2*pi*v
    return sum(float(B(q*(x-k)))*complex(cos(k*theta),sin(k*theta)) for k in range(-8,9))

checks=0
for i in range(41):
    q=F(3,5)+F(i,100)
    assert q <= 1
    mu=q/(2*q-1)
    for j in range(101):
        x=F(j,200)
        assert H(q,x)>=0, (q,x,H(q,x))
        checks+=1
        assert S(q,x)==(2*q-1)**2*S(mu,x),(q,x)
        checks+=1
        if x<F(1,2):
            assert S(mu,x)>0, (q,x,mu,S(mu,x))
        else:
            assert S(mu,x)==0
        checks+=1
        if x>0:
            Aj1=B(q*(1-x))-B(q*(1+x))
            Aj2=B(q*(2-x))-B(q*(2+x))
            assert Aj1>2*Aj2,(q,x,Aj1,Aj2)
            checks+=1
        for k in range(1,6):
            v=F(k,12)
            if x>0:
                assert finite_zero(q,x,v).imag>1e-13,(q,x,v)
            checks+=1
for j in range(1,17):
    q=F(3,7)+(F(3,5)-F(3,7))*F(j,17)
    assert F(3,7)<q<F(3,5)
    d=abs(F(1,q)-2)
    for k in range(21):
        x=F(3,2)*d+(1-3*d)*F(k,20)
        assert S(q,x)==0,(q,x,S(q,x))
        checks+=1
print('VERIFY_OK',checks,'exact and supplementary numeric comparisons; distinct-boundary and zero-segment tests')
