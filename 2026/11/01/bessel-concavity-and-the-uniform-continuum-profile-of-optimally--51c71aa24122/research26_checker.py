"""Numerical supplementary checks for the Bessel profile of optimal second-difference smoothing.
Run: python research26_checker.py (requires numpy and scipy)."""
import numpy as np
from scipy.fft import dct
from scipy.integrate import quad
from scipy.special import j1

MASS = np.pi/2

def h(s):
    z = np.sqrt(max(0., 1.-s*s))
    return MASS*j1(MASS*z)/z if z > 1.e-9 else MASS*MASS/2.

def K(s):
    s=abs(s)
    if s>=1.: return 0.
    v1=quad(h,0,s,epsabs=3e-11)[0]
    v2=quad(lambda v:(1-v)*h(v),s,1,epsabs=3e-11)[0]
    return np.pi/2*((1-s)*v1+v2)

def F(t):
    return 1. if t==0 else -np.pi*np.cos(np.sqrt(t*t+MASS*MASS))/(t*t)

def coefficients(n):
    N=n+1
    theta=np.pi/(2*N)
    c=np.cos(theta)
    a=(1+c)/2
    A=2*np.sin(theta)/(N*(1+c))
    M=2*N+12
    ang=(np.arange(M)+.5)*np.pi/M
    x=np.cos(ang)
    L=a*(x+1)-1
    y=A*np.cos(N*np.arccos(np.clip(L,-1,1)))/(x-1)
    co=dct(y,type=2)/M
    return np.r_[co[0]/2,co[1:n+1]/2]

def main():
    cnt=0
    for t in (0.,.1,.3,.7,1.,2.,4.,6.,10.,15.):
        inv=2*quad(lambda s: np.cos(t*s)*K(s),0,1,epsabs=3e-9)[0]
        assert abs(inv-F(t))<1.0e-8,(t,inv,F(t))
        cnt+=1
    assert abs(2*quad(K,0,1)[0]-1)<1e-9
    cnt+=1
    assert abs(K(0)-0.7414177759714685)<1e-9
    cnt+=1
    # Check strict concavity and monotonicity of the limiting profile on a mesh.
    pts=np.linspace(0,1,81)
    kval=[K(float(x)) for x in pts]
    assert all(kval[i]>kval[i+1] for i in range(len(kval)-1))
    cnt+=1
    for n in (8,16,32,64,128,256):
        N=n+1
        u=coefficients(n)
        assert abs(u[0]+2*np.sum(u[1:])-1)<1e-8
        cnt+=1
        errs=[]
        for k in range(n+1):
            errs.append(abs(N*u[k]-K(k/N)))
            cnt+=1
        error=max(errs)
        print('n',n,'maximum sampled profile error',round(error,9))
        assert error<.40
        cnt+=1
    print('Passed',cnt,'supplementary numerical assertions.')

if __name__=='__main__':main()
