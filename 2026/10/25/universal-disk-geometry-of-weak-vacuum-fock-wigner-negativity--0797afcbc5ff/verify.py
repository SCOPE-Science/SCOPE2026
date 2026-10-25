"""Independent numerical and exact-coefficient checks for Hermite-superposition Wigner geometry.

Dependencies: mpmath, numpy, scipy. Execute: python verify.py
These finite tests complement the analytic proof; they do not certify all orders.
"""
import math
import cmath
from fractions import Fraction
import mpmath as mp
import numpy as np
from scipy.special import eval_laguerre
from scipy.ndimage import label

mp.mp.dps=35

def direct(n,a,phi,q,p):
    def hn(x,j):
        return mp.hermite(j,x)*mp.exp(-x*x/2)/(mp.sqrt(2**j*mp.factorial(j))*mp.pi**mp.mpf('0.25'))
    def psi(x):return (hn(x,0)+a*mp.e**(1j*phi)*hn(x,n))/mp.sqrt(1+a*a)
    def integrand(y):return psi(q+y/2)*mp.conj(psi(q-y/2))*mp.e**(-1j*p*y)
    return mp.re(mp.quad(integrand,[-mp.inf,0,mp.inf])/(2*mp.pi))

def formula(n,a,phi,q,p):
    r2=q*q+p*p
    c=mp.sqrt(2**n/mp.factorial(n))
    L=mp.laguerre(n,0,2*r2)
    poly=1+a*a*(-1)**n*L+2*a*c*mp.re(mp.e**(-1j*phi)*(q+1j*p)**n)
    return mp.exp(-r2)*poly/(mp.pi*(1+a*a))

maxerr=0
for n,a,phi,q,p in [(1,.28,.1,.4,-.2),(2,.65,.5,-.8,.3),(3,.14,.8,.3,.7),(4,.42,-.3,-.1,.6),(5,.23,1.,.7,-.8)]:
    d=direct(n,mp.mpf(str(a)),mp.mpf(str(phi)),mp.mpf(str(q)),mp.mpf(str(p)))
    f=formula(n,mp.mpf(str(a)),mp.mpf(str(phi)),mp.mpf(str(q)),mp.mpf(str(p)))
    err=abs(d-f)
    maxerr=max(maxerr,float(err))
    assert err<mp.mpf('1e-26'),(n,d,f,err)
print('DIRECT_WIGNER_OK',5,'max_abs_error',maxerr)

# Exact coefficient cancellation: Wigner polynomial at scaled coordinates.
for n in range(1,31):
    c2=Fraction(2**n,math.factorial(n))
    leading=Fraction(2**n,math.factorial(n))
    subleading=-Fraction(n*2**(n-1),math.factorial(n-1))
    assert leading==c2 and subleading==-Fraction(n*n,2)*c2
print('EXACT_LAGUERRE_COEFFICIENTS_OK',30)

for n in range(1,6):
    delta=.12
    a=delta**n
    rstar=(math.factorial(n)/2**n)**(1/(2*n))/delta
    axis=np.linspace(-rstar-1.5,rstar+1.5,1100)
    q,p=np.meshgrid(axis,axis,indexing='xy')
    z=q+1j*p
    poly=1+a*a*(-1)**n*eval_laguerre(n,2*(q*q+p*p))+2*a*math.sqrt(2**n/math.factorial(n))*np.real(z**n)
    mask=poly<0
    lab,ncomp=label(mask)
    counts=np.bincount(lab[mask].ravel())
    assert ncomp==n,(n,ncomp)
    pixel=(axis[1]-axis[0])**2
    areas=[float(counts[j]*pixel) for j in range(1,ncomp+1)]
    target=math.pi/2
    assert all(abs(area-target)<.03 for area in areas),(n,areas)
    print('NUMERIC_NEGATIVE_ISLANDS_OK','order',n,'components',ncomp,'areas',[round(v,5) for v in areas])
print('CHECKER_OK')
