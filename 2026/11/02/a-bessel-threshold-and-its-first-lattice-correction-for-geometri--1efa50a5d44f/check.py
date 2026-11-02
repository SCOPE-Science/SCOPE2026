"""Independent finite truncation and recurrence diagnostics for the stated Jacobi family.
Run: python check.py (requires numpy, scipy). These finite tests are not proofs.
"""
import numpy as np
from scipy.optimize import brentq
from scipy.special import jv, jn_zeros
from scipy.linalg import eigh_tridiagonal

LSTAR = float(jn_zeros(0,1)[0]**2/4)

def resonance_slope(h, lam, end_x=36.0):
    n = int(end_x / h)
    w = np.sqrt(1.0 + lam*h*h*np.exp(-np.arange(n+1)*h))
    previous, current = 0.0, 1.0
    for j in range(n):
        nxt = (2*current - (w[j-1]*previous if j else 0.0))/w[j]
        previous, current = current, nxt
    return current-previous

def root_at(h):
    return brentq(lambda lam:resonance_slope(h,lam),0.6,2.2,xtol=1e-12)

def kappa_at(lam):
    z = 2*np.sqrt(lam)
    return brentq(lambda k:jv(2*k,z), 0.0, z/2.0+2, xtol=1e-13)

def truncation_top(h,lam,end_x=30):
    n=int(end_x/h)
    off = np.sqrt(1+lam*h*h*np.exp(-np.arange(n-1)*h))/2
    return float(eigh_tridiagonal(np.zeros(n),off,select='i',select_range=(n-1,n-1),eigvals_only=True)[0])

if __name__=='__main__':
    rows=[]
    for h in [0.2,0.1,0.05,0.025]:
        root=root_at(h)
        first=LSTAR*(1-1.5*h)
        err=abs(root-first)
        assert err<3.0*h*h
        rows.append((h,root,first,err))
    print('threshold comparisons:',rows)
    for lam in [2.0,4.0]:
        k=kappa_at(lam)
        predicted=k*k/2
        measurements=[]
        for h in [0.16,0.08,0.04]:
            num=(truncation_top(h,lam)-1)/h**2
            assert num>0
            measurements.append((h,num))
        assert abs(measurements[-1][1]-predicted)<0.045
        print('Bessel coefficient:',lam,predicted,measurements)
    print('PASS: recurrence and finite-section diagnostics')
