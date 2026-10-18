#!/usr/bin/env python3
"""Independent numerical tests for the coherence-window absorption theorem."""
from math import pi, sin, sqrt
import numpy as np
from scipy.integrate import quad
from scipy.special import roots_legendre
from scipy.sparse import diags
from scipy.sparse.linalg import expm_multiply

checks = 0

def check(condition, message):
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1

def band_matrix(K, eta=1.0, nodes=1400):
    x,w = roots_legendre(nodes)
    k=(x+1)*pi/2; w=w*pi/2
    kernel=w*(2*eta/pi)*np.sin(k)/(1+eta*eta+2*eta*np.sin(k))
    V=np.exp(1j*np.outer(k,np.arange(K)))
    return (V.conj().T*kernel)@V

def p_out(n,eta):
    return (2*eta/pi)*quad(lambda q: q**(2*n-2)*(1-q*q)/(1+eta*eta*q*q),0,1,epsabs=1e-13)[0]

def two_site_matrix(n,eta):
    P=band_matrix(2,eta)
    return P+np.diag([p_out(n,eta),p_out(n+1,eta)])

# Exact K=1 and K=2 spectral claims.
for K,expected in [(1,1-2/pi),(2,2/pi)]:
    actual=np.linalg.eigvalsh(band_matrix(K))[-1]
    check(abs(actual-expected)<2e-10,f'closed K={K} value')
T2=band_matrix(2)
check(abs(T2[0,1]-1j*(4/pi-1))<2e-10,'chiral off-diagonal')
check(abs(np.linalg.eigvalsh(T2)[0]-(2-6/pi))<2e-10,'opposite phase minimum')

# Sharp finite-K inequalities and explicit sine packet.
for K in [1,2,3,4,5,8,12,20,32,64]:
    T=band_matrix(K)
    eigen=np.linalg.eigvalsh(T)
    lam=4*sin(pi/(2*(K+1)))**2
    e2=lam**2+4*sin(pi/(K+1))**2/(K+1)
    deficiency=1-eigen[-1]
    check(deficiency>=lam/4-2e-10,f'gap lower K={K}')
    check(deficiency<=lam/4+e2/8+2e-10,f'gap upper K={K}')
    check(0<eigen[-1]<1,f'strict feasible K={K}')
    j=np.arange(K)
    c=(-1j)**j*sqrt(2/(K+1))*np.sin(pi*(j+1)/(K+1))
    check(abs(np.vdot(c,c).real-1)<3e-13,f'packet norm K={K}')
    deficiency_packet=1-np.vdot(c,T@c).real
    check(lam/4-2e-10<=deficiency_packet<=lam/4+e2/8+2e-10,f'explicit extremizing family K={K}')

# Rate optimality and symmetry on randomized complex preparations.
for K in [2,4,9]:
    for seed in range(8):
        rng=np.random.default_rng(100*K+seed)
        c=rng.standard_normal(K)+1j*rng.standard_normal(K)
        c/=np.linalg.norm(c)
        peak=np.vdot(c,band_matrix(K,1)@c).real
        for eta in [0.12,0.45,0.8,1.25,2.4,7.5]:
            v=np.vdot(c,band_matrix(K,eta)@c).real
            check(v<peak+5e-12,f'matched rate K={K} seed={seed} eta={eta}')

# Finite-distance correction, stochastic positivity, and far-field bound.
for n in [2,3,5,10,25]:
    for eta in [0.1,0.5,1.0,3.0,10.0]:
        M=two_site_matrix(n,eta)
        eigen=np.linalg.eigvalsh(M)
        check(eigen[0]>-1e-10 and eigen[-1]<1+1e-10,f'absorption effect n={n}')
        check(p_out(n,eta)<=1/(2*pi*n*(n-1))+5e-13,f'uniform error n={n}')
        check(eigen[-1]<=2/pi+1/(pi*n*(n-1))+5e-11,f'safe distant optimum n={n}')

# Independent direct finite-lattice non-Hermitian time evolution.
N=500; n=8; eta=1.3
H=diags([-0.5*np.ones(N-1),np.ones(N),-0.5*np.ones(N-1)],[-1,0,1],format='lil',dtype=np.complex128)
H[0,0]-=0.5j*eta
H=H.tocsc()
for a,b in [(1.0,0.0j),(1/sqrt(2),-1j/sqrt(2)),(1/sqrt(2),1j/sqrt(2))]:
    psi=np.zeros(N,dtype=complex)
    psi[n-1]=a;psi[n]=b
    states=expm_multiply(-1j*H,psi,start=0,stop=120,num=601,endpoint=True)
    measured=1-np.vdot(states[-1],states[-1]).real
    target=np.vdot(np.array([a,b]),two_site_matrix(n,eta)@np.array([a,b])).real
    check(measured<=target+3e-5,'finite-time absorption <= eventual')
    check(target-measured<0.002,'direct propagated absorption convergence')

print(f'PASS: {checks} explicit checks. Exact proof is in RESULT.md.')
print('K=2 far-field maxima/minima:',2/pi,2-6/pi)
print('K=64 sharp asymptotic coefficient estimate:',(1-np.linalg.eigvalsh(band_matrix(64))[-1])*65**2)
