"""Independent finite quadrature checks for spectral-merger chord-tail crossover.
This does not replace the all-dimensional mathematical proof.
"""
import numpy as np
from scipy.special import roots_legendre, gamma

z, w = roots_legendre(1024)
ang = np.arccos(z)  # not equispaced: use equispaced midpoint quadrature below
th = 2*np.pi*(np.arange(36000)+0.5)/36000
u2 = np.sin(th)**2

def profile(lam):
    return float(np.mean(np.maximum(1-lam*u2, 0)**0.5))

def exact_scaled(lam,s):
    v=(1-s/2)**2
    t=lam*s*u2
    numerator=np.mean(np.sqrt(1+t)*np.maximum(1-v*(1+t),0)**0.5)
    denominator=np.mean(np.sqrt(1+t))
    return float(numerator/denominator/s**0.5)

for lam in (0.,0.5,1.,2.,8.):
    f=profile(lam)
    checks=[exact_scaled(lam,s) for s in (0.02,0.005,0.001)]
    print('lambda=',lam,'F=',f,'scaled_exact=',checks,'last_error=',abs(checks[-1]-f))
    assert abs(checks[-1]-f)<0.026
for lam in (25.,100.,400.):
    v=profile(lam)*lam**0.5
    print('large_lambda=',lam,'rescaled_F=',v)
    assert abs(v-0.5)<0.01
print('CROSSOVER_VERIFICATION_PASS')
