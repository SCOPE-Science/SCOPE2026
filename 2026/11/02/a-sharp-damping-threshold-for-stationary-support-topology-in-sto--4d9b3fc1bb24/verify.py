"""Standalone checks for exact damped Chebyshev descent stationary phase theorem.
Only Python standard library is required. No external data or software is needed.
"""
from fractions import Fraction as F
from itertools import product
from math import acosh, cosh, cos, pi, log, isclose

N = 0
def check(condition, message):
    global N
    N += 1
    if not condition:
        raise AssertionError(message)

def cheb(n, x):
    if n == 0:
        return x*0+1
    a, b = x*0+1, x
    for _ in range(2, n+1):
        a, b = b, 2*x*b-a
    return b

def cheb_deriv(n,x):
    if n==0: return x*0
    a,b=x*0+1,x
    da,db=x*0,x*0+1
    for _ in range(2,n+1):
        a,b,da,db=b,2*x*b-a,db,2*b+2*x*db-da
    return db

def params(s,eps):
    o=1+eps/F(s*s) if isinstance(eps,F) else 1+eps/(s*s)
    c=cheb(s,o)
    w=c/cheb_deriv(s,o)
    h=2*o/w
    return o,c,w,h

def step_poly(s,eps,t,y,offset):
    o,c,w,h=params(s,eps)
    r=cheb(s,o-w*t)/c
    return r*y+(1-r)*offset, r

def step_stages(s,eps,t,y,offset):
    o,c,w,h=params(s,eps)
    val0=y
    val1=y-(w/o)*t*(y-offset)
    for j in range(2,s+1):
        tj=cheb(j,o)
        tjm1=cheb(j-1,o)
        tjm2=cheb(j-2,o)
        mu=2*o*tjm1/tj
        nu=-tjm2/tj
        mtilde=2*w*tjm1/tj
        val0,val1=val1,mu*val1+nu*val0-mtilde*t*(val1-offset)
    return val1

# Exact-rational independent stage recurrence / Chebyshev polynomial identity.
for s in (2,4,6,8):
    for eps in (F(1,10), F(3,4), F(2,1)):
        o,c,w,h=params(s,eps)
        check(c>1 and w>0 and h>0, 'positive damped coefficients')
        check(cheb(s,o)==c,'definition C')
        check(cheb(s,o-w*h)==c,'even-stage symmetric endpoint')
        check(w*cheb_deriv(s,o)==c,'first order consistency')
        for fr in (F(1,11),F(2,9),F(3,8),F(1,2),F(7,10),F(10,11)):
            t=h*fr
            for y in (F(-7,3),F(0),F(13,7)):
                for z in (F(-5,4),F(2,3)):
                    py,r=step_poly(s,eps,t,y,z)
                    sy=step_stages(s,eps,t,y,z)
                    check(sy==py,'stage-vs-stability-polynomial exact rational')
                    check(-1<r<1,'interior scalar strict contraction')

# Complete finite sign enumeration versus exact time-n second moment and mean.
for s, eps, frac in [(2,F(1,2),F(1,5)),(2,F(1,2),F(1,2)),
                    (4,F(1,4),F(2,7)),(4,F(1,4),F(4,9)),
                    (6,F(1,3),F(4,11))]:
    h=params(s,eps)[3]
    t=h*frac
    _,r=step_poly(s,eps,t,F(0),F(0))
    offset=F(3,2)
    for n in (1,2,3,4,5,6,7,8):
        v=F(0); m=F(0)
        for signs in product((-1,1),repeat=n):
            x=F(0)
            for sigma in signs:
                x=r*x+(1-r)*offset*sigma
            m+=x
            v+=x*x
        m/=2**n; v/=2**n
        expected=offset**2*(1-r)**2*(1-r**(2*n))/(1-r*r)
        check(m==0,'exact finite-chain mean')
        check(v==expected,'exact finite-chain second moment')

# Local extrema, exact stationary variance max and merger criterion.
for s in (2,4,6,8,10,12):
    root=s*s*(cosh(acosh(2)/s)-1)
    for eps in (root/4,root*0.95,root,root*1.05,root*4):
        o,c,w,h=params(s,eps)
        check(abs(c-cosh(s*acosh(o)))<2e-9,'hyperbolic Chebyshev identity')
        vmax=(c+1)/(c-1)
        for j in range(1,s,2):
            x=cos(j*pi/s)
            r=cheb(s,x)/c
            check(abs(r+1/c)<2e-9,'negative Chebyshev extremum')
            check(abs((1-r)/(1+r)-vmax)<2e-9,'sharp global variance attained')
        for k in range(1,400):
            x=o*(1-2*k/400)
            r=cheb(s,x)/c
            check(-1<r<1,'damped stability strict inside')
            check((1-r)/(1+r)<=vmax+1e-8,'uniform variance bound')
        for j in range(1,s):
            extremum=cos(j*pi/s)
            r=abs(cheb(s,extremum)/c)
            check((r<0.5)==(c>2), 'merger strict threshold away from equality') if abs(c-2)>1e-9 else check(abs(r-.5)<2e-9,'critical touching')
        if abs(c-2)<2e-9:
            check(abs(vmax-3)<2e-8,'sharp variance three boundary')
        else:
            check((vmax<3)==(c>2),'uniform variance bound vs topology')

# Bernoulli convolutions at critical overlaps are uniform: moment identities.
for r in (F(1,2),F(-1,2)):
    b=F(3,5)
    M=b*(1-r)/(1-abs(r))
    v=b*b*(1-r)/(1+r)
    check(v==M*M/3,'uniform law second moment at critical overlap')

# Small/large damping asymptotic rates (numerical sanity checks, not proofs).
for s in (2,4,8,16):
    o,c,w,h=params(s,1e-6)
    vmax=(c+1)/(c-1)
    check(abs(vmax*1e-6/2-1)<1e-5,'small damping scaling')
for eps in (0.2,1.0,3.0):
    expected=(cosh((2*eps)**0.5)+1)/(cosh((2*eps)**0.5)-1)
    vals=[(params(s,eps)[1]+1)/(params(s,eps)[1]-1) for s in (8,32,128,512)]
    check(abs(vals[-1]-expected)<1e-4,'large-stage variance limit')
    check(all(abs(vals[i+1]-expected)<abs(vals[i]-expected) for i in range(3)), 'limit approach')

print('CHECKS_PASS',N)
