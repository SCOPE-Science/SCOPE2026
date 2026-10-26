"""Reproduce three-site mean-calibration boundary; Python 3 with NumPy/SciPy.
Public proof is analytic; these floating-point checks are non-exhaustive corroboration.
"""
import math
import numpy as np
from scipy.linalg import expm, logm

def corrected(c, h, p=1.0, q=1.0):
    C=np.diag(c)
    M=np.array([[0.,p,0.],[0.,0.,q],[0.,0.,0.]])
    Q=expm(-h*C)@expm(h*M)
    K=C+np.real(logm(Q))/h
    return M,C,Q,K

def check():
    tested=0
    for h in [0.2,0.5,1.,2.]:
        for c in [[0.,0.,0.],[1.,0.,1.],[0.,1.,0.],[1.,2.,3.],[3.,2.,1.],[0.,2.,1.],[1.,0.,2.],[2.,0.,1.],[0.,0.,3.],[3.,0.,0.],[0.5,2.,1.5]]:
            for p,q in [(1.,1.),(.3,4.),(2.,.7)]:
                M,C,Q,K=corrected(c,h,p,q)
                assert np.linalg.norm(expm(h*(K-C))-Q,ord=np.inf)<4e-12
                assert abs(K[0,0])+abs(K[1,1])+abs(K[2,2])<4e-12
                assert K[0,1]>0 and K[1,2]>0
                d=c[0]+c[2]-2*c[1]
                if abs(d)>1e-9:
                    assert np.sign(K[0,2])==-np.sign(d) or abs(K[0,2])<1e-11
                    assert abs(K[0,2])>1e-11
                else:assert abs(K[0,2])<3e-12
                # The mean operator from independent Gaussian exponentials of known variances
                # is exp(C h) exp((K-C)h) = exp(Mh).
                assert np.linalg.norm(expm(C*h)@expm(h*(K-C))-expm(M*h),ord=np.inf)<4e-11
                tested+=1
    for h in [0.05,.2,.5,1.,2.,3.]:
        M,C,Q,K=corrected([1.,0.,1.],h)
        exact=h*math.exp(h)*(h-math.sinh(h))/(math.expm1(h)**2)
        assert abs(K[0,2]-exact)<3e-12
    print('VERIFIED:',tested,'three-state independent checks and six closed-form special cases')

if __name__=='__main__':check()
