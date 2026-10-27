"""Reproducible finite-dimensional checks for phase-matched two-phonon Lindblad motion.

All identities concerning infinite Fock space in the companion proof are analytic;
these tests only check finite sections and special-function calculations.
Requires numpy and mpmath.
"""
from __future__ import annotations
import math
import numpy as np
import mpmath as mp

COUNT=0

def check(condition, label):
    global COUNT
    COUNT+=1
    if not condition: raise AssertionError(label)

def data(N, lam, phase=0.0):
    b=np.zeros((N,N), dtype=complex)
    for k in range(1,N): b[k-1,k]=math.sqrt(k)
    b2=b@b; bd2=b2.conj().T
    A=1/math.sqrt(1-lam**2)
    L=A*(b2-lam*np.exp(1j*phase)*bd2)
    plus=np.zeros(N,dtype=complex); minus=np.zeros(N,dtype=complex)
    plus[0]=1; minus[1]=1
    for k in range(4,N,4):
        plus[k]=plus[k-4]*lam*np.exp(1j*phase)*math.sqrt((k-3)*(k-2)/((k-1)*k))
    for k in range(5,N,4):
        minus[k]=minus[k-4]*lam*np.exp(1j*phase)*math.sqrt((k-3)*(k-2)/((k-1)*k))
    plus/=np.linalg.norm(plus); minus/=np.linalg.norm(minus)
    return b2,bd2,L,plus,minus

def generate_derivatives(N,lam,omega,gamma,nu,psi):
    b2,bd2,L,_,_=data(N,lam)
    H=np.diag(omega*np.arange(N)).astype(complex)
    A=1/math.sqrt(1-lam**2)
    L1=-1j*nu*A*lam*bd2
    L2=nu**2*A*lam*bd2
    def comm(x): return -1j*(H@x-x@H)
    def deriv(x,order):
        if order==0:
            p=L@x@L.conj().T
            q=L.conj().T@L
        if order==1:
            p=L1@x@L.conj().T + L@x@L1.conj().T
            q=L1.conj().T@L + L.conj().T@L1
        if order==2:
            p=L2@x@L.conj().T+2*L1@x@L1.conj().T+L@x@L2.conj().T
            q=L2.conj().T@L+2*L1.conj().T@L1+L.conj().T@L2
        return (comm(x) if order==0 else 0) + gamma*(p-(q@x+x@q)/2)
    rho=np.outer(psi,psi.conj())
    r1=deriv(rho,0)
    r2=deriv(r1,0)+deriv(rho,1)
    r3=deriv(r2,0)+2*deriv(r1,1)+deriv(rho,2)
    third=2*np.trace(rho@r3+3*r1@r2).real
    return -third/6

for N in (6,10,14,18):
    for lam in (.12,.35,.65):
        b2,bd2,L,plus,minus=data(N,lam)
        for psi in (plus,minus,(plus+1j*minus)/math.sqrt(2)):
            check(np.linalg.norm(L@psi)<1e-11, 'finite dark condition')
            check(abs(np.linalg.norm(psi)-1)<1e-12, 'normalization')
            check(abs(np.vdot(psi,b2@psi))<1e-12, 'orthogonal excursion')
            for omega,gamma,nu in ((.7,.6,0.),(1.3,.2,-5.2),(.9,.7,-2.),(.2,1.,2.)):
                got=generate_derivatives(N,lam,omega,gamma,nu,psi)
                B=np.linalg.norm(b2@psi)**2
                want=(2*gamma/3)*(nu+4*omega)**2/(1-lam**2)*B
                check(abs(got-want)<2e-8*max(1,abs(want)),f'cubic coefficient got={got}, want={want}')
                if abs(nu+4*omega)<1e-12:
                    check(abs(got)<1e-8, 'chirp zero leakage coefficient')
        for t in (.1,.6,1.7):
            omega=.73
            theta=-4*omega*t
            L_t=data(N,lam,theta)[2]
            U=np.diag(np.exp(-1j*omega*t*np.arange(N)))
            for psi in (plus,minus,(plus+minus)/math.sqrt(2)):
                check(np.linalg.norm(L_t@U@psi)<2e-11, 'exact phase-tracked dark sector')

mp.mp.dps=65
for zstring in ('.1','.3','.6','.9','.999999','.999999999999999999999'):
    z=mp.mpf(zstring)
    for a,b,c,linear in ((mp.mpf(1)/4,mp.mpf(1)/2,mp.mpf(3)/4,12),
                         (mp.mpf(1)/2,mp.mpf(3)/4,mp.mpf(5)/4,20)):
        F=mp.hyp2f1(a,b,c,z)
        Fp=a*b/c*mp.hyp2f1(a+1,b+1,c+1,z)
        Fpp=a*b*(a+1)*(b+1)/(c*(c+1))*mp.hyp2f1(a+2,b+2,c+2,z)
        B=(16*z*z*Fpp+linear*z*Fp)/F
        check(B>0,'positive moment')
        if z<mp.mpf('.91'):
            terms=[mp.rf(a,j)*mp.rf(b,j)/mp.rf(c,j)/mp.factorial(j)*z**j for j in range(700)]
            mean=sum(terms[j]*(16*j*j+(linear-16)*j) for j in range(len(terms)))/sum(terms)
            check(abs((B-mean)/B)<mp.mpf('1e-24'),'hypergeometric derivative and series')
        if z>mp.mpf('.999999999999'):
            ratio=B*(1-z)**2*mp.log(1/(1-z))/16
            check(mp.mpf('.8')<ratio<mp.mpf('1.05'),'zero-balanced asymptotic')

print('PASS:',COUNT,'finite and special-function assertions')
