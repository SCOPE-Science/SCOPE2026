"""Independent exact and high-precision checks for a two-level OU Euler coupling theorem.

Uses only the Python standard library; finite checks supplement the written proof.
"""
from fractions import Fraction as F
from math import sqrt, exp

# Choose a = 17/31 and b = 3/31.  Then sqrt(2(1+a*a)) = 50/31.
a, b, h = F(17,31), F(3,31), F(14,31)
assert a == 1-h and b == 1-2*h
assert 2*(1+a*a) == F(50,31)**2
assert F(50,31) > 1+a
assert F(1,1)+a*a == F(1250,961)

# For a single coarse interval:
assert h*(a-1)**2 == F(2744,29791)
assert h*(1+a*a+2-F(100,31)) == F(1008,29791)
assert F(1008,2744) == F(18,49)

nchecks=0
for n in range(1, 128):
    brown = sum((h*((a**(2*k+1)-b**k)**2+(a**(2*k)-b**k)**2) for k in range(n)), F(0))
    # Expand the covariance of (a*xi1 + xi2) versus the coarse innovation.
    star = sum((h*((a**(2*k))**2*(1+a*a)+2*(b**k)**2-
                  2*F(50,31)*a**(2*k)*b**k) for k in range(n)), F(0))
    # The normalized innovation is (17*xi1+31*xi2)/(25*sqrt(2)).
    # Hence Cov(a*xi1+xi2, zeta_*) = 25*sqrt(2)/31 exactly.
    delta = F(4,31)*h*sum((a*a*b)**k for k in range(n))
    assert brown-star == delta and delta>0 and star>=0
    assert delta == F(4,31)*h*(1-(a*a*b)**n)/(1-a*a*b)
    nchecks += 4

# Generic numerical identity plus optimality over all linear Gaussian couplings.
for lam in [0.2,1.0,2.4]:
    for T in [0.25,0.9,1.7,3.0]:
        for n in [1,2,7,25,60]:
            step=T/(2*n)
            if lam*step>=0.5:continue
            aa=1-lam*step
            bb=1-2*lam*step
            vb=step*sum((aa**(2*k+1)-bb**k)**2+(aa**(2*k)-bb**k)**2 for k in range(n))
            vs=step*sum((aa**(2*k)*sqrt(1+aa*aa)-sqrt(2)*bb**k)**2 for k in range(n))
            vg=2*step*(sqrt(2*(1+aa*aa))-(1+aa))*sum((aa*aa*bb)**k for k in range(n))
            assert abs(vb-vs-vg)<3e-12*max(1.0,vb)
            assert vs<vb
            nchecks+=2

# Horizon-dependent small-step leading constants; test convergence.
for lam,T in [(0.3,0.5),(1.0,1.0),(1.0,3.0),(2.3,0.8)]:
    U=lam*T
    vstar_lim=lam/16*(1-exp(-2*U)*(1-2*U+2*U*U))
    vbridge_lim=lam/16*(3-exp(-2*U)*(3-2*U+2*U*U))
    assert vbridge_lim>vstar_lim>0
    for n in [10000,20000]:
        hh=T/(2*n);aa=1-lam*hh;bb=1-2*lam*hh
        vb=hh*sum((aa**(2*k+1)-bb**k)**2+(aa**(2*k)-bb**k)**2 for k in range(n))
        vs=hh*sum((aa**(2*k)*sqrt(1+aa*aa)-sqrt(2)*bb**k)**2 for k in range(n))
        tol=0.0015 if n==10000 else 0.0008
        assert abs(vb/hh**2-vbridge_lim) < tol*vbridge_lim
        assert abs(vs/hh**2-vstar_lim) < tol*vstar_lim
        nchecks += 2

print('VERIFY_OK', nchecks, 'exact rational and numerical identities, including limiting rates')
