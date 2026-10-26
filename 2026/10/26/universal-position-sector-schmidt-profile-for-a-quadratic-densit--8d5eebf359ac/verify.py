"""Independent numerical checks for a massless-oscillator spatial-sector Schmidt law.

Dependencies: numpy, scipy. Run: python verify.py
The infinite-level theorem uses Airy asymptotics, not finite enumeration.
"""
from math import pi, sqrt, log
import numpy as np
from scipy.special import ai_zeros, airy
from scipy.optimize import brentq
from scipy.fft import fft, fftfreq

checks = 0

def require(test, detail):
    global checks
    if not bool(test):
        raise AssertionError(detail)
    checks += 1

def airy_root(n):
    zeros, derivative_zeros, _, _ = ai_zeros((n + 1)//2)
    return float(-derivative_zeros[(n-1)//2] if n%2 else -zeros[n//2-1])

def energy(n, g, omega):
    r = airy_root(n)
    f = lambda w: w**3 * (w-omega) - g*g*r**3
    high = max(omega+1., sqrt(10*g*n)+omega+3.)
    while f(high)<0:
        high *= 2
    return brentq(f, omega, high, xtol=1e-13)

def excitation(n,g,omega):
    w=energy(n,g,omega)
    p=w/(4*w-3*omega)
    return w,p

def shape_moments(n, grid=32768):
    """Scaled momentum Airy eigenstate and Fourier-derived spatial observables."""
    r = airy_root(n)
    h = r**(-1.5)
    length=5.0
    dK=length/grid
    K=(np.arange(grid)-grid//2)*dK
    F=airy((abs(K)-1)*h**(-2/3))[0]
    if n%2 == 0:
        F *= np.sign(K)
    F=F/np.sqrt(np.sum(F*F)*dK)
    X=2*pi*h*fftfreq(grid,dK)
    weights=abs(fft(F))**2
    weights/=sum(weights)
    m1=float(np.dot(abs(X),weights))
    m2=float(np.dot(X*X,weights))
    ch={t:float(np.dot(np.cos(t*X), weights)) for t in (.4,1.2,3.5)}
    return m1,m2,ch

for n in (1,2,3,4,5,10,20,50,100,200):
    r=airy_root(n)
    require(r>0, ('positive Airy root',n))
    if n>1:
        require(r>airy_root(n-1), ('interlacing',n))
    for g,omega in ((.2,3.),(1.,2.),(3.,1.)):
        w,p=excitation(n,g,omega)
        require(w>omega,('energy above continuum',n,g,omega))
        require(abs(w**3*(w-omega)-g*g*r**3)<1e-6*max(1.,g*g*r**3),('spectral identity',n,g,omega))
        require(.25<p<1.,('atomic participation',n,g,omega))
        # Direct scalar virial norm ratio vs normalized two-component occupation.
        ratio=w/(3*(w-omega))
        require(abs(p-ratio/(1+ratio))<1e-12,('virial and normalization',n,g,omega))

for n in (3,5,10,20,50,100,200):
    eta,m2,char=shape_moments(n)
    require(abs(m2-1/3)<2e-4,('virial second moment',n,m2))
    require(0<eta<sqrt(m2),('strict spatial variance',n,eta,m2))
    if n>=20:
        require(abs(eta-.5)<4e-4,('uniform-orbit first moment',n,eta))
        for t,value in char.items():
            require(abs(value-np.sinc(t/pi))<4e-4,('sinc spatial law',n,t,value))
    for g,omega in ((.2,3.),(1.,2.),(3.,1.)):
        w,p=excitation(n,g,omega)
        offdiag=sqrt(3*p*(1-p))*eta
        rho=np.array([[1-p,offdiag],[offdiag,p]])
        eigen=np.linalg.eigvalsh(rho)
        require(eigen[0]>0,('positive Schmidt eigenvalues',n,g,omega))
        require(abs(eigen.sum()-1)<1e-12,('reduced trace',n,g,omega))
        require(abs(np.linalg.det(rho)-p*(1-p)*(1-3*eta*eta))<1e-12,('Schmidt determinant',n,g,omega))

for s in (.1,sqrt(3)/pi,2.):
    target=brentq(lambda z:z**3*(z-1)-(3*pi*s/4)**2, 1., 100.)
    ps=target/(4*target-3)
    for n in (50,200,800):
        g=1.;omega=sqrt(n/s)
        w,p=excitation(n,g,omega)
        require(abs(w/omega-target)<.6/n,('double scaling energy',s,n,w/omega,target))
        require(abs(p-ps)<.10/n,('double scaling occupation',s,n,p,ps))

sstar=sqrt(3)/pi
zstar=1.5
require(abs(zstar**3*(zstar-1)-(3*pi*sstar/4)**2)<1e-12,'critical exact equation')
pstar=zstar/(4*zstar-3)
require(abs(pstar-.5)<1e-12,'critical half occupation')
for n in (50,100,200):
    eta,_,_=shape_moments(n)
    g=1.;omega=2.
    _,p=excitation(n,g,omega)
    rho=np.array([[1-p,sqrt(3*p*(1-p))*eta],[sqrt(3*p*(1-p))*eta,p]])
    target=np.array([[.75,.375],[.375,.25]])
    if n>=100:
        require(np.max(abs(rho-target))<.31/sqrt(n),('fixed parameters limiting Schmidt matrix',n,rho))
require(abs((.25*.75 - .375**2)-3/64)<1e-12,'limiting determinant')
require(abs((.75**2+.25**2+2*.375**2)-29/32)<1e-12,'limiting purity')
print(f'PASS: {checks} root, norm, spatial Fourier, Schmidt, and double-scaling assertions')
