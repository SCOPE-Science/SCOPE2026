"""Numerical finite-section checks for weighted Bergman concentration shape expansion.
The computations illustrate, rather than prove, the infinite-dimensional claim.
"""
import numpy as np
from scipy.special import beta, betainc, gammaln
from scipy.linalg import eigvalsh

def coefficients(a, n):
    j=np.arange(n, dtype=float)
    return np.exp(gammaln(a+1+j)-gammaln(a+1)-gammaln(j+1))

def matrix(a,H,eps,h,N=15,Q=400):
    theta=2*np.pi*np.arange(Q)/Q
    v=H+eps*h(theta)
    if np.min(v)<=0:raise ValueError('bad positive radial parameter')
    u=v/(1+v)
    c=coefficients(a,N)
    K=np.zeros((N,N),dtype=np.complex128)
    for m in range(N):
        for n in range(N):
            p=(m+n)/2+1
            I=beta(p,a)*betainc(p,a,u)
            K[m,n]=a*np.sqrt(c[m]*c[n])*np.mean(I*np.exp(1j*(n-m)*theta))
    return (K+K.conj().T)/2

def qval(a,u,n):
    b=a*u;B=b
    if n==1:return 0.0
    for k in range(2,n+1):
        b*=u*(a+k-1)/k
        B+=b
    return 1-(a+n)*b/((a+1)*B)

def verify():
    print('a,H,q2 analytic, q2 formula, monotone qn')
    for a in [0.1,0.7,1,2.4,10]:
        for H in [0.05,1,10]:
            u=H/(1+H)
            q=[qval(a,u,n) for n in range(1,26)]
            assert abs(q[0])<1e-11 and min(np.diff(q[1:]))>=-1e-12
            assert abs(q[1]-(2-u)/(2+(a+1)*u))<1e-11
            print(a,H,'q2',round(q[1],9),'q25',round(q[-1],9))
    a=1.7; H=.9;u=H/(1+H)
    theta=2*np.pi*np.arange(512)/512
    h=lambda t: np.cos(2*t)+.5*np.cos(3*t)
    baseline=1-(1+H)**(-a)
    q2=qval(a,u,2);q3=qval(a,u,3)
    coefficient=a*(a+1)/(1+H)**(a+2)*(q2*.25+q3*.0625)
    print('predicted quadratic deficit', coefficient)
    for eps in [.08,.04,.02,.01,.005]:
        K=matrix(a,H,eps,h,N=13,Q=512)
        d=(baseline-eigvalsh(K)[-1])/eps**2
        print('eps',eps,'finite-section deficit coefficient',d,'relerr',d/coefficient-1)
        assert abs(d/coefficient-1)<2
    print('All spot tests passed')

if __name__=='__main__':verify()
