#!/usr/bin/env python3
"""Standalone numerical and exact-algebra checks for the three-time design theorem.
Scientific proof and assumptions are in RESULT.md; finite checks are corroborative.
"""
from fractions import Fraction
from itertools import product
from math import cos, sin, exp, isclose, pi

N = 0

def check(cond, msg='assertion failed'):
    global N
    N += 1
    if not cond:
        raise AssertionError(msg)

def gramdet(rows):
    x = sum(row[0]*row[0] for row in rows)
    y = sum(row[0]*row[1] for row in rows)
    z = sum(row[1]*row[1] for row in rows)
    return x*z-y*y

def minors(rows):
    return sum((rows[i][0]*rows[j][1]-rows[i][1]*rows[j][0])**2
               for i in range(len(rows)) for j in range(i+1,len(rows)))

# Exact arithmetic (not floating point): Cauchy--Binet identity for arbitrary
# integer 3x2 design matrices and the bound's key polynomial certificate.
for a,b,c,d,e,f in product(range(-2,3),repeat=6):
    rows=[(a,b),(c,d),(e,f)]
    check(gramdet(rows)==minors(rows), 'integer Cauchy--Binet')
for j in range(1,201):
    r=Fraction(j,201)
    P=(1+4*r+r*r)**2-12*r*(1+r+r*r)
    check(P==(1-r)**4 and P>=0, 'rational polynomial certificate')

def exact_formula(a,w,h):
    return (exp(-2*a*h)*sin(w*h)**2+exp(-4*a*h)*sin(2*w*h)**2+
            exp(-6*a*h)*sin(w*h)**2)

def design(a,w,h):
    return [(exp(-a*j*h)*cos(w*j*h),exp(-a*j*h)*sin(w*j*h))
            for j in range(3)]

for a in (0.2, 0.7, 2., 12.):
    for w in (0.13, 0.8, 2.4, 7.):
        for h in (0.001, 0.13, 0.51, 1.13, 2.7, 8.):
            d=gramdet(design(a,w,h))
            e=exact_formula(a,w,h)
            check(isclose(d,e,rel_tol=2e-9,abs_tol=1e-13),'normal-matrix vs minors')
            check(e>=-1e-14,'nonnegativity')

def g(u):
    return u*u*(exp(-2*u)+4*exp(-4*u)+exp(-6*u))

def k(u):
    return u**4/3*(exp(-2*u)+16*exp(-4*u)+exp(-6*u))

def m(u):
    r=exp(-2*u)
    return (1+8*r+3*r*r)/(1+4*r+r*r)

def root(fun,lo,hi,iterations=90):
    left=fun(lo)
    right=fun(hi)
    check(left*right<0, 'root bracket')
    for _ in range(iterations):
        mid=(lo+hi)/2
        fm=fun(mid)
        if fm*left>0:
            lo,left=mid,fm
        else:
            hi,right=mid,fm
    return (lo+hi)/2

u=root(lambda z:1/z-m(z),.5,1.)
C=g(u)
check(abs(u-0.6312899580741505)<4e-14, 'unique root constant')
check(abs(C-0.249379061959616)<3e-14, 'envelope constant')
for j in range(1,5001):
    x=j/500
    check(g(x)<=C+2e-15, 'sampled envelope')

# Derivatives for the next-order coefficient use analytic exponential sums.
def gp2(z):
    return sum(co*(z*z*rate*rate-4*z*rate+2)*exp(-rate*z)
               for rate,co in ((2,1),(4,4),(6,1)))
def kp(z):
    return sum(co*(4*z**3-rate*z**4)*exp(-rate*z)/3
               for rate,co in ((2,1),(4,16),(6,1)))
curv=gp2(u)
corr=kp(u)/curv
K=k(u)
check(curv<-.93 and abs(curv+0.9369704250061517)<2e-13,'strict curvature')
check(abs(corr+0.2388090255494174)<2e-13,'spacing coefficient')
check(abs(K-0.08398062386722377)<2e-14,'determinant second term')

def phi(z,eps):
    t=eps*z
    return (exp(-2*z)*sin(t)**2+exp(-4*z)*sin(2*t)**2+
            exp(-6*z)*sin(t)**2)/eps**2

def dphi(z,eps):
    return sum(exp(-rate*z)*
        (mult*eps*sin(2*mult*eps*z)-rate*sin(mult*eps*z)**2)/eps**2
        for rate,mult in ((2,1),(4,2),(6,1)))

for eps in (.3,.15,.075,.03):
    v=root(lambda z:dphi(z,eps),.4,.9)
    check(abs(v-(u+corr*eps**2))<.18*eps**4,'spacing expansion')
    check(abs(phi(v,eps)-(C-K*eps**2))<.13*eps**4,'determinant expansion')
    for j in range(1,1800):
        z=j/140
        check(phi(z,eps)<=C+1e-12,'universal bound')
        check(phi(z,eps)<=phi(v,eps)+5e-12,'high-damping optimum on grid')

for j in (1,2,3,4):
    w=float(j)
    h=pi/w
    check(abs(exact_formula(1.,w,h))<2e-29,'resonant zero determinant')

print('VERIFY_OK',N, 'checks', 'u3=',format(u,'.15g'),
      'C3=',format(C,'.15g'), 'K3=',format(K,'.15g'),
      'c3=',format(corr,'.15g'))
