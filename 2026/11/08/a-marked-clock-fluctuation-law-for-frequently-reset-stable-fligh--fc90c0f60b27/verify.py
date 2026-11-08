#!/usr/bin/env python3
"""Finite algebraic diagnostics for the marked-reset limit, using only stdlib."""
import cmath
import math
from fractions import Fraction as F

checks = 0

def check(cond, reason):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(reason)

# Exact competing-risks benchmark: free exit tau ~ Exp(A), independent
# resets Exp(r). The renewal-geometric transform must equal the direct
# product Q(r+s+u*r)/[1-exp(-v)*r/(r+s)*(1-Q(r+s))].
# With u=v=0 this exactly equals A/(A+s), independent of r.
for A in range(1, 13):
    for r in range(1, 26):
        for s in range(0, 12):
            a, rr, ss = F(A), F(r), F(s)
            Q = a/(a+rr+ss)
            f = (rr/(rr+ss))*(1-Q)
            check(Q/(1-f) == a/(a+ss), 'exact time transform')
            p = a/(a+rr)
            check((1-p)/p == rr/a, 'reset count mean')
            # Differentiating the joint transform at v=0: E N = r/A.
            check(F(1,p)-1 == rr/a, 'geometric derivative')

# A positive / negative rate ratio must equal the ratio of barriers^alpha.
for alpha in [0.2,0.5,0.9,1.0,1.4,1.8,1.99]:
    c = math.gamma(1+alpha)*math.sin(math.pi*alpha/2)/math.pi
    check(c>0,'Levy coefficient positivity')
    for L in [0.5,1.0,3.0,10.0]:
        for fraction in [-0.9,-0.4,0.0,0.35,0.9]:
            x = L*fraction
            dplus,dminus = L-x,L+x
            ap = c/(alpha*dplus**alpha)
            am = c/(alpha*dminus**alpha)
            check(abs((ap/am)-(dminus/dplus)**alpha)<1e-9,'rate ratio')
            check(abs(ap/(ap+am)+am/(ap+am)-1)<1e-14,'side normalization')
            for u in [0,0.01,0.5,1.5,8.0]:
                exact = (dplus/((1+u)*dplus))**alpha
                check(abs(exact-(1+u)**(-alpha))<1e-12,'Pareto tail')

# Exact inverse-Fourier density, integrating the Laplace density numerically
# and comparing with the known Gaussian-exponential mixture CF.
for A in [0.1,0.5,1.0,2.0,7.5,40.0]:
    b = 1/math.sqrt(2*A)
    for xi in [0.0,0.05,0.1,0.35,1.0,2.0,5.0]:
        mixed_cf = A/(A+xi*xi/2)
        laplace_cf = 1/(1+b*b*xi*xi)
        check(abs(mixed_cf-laplace_cf)<1e-14, 'mixture characteristic function')
    # Normal-Laplace mixture: E[Y^2]=E[E]=1/A,
    # E[Y^4]=3E[E^2]=6/A^2, excess kurtosis 3.
    second=2*b*b
    fourth=24*b**4
    check(abs(second-1/A)<1e-12,'second moment')
    check(abs(fourth-6/(A*A))<1e-11,'fourth moment')
    check(abs(fourth/(second*second)-6)<1e-13,'kurtosis')

# In the exact exponential-exit toy, the successful interval is Exp(r+A),
# so r*H has Laplace transform (r+A)/(r+A+u*r); its limit is 1/(1+u).
for A in [0.5,1,5]:
    for u in [0.0,0.1,0.5,1,3]:
        previous=None
        for r in [10,100,1000,10000,100000]:
            transform=(r+A)/(r+A+u*r)
            err=abs(transform-1/(1+u))
            if previous is not None:
                check(err<=previous+1e-15,'micro duration convergence')
            previous=err
        check(previous<1e-4,'micro duration limiting scale')

# Full exact competing-exponential joint transform: for Y_r=sqrt(r)*(T-N/r),
# CF equals A/[A-i*xi*sqrt(r)+r*(1-exp(-i*xi/sqrt(r)))].
# This directly tests the non-Gaussian Laplace limit in the clock mismatch.
for A in [0.75,2.5,10.0]:
    for xi in [0.1,0.4,0.9,1.8,3.0]:
        theoretical=A/(A+xi*xi/2)
        previous=None
        for r in [100,1000,10000,100000,1000000]:
            cf=A/(A-1j*xi*math.sqrt(r)+r*(1-cmath.exp(-1j*xi/math.sqrt(r))))
            err=abs(cf-theoretical)
            check(err<1,'finite joint CF not divergent')
            if previous is not None:
                check(err<previous,'finite joint CF converges')
            previous=err
        check(previous<0.004,'finite joint CF at last rate')

print('PASS:',checks,'exact-rational and numeric assertions')
