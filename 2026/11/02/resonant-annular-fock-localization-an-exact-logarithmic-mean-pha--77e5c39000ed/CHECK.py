"""Supplementary finite matrix computations for annular Gaussian localization."""
import numpy as np
from scipy.optimize import brentq
from math import factorial
from scipy.special import gammainc, gammaln
from numpy.linalg import eigvalsh

def resonance_outer(s,m):
    return brentq(lambda t:(t-s)/np.log(t/s)-m,s+1e-9,10*m+10)

def mat(s,t,eps,n=24,nang=512):
    theta=2*np.pi*np.arange(nang)/nang
    u=t+eps*np.cos(theta)
    k=np.arange(n)
    i,j=np.meshgrid(k,k,indexing='ij')
    p=1+(i+j)/2
    coef=np.exp(gammaln(p)-.5*(gammaln(i+1)+gammaln(j+1)))
    M=np.zeros((n,n),complex)
    for tt,uu in zip(theta,u):
        M+=coef*(gammainc(p,uu)-gammainc(p,s))*np.exp(1j*(i-j)*tt)/nang
    return .5*(M+M.conj().T)

for m,s in [(1,.3),(2,.3),(3,.7),(5,2.3)]:
    t=resonance_outer(s,m)
    L=(t-s)/np.log(t/s)
    diag=np.array([(gammainc(n+1,t)-gammainc(n+1,s)) for n in range(25)])
    g=np.exp(-t)*t**(m-.5)/np.sqrt(factorial(m-1)*factorial(m))/2
    assert abs(L-m)<1e-10
    assert abs(diag[m]-diag[m-1])<1e-10
    assert np.count_nonzero(abs(diag-max(diag))<1e-10)==2
    errs=[]
    for e in [.015,.0075,-.015,-.0075]:
        largest=eigvalsh(mat(s,t,e))[-1]
        pred=diag[m]+abs(e)*g
        errs.append(abs(largest-pred)/(e**2))
        assert abs(largest-pred)<2*e**2
    print(f'm={m} s={s} t={t:.9f} cusp_coef={g:.9f}, max_error_ratio={max(errs):.5f}')
print('all annular resonance checks passed')
