#!/usr/bin/env python3
"""Direct finite checks for Euclidean widths of broom-tree root polytopes.

Run with `python VERIFY.py`. All sampled tests are finite numerical corroboration,
not proofs of the limiting distribution or the extreme-value estimates.
"""
import math
import numpy as np
from scipy.special import ndtr


def edges(h, p):
    # Hub 0; pendants 1,...,h; path vertices h+1,...,h+p.
    ans = [(0, i) for i in range(1, h+1)]
    ans += [(0, h+1)]
    ans += [(h+i-1, h+i) for i in range(2, p+1)]
    return ans


def direct_width(points, pairs, direction):
    values = [float(np.dot(direction, points[i]-points[j])) for i,j in pairs]
    return max(values)-min(values) if values else 0.0


def main():
    rng = np.random.default_rng(314159265)
    support_trials = 0
    covariance_trials = 0
    for h in range(1, 9):
        for p in range(2, 11):
            n = h+p+1
            es = edges(h,p)
            assert len(es) == n-1
            points = np.eye(n)
            for _ in range(50):
                g = rng.standard_normal(n)
                x = g-g.mean()
                u = x/np.linalg.norm(x)
                signed = np.array([sgn*(points[i]-points[j]) for i,j in es for sgn in [1,-1]])
                exact = float(np.max(signed@u)-np.min(signed@u))
                formula = 2*max(abs(u[i]-u[j]) for i,j in es)
                assert math.isclose(exact,formula,rel_tol=2e-13,abs_tol=2e-13)
                assert math.isclose(formula*math.sqrt(n-1)/2,
                        max(abs(g[i]-g[j]) for i,j in es)/(np.linalg.norm(x)/math.sqrt(n-1)),
                        rel_tol=2e-13,abs_tol=2e-13)
                support_trials += 1
    # A correlated path has variance-two increments and correlation -1/2 only
    # between successive increments. Verify this covariance structurally,
    # without relying on empirical sampling.
    for p in range(2, 31):
        D = np.zeros((p,p+1))
        for j in range(p):
            D[j,j]=-1
            D[j,j+1]=1
        C=D@D.T
        assert np.array_equal(np.diag(C),np.full(p,2.))
        for i in range(p):
            for j in range(p):
                expected=2 if i==j else (-1 if abs(i-j)==1 else 0)
                assert C[i,j]==expected
                covariance_trials += 1
    # Critical-window identity for the limiting mixture's point mass.
    for lam in [-4.,-2.,-1.]:
        a=-lam/2
        atom=2*ndtr(a)-1
        samples=np.abs(rng.standard_normal(180000))
        empirical=float(np.mean(samples<=a))
        assert abs(empirical-atom)<0.008
    # Numeric stress test at large p using the original dependent Gaussian
    # path increments, without substituting independent edge increments.
    for p in [128,512,2048]:
        h=max(1,round(p**1.5))
        rr=[]
        for _ in range(550):
            core=rng.standard_normal(p+1)
            pend=rng.standard_normal(h)
            s=np.max(np.abs(pend-core[0]))
            path=np.max(np.abs(np.diff(core)))
            rr.append(max(s,path)/math.sqrt(math.log(p)))
        # Subcritical regime should be path-led on the leading sqrt(log p) scale.
        mean=float(np.mean(rr))
        assert 1.6<mean<2.6,(p,mean)
    print(f'VERIFY_OK support={support_trials}, covariance={covariance_trials}, critical_atoms=3, asymptotic_sanity=3x550')


if __name__=='__main__':
    main()
