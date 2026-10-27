"""Independent numerical and Fourier-Parseval checks for weighted Gaussian circular logarithmic means."""
import numpy as np
from scipy.special import spence, zeta

def variance(n,alpha,oversample=16):
    size=1 << int(np.ceil(np.log2(max(4096,oversample*n))))
    j=np.arange(1,n+1,dtype=float)
    w=j**(-alpha)
    S=w.sum()
    r=np.fft.fft(w,n=size)/S
    x=np.minimum(1.,np.maximum(0.,(r.real*r.real+r.imag*r.imag)))
    V=0.25*np.mean(spence(1.-x))
    V1=0.25*(w*w).sum()/S**2
    return V,V1

def check():
    for n in (8,16,37,128):
        for a in (0.,.25,.5,.8,1.,1.3):
            V,V1=variance(n,a)
            assert V>=V1-2e-13, (n,a,V,V1)
            assert V<=np.pi**2/24+1e-11
            if n==8:
                # exact Fourier Parseval of first covariance-chaos term
                j=np.arange(1,n+1,dtype=float)
                w=j**(-a); q=np.fft.fft(w,n=4096)/w.sum()
                assert abs(np.mean(abs(q)**2)/4-V1)<2e-13
    for n in (512,2048,8192):
        for alpha in (.5,.65,.85,1.):
            V,V1=variance(n,alpha,oversample=8)
            assert 0 <= (V-V1)/V1 < {512:.40,2048:.31,8192:.25}[n], (n,alpha,(V-V1)/V1)
    # Separate Monte Carlo verification through Jensen's root formula, not the
    # angular covariance formula used by variance().
    rng=np.random.default_rng(1766)
    for a in (0., .6, 1.2):
        n=3
        obs=[]
        for _ in range(16000):
            c=(rng.standard_normal(n)+1j*rng.standard_normal(n))/np.sqrt(2)
            c *= np.arange(1,n+1,dtype=float)**(-a/2)
            zeros=np.roots(c[::-1])
            obs.append(np.log(abs(c[-1]))+np.log(np.maximum(1.,abs(zeros))).sum())
        empirical=np.var(obs,ddof=1)
        expected,_=variance(n,a)
        assert abs(empirical-expected)/expected < .04, (a,empirical,expected)
    print('PASS: 24 first-chaos/Parseval checks, 12 remainder checks, 3 root-based Monte Carlo checks')
    print('n alpha variance leading_first_chaos ratio')
    for a in (.25,.5,.65,.85,1.,1.25):
        for n in (512,4096):
            v,v1=variance(n,a,oversample=8)
            print(n,a,format(v,'.11g'),format(v1,'.11g'),format(v/v1,'.8g'))
    for lam in (-1.,0.,1.):
        n=8192
        al=.5+lam/np.log(n)
        v,_=variance(n,al,oversample=8)
        target=(np.log(n)/(16*n))* (np.expm1(2*lam)/(2*lam) if lam else 1.)
        print('critical_half',lam,'actual',v,'target',target,'ratio',v/target)
        al=1+lam/np.log(n)
        v,_=variance(n,al,oversample=8)
        target=zeta(2,1)/(4*np.log(n)**2)*(lam/(-np.expm1(-lam)) if lam else 1.)**2
        print('critical_one',lam,'actual',v,'target',target,'ratio',v/target)
if __name__=='__main__':check()
