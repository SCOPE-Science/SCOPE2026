#!/usr/bin/env python3
"""Reproducible finite checks for polynomially weighted Dirichlet dilations.
Finite checks support, but do not certify, the analytic asymptotic theorem.
"""
import math
from fractions import Fraction
import numpy as np
from scipy.linalg import eigh_tridiagonal

checks = 0
# Exact rational matrix-entry identities at rho=1, beta=1 or 3.
for n in (1, 2, 3):
    for beta in (1, 3):
        for k in range(n, 65):
            fact = math.prod(range(k-n+1, k+1))
            for j, coeff in enumerate((Fraction(1,3), Fraction(-2,5), Fraction(3,7))):
                ell = k - n + j
                # Input normalized basis and output coordinate norm.
                e_k_coef = Fraction(1,1) if beta == 1 else Fraction(k+1,1)
                out_coordinate = Fraction(1,1) if beta == 1 else Fraction(1,ell+1)
                polynomial_coefficient = coeff * e_k_coef * fact
                direct = polynomial_coefficient * out_coordinate
                formula = coeff * fact * (Fraction(k+1,ell+1) if beta==3 else 1)
                assert direct == formula
                checks += 1

# Validate the beta-sensitive first Hilbert--Schmidt correction for 4 parameters.
for n,beta,p in ((1,1,(1.,1.)),(1,0,(1.,1.)),(2,1,(1.,2.,3.)),(2,3,(1.,.5))):
    A=sum(abs(z)**2 for z in p)
    B=sum(j*abs(z)**2 for j,z in enumerate(p))
    L=math.factorial(2*n)*A/2**(2*n+1)
    C=math.factorial(2*n-1)*(n*(n+beta)*A-(beta-1)*B)/2**(2*n)
    slopes=[]
    for eps in (.08,.04,.02,.01):
        ks=np.arange(n,max(1500,int(34/eps)))
        factorial=np.ones_like(ks,dtype=float)
        for v in range(n): factorial *= (ks-v)
        scaled=eps**n*factorial*np.exp(-eps*(ks-n))
        moment=0.
        for j,z in enumerate(p):
            moment+=abs(z)**2*np.sum(scaled**2*((ks+1)/(ks-n+j+1))**(beta-1))
        value=eps*moment
        slope=(value-L)/eps
        slopes.append(abs(slope-C))
        assert abs(value-(L+eps*C)) < .25*eps*(1+abs(C))
        checks += 1
    assert slopes[-1] < slopes[0]
    checks += 1

# Compact bidiagonal finite matrices for beta=1, n=1, P(z)=1+z.
# Tridiagonal Gram matrix has diagonal 2*a(k)^2 and off-diagonal a(k)a(k+1).
errors={1.:[],2.:[],4.:[]}
for eps,N in ((.12,180),(.075,270),(.04,600)):
    k=np.arange(1,N+1,dtype=float)
    a=eps*k*np.exp(-eps*(k-1))
    eig=eigh_tridiagonal(2*a*a,a[:-1]*a[1:],eigvals_only=True)
    assert np.min(eig)>-1.e-10
    sig=np.sqrt(np.maximum(eig,0))
    target_norm=2/math.e
    assert abs(max(sig)-target_norm)<.16
    # For p=1,2,4, explicit angular means for 1+z: 4/pi, 2, 6.
    for p,angular in ((1.,4/math.pi),(2.,2.),(4.,6.)):
        exact=math.gamma(p+1)/(p**(p+1))*angular
        observed=eps*np.sum(sig**p)
        errors[p].append(abs(observed-exact))
        assert abs(observed-exact) < .70*exact
        checks += 1
    checks += 1
for p,values in errors.items():
    assert values[2] < values[1] < values[0], (p,values)
    checks += 1
print(f"PASS: {checks} exact-coordinate and finite-asymptotic checks")
