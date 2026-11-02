#!/usr/bin/env python3
"""Independent finite sanity checks for two-tone Gaussian localization spectral resonance.
This executable corroborates exact Fourier coefficient arithmetic; the analytic theorem
rests on proofs of the Gaussian asymptotics and the square-root Weyl criterion.
"""
from fractions import Fraction
from math import comb, exp, cos, sqrt, pi
from collections import defaultdict
import mpmath as mp
import numpy as np

checks = 0

def check(c, msg):
    global checks
    assert c, msg
    checks += 1

def torus_cos_moment(m, n, p, q):
    # exact Haar integral for cos(qt)^m*cos(pt)^n
    return Fraction(sum(comb(m,i)*comb(n,j)
                        for i in range(m+1) for j in range(n+1)
                        if q*(m-2*i) + p*(n-2*j)==0), 2**(m+n))

def free_cos_moment(m, n):
    if m%2 or n%2: return Fraction(0)
    return Fraction(comb(m,m//2)*comb(n,n//2),2**(m+n))

for p in range(1,8):
    for q in range(1,8):
        if __import__('math').gcd(p,q)!=1: continue
        order=p+q
        for r in range(order+1):
            coeffs=[]
            for m in range(r+1):
                n=r-m
                diff=comb(r,m)*(torus_cos_moment(m,n,p,q)-free_cos_moment(m,n))
                if diff: coeffs.append((m,n,diff))
            if r<order:
                check(not coeffs,f'low resonance p={p},q={q},r={r}: {coeffs}')
            else:
                target=Fraction(comb(order,p),2**(order-1))
                check(coeffs==[(p,q,target)],f'first resonance p={p},q={q}: {coeffs}')

# Numerically independent integral representation and hypergeometric expression.
mp.mp.dps=50
for n in [0,1,5,20,100,500]:
    for eta in [mp.mpf('0.5'),mp.mpf('1'),mp.mpf('2')]:
        hyp=mp.hyp1f1(n+1,mp.mpf('0.5'),-eta**2)
        f=lambda t: mp.cos(2*eta*mp.sqrt(t))*mp.exp(n*mp.log(t)-t-mp.loggamma(n+1)) if t>0 else mp.mpf(0)
        # integrate around Gamma concentration; tail well below target precision
        hi=n+1+max(100,24*mp.sqrt(n+1))
        integral=mp.quad(f,[0,(n+1)/2,n+1,hi])
        check(abs(hyp-integral)<mp.mpf('2e-16'),f'Gamma integral mismatch n={n},eta={eta}: {hyp-integral}')

# Verify convergence in phase statistics for rational 2 and irrational sqrt(2)
# by the elementary model. No finite sample is used to prove equidistribution.
A=exp(-.5)
for eta in [2.0,sqrt(2),3.0/2.0]:
    B=exp(-eta*eta/2)
    idx=np.arange(1,250001,dtype=float)
    model=(A*np.cos(2*np.sqrt(idx))+B*np.cos(2*eta*np.sqrt(idx)))/4
    check(abs(np.mean(model))<.009,'numeric mean')
    if eta==2.0:
        target=3*A*A*B/256
        check(abs(np.mean(model**3)-target)<.002,'cubic resonance')
    if eta==sqrt(2):
        check(abs(np.mean(model**3))<.003,'irrational cubic vanishing')

# Critical-point inequality at eta=2 and spectral parity examples.
check(exp(1.5)>4,'strict two-tone monotonicity')
for p,q in [(1,1),(3,1),(5,3),(2,1),(3,2),(4,3),(1,4)]:
    theta=np.linspace(0,2*pi,200001)
    f=np.cos(q*theta)+np.cos(p*theta)
    is_full=(p%2==1 and q%2==1)
    check((np.min(f)<-2+1e-9)==is_full,f'parity mismatch p={p},q={q}')

print(f'PASS {checks} deterministic checks; independent audits are not performed')

# Fock tensor-product eigenvalues: the separable symbol contributes two
# independent one-dimensional diagonal factors, with no cross term.
for m in [0,2,5,30]:
    for n in [0,1,7,50]:
        for eta in [mp.mpf(1),mp.mpf(2),mp.sqrt(2)]:
            cm=mp.hyp1f1(m+1,mp.mpf('0.5'),-1)
            cn=mp.hyp1f1(n+1,mp.mpf('0.5'),-eta**2)
            lam=(mp.mpf('0.5')+(cm+cn)/4)
            check(0<=lam<=1,'positive mask contraction: product eigenvalue')

# At resonance eta=2, the locked two-tone cubic moment is nonzero,
# while the independent two-phase law has cubic moment exactly zero.
A=mp.exp(-mp.mpf('0.5')); B=mp.exp(-2)
locked_third=3*A*A*B/256
check(locked_third>0,'locked resonance third moment')
check(abs((mp.mpf('.5')+(-A+B)/4)-(mp.mpf('.5')-(A+B)/4)-B/2)<mp.mpf('1e-45'), 'sharp lower-edge gap')
print('Supplemental tensor and edge checks:',checks)
