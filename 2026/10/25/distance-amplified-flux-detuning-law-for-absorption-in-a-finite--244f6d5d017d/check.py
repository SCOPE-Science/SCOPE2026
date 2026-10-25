"""Reproducibility checks for the finite magnetic rhombic chain with terminal sink."""
import numpy as np
from scipy.linalg import sqrtm, solve_continuous_lyapunov, expm

def chain(L,phi,gamma):
    n=L+1
    B=np.zeros((n,2*L),dtype=complex)
    for j in range(L):
        B[j,2*j]=B[j,2*j+1]=1
        B[j+1,2*j]=np.exp(0.5j*phi)
        B[j+1,2*j+1]=np.exp(-0.5j*phi)
    H=np.block([[np.zeros((n,n)),B],[B.conj().T,np.zeros((2*L,2*L))]])
    K=B@B.conj().T
    return H,K

def mean_absorption(L,g,gamma):
    n=L+1
    K=np.diag([2]+[4]*(n-2)+[2]).astype(float)
    for j in range(L): K[j,j+1]=K[j+1,j]=g
    B=np.asarray(sqrtm(K),dtype=complex)
    H=np.block([[np.zeros((n,n)), B],[B.conj().T,np.zeros((n,n))]])
    A=-1j*H;A[0,0]-=gamma/2
    X=solve_continuous_lyapunov(A.conj().T,-np.eye(2*n))
    return X[L,L].real

checks=0
for L in range(1,5):
    for phi in [0.4,1.7,2.6,3.0]:
        for gamma in [0.5,1,2.0]:
            H,K=chain(L,phi,gamma)
            g=2*np.cos(phi/2)
            expected=np.diag([2]+[4]*(L-1)+[2]).astype(complex)
            for j in range(L): expected[j,j+1]=expected[j+1,j]=g
            assert np.max(abs(K-expected))<1e-12
            checks+=1
            n=L+1
            A=-1j*H;A[0,0]-=gamma/2
            init=np.zeros(3*L+1,complex);init[L]=1
            for t in [0.4,1.2]:
                psi=expm(t*A)@init
                assert 0 <= np.linalg.norm(psi)**2 <= 1+1e-10
                checks+=1
            tau=mean_absorption(L,g,gamma)
            P=np.zeros((n,n));P[0,0]=1
            AO=np.block([[-gamma/2*P,np.eye(n)],[-expected.real,np.zeros((n,n))]])
            W=np.block([[np.eye(n),np.zeros((n,n))],[np.zeros((n,n)),np.linalg.inv(expected.real)]])
            XO=solve_continuous_lyapunov(AO.T,-W)
            assert abs(XO[L,L]/tau-1)<2e-6,(L,phi,gamma,tau,XO[L,L])
            checks+=1
for L in range(1,5):
    for gamma in [0.4,1,3]:
        ratios=[]
        for g in [0.5,0.3,0.2]:
            tau=mean_absorption(L,g,gamma)
            ratios.append(tau*g**(2*L)/(gamma*4**(L-1)))
        assert ratios[-1]>0
        assert abs(ratios[-1]-1)<abs(ratios[0]-1)
        checks+=1
print('PASSED',checks,'matrix/survival/mean/limiting checks')
