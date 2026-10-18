"""Independent finite checks of antipodal-link quantum loss resonance formulas.
Run: python verify_cubelike_resonance.py ; requires numpy, scipy.
"""
import math
from fractions import Fraction
from itertools import product
import numpy as np
from scipy.linalg import expm, solve_continuous_lyapunov
from scipy.special import comb

COUNT=0

def require(z, note):
    global COUNT
    COUNT+=1
    if not z:
        raise AssertionError(note)

def qvec(d):
    return np.array([math.comb(d,k)/2**d for k in range(d+1)],float)

def pairset(d,r,sgn):
    return [(k,k+r) for k in range(0 if sgn<0 else 1,d-r+1,2)]

def absorption(d,lam):
    q=qvec(d)
    p=1.0
    for r in range(1,d+1,2):
        if lam == r or lam == -r:
            p-=4*sum(q[k]*q[l]/(q[k]+q[l]) for k,l in pairset(d,r,1 if lam>0 else -1))
    return p

def K_reduced(d,lam,J,gamma):
    q=qvec(d)
    v=np.sqrt(q)
    E=J*np.array([d-2*k+lam*(-1)**k for k in range(d+1)])
    return -1j*np.diag(E)-gamma/2*np.outer(v,v),v,E

def mean_nondegen(d,lam,J,gamma):
    K,v,E=K_reduced(d,lam,J,gamma)
    W=solve_continuous_lyapunov(K.conj().T,-np.eye(d+1))
    signs=(-1.)**np.arange(d+1)
    psi=signs*v
    return float(np.real(np.vdot(psi,W@psi))),W

def coeff(d,r,sgn,gamma,J):
    q=qvec(d)
    return gamma/(4*J**2)*sum((q[k]+q[l])**2 for k,l in pairset(d,r,sgn))

# Exact rational audit of resonance discontinuities and plus/minus-one identity.
for d in range(2,19):
    qq=[Fraction(math.comb(d,k),2**d) for k in range(d+1)]
    for sign in [-1,1]:
        exact=1-sum(4*qq[k]*qq[l]/(qq[k]+qq[l]) for k,l in pairset(d,1,sign))
        require(exact==Fraction(1,d+1),('unit resonance',d,sign,exact))
    for r in range(3,d+1,2):
        for sign in [-1,1]:
            actual=Fraction(1)-sum(4*qq[k]*qq[l]/(qq[k]+qq[l]) for k,l in pairset(d,r,sign))
            require(0<actual<=1,('higher resonance',d,r,sign))

# Independent full 2^d quantum Hilbert-space propagation vs reduced Fourier system.
for d in range(2,6):
    n=2**d
    for lam,gamma,J in [(0.3,0.4,1.),(1.,1.5,0.7),(-1.,0.8,1.3),(0.77,2.0,0.5)]:
        H=np.zeros((n,n),dtype=float)
        for x in range(n):
            for j in range(d):H[x,x^(1<<j)]+=J
            H[x,x^(n-1)]+=J*lam
        K=-1j*H;K[0,0]-=gamma/2
        Ksmall,v,_=K_reduced(d,lam,J,gamma)
        psi=((-1.)**np.arange(d+1))*v
        for t in [0.1,0.7,3.0,9.0]:
            a=np.linalg.norm(expm(K*t)[:,n-1])**2
            b=np.linalg.norm(expm(Ksmall*t)@psi)**2
            require(abs(a-b)<1e-10,('full/reduced',d,lam,gamma,t,a,b))

# Stable Lyapunov integral, positive semidefinite, direct formula, resonance divergence.
for d in range(2,10):
    for gamma,J in [(0.4,1.),(1.3,0.9),(2.,1.5)]:
        for lam in [.37,-.63,1.31]:
            T,W=mean_nondegen(d,lam,J,gamma)
            K,v,E=K_reduced(d,lam,J,gamma)
            require(np.linalg.norm(K.conj().T@W+W@K+np.eye(d+1),ord=np.inf)<3e-7,('Lyapunov residual',d,lam))
            require(np.linalg.eigvalsh((W+W.conj().T)/2).min()>-1e-8,('positive time',d,lam))
            q=v**2
            yy=-np.array([sum((q[i]+q[j])/(E[i]-E[j]) for j in range(d+1) if i!=j)/(2*v[i]) for i in range(d+1)])
            signs=(-1)**np.arange(d+1)
            model=(d+1)/gamma
            for i in range(d+1):
                for j in range(i+1,d+1):
                    model+=gamma*(signs[i]*signs[j]-1)*v[i]*v[j]*(v[j]*yy[i]-v[i]*yy[j])/(E[i]-E[j])
            require(abs(T-model)<3e-7*max(1,T),('explicit mean formula',d,lam,T,model))
        for r in range(1,min(d,4)+1,2):
            for sgn in [-1,1]:
                if not pairset(d,r,sgn):continue
                lam0=sgn*r
                delta=.00025
                T,_=mean_nondegen(d,lam0+delta,J,gamma)
                target=coeff(d,r,sgn,gamma,J)
                require(abs(delta**2*T-target)<.05*target+1e-6,('resonance coefficient',d,r,sgn,T,target))

# Gaussian central-binomial local asymptotic for large dimensions.
for d in [100,200,500,1000,2000]:
    from scipy.special import gammaln
    ks=np.arange(d+1)
    q=np.exp(gammaln(d+1)-gammaln(ks+1)-gammaln(d-ks+1)-d*np.log(2))
    C=sum((q[k]+q[k+1])**2 for k in range(1,d,2))/4
    expected=1/(2*np.sqrt(np.pi))
    require(abs(np.sqrt(d)*C-expected)<.012,('large-d coefficient',d,np.sqrt(d)*C,expected))

print(f'VERIFY_OK {COUNT} exact-rational, full-Hilbert, Lyapunov, sharp-resonance and large-d checks')
