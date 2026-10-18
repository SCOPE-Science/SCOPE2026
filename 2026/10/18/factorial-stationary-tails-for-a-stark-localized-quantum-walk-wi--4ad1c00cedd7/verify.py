"""Numerical consistency checks for the stationary Stark-reset tail."""
import numpy as np
import mpmath as mp
from scipy.linalg import expm
from scipy.special import jv

for h,F,t in [(0.7,1.3,2.4),(1.2,0.8,0.9),(0.2,3.1,1.7)]:
    width=63
    sites=np.arange(-width,width+1)
    H=np.diag(F*sites.astype(float))-h*np.diag(np.ones(2*width),1)-h*np.diag(np.ones(2*width),-1)
    amplitude=expm(-1j*t*H)[:,width]
    arg=4*h/F*np.sin(F*t/2)
    error=max(abs(abs(amplitude[width+k])**2-jv(k,arg)**2) for k in range(-11,12))
    assert error<2e-10,(h,F,t,error)
mp.mp.dps=55
count=0
for h,F,r in [(0.7,2.0,0.6),(0.9,1.7,1.2),(0.5,1.1,2.0)]:
    A=4*mp.mpf(h)/F
    period=2*mp.pi/F
    a=mp.mpf(r)/F
    for n in [30,50,80]:
        raw=r/(1-mp.exp(-r*period))*mp.quad(lambda t:mp.exp(-r*t)*mp.besselj(n,A*mp.sin(F*t/2))**2,[0,period/2,period])
        asym=r*mp.sqrt(mp.pi)/(F*mp.sqrt(n)*mp.sinh(mp.pi*a))*(2*mp.mpf(h)/F)**(2*n)/mp.factorial(n)**2
        assert 0.80<float(raw/asym)<1.20,(h,F,r,n,raw/asym)
        # Compare the sine-power renewal integral with its independent finite product.
        sine=r/(1-mp.exp(-r*period))*mp.quad(lambda t:mp.exp(-r*t)*mp.sin(F*t/2)**(2*n),[0,period/2,period])
        exact=mp.binomial(2*n,n)/4**n*mp.fprod([1/(1+a*a/(j*j)) for j in range(1,n+1)])
        assert abs(sine/exact-1)<mp.mpf('1e-35'),(h,F,r,n)
        count+=1
print('VERIFY_OK finite_hamiltonians=3 bessel_integrals='+str(count)+' sine_products='+str(count))
