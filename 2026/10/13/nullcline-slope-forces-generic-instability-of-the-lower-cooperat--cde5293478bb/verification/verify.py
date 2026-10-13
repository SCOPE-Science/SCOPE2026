#!/usr/bin/env python3
import math

beta=2.0
b=0.49
c=3.0

def S(y):
    return math.exp(-y*(1.0+c*y))

def f(y,r):
    return 1.0 + math.log((1.0-b)+b*S(y))/r

def g(y):
    return y/(beta*b*(1.0-S(y)))

def fp(y,r):
    d=(1.0-b)+b*S(y)
    return -b*S(y)*(1.0+2.0*c*y)/(r*d)

def gp(y):
    u=1.0-S(y)
    up=S(y)*(1.0+2.0*c*y)
    return (u-y*up)/(beta*b*u*u)

def H(y,r):
    return f(y,r)-g(y)

def bisect(a0,b0,r):
    fa=H(a0,r)
    fb=H(b0,r)
    assert fa*fb < 0.0
    for _ in range(100):
        m=(a0+b0)/2.0
        fm=H(m,r)
        if fa*fm <= 0.0:
            b0=m
            fb=fm
        else:
            a0=m
            fa=fm
    return (a0+b0)/2.0

def lower_root(r):
    return bisect(1e-8,0.1,r)

def check(r, x_ref, y_ref):
    y=lower_root(r)
    x=f(y,r)
    sy=S(y)
    expfac=math.exp(r*(1.0-x))
    j11=1.0-r*x
    j12=-b*x*expfac*sy*(1.0+2.0*c*y)
    j21=y/x
    j22=beta*b*x*sy*(1.0+2.0*c*y)

    tr=j11+j22
    det=j11*j22-j12*j21
    p1=1.0-tr+det
    rhs=-r*y*(fp(y,r)-gp(y))
    assert abs(p1-rhs) < 1e-11
    assert fp(y,r)-gp(y) > 0.0
    assert p1 < 0.0

    disc=tr*tr-4.0*det
    assert disc > 0.0
    root=math.sqrt(disc)
    lam1=(tr-root)/2.0
    lam2=(tr+root)/2.0
    assert max(lam1,lam2) > 1.0

    assert abs(x-x_ref) < 2e-7
    assert abs(y-y_ref) < 2e-7
    return x,y,lam1,lam2

x1,y1,l11,l12=check(1.0,0.9947339,0.0104492)
assert -1.0 < min(l11,l12) < 1.0
assert abs(min(l11,l12)-0.0106013) < 5e-5
assert abs(max(l11,l12)-1.0195174) < 5e-5

x3,y3,l31,l32=check(3.0,0.9985180,0.0088588)
assert max(l31,l32) > 1.0

print("VERIFY_OK")
