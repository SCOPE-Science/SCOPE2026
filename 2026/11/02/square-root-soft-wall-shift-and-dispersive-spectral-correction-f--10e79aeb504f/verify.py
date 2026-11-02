#!/usr/bin/env python3
"""Independent numerical checks for the interval quadratic-penalty diffusion spectrum.
No numerical sample is used as a proof of an infinite-range assertion.
"""
import math
import mpmath as mp
import numpy as np
from scipy.linalg import eigh_tridiagonal

mp.mp.dps=60
CHECKS=0

def check(test, label):
    global CHECKS
    CHECKS+=1
    if not test:
        raise AssertionError(label)

def close(x,y,tol,label):
    check(abs(x-y)<=tol,label)

beta=mp.sqrt(mp.pi/2)
d=beta*(mp.log(2)-mp.pi/6)
check(d>0,'positive dispersive coefficient')

def R(v):
    return v/mp.sqrt(2)*mp.gamma((1-v)/2)/mp.gamma(1-v/2)

def eig(n,j,a=1):
    n=mp.mpf(n); a=mp.mpf(a)
    kappa=j*mp.pi/2
    f=lambda k: a*k+mp.atan(mp.sqrt(n)*R(k*k/n)/k)-kappa
    k=mp.findroot(f,kappa/(a+beta/mp.sqrt(n)))
    check(0<k*k/n<1,'valid OU order')
    check(abs(f(k))<mp.mpf('1e-45'),'exact matching residual')
    return k*k

def approxs(n,j,a=1):
    n=mp.mpf(n); a=mp.mpf(a)
    s=n**(-mp.mpf('.5'))
    kappa=j*mp.pi/2
    A=a+beta*s
    eff=kappa**2/A**2
    refined=eff-2*d*kappa**4*s**3/A**5
    return eff,refined

# Verify gamma ratio by independent parabolic-cylinder evaluation and derivative.
for nu in [mp.mpf('0.01'), mp.mpf('0.1'),mp.mpf('0.33'),mp.mpf('0.72')]:
    z0=mp.pcfd(nu,0)
    slope=mp.diff(lambda z: mp.exp(z*z/4)*mp.pcfd(nu,z),mp.mpf(0))/z0
    close(slope,R(nu),mp.mpf('1e-49'),'D_nu derivative at origin')
    u=lambda z:mp.exp(z*z/4)*mp.pcfd(nu,z)/z0
    for z in [mp.mpf('0.1'),mp.mpf('0.7'),mp.mpf('1.3')]:
        ode=mp.diff(u,z,2)-z*mp.diff(u,z)+nu*u(z)
        close(ode,mp.mpf(0),mp.mpf('1e-42'),'exterior OU eigen ODE')

# Compare exact roots, beta effective-wall law, and cubic dispersive correction.
for a in [mp.mpf('0.7'),mp.mpf('1'),mp.mpf('1.8')]:
 for j in range(1,5):
    for n in [400,1600,6400,25600]:
        lam=eig(n,j,a)
        eff,corrected=approxs(n,j,a)
        check(lam<eff,'strict below effective wall spectrum')
        check(corrected<eff,'negative dispersion')
        check(abs(lam-corrected)<abs(lam-eff),'refined better than pure length')
        check(lam>0,'positive eigenvalue')
        if n>=1600:
            # A conservative, non-asymptotic numeric consistency check.
            check(abs(lam-corrected)<mp.mpf(50000)*(j**6)*n**(-mp.mpf('2.5'))/a**8,'O(n^-5/2) scale')

# Numerically confirm the exact first asymptotic coefficient for fixed j.
for j in (1,2,3):
 for n in (10000,100000,1000000):
    actual=eig(n,j)
    eff,_=approxs(n,j)
    coeff=n**mp.mpf('1.5')*(actual-eff)
    target=-2*d*(j*mp.pi/2)**4
    check(abs(coeff-target)/abs(target)<mp.mpf('0.07'), 'dispersive limit')

# Independent finite-difference solution of the symmetrized Schrödinger operator.
# For n=36, V=n*d(x,[-a,a])^2/2, H=-d²/dx²+(V')²/4-V''/2.
n=36.;a=1.;L=2.1;N=20001
h=2*L/(N+1)
x=np.linspace(-L+h,L-h,N)
dist=np.maximum(np.abs(x)-a,0)
Vpp=(np.abs(x)>a)*n
potential=(n*dist)**2/4-Vpp/2
main=2/h**2+potential
sub=np.full(N-1,-1/h**2)
vals=eigh_tridiagonal(main,sub,select='i',select_range=(0,3),check_finite=False, eigvals_only=True,lapack_driver='stebz')
check(abs(vals[0])<0.005,'Schrodinger ground state near zero')
for j in (1,2,3):
    exact=float(eig(n,j))
    check(abs(vals[j]-exact)<0.006, f'independent finite-difference eigenvalue {j}')

print(f'PASS {CHECKS} assertions')
print(f'beta={float(beta):.15f}; d={float(d):.15f}')
print('n=100,a=1 exact eigenvalues 1..3: '+', '.join(f'{float(eig(100,j)):.12f}' for j in (1,2,3)))
print('Schrodinger finite-difference n=36 eigenvalues 0..3: '+', '.join(f'{v:.10f}' for v in vals))
print('Scope: numeric checks only. Infinite-mode-index and remainder assertions use analytical proof.')
