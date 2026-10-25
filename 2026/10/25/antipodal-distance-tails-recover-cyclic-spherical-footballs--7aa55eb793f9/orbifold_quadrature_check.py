"""Independent finite-epsilon quadrature for distance tails on spherical rotation quotients.
This standalone verification uses the exact cosine condition rather than the asymptotic integrand.
"""
import numpy as np
from scipy.special import roots_legendre
from math import pi

def tail(q, eps, n=160):
    nodes, weights=roots_legendre(n)
    a=pi/q
    uu=eps*(nodes+1)/2
    dd=a*(nodes+1)/2
    U=uu[:,None]; D=dd[None,:]
    A=np.cos(U); B=np.sin(U)*np.cos(D)
    R=np.sqrt(A*A+B*B)
    phase=np.arctan2(B,A)
    vmax=np.maximum(0,np.arccos(np.clip(np.cos(eps)/R,-1,1))-phase)
    integrated=np.sin(U)*(-2*np.sin(vmax/2)**2)
    # 1-cos v = 2sin^2(v/2)
    integrated=-integrated
    return 0.5*(weights[:,None]*weights[None,:]*integrated).sum()*(eps/2)*0.5

def c_formula(q):
    a=pi/q
    return (1/np.sin(a)**2-np.cos(a)/(a*np.sin(a)))/32

if __name__=='__main__':
    for q in [2,3,4,8]:
      c=c_formula(q)
      for eps in [.30,.15,.075,.0375]:
        obs=tail(q,eps);print(f'q={q}, eps={eps:g}, P={obs:.14g}, normalized={obs/eps**4:.11g}, C={c:.11g}, rel_err={obs/eps**4/c-1:+.4e}')
