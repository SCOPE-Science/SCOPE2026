#!/usr/bin/env python3
"""Numerical finite-degree checks of Chebyshev affine restriction (NumPy required)."""
import numpy as np


def restriction(N, a, b):
    m = N + 1
    x = np.cos(np.pi * (np.arange(m) + .5) / m)
    ell = .5 * (b-a) * x + .5 * (a+b)
    cols = np.arange(m)[None, :]
    def evaluation(points):
        v = np.cos(np.arccos(points)[:, None] * cols) * np.sqrt(2.0 / m)
        v[:, 0] /= np.sqrt(2.0)
        return v
    U, V = evaluation(x), evaluation(ell)
    # DCT orthogonality and Gauss-Chebyshev exactness for degree <= 2N.
    assert np.max(np.abs(U.T @ U - np.eye(m))) < 1.e-10
    return U.T @ V


def limit_norm(N, a, b):
    alpha, beta = (b-a)/2, (a+b)/2
    fixed = beta/(1-alpha)
    return np.sqrt(1+2*sum(np.cos(j*np.arccos(np.clip(fixed, -1, 1)))**2
                           for j in range(1, N+1)))


def main():
    checks = 0
    for a,b in [(0.,1.),(-1.,.4),(-.5,.5),(-.75, .35)]:
        scaled = []
        for N in [8,16,32,64,128]:
            R = restriction(N,a,b)
            val = np.linalg.svd(R, compute_uv=False)[0]
            scaled.append(val/N**.25)
            # Diagonal entries are the source's exact triangular eigenvalues.
            alpha = (b-a)/2
            assert np.max(np.abs(np.diag(R)-alpha**np.arange(N+1))) < 1e-9
            assert np.max(np.abs(np.tril(R,-1))) < 2e-9
            assert val >= 1-1e-10
            checks += 4
        # Numerical trend, not a proof of the rate or of optimal constants.
        assert min(scaled)>0.4 and max(scaled)<2.0
        assert max(scaled)/min(scaled)<1.3
        N=24
        R=restriction(N,a,b)
        power=np.linalg.matrix_power(R,250)
        target=limit_norm(N,a,b)
        observed=np.linalg.svd(power, compute_uv=False)[0]
        assert abs(observed-target)<2e-8
        checks += 3
        print((a,b), 'scaled_N128=',round(scaled[-1],6),
              'power_limit_N24=',round(target,6))
    for N in (4,16,80):
        I=restriction(N,-1.,1.)
        assert np.max(np.abs(I-np.eye(N+1)))<3e-12
        checks += 1
    print('PASS',checks,'finite algebraic/quadrature checks; universal proof is analytical')

if __name__ == '__main__':
    main()
