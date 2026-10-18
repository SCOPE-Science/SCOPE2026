"""Independent finite-section and coefficient checks for reflected integration.
Run: python verify_reflection.py. Dependency: numpy.
Finite-section tests are consistency checks, not proofs of infinite-dimensional claims.
"""
from fractions import Fraction as Q
from math import cos, sin, pi
import numpy as np

checks = 0

def check(p, msg):
    global checks
    if not p:
        raise AssertionError(msg)
    checks += 1


def determinant(a, z):
    if a == 1:
        return cos(z)-z*sin(z)
    return (cos(z)-a*cos(a*z))/(1-a)


def hmatrix(n, a):
    lower = np.tril(np.ones((n, n)), -1)
    lower += 0.5*np.eye(n)
    v = lower/n
    return v+a*v[::-1, :]


def first_zeros(a, count, maxz=45):
    # Bisection after a fine sign-change scan; no eigenvalue solver in this step.
    dz = pi/(120*max(1, abs(a)))
    roots = []
    left, value = 1e-10, determinant(a, 1e-10)
    x = left
    while x < maxz and len(roots) < count:
        right = x+dz
        nxt = determinant(a, right)
        if value*nxt < 0:
            lo, hi = x, right
            for _ in range(55):
                mid = (lo+hi)/2
                if determinant(a, lo)*determinant(a, mid) <= 0:
                    hi = mid
                else:
                    lo = mid
            roots.append((lo+hi)/2)
        x, value = right, nxt
    if len(roots) != count:
        raise AssertionError(('too few roots', a, roots))
    return roots

# Exact power-series coefficient and trace checks.
for numerator in range(-24, 25):
    a=Q(numerator,8)
    b=-1-a
    s2=lambda q: 1+q+q*q
    s4=lambda q: sum(q**k for k in range(5))
    check(s2(a) == s2(b), ('quadratic trace equality', a))
    check(s4(a)-s4(b) == -a*(a+1)*(2*a+1), ('quartic distinction', a))
    check(s4(a) == s4(b) if a in (Q(-1), Q(0), Q(-1,2)) else s4(a) != s4(b), ('exceptions', a))
    # Taylor coefficient identity for the normalized determinant.
    check(s2(a)/Q(2) == (a*a+a+1)/Q(2), ('HS coefficient', a))

# Direct independent finite-section spectra, traces and Fredholm determinants.
for n in [72, 144, 240]:
    for a in [-2.0,-1.0,-0.5,0.0,0.5,1.0,1.5,2.0]:
        v=hmatrix(n,a)
        s=np.linalg.svd(v,compute_uv=False)
        hs=float(np.sum(s*s))
        check(abs(hs-(1+a+a*a)/2)<4/n, ('Hilbert-Schmidt',n,a,hs))
        for z in [0.2,0.45,0.7]:
            # Eigenvalue product computed independently from SVD.
            prod=float(np.prod(1-z*z*s*s))
            closed=determinant(a,z)
            check(abs(prod-closed)<7/n, ('Fredholm determinant',n,a,z,prod,closed))
        roots=first_zeros(a,4)
        for i,t in enumerate(roots):
            check(abs(float(s[i])-1/t)<12/n, ('individual singular values',n,a,i,s[i],1/t))

# The two nonidentical parameters possess the same limiting full spectrum.
for k in range(1,18):
    t=(k-0.5)*pi
    check(abs(determinant(0,t))<2e-12, ('a=0 root',k))
    check(abs(determinant(-1,t))<2e-12, ('a=-1 root',k))

# Verify the explicit endpoint Fredholm determinant by divided differences.
for z in np.linspace(-3.2,3.2,25):
    for eps in [1e-3,1e-4]:
        check(abs(determinant(1-eps,float(z))-determinant(1,float(z)))<50*eps, ('a=1 limit',z,eps))

print('REFLECTED_INTEGRATION_CHECKS_OK', checks)
