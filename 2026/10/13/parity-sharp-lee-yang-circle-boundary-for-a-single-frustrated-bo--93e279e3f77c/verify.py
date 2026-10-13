"""Finite numerical consistency tests for the single-defect Ising ring theorem.
Uses numpy (version reported at runtime); analytic proof is independent of these tests.
"""
import numpy as np
from numpy.polynomial import Polynomial as Poly
from math import exp,log,sqrt
from itertools import product

def ising_coefficients(n,K,L):
    coeff=np.zeros(n+1)
    for spin in product((1,-1), repeat=n):
        idx=sum(a==-1 for a in spin)
        exponent=K*sum(spin[i]*spin[i+1] for i in range(n-1))+L*spin[-1]*spin[0]
        coeff[idx]+=exp(exponent)
    return coeff

def U(k):
    U0=Poly([1]);U1=Poly([0,2])
    if k==0:return U0
    if k==1:return U1
    for _ in range(2,k+1):U0,U1=U1,Poly([0,2])*U1-U0
    return U1

def Q(n,K,L):
    c2=1-exp(-4*K)
    lam=(exp(-2*(K+L))-1)/c2
    return Poly([0,1])*U(n-1)+lam*U(n-2)

def predicted(n,K,L):
    crit= -K-(n%2)*0.5*log(1+(1-exp(-4*K))/(n-1))
    return L>=crit-1e-12,crit

def test():
    checks=0;thresholds=0;identity=0
    for n in range(3,12):
        for K in (0.18,0.53,1.1):
            _,crit=predicted(n,K,0)
            for L in (crit+0.06,crit+0.18,crit-0.07,crit-0.2,0.0):
                a=ising_coefficients(n,K,L)
                roots=np.roots(a[::-1]/a[-1]);iscircle=bool(np.max(abs(abs(roots)-1))<1e-5)
                assert iscircle==predicted(n,K,L)[0], (n,K,L,roots)
                checks+=1
            c=sqrt(1-exp(-4*K));
            for angle in (0.2,0.6,1.17,1.9,2.6):
                L=crit+0.15
                h=1j*angle
                TK=np.array([[np.exp(K+h),np.exp(-K)],[np.exp(-K),np.exp(K-h)]],dtype=complex)
                TL=np.array([[np.exp(L+h),np.exp(-L)],[np.exp(-L),np.exp(L-h)]],dtype=complex)
                zt=np.trace(np.linalg.matrix_power(TK,n-1)@TL)
                x=np.cos(angle)/c
                rhs=2*np.exp(K+L)*(np.exp(K)*c)**(n-2)*(c*c)*Q(n,K,L)(x)
                assert abs(zt-rhs)<1e-7*max(1,abs(zt)),(n,K,L,zt,rhs)
                identity+=1
            qc=Q(n,K,crit)
            if n%2==0:
                assert abs(qc(0))<1e-10 and abs(qc.deriv()(0))<1e-9
            else:
                assert abs(qc(0))<1e-10 and abs(qc.deriv()(0))<1e-9 and abs(qc.deriv(2)(0))<1e-9
                assert abs(qc.deriv(3)(0))>0.01
            thresholds+=1
    print('VERIFY_OK numerical_zero_loci=',checks,'transfer_identities=',identity,'boundary_multiplicities=',thresholds,'numpy=',np.__version__)
if __name__=='__main__':test()
