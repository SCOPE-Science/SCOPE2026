#!/usr/bin/env python3
"""Independent finite diagnostics for the two-clock Brownian search formulas.

These checks illustrate the analytic theorem but do not certify its infinite scope.
Only Python's standard library is needed.
"""
import math
import random

checks = 0

def assert_close(a, b, rtol=2e-10, atol=2e-10):
    global checks
    checks += 1
    if not math.isclose(a, b, rel_tol=rtol, abs_tol=atol):
        raise AssertionError((a, b))

def assert_true(cond):
    global checks
    checks += 1
    if not cond:
        raise AssertionError("Boolean diagnostic failed")

def taylor(s):
    """Return A, A', A'', G, G', G'' from their entire series."""
    aa = [0.0, 0.0, 0.0]
    gg = [0.0, 0.0, 0.0]
    for n in range(75):
        c1 = 1.0 / math.factorial(2*n+2)
        c2 = 1.0 / math.factorial(2*n+1)
        p = s**n
        aa[0] += c1*p
        gg[0] += c2*p
        if n >= 1:
            aa[1] += n*c1*s**(n-1)
            gg[1] += n*c2*s**(n-1)
        if n >= 2:
            aa[2] += n*(n-1)*c1*s**(n-2)
            gg[2] += n*(n-1)*c2*s**(n-2)
    return aa, gg

def normalized_mean(s, w):
    a, g = taylor(s)
    return a[0] + g[0]/math.sqrt(s+w*w)

def derivs(s, w):
    a, g = taylor(s)
    v = s+w*w
    fp = a[1] + g[1]/math.sqrt(v) - g[0]/(2*v**1.5)
    fpp = a[2] + (v*v*g[2]-v*g[1]+.75*g[0])/v**2.5
    return fp, fpp

def d1(w):
    return (w**3+4*w*w-12)/(24*w**3)

def d2(w):
    return 1/720+1/(120*w)-1/(12*w**3)+3/(8*w**5)

def bisect_root(func, lo, hi, steps=80):
    assert_true(func(lo)*func(hi) < 0)
    for _ in range(steps):
        mid = (lo+hi)/2
        if func(mid)*func(lo) <= 0:
            hi=mid
        else:
            lo=mid
    return (lo+hi)/2

wc = bisect_root(lambda w: w**3+4*w*w-12, 1, 2)
assert_close(wc, 1.4798157487551455)
assert_close(derivs(0,wc)[0], 0, atol=1e-14)
assert_close(derivs(0,wc)[1], 2*d2(wc), atol=1e-14)
assert_close(wc**2, 2.189854650263752)

# Direct mean backward equations, including matching derivatives at x=0.
rng=random.Random(901247)
for i in range(500):
    w = math.exp(rng.uniform(-2, 2))
    s = math.exp(rng.uniform(-3, 1.3))
    m0=normalized_mean(s,w)
    k0=math.sqrt(s)
    k1=math.sqrt(s+w*w)
    mxp=lambda x: m0+(1-math.cosh(k0*x))/s-math.sinh(k0*x)/(k0*k1)
    mxn=lambda x: m0+(1-math.exp(k1*x))/(s+w*w)
    assert_close(mxp(1),0,atol=1e-8)
    assert_close(mxp(0),mxn(0))
    assert_close(-k0/(k0*k1),-k1/(s+w*w))
    for _ in range(3):
        x=rng.uniform(.02,.98)
        # Dm'' - s(m-m0) = -1 in scaled coordinates.
        curv=-math.cosh(k0*x)-k0/k1*math.sinh(k0*x)
        assert_close(curv-s*(mxp(x)-m0),-1)
        y=-rng.uniform(.01,2)
        curvneg=-math.exp(k1*y)
        assert_close(curvneg-(s+w*w)*(mxn(y)-m0),-1)

# Finite checks for positivity of the curvature and the sine-product margin.
for w in [.02,.05,.1,.3,.7,1,1.4,wc,1.6,2,4,10,50]:
    for s in [0,1e-5,.01,.1,.25,.5,1,2,4,8,16,25,40]:
        aa,g=taylor(s)
        vv=s+w*w
        square=vv*vv*g[2]-vv*g[1]+.75*g[0]
        assert_true(square>0)
        assert_true(derivs(s,w)[1]>0)
        assert_true(g[1]*g[1]/(g[0]*g[2]) < 5/3+1e-11)
        # Renewal and the Poisson race (first-passage Laplace transform).
        if s>0:
            gamma=math.sqrt(s)
            phi=1/(math.cosh(gamma)+math.sqrt(s/(s+w*w))*math.sinh(gamma))
            renewal=(1/phi-1)/s
            assert_close(normalized_mean(s,w),renewal,rtol=1e-8,atol=1e-8)
    assert_close(derivs(0,w)[0],d1(w),rtol=1e-9,atol=1e-9)
    assert_close(normalized_mean(0,w),.5+1/w)

# Sharp regime split; convexity ensures these finite roots represent unique optima.
for w in [.02,.1,.3,.5,.8,1,1.2,1.4,wc-.01,wc-.001]:
    assert_true(d1(w)<0)
    ss=bisect_root(lambda s:derivs(s,w)[0],0,30)
    assert_true(ss>0)
    assert_true(normalized_mean(ss,w)<normalized_mean(0,w))
    assert_true(derivs(ss/2,w)[0]<0)
    assert_true(derivs((ss+30)/2,w)[0]>0)
for w in [wc,wc+.001,wc+.1,2,3,5,10,50]:
    assert_true(d1(w)>=-1e-12)
    for s in [.001,.1,1,2,4,9,20]:
        assert_true(normalized_mean(s,w)>normalized_mean(0,w))

ap=(9-wc*wc)/(6*wc**4)
coeff=ap/(2*d2(wc))
assert_close(coeff,3.4655713304274425)
for eps in [1e-3, 1e-4, 1e-5]:
    ss=bisect_root(lambda s:derivs(s,wc-eps)[0],0,1)
    assert_close(ss/eps,coeff,rtol=.001,atol=.01)

print("PASS:", checks, "finite diagnostics; analytic theorem proved separately")
print("critical w:", format(wc,'.15f'), "optimal-rate slope:",format(coeff,'.12f'))
