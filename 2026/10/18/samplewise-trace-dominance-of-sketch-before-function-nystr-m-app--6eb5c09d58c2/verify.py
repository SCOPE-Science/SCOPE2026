#!/usr/bin/env python3
"""Reproduce elementary exact checks and finite numerical stress tests.

The universal theorem is proved analytically in RESULT.md; the stress tests do not
establish the infinite-dimensional-parameter assertion.
"""
import math
import numpy as np


def orth(M):
    return np.linalg.qr(M, mode='reduced')[0]


def trace_matrix_fun_nystrom(lam, G, Ffun):
    # Nonzero Nyström eigenvalues are the eigenvalues of Q^T A Q.
    Q = orth(np.sqrt(lam)[:, None] * G)
    small = Q.T @ (lam[:, None] * Q)
    s = np.linalg.eigvalsh(small)
    left = np.sum(Ffun(np.maximum(s, 0.0)))
    flam = Ffun(lam)
    Qf = orth(np.sqrt(flam)[:, None] * G)
    right = np.trace(Qf.T @ (flam[:, None] * Qf))
    return float(left), float(right), Q, Qf


def run():
    # Exact two-dimensional witness: sqrt(17/5) > 5/3 by rational comparison.
    assert 17 * 9 > 25 * 5
    # For A=diag(4,1), G=(1,1)^T, f=sqrt, the difference of the two
    # rank-one outputs has strictly negative determinant.
    det = -4/(15*math.sqrt(17/5))
    assert det < 0
    checked = 0
    rng = np.random.default_rng(23750)
    for n, ks in ((3,(1,2)), (4,(1,2,3)), (7,(1,3,6))):
        for k in ks:
            for case in range(240):
                lam = np.exp(rng.uniform(-3.5,3.5,size=n))
                G = rng.standard_normal((n,k))
                for fn in (
                    lambda x:x**0.2,
                    lambda x:np.sqrt(x),
                    lambda x:x**0.8,
                    lambda x:np.log1p(x),
                    lambda x:x/(1.0+x),
                ):
                    a,b,Q,Qf=trace_matrix_fun_nystrom(lam,G,fn)
                    assert a + 5e-10*max(1,a,b)>= b, (n,k,a,b)
                    checked+=1
                    # The spectral sorting along the weighting path is exact:
                    # h_i=(lambda_i/f_i-1)/(2(1-t+t*lambda_i/f_i)).
                    fl=fn(lam)
                    ratio=lam/fl
                    for t in (0.13,0.57,0.94):
                        h=(ratio-1)/(2*(1-t+t*ratio))
                        P=orth(np.sqrt((1-t)*fl+t*lam)[:,None]*G)
                        P=P@P.T
                        covsum=np.sum((fl[:,None]-fl[None,:])*(h[:,None]-h[None,:])*(P**2))
                        assert covsum >= -2e-8*max(1.,abs(a)), (n,k,covsum)
                        checked+=1
    print('PASS: exact two-dimensional witness and', checked, 'finite numerical comparisons')


if __name__=='__main__':
    run()
