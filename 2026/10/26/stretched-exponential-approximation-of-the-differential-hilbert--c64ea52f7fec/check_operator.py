"""Finite-section numerical checks for the differential Hilbert matrix and dyadic quadrature.
These checks illustrate analytic estimates; finite sections are not a proof of infinite-rank claims.
"""
import numpy as np
from scipy.special import gammaln, roots_legendre

def weights(g,n):
    k=np.arange(n,dtype=float)
    return np.exp(gammaln(g+2)+gammaln(k+1)-gammaln(k+g+2))

def matrix(alpha,beta,N):
    n=np.arange(N)
    w0=weights(alpha,N); w1=weights(beta,N)
    return (n[:,None]+1)/(n[:,None]+n[None,:]+1)*np.sqrt(w1[:,None]/w0[None,:])

def quad_matrix(alpha,beta,N,J,m):
    x,wx=roots_legendre(m)
    k=np.arange(N)
    u=(k+1)*np.sqrt(weights(beta,N))
    v=1/np.sqrt(weights(alpha,N))
    A=np.zeros((N,N))
    for j in range(J):
        h=2.0**(-j-2); c=1-3*h
        for xi,wi in zip(x,wx):
            t=c+h*xi
            A+=(h*wi)*np.outer(u*t**k,v*t**k)
    return A

if __name__=='__main__':
    for alpha,beta in [(-.5,1.75),(-.5,2.5),(-.9,1.2)]:
        N=100
        M=matrix(alpha,beta,N)
        print('parameters',alpha,beta,'Hilbert-Schmidt finite norm',np.linalg.norm(M))
        for J,m in [(4,4),(6,6),(8,8),(10,10)]:
            Q=quad_matrix(alpha,beta,N,J,m)
            diff=np.linalg.norm(M-Q,ord=2)
            print(' J=m=',J,'rank<=',J*m,'finite operator error',f'{diff:.5e}')
        ss=np.linalg.svd(M,compute_uv=False)
        print(' finite singular values',[(idx,float(ss[idx-1])) for idx in [1,3,5,10,20,40] ])
