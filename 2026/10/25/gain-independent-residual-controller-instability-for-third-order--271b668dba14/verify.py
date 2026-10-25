#!/usr/bin/env python3
"""Exact polynomial identities and independent numerical checks for the stated RK residual-controller theorem."""
from fractions import Fraction as F
from math import sqrt, log, exp

# Univariate polynomial arithmetic over Q, indexed by powers of y.
def add(a,b):
    return trim(tuple((a[i] if i<len(a) else F(0))+(b[i] if i<len(b) else F(0)) for i in range(max(len(a),len(b)))))
def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0: a.pop()
    return tuple(a)
def mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return trim(c)
def scale(a,c):return trim(tuple(v*c for v in a))
def neg(a):return scale(a,-1)
def sub(a,b):return add(a,neg(b))
def C(a):return (F(a),)

def cmul(a,b):return (sub(mul(a[0],b[0]),mul(a[1],b[1])),add(mul(a[0],b[1]),mul(a[1],b[0])))
def cadd(a,b):return (add(a[0],b[0]),add(a[1],b[1]))
def cscale(a,c):return (scale(a[0],c),scale(a[1],c))
def conj(a):return (a[0],neg(a[1]))
ONE=(C(1),C(0))
Z=(C(-1),(F(0),F(1)))
Z2=cmul(Z,Z)
Z3=cmul(Z2,Z)
R=cadd(cadd(cadd(ONE,Z),cscale(Z2,F(1,2))),cscale(Z3,F(1,6)))
Rp=cadd(cadd(ONE,Z),cscale(Z2,F(1,2)))
assert R==((F(1,3),),(F(0),F(1,2),F(0),F(-1,6)))
assert Rp==((F(1,2),F(0),F(-1,2)),C(0))
absR2=cmul(R,conj(R))[0]
y2=(F(0),F(0),F(1))
wminus3=sub(y2,C(3))
f=sub(mul(y2,mul(wminus3,wminus3)),C(32))
assert sub(absR2,C(1))==scale(f,F(1,36))
real_zrp_R=cmul(cmul(Z,Rp),conj(R))[0]
target=scale(mul(mul(sub(y2,C(1)),sub(y2,C(1))),sub(y2,C(2))),F(1,12))
assert real_zrp_R==target

def fvalue(w):return w*(w-3)*(w-3)-32
def muvalue(w):return (w-1)**2*(w-2)/12
assert fvalue(F(53,10))==F(-3963,1000)
assert fvalue(F(11,2))==F(19,8)
assert muvalue(F(53,10))-5==F(339,4000)>0
# f is strictly increasing for w>3 by f'(w)=3(w-3)(w-1)>0.
a,b=5.3,5.5
for _ in range(70):
    m=(a+b)/2
    if fvalue(m)>0:b=m
    else:a=m
w=(a+b)/2
z=-1+1j*sqrt(w)
RR=lambda zz:1+zz+zz**2/2+zz**3/6
mu=(z*(1+z+z**2/2)/RR(z)).real
assert abs(abs(RR(z))-1)<1e-12
assert abs(mu-muvalue(w))<1e-10 and mu>5

def simpson(g,N=12000):
    h=1/N
    return h/3*(g(0)+g(1)+4*sum(g(j*h) for j in range(1,N,2))+2*sum(g(j*h) for j in range(2,N,2)))
def profile(v,zz):return v*(1-v)*abs(2-v-v*zz)
def sensitivity(v,zz):
    a=2-v-v*zz
    if v==0 or v==1:return 0.0
    return ((-v*zz)*a.conjugate()).real/(abs(a)**2)
def nu(p,zz):
    denominator=simpson(lambda v: profile(v,zz)**p)
    numerator=simpson(lambda v: profile(v,zz)**p*sensitivity(v,zz))
    return 4+numerator/denominator
for p in (1,2,4):
    n=nu(p,z)
    assert 4<n<5<mu
    for beta in (F(1,10),F(1),F(10)):
        det=1+float(beta)*(mu-n)/4
        assert det>1
    # Numerical derivative check of the h^4 profile, with fixed lambda=z/h at h=1.
    eps=1e-5
    prof=lambda h:h**4*simpson(lambda v:profile(v,h*z)**p)**(1/p)
    approx=(log(prof(exp(eps)))-log(prof(exp(-eps))))/(2*eps)
    assert abs(approx-n)<3e-8
print('VERIFY_OK: exact polynomial identities, rational enclosure and p=1,2,4 local determinant and differential checks')
