#!/usr/bin/env python3
"""Exact rational verification of the RF-SSPRK(3,3) two-frequency mixing frontier.

Run with Python 3; no third-party dependencies. Every identity is checked over Q.
The proof of the universal real-root classification is in RESULT.md.
"""
from fractions import Fraction as F
from math import sqrt

# Bivariate polynomials in formal z and e, with exact rational coefficients.
def mon(z=0, e=0, c=1):
    return {(z, e): F(c)} if c else {}

def add(*items):
    out = {}
    for p in items:
        for key, val in p.items():
            out[key] = out.get(key, F(0)) + val
    return {k: v for k, v in out.items() if v}

def mul(p, q):
    out = {}
    for (i,j), a in p.items():
        for (k,l), b in q.items():
            key = (i+k,j+l)
            out[key] = out.get(key,F(0))+a*b
    return {k:v for k,v in out.items() if v}

def scale(p,c):return {k:v*F(c) for k,v in p.items() if v*F(c)}

O, Z, E = mon(), mon(z=1), mon(e=1)
p1 = O
p2 = add(O,Z)
p3 = add(O,scale(Z,F(1,2)),scale(mul(Z,Z),F(1,4)))
b1 = add(mon(c=F(1,6)),scale(E,2))
b2 = add(mon(c=F(1,6)),scale(E,-1))
b3 = add(mon(c=F(2,3)),scale(E,-1))
R = add(O,mul(Z,add(mul(b1,p1),mul(b2,p2),mul(b3,p3))))
expect_R = add(O,Z,
    mul(add(mon(c=F(1,2)),scale(E,F(-3,2))),mul(Z,Z)),
    mul(add(mon(c=F(1,6)),scale(E,F(-1,4))),mul(mul(Z,Z),Z)))
assert R==expect_R, (R,expect_R)

def qcoeff(r):
    r=F(r)
    # R(i sqrt(r)) = Re(e) + i sqrt(r) Im(e)
    real={}
    imag={}
    for (z,e),c in R.items():
        if z%2==0:
            idx=e
            real[idx]=real.get(idx,F(0))+c*(-r)**(z//2)
        else:
            idx=e
            imag[idx]=imag.get(idx,F(0))+c*(-r)**((z-1)//2)
    def convolution(u,v):
        ans={}
        for i,a in u.items():
            for j,b in v.items(): ans[i+j]=ans.get(i+j,F(0))+a*b
        return ans
    rr=convolution(real,real)
    ii=convolution(imag,imag)
    ans={i:rr.get(i,F(0))+r*ii.get(i,F(0)) for i in range(3)}
    ans[0]-=1
    return tuple(ans.get(i,F(0)) for i in [2,1,0]) # a,b,c

# Direct RK stage multiplication recovers the amplitude defect coefficients.
assert qcoeff(1)==(F(37,16),F(23,12),F(-1,18))
assert qcoeff(7)==(F(2107,16),F(-679,12),F(49,9))

def discr(abc):
    a,b,c=abc
    return b*b-4*a*c
assert discr(qcoeff(1))==F(67,16)
assert discr(qcoeff(7))==F(5341,16)

def mixed(w):
    q1,q7=qcoeff(1),qcoeff(7)
    return tuple(F(w)*q1[i]+(1-F(w))*q7[i] for i in range(3))
assert mixed(F(2,3))==(F(727,16),F(-211,12),F(16,9))
assert discr(mixed(F(2,3)))==-F(223,16)
assert -discr(mixed(F(2,3)))/(4*mixed(F(2,3))[0]) == F(223,2908)

# D(w) has degree <=2. Values at three rational w verify the full identity.
D_expected = lambda w: (9216*F(w)*F(w)-14490*F(w)+5341)/16
for w in [F(0), F(1), F(2)]:
    assert discr(mixed(w)) == D_expected(w)

# Fractional bracketing of the exact two endpoints, without approximations.
# Roots are (2415 +/- 7sqrt(7409))/3072. 85^2<7409<87^2.
assert 85*85<7409<87*87
assert 2415-7*87>0 and 2415+7*87<3072
assert discr(mixed(F(2,3)))<0

# Independent numerical check: actual real 4D stage algorithm versus Q_w(e).
def step(u, e):
    def f(x): return [-x[1],x[0],-sqrt(7)*x[3],sqrt(7)*x[2]]
    y1=list(u)
    f1=f(y1)
    y2=[u[i]+f1[i] for i in range(4)]
    f2=f(y2)
    y3=[u[i]+(f1[i]+f2[i])/4 for i in range(4)]
    f3=f(y3)
    return [u[i]+(1/6+2*e)*f1[i]+(1/6-e)*f2[i]+(2/3-e)*f3[i] for i in range(4)]

for w in [0,1/9,1/2,2/3,3/4,1]:
    u=[sqrt(w),0,sqrt(1-w),0]
    for eps in [-3,-1,-.3,0,.04,.2,.5,1,2]:
        v=step(u,eps)
        observed=sum(x*x for x in v)-sum(x*x for x in u)
        a,b,c=mixed(F(w).limit_denominator())
        predicted=float(a)*eps*eps+float(b)*eps+float(c)
        assert abs(observed-predicted)<1e-10*(1+abs(predicted)),(w,eps,observed,predicted)

print('VERIFY_OK exact stage polynomial, two mode certificates, quadratic frontier identity, 54 direct 4D runs')
