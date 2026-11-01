"""Numerical supplementary checks for the angular Fock Hilbert-Schmidt defect.
Uses no external data. Run: python checker.py (requires numpy/scipy).
"""
import math
import numpy as np
from scipy.special import gammainc, gammaln

def norms(x, k):
    n = np.arange(int(x + 18*math.sqrt(x) + 100 + k))
    c0 = gammainc(n+1.,x)
    a = k/2.
    r = np.exp(2*gammaln(n+a+1)-gammaln(n+1)-gammaln(n+k+1))
    ck = gammainc(n+a+1,x)
    return float(np.sum(c0*c0)),float(np.sum(r*ck*ck))

checks=0
for k in (1,2,3,5):
    ds=[]
    for x in (500,2000,8000):
        radial,angular=norms(x,k)
        assert radial>=angular-1e-7,(k,x,radial,angular)
        ds.append(radial-angular)
        checks+=1
    predicted=(k*k/4)*math.log(4)
    for j in (0,1):
        observed=ds[j+1]-ds[j]
        assert abs(observed-predicted)<0.09*predicted+0.02,(k,j,observed,predicted)
        checks+=1
# Exact matrix coefficient (polar integration) vs gamma shape formula for k=2.
from scipy.integrate import quad
for x in (3.0,10.0):
    for n in (0,1,3):
        direct=quad(lambda t: math.exp(-t)*t**(n+1),0,x)[0]/math.sqrt(math.factorial(n)*math.factorial(n+2))
        formula=math.exp(gammaln(n+2)-0.5*(gammaln(n+1)+gammaln(n+3)))*gammainc(n+2,x)
        assert abs(direct-formula)<5e-12,(x,n,direct,formula)
        checks+=1
print('PASS',checks,'numeric assertions: positivity, logarithmic slopes, exact coefficient quadratures')
