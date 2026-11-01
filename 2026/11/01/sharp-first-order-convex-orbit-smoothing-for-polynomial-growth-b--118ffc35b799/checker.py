#!/usr/bin/env python3
"""Finite checks of exact convex orbit smoothing for polynomial weighted shifts.
Only finite instances are checked; no infinite-dimensional certification is claimed.
"""
from fractions import Fraction
from math import isclose, fsum, log

checks = 0

def check(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)

def coefficients(n, theta):
    """Optimal n coefficients a_0,...,a_{n-1}, n>=1; rational if theta is int."""
    if isinstance(theta,int):
        r = [Fraction(1)] + [Fraction(1, k**(2*theta)) for k in range(1,n+1)]
    else:
        r = [1.] + [k**(-2*theta) for k in range(1,n+1)]
    s0 = sum(r)
    s1 = sum(k*r[k] for k in range(n+1))
    s2 = sum(k*k*r[k] for k in range(n+1))
    den = s0*s2-s1*s1
    a=[]
    partial=0
    for k in range(n):
        partial+=r[k]*(s1-k*s0)
        a.append(partial/den)
    return r,a,s0/den

def norm2(a,r):
    b = [a[0]] + [a[k]-a[k-1] for k in range(1,len(a))] + [-a[-1]]
    return sum(b[k]*b[k]/r[k] for k in range(len(b)))

for theta in (0,1,2,3,4):
    for n in range(1,35):
        r,a,E = coefficients(n,theta)
        check(sum(a)==Fraction(1), ('mass',theta,n))
        check(all(v>0 for v in a), ('strict positivity',theta,n))
        check(norm2(a,r)==E, ('exact energy',theta,n))
        # Compute discrete weighted Laplacian at each of the n coefficients.
        gradient=[a[0]]+[a[k]-a[k-1] for k in range(1,n)]+[-a[-1]]
        flux=[gradient[k]/r[k] for k in range(n+1)]
        check(all(flux[k]-flux[k+1]==E for k in range(n)), ('Euler-Lagrange',theta,n))
        # A perturbation with zero total mass cannot reduce the energy.
        for k in range(1,n):
            check(isclose(float(flux[k]-flux[k+1]),float(flux[0]-flux[1]),rel_tol=1e-12),('gradient consistency',theta,n,k))
        uniform=[Fraction(1,n)]*n
        check(norm2(uniform,r)>=E, ('uniform comparison',theta,n))

# Numeric non-integral exponents: direct variational identities and asymptotics.
for theta in (0.25,0.49,0.5,0.75,1.0,1.2,1.49,1.5,1.6,2.1):
    prev=1e100
    for n in (10,25,50,100,250,500,1000):
        r,a,E=coefficients(n,theta)
        check(all(v>0 for v in a),('real weights positive',theta,n))
        check(abs(sum(a)-1)<3e-8,('real mass',theta,n))
        check(isclose(float(norm2(a,r)),float(E),rel_tol=2e-7),('real energy',theta,n))
        check(E<=prev*(1+3e-8),('monotone',theta,n))
        prev=E
    # Asymptotic rate against derived sharp coefficient (rel error decreases with n).
    n=50000
    r,a,E=coefficients(n,theta)
    alpha=2*theta
    if theta < .5:
        target=(3-alpha)*(2-alpha)**2/n**(3-alpha)
    elif theta == .5:
        target=2/n**2
    elif theta < 1.5:
        target=(3-alpha)/n**(3-alpha)
    elif theta == 1.5:
        target=1/log(n)
    else:
        target=None
    if target is not None and theta not in (1.49,):
        check(.5<E/target<2.1,('asymptotic scale',theta,E,target))

print('PASS',checks,'finite assertions')
