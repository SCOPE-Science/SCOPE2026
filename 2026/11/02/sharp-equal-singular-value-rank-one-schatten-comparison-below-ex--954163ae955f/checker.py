#!/usr/bin/env python3
"""Finite consistency checks for the sharp equal-rank-one Schatten quotient.

Only the Python standard library is required.  The analytical uniqueness and
endpoint asymptotics are proved in RESULT.md, not inferred from these tests.
"""
import math
import random

RNG = random.Random(867241)
checks = 0

def check(ok, msg):
    global checks
    if not ok:
        raise AssertionError(msg)
    checks += 1

def f(p,u):
    gamma=p/(2-p)
    def logcosh(v):
        return abs(v)+math.log1p(math.exp(-2*abs(v)))-math.log(2)
    return (p*logcosh(u)/2 + (1-p/2)*logcosh(gamma*u) - logcosh(p*u))/p

def dg(p,u):
    gamma=p/(2-p)
    return math.tanh(u)+math.tanh(gamma*u)-2*math.tanh(p*u)

def optimum(p):
    lo,hi=0.05,5.0
    check(dg(p,lo)>0 and dg(p,hi)<0,'bracketing')
    for _ in range(90):
        mid=(lo+hi)/2
        if dg(p,mid)>0:lo=mid
        else:hi=mid
    return (lo+hi)/2

def eig2_sym(a,b,c):
    tr=a+c
    disc=math.sqrt(max(0.,(a-c)**2+4*b*b))
    return (max(0.,(tr+disc)/2),max(0.,(tr-disc)/2))

def matrix_ratio(p,c,d):
    # The two unit-amplitude real rank-one matrices A=e1 e1^T,
    # B=(d,sqrt(1-d^2))^T (c,sqrt(1-c^2)).
    s=math.sqrt(max(0,1-c*c)); t=math.sqrt(max(0,1-d*d))
    m00,m01,m10,m11=1+d*c,d*s,t*c,t*s
    num=eig2_sym(m00*m00+m10*m10,m00*m01+m10*m11,m01*m01+m11*m11)
    # |A|+|B|=e1e1^T+vv^T; calculate from its entries.
    den=eig2_sym(1+c*c,c*s,s*s)
    return (sum(v**(p/2) for v in num)/sum(v**p for v in den))**(1/p)

def scalar_ratio(p,c,d):
    r=p/2
    return (((1+c)**r*(1+d)**r+(1-c)**r*(1-d)**r)/((1+c)**p+(1-c)**p))**(1/p)

u0=1.19967864025773383391636984864
kappa=(u0*u0-1)/2

for p in (1.01,1.05,1.2,1.5,1.8,1.95):
    u=optimum(p)
    c=math.tanh(u)
    d=math.tanh(p/(2-p)*u)
    ratio=math.exp(f(p,u))
    check(0<c<d<1 and ratio>1,'interior optimizer')
    check(abs(dg(p,u))<5e-12,'critical equation')
    check(abs(ratio-scalar_ratio(p,c,d))<3e-13,'hyperbolic formula')
    check(abs(ratio-matrix_ratio(p,c,d))<3e-13,'explicit matrices')
    # Check critical sign and strict global improvement on a deterministic grid.
    for u_test in (0.001,0.08,0.2,0.5,0.8,1.0,1.3,2.0,3.0,6.0):
        if abs(u_test-u)>1e-4:
            check(f(p,u_test)<f(p,u)+1e-12,'unique max grid')
    for i in range(180):
        c1=RNG.random();d1=RNG.random()
        q=matrix_ratio(p,c1,d1)
        check(abs(q-scalar_ratio(p,c1,d1))<2e-12,'independent Gram formula')
        check(q<=ratio+2e-12,'rank-one numerical envelope')
    for _ in range(120):
        c1=RNG.random()
        d_opt=math.tanh((p/(2-p))*math.atanh(c1))
        d_alt=RNG.random()
        check(scalar_ratio(p,c1,d_alt)<=scalar_ratio(p,c1,d_opt)+2e-12,'fixed input optimality')

for eps in (0.02,0.01,0.005,0.002):
    p=1+eps
    u=optimum(p)
    logc=f(p,u)
    check(abs(logc/eps**2-kappa)<2.0*eps,'sharp quadratic onset')
    check(abs((u-u0)/eps+u0)<4*eps,'optimizer displacement')

# The conjectural common-output value has exponentially small, not quadratic,
# defect; use a scalar root instead of overflowing x**p for small epsilon.
for eps in (0.25,0.1,0.05):
    p=1+eps
    left,right=2.0,math.log(2)/eps+2.0
    def h(t):return math.exp(eps*t)-2-math.exp(-t)
    check(h(left)<0 and h(right)>0,'conjectural root bracket')
    for _ in range(90):
        t=(left+right)/2
        if h(t)<0:left=t
        else:right=t
    x=math.exp((left+right)/2)
    logtz=(math.log1p(1/(2*x))+(eps-1)/2*math.log1p(1/x))/(1+eps)
    check(math.exp(f(p,optimum(p)))>math.exp(logtz),'model improves conjectured value')

print('PASS:',checks,'deterministic checks')
print('u0 =',u0,'kappa =',kappa)
