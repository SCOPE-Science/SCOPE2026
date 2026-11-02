#!/usr/bin/env python3
"""Exact finite-state checks for two-patch occupancy covariance phase law.

Standard-library only.  Tests numerical/rational instances; the general results
are proved algebraically in RESULT.md rather than by a finite enumeration.
"""
from fractions import Fraction as Q
from itertools import product
from math import sqrt

checks = 0

def ensure(x):
    global checks
    assert x
    checks += 1

def stationary_direct(a, b, e, d):
    # states 00, 10, 01, 11; row generator Q
    rows = [
        [-2*a, a, a, Q(0)],
        [e+d, -(e+b+d), Q(0), b],
        [e+d, Q(0), -(e+b+d), b],
        [d, e, e, -(2*e+d)],
    ]
    mat = [[rows[j][i] for j in range(4)] + [Q(0)] for i in range(3)]
    mat.append([Q(1), Q(1), Q(1), Q(1), Q(1)])
    for i in range(4):
        pivot = next(k for k in range(i, 4) if mat[k][i])
        mat[i], mat[pivot] = mat[pivot], mat[i]
        z = mat[i][i]
        mat[i] = [v / z for v in mat[i]]
        for j in range(4):
            if j != i:
                z = mat[j][i]
                mat[j] = [mat[j][h]-z*mat[i][h] for h in range(5)]
    return [mat[i][4] for i in range(4)]

def explicit(a,b,e,d):
    h = 2*b/(2*e+d)
    k = (e+d+b*d/(2*e+d))/a
    v=1/(k+2+h)
    return (k*v,v,v,h*v)

def phase(a,b,e,d):
    return 2*b*((e+d)*(2*e+d)+b*d)-a*(2*e+d)**2

def covariance(x):
    u,v1,v2,w = x
    return u*w-v1*v2

for a,b,e,d in product([Q(1,3),Q(1),Q(3),Q(10)], [Q(1,4),Q(1),Q(4),Q(7)], [Q(1,2),Q(1),Q(3)], [Q(0),Q(1,3),Q(2),Q(4),Q(6),Q(15)]):
    pi=stationary_direct(a,b,e,d)
    pi2=explicit(a,b,e,d)
    ensure(pi==list(pi2))
    ensure(sum(pi)==1 and all(x>0 for x in pi))
    c=covariance(pi)
    ensure((c>0)-(c<0)==(phase(a,b,e,d)>0)-(phase(a,b,e,d)<0))
    for i in range(4):
        ensure(sum(pi[j]*([[-2*a,a,a,Q(0)],[e+d,-(e+b+d),Q(0),b],[e+d,Q(0),-(e+b+d),b],[d,e,e,-(2*e+d)]][j][i]) for j in range(4))==0)

# A complete double crossing in exact arithmetic, not just floating point.
a,b,e=Q(10),Q(4),Q(1)
for d,sgn in [(Q(0),-1),(Q(1),-1),(Q(2),0),(Q(4),1),(Q(6),0),(Q(8),-1)]:
    c=covariance(stationary_direct(a,b,e,d))
    ensure((c>0)-(c<0)==sgn)
    ensure(phase(a,b,e,d)==-2*(d-2)*(d-6))

# Thresholds and uniqueness of the critical b at a fixed catastrophe rate.
for aa in [Q(1,3),Q(1),Q(2),Q(3),Q(10),Q(20)]:
    ee=Q(1)
    for dd in [Q(0),Q(1),Q(3),Q(10),Q(100)]:
        threshold = float(aa)*(2*float(ee)+float(dd))/(sqrt((float(ee)+float(dd))**2+2*float(aa)*float(dd))+float(ee)+float(dd))
        for s in [0.8,1.2]:
            bb=Q.from_float(threshold*s)
            ensure((phase(aa,bb,ee,dd)>0)==(s>1))

# Analytic stationary tangency (compared with phase polynomial and derivative).
for aa in [Q(5,2),Q(3),Q(5),Q(10),Q(20)]:
    e0=1.0; a0=float(aa)
    bs=2*sqrt(e0*(a0+2*e0))-3*e0
    ds=2*e0*(bs+e0)/(bs-e0)
    F=2*bs*((e0+ds)*(2*e0+ds)+bs*ds)-a0*(2*e0+ds)**2
    Fd=2*(2*bs-a0)*ds + 2*(bs**2+3*bs*e0-2*a0*e0)
    ensure(abs(F)<1e-8*max(1,a0*ds**2))
    ensure(abs(Fd)<1e-9*max(1,a0*ds))
    ensure(e0<bs<a0/2 and ds>0)

print(f'VERIFY_OK assertions={checks}')
