"""Supplementary numerical verification for a critical spherical Bessel-mode gap.
Requires NumPy and SciPy. Numerical checks are NOT a proof of an infinite claim.
"""
from math import gamma, pi, sqrt
import numpy as np
from scipy.special import jv
from scipy.special import jn_zeros
from numpy.polynomial.legendre import leggauss

def mean_abs_cos(q):
    return gamma((q+1)/2)/(sqrt(pi)*gamma((q+2)/2))

def moments(d, q, cells=320, nodes=140):
    nu = d/2-1
    x,w = leggauss(nodes)
    k = np.arange(cells, dtype=float)[:,None]
    r = pi*(k+(1+x[None,:])/2)
    u0 = jv(nu,r)/r**nu
    u1 = jv(nu+1,r)/r**nu
    a0 = r**(d-1)*np.abs(u0)**q
    a1 = r**(d-1)*np.abs(u1)**q
    int0 = float((pi/2)*np.sum(a0*w[None,:]))
    int1 = float((pi/2)*np.sum(a1*w[None,:]))
    qc = 2*d/(d-1)
    if q>qc:
        alpha=(d-1)*(q-qc)/2
        common=(2/pi)**(q/2)*mean_abs_cos(q)*(cells*pi)**(-alpha)/alpha
        return int0+common,int1+common,int0-int1
    return int0,int1,int0-int1

def constants(d, cells=320):
    qc=2*d/(d-1)
    nu=d/2-1
    a=(d-1)/2
    residue=(2/pi)**(qc/2)*mean_abs_cos(qc)/a
    _,_,gap=moments(d,qc,cells=cells)
    K=(2*pi)**d*(2/qc)*gap*residue**(-1/d)
    rel=(2/qc)*gap/residue
    return qc,residue,gap,K,rel

if __name__=='__main__':
    for d in (3,4):
        qc,A,D,K,rel=constants(d)
        assert abs(qc-2*d/(d-1))<1e-14
        assert A>0 and D>0 and K>0 and rel>0
        print('d',d,'qc',qc,'residue',A,'D',D,'K',K,'relative',rel)
        for eps in (.2,.1,.05):
            x,y,z=moments(d,qc+eps)
            gamma_gap=(2*pi)**d*(x**(2/(qc+eps))-y**(2/(qc+eps)))
            normalized=gamma_gap/((2*pi)**d*x**(2/(qc+eps)))
            print(' epsilon',eps,'D_eps',z,'K_emp',gamma_gap/eps**(1/d),'ratio_emp',normalized/eps)
            assert x>y>0 and 0<gamma_gap
            assert abs(gamma_gap/eps**(1/d)/K-1)<.3
            assert abs(normalized/eps/rel-1)<.3
    print('NUMERICAL_SUPPORT_PASS: two dimensions, six near-endpoint cases; analytic argument necessary.')
