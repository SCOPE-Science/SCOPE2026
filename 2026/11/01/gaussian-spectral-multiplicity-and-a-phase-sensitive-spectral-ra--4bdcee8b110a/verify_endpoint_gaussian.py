#!/usr/bin/env python3
"""Supplementary finite checks for a Gaussian-weighted Fock composition endpoint.

Only numerical/algebraic consistency checks: the proof in RESULT.md supplies
all infinite-dimensional operator-theoretic conclusions.
"""
import math
import cmath
import numpy as np

CHECKS = 0

def check(condition, message):
    global CHECKS
    assert condition, message
    CHECKS += 1

def kernel_gaussian(q, tau, z, w):
    # 0<q<1; tau positive real; q=abs(a)**2.
    D = 1 - 4*tau*tau
    return D**(-.5)*cmath.exp((q*z*w.conjugate() + tau*q*(z*z+(w.conjugate())**2))/D)

def bargmann_multiplier_kernel(q, z, w):
    k = 1-q
    M = q**(-.5)
    return M/math.sqrt(1+k)*cmath.exp(
        z*w.conjugate()/(1+k) - k*(z*z+(w.conjugate())**2)/(2*(1+k)))

def compact_top_singular(q, tau):
    u = 2*abs(tau)
    up=math.sqrt((1+q)**2-u*u)
    down=math.sqrt((1-q)**2-u*u)
    L=2/(up+down)
    r=(up-down)/(up+down)
    return math.sqrt(L),r

rng=np.random.default_rng(91135)
for q in (0.07,0.2,0.4,0.7,0.95):
    tau=(1-q)/2
    for _ in range(16):
        z=complex(*rng.normal(size=2))
        w=complex(*rng.normal(size=2))
        # Rotate the quadratic term by pi/2; the Bargmann multiplication model.
        original=kernel_gaussian(q,tau,1j*z,1j*w)
        model=bargmann_multiplier_kernel(q,z,w)
        check(abs(original-model)<1e-10*max(1,abs(model)), 'endpoint Gaussian kernel identity')
    # spectral radius of all real-a powers matches q^(-n/4).
    for n in (1,2,3,4,6):
        qn=q**n
        tn=(1-qn)/2
        up=math.sqrt((1+qn)**2-(2*tn)**2)
        top=math.sqrt(2/up)
        check(abs(top-qn**(-.25))/max(1,qn**(-.25))<1e-8,'critical norm limit')
    for ratio in (0.1,0.2,0.4,0.7,0.95,0.99):
        top,r=compact_top_singular(q,tau*ratio)
        check(0<r<1 and 0<top<=q**(-.25)+1e-9,'subcritical norm monotonic bound')

for q in (0.1,0.3,0.7):
    for ang in (0.02,0.4,1.0,1.57,2.01,3.0):
        a=math.sqrt(q)*cmath.exp(1j*ang)
        lhs=(1-q)*abs(1+a*a)
        rhs=1-q*q
        check(lhs<rhs-1e-12,'non-real slope makes square compact')
    for a in (math.sqrt(q),-math.sqrt(q)):
        check(abs((1-q)*abs(1+a*a)-(1-q*q))<1e-12,
              'real slopes stay critically noncompact under squaring')

# Compare finite-rank monomial-matrix singular values in an interior example.
q=0.25; a=math.sqrt(q); tau=0.13; N=110
W=np.zeros((N,N))
for n in range(N):
    for j in range((N-1-n)//2+1):
        m=n+2*j
        # log factorial for stable elementary monomial coefficients
        W[m,n]=a**n*tau**j/math.factorial(j)*math.exp(.5*(math.lgamma(m+1)-math.lgamma(n+1)))
s=np.linalg.svd(W,compute_uv=False)
top,r=compact_top_singular(q,tau)
for n in range(10):
    check(abs(s[n]-top*r**(n/2))<1e-7,'interior finite-section singular value')

print(f'PASS: {CHECKS} supplementary algebraic and numerical checks.')
