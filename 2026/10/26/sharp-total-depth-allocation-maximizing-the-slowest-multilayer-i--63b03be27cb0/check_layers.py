"""Numerical checks for a sharp fixed-depth multilayer modal speed bound.

This script is supplementary finite evidence; the universal bound follows from
Rayleigh--Ritz, Cauchy--Schwarz, and Perron--Frobenius in RESULT.md.
"""
import numpy as np
from scipy.linalg import eigh


def inverse_speed_squared(depth, reduced_gravity):
    depth = np.asarray(depth, dtype=float)
    g = np.asarray(reduced_gravity, dtype=float)
    n = len(depth)
    assert n >= 2 and len(g) == n - 1
    assert np.all(depth > 0) and np.all(g > 0)
    K = np.zeros((n - 1, n - 1))
    for layer in range(n):
        v = np.zeros(n - 1)
        if layer: v[layer - 1] += 1
        if layer < n - 1: v[layer] -= 1
        K += np.outer(v, v)/depth[layer]
    D = np.diag(g)
    return eigh(K, D, eigvals_only=True)


def optimal(depth_total, reduced_gravity):
    a = 1/np.asarray(reduced_gravity, dtype=float)
    S = a.sum()
    padded = np.r_[0., a, 0.]
    return depth_total*(padded[1:]+padded[:-1])/(2*S), depth_total/(4*S)


def run():
    rng = np.random.default_rng(7302026)
    counts = {'optimizer_eigenvalue':0, 'global_bound':0,
              'unique_optimization':0, 'critical_eigenvector':0,
              'three_layer_ratio':0, 'two_layer_benchmark':0}
    for n in range(2, 18):
        for _ in range(200):
            g = np.exp(rng.uniform(-4,4,size=n-1))
            H = np.exp(rng.uniform(-2,3))
            hopt, predicted = optimal(H,g)
            eigen = inverse_speed_squared(hopt,g)
            expect_lambda = 1/predicted
            assert abs(eigen[-1]-expect_lambda) < 1.e-8*expect_lambda
            counts['optimizer_eigenvalue'] += 1
            # Check the predicted out-of-phase modal vector in the full operator.
            x = ((-1.)**np.arange(n-1))/g
            K = np.zeros((n-1,n-1))
            for j in range(n):
                b = np.zeros(n-1)
                if j: b[j-1] += 1
                if j < n-1: b[j] -= 1
                K += np.outer(b,b)/hopt[j]
            residual = K@x-expect_lambda*(g*x)
            assert np.linalg.norm(residual) < 5e-8*expect_lambda*np.linalg.norm(g*x)
            counts['critical_eigenvector'] += 1
            h=H*rng.dirichlet(np.ones(n))
            given = inverse_speed_squared(h,g)
            slow_speed_sq = 1/given[-1]
            assert slow_speed_sq <= predicted*(1+3.e-12)
            counts['global_bound']+=1
            if np.linalg.norm(h-hopt)>1.e-8*H:
                assert slow_speed_sq < predicted*(1-5e-13)
                counts['unique_optimization']+=1
            if n==3:
                fast_sq=1/eigen[0]
                assert abs(fast_sq/predicted-2)<1e-9
                counts['three_layer_ratio']+=1
            if n==2:
                assert abs(hopt[0]-H/2)<1e-12*H
                counts['two_layer_benchmark']+=1
    print('PASS',counts,'TOTAL',sum(counts.values()))

if __name__ == '__main__':run()
