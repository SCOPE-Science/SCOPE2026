#!/usr/bin/env python3
import math

def F(k, alpha, V0, d):
    q = math.sqrt(V0 + k*k)
    return k*math.tanh(k*d) + q*math.tanh(q*d) - alpha

def root(alpha, V0, d):
    lo, hi = 0.0, max(alpha, math.sqrt(V0) + alpha)
    flo, fhi = F(lo, alpha, V0, d), F(hi, alpha, V0, d)
    if not (flo < 0.0 and fhi > 0.0):
        raise AssertionError((alpha, V0, d, flo, fhi))
    for _ in range(180):
        mid = (lo + hi)/2.0
        fm = F(mid, alpha, V0, d)
        if fm > 0.0:
            hi = mid
        else:
            lo = mid
    k = (lo + hi)/2.0
    if abs(F(k, alpha, V0, d)) > 2e-13:
        raise AssertionError('root residual too large')
    return k

sub_cases = [
    (2.0, 1.0, 10.0, 0.02),
    (1.0, 0.2, 14.0, 0.02),
    (2.0, 3.0, 24.0, 0.03),
]
errs=[]
for alpha, V0, d, tol in sub_cases:
    a=(alpha*alpha-V0)/(2.0*alpha)
    b=(alpha*alpha+V0)/(2.0*alpha)
    mu=-a*a
    k=root(alpha,V0,d)
    mud=-k*k
    scaled=(mu-mud)*math.exp(2.0*a*d)
    target=4.0*a*a*b/alpha
    rel=abs(scaled/target-1.0)
    errs.append(rel)
    if rel > tol:
        raise AssertionError(('subcritical',alpha,V0,d,scaled,target,rel))

crit_cases=[
    (1.0,10.0,0.002),
    (0.5,18.0,0.004),
]
for alpha,d,tol in crit_cases:
    V0=alpha*alpha
    k=root(alpha,V0,d)
    y=k*k
    scaled=(d+1.0/(2.0*alpha))*math.exp(2.0*alpha*d)*y
    target=2.0*alpha
    rel=abs(scaled/target-1.0)
    errs.append(rel)
    if rel > tol:
        raise AssertionError(('critical',alpha,d,scaled,target,rel))

print('VERIFY_OK subcritical_cases=%d critical_cases=%d max_rel=%.6g' % (len(sub_cases),len(crit_cases),max(errs)))
