"""Independent finite checks for the Gaussian leave-one-out trace law.

Run: python verify.py
Requires: Python 3.10+, NumPy.
All theorems are proved in RESULT.md; random tests do not prove them.
"""
from fractions import Fraction
from math import sqrt
import numpy as np


def moment_formula(n, k):
    d = n-k+1
    assert n >= 1 and 1 <= k <= n
    v = Fraction(2*d*(n+3), k*(d+3))
    e = Fraction(2*d*(d+2), k*(d+3)) if k >= 2 else None
    return v, e


def residuals(omega):
    n,k = omega.shape
    values = np.empty(k)
    for i in range(k):
        minus = np.delete(omega, i, axis=1)
        if k == 1:
            proj = np.zeros((n,n))
        else:
            q,_ = np.linalg.qr(minus, mode='reduced')
            proj = q@q.T
        values[i] = np.linalg.norm(omega[:,i]-proj@omega[:,i])**2
    return values


def nystrom_projector(omega):
    gram = omega.T@omega
    return omega @ np.linalg.pinv(gram, rcond=1e-12) @omega.T


def check():
    counts = {'exact':0,'matrix':0,'sampling':0}
    for n in range(1,81):
        for k in range(1,n+1):
            d=n-k+1
            m=d+1
            var_single=Fraction(2*d)
            if k==1:
                assert moment_formula(n,k)[0] == var_single
            else:
                second_sin=Fraction(m*m-1, m*(m+2))
                cross=Fraction(m*m)*second_sin-Fraction((m-1)**2)
                assert cross == Fraction(2*d, d+3)
                actual_var=(var_single+(k-1)*cross)/k
                expected_err=(var_single-cross)/k
                v,e=moment_formula(n,k)
                assert actual_var==v and expected_err==e
                assert v/e == Fraction(n+3,n-k+3)
            counts['exact']+=1
    rng=np.random.default_rng(60173)
    for n in range(1,9):
        for k in range(1,n+2):
            for trial in range(12):
                omega=rng.normal(size=(n,k))
                all_proj=nystrom_projector(omega)
                individual=[]
                for i in range(k):
                    minus=np.delete(omega,i,axis=1)
                    pminus=nystrom_projector(minus) if k>1 else np.zeros((n,n))
                    lhs=np.trace(pminus)+omega[:,i]@(all_proj-pminus)@omega[:,i]
                    if k<=n:
                        qminus=np.linalg.qr(minus, mode='reduced')[0] if k>1 else np.empty((n,0))
                        r=omega[:,i]-qminus@(qminus.T@omega[:,i])
                        rhs=(k-1)+r@r
                    else:
                        rhs=n
                    assert abs(lhs-rhs)<1e-7 * (n+1), (n,k,trial,lhs,rhs)
                    individual.append(lhs)
                if k>n: assert abs(np.mean(individual)-n)<1e-7
                counts['matrix']+=1
    # Spherical moments for pairwise leave-one-out residuals in ambient m.
    for m in [2,3,4,8,16]:
        samples=150000
        x=rng.normal(size=(samples,m)); y=rng.normal(size=(samples,m))
        nx=(x*x).sum(axis=1); ny=(y*y).sum(axis=1)
        cross=(x*y).sum(axis=1)
        rx=nx-cross*cross/ny
        ry=ny-cross*cross/nx
        d=m-1
        target_cross=2*d/(d+3)
        empirical_cov=np.mean((rx-d)*(ry-d))
        assert abs(empirical_cov-target_cross)<0.12*(1+target_cross), (m,empirical_cov,target_cross)
        assert abs(rx.mean()-d)<0.035*(1+d), (m,rx.mean())
        counts['sampling']+=samples
    print('PASS', counts)

if __name__=='__main__':
    check()
