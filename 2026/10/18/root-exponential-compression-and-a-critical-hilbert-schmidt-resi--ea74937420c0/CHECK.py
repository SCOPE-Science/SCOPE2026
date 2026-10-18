"""Finite diagnostics for weighted differential Hilbert operator compression.
All assertions concern explicitly finite matrices only.
"""
import numpy as np
from scipy.special import gammaln, beta

def weights(n, gamma):
    n=np.asarray(n,dtype=float)
    return np.exp(gammaln(gamma+2)+gammaln(n+1)-gammaln(n+gamma+2))

def matrix(alpha,beta,N,K):
    n=np.arange(N,dtype=float)
    k=np.arange(K,dtype=float)
    return ((n+1)*np.sqrt(weights(n,beta)))[:,None] * (1/np.sqrt(weights(k,alpha)))[None,:]/(n[:,None]+k[None,:]+1)

def rank_approximant(alpha,beta,N,K,J):
    n=np.arange(N,dtype=float)
    k=np.arange(K,dtype=float)
    u=(n+1)*np.sqrt(weights(n,beta))
    v=1/np.sqrt(weights(k,alpha))
    R=np.zeros((N,K),dtype=float)
    R[0,:]=u[0]*v/(k+1)
    for i in range(J):
        ix=np.where((n>=2**i)&(n<2**(i+1)))[0]
        c=1.5*2**i
        x=c-n[ix]
        y=k+c+1
        for ell in range(J):
            R[ix,:]+=(u[ix]*x**ell)[:,None]*(v/y**(ell+1))[None,:]
    return R

def run():
    a=-0.5
    for b in [1.7,2.1,2.8]:
        N,K=512,2048
        B=matrix(a,b,N,K)
        hs=np.linalg.norm(B)
        for J in [4,5,6,7]:
            R=rank_approximant(a,b,N,K,J)
            err=np.linalg.norm(B-R)
            removed=np.linalg.norm(B[2**J:,:])
            active=np.linalg.norm((B-R)[:2**J,:])
            assert active<=3**(-J)*hs*(1+1e-9),(b,J,active,hs)
            assert err<=3**(-J)*hs+removed+1e-9
            print(f'alpha={a} beta={b} dyadic J={J} finite_HS={hs:.5f} error={err:.5g} guarantee={3**(-J)*hs+removed:.5g}')
    # Compare the exact first moment to its asymptotic Mellin beta coefficient.
    b=a+2+0.2
    n=2000
    k=np.arange(100000,dtype=float)
    row=(n+1)**2*weights([n],b)[0]*np.sum(1/weights(k,a)/(n+k+1)**2)
    asym=(np.exp(gammaln(b+2)-gammaln(a+2))*beta(a+2,-a))* (n+1)**(-1-(b-a-2))
    print('large-row scaled asymptotic finite-k ratio',row/asym)
    print('critical coefficient', (a+2)*(a+3)*beta(a+2,-a))
    assert abs(row/asym-1)<0.2
    print('finite diagnostics passed')

if __name__=='__main__':run()
