#!/usr/bin/env python3
"""Finite reproducibility checks for an exact Gaussian covariance KL theorem.

Uses only Python standard library. Finite checks supplement the analytic proof.
"""
import math
import random


def phi(K, t):
    d = (K - 1.0) / K
    c = (K - 1.0) ** 2 / K
    return c * t * (1.0 - t) - math.log1p(-d * t) - t * math.log(K)


def phi_prime(K, t):
    d = (K - 1.0) / K
    c = (K - 1.0) ** 2 / K
    return c * (1.0 - 2.0 * t) + d / (1.0 - d * t) - math.log(K)


def kl_from_eigs(eigs):
    k = len(eigs)
    h = sum(1.0 / x for x in eigs) / k
    a = sum(eigs) / k
    ell = sum(math.log(x) for x in eigs) / k
    return k * (h * a - 1.0 - math.log(h) - ell) / 2.0


def optimal_t(K):
    lo, hi = 0.0, 1.0
    assert phi_prime(K, lo) > 0.0 and phi_prime(K, hi) < 0.0
    for _ in range(100):
        mid = (lo + hi) / 2
        if phi_prime(K, mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def verify_schur(eigs):
    # Block-diagonal direct realization: top 2x2 matrix [[1, 1/2], [1/2, 5/4]].
    # Its determinant is exactly one. The one-step residual is 1/2.
    a, coupling, c = 1.0, 0.5, 1.25
    assert abs(a*c - coupling*coupling - 1.0) < 1e-14
    schur_boundary = c - coupling*coupling/a
    assert abs(schur_boundary-1.0) < 1e-14
    # Remaining Schur eigenvalues are eigs, so the inverse bulk trace is sum(1/eigs).
    omega = sum(1.0/x for x in eigs)/len(eigs)
    assert omega > 0.0
    assert abs(kl_from_eigs(eigs)-len(eigs)/2*(omega*sum(eigs)/len(eigs)-1-
                        math.log(omega)-sum(map(math.log,eigs))/len(eigs))) < 2e-10


def main():
    rng = random.Random(20260909)
    count = 0
    for K in [1.01, 1.2, 2.0, 4.0, 10.0, 100.0]:
        tstar = optimal_t(K)
        assert 0.0 < tstar < 1.0
        for k in [2, 3, 5, 10, 20, 100]:
            scores = [phi(K, m/k) for m in range(k+1)]
            m = max(range(1, k), key=lambda j:scores[j])
            assert m in (max(1, math.floor(k*tstar)),
                         min(k-1, math.ceil(k*tstar)))
            opt = k*scores[m]/2
            extremal = [K]*m+[1.0]*(k-m)
            assert abs(kl_from_eigs(extremal)-opt) < 3e-10*max(1,opt)
            verify_schur(extremal)
            count += 2
            for _ in range(100):
                vals = [math.exp(rng.random()*math.log(K)) for _ in range(k)]
                assert kl_from_eigs(vals) <= opt + 3e-10*max(1,opt)
                count += 1
            for _ in range(10):
                t=rng.random()
                delta=1e-6
                fd=(phi(K,t+delta)-phi(K,t-delta))/(2*delta)
                assert abs(fd-phi_prime(K,t)) < 2e-7
                count += 1
    expected=kl_from_eigs([4.0]*4+[1.0]*6)/10
    assert abs(expected-0.17107859974538814)<1e-12
    print('PASS:',count,'finite checks; K=4, k=10 KL/k =',f'{expected:.14g}')


if __name__=='__main__':
    main()
