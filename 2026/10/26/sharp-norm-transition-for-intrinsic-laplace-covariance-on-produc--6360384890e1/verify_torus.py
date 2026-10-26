"""Supplementary arithmetic checks for toroidal lp Laplace covariance; no proof by enumeration."""
import math
import numpy as np
from scipy.integrate import quad


def constant(a,p):
    integrand=lambda s: math.exp(-a*math.hypot(math.pi,s)) * math.pi/(math.hypot(math.pi,s)) if p==2 else (math.exp(-a*(math.pi**p+s**p)**(1/p))*math.pi**(p-1)*(math.pi**p+s**p)**((1-p)/p))
    return -a/(math.pi**2)*quad(integrand,0,math.pi,epsabs=1e-12)[0]


def coeff_fft(a,p,N=1024):
    th=2*math.pi*np.minimum(np.arange(N),N-np.arange(N))/N
    D=(th[:,None]**p+th[None,:]**p)**(1/p)
    f=np.exp(-a*D)
    return np.fft.fft2(f).real/(N*N)


def exact_p1(a,n):
    return a*(1-(-1)**n*math.exp(-a*math.pi))/(math.pi*(a*a+n*n))

if __name__=='__main__':
    for p in (1.,1.5,2.,3.,8.):
        a=1.
        v=coeff_fft(a,p,1024)
        print('p=',p,'a=',a,'coeff(20,0)=',f'{v[20,0]:.12g}', 'coeff(32,0)=',f'{v[32,0]:.12g}', 'coeff(64,0)=',f'{v[64,0]:.12g}')
        if p>1:
            c=constant(a,p)
            print('  sharp asymptotic constant:',f'{c:.12g}','observed 64^2 coefficient:',f'{64*64*v[64,0]:.12g}')
            assert c<0
            if p>=2: assert v[64,0]<-1e-7
        else:
            for n in [0,2,5,20,32,64]:
                expected=exact_p1(a,n)*exact_p1(a,0)
                assert abs(v[n,0]-expected)<1e-6, (n,expected,v[n,0])
    n=64; p=2.; N=128
    g=2*math.pi*np.minimum(np.arange(N),N-np.arange(N))/N
    K=np.exp(-np.hypot(g[:,None],g[None,:]))
    lam=np.fft.fft2(K).real/(N*N)
    assert lam[24,0]<-4e-6
    print('N=128 grid, p=2, a=1, frequency (24,0), normalized eigenvalue:',f'{lam[24,0]:.12g}')
    print('ALL TESTS PASS')
