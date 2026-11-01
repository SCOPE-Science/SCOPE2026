"""Reproduce finite consistency checks for optimal circular Fock polynomial sampling.

The infinite-dimensional and all-degree assertions require the accompanying proof.
"""
from math import exp, factorial, lgamma, log, pi, sqrt
import numpy as np

ASSERTIONS = 0

def check(condition, explanation):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(explanation)

def optimum_x(n):
    return exp(lgamma(n + 1) / n)

def log_weights(n, x):
    return np.array([k * log(x) - lgamma(k + 1) for k in range(n + 1)])

def matrix(n, x, phases, weights):
    ww = np.exp(log_weights(n, x))
    K = float(ww.sum())
    return np.array([
        [sqrt(weights[j] * ww[k] / K) * np.exp(1j * k * phases[j])
         for k in range(n + 1)]
        for j in range(n + 1)
    ], dtype=complex)

def squared_condition(A):
    eig = np.linalg.eigvalsh(A.conj().T @ A)
    return max(0., float(eig[-1])) / max(1e-300, float(eig[0]))

def main():
    rng = np.random.default_rng(260826)
    for n in range(1, 15):
        N = n + 1
        x = optimum_x(n)
        w = np.exp(log_weights(n, x))
        target = float(max(w) / min(w))
        regular = matrix(n, x, 2*pi*np.arange(N)/N, np.ones(N))
        eig = np.linalg.eigvalsh(regular.conj().T @ regular)
        expected = N*w/sum(w)
        check(np.allclose(eig, np.sort(expected), rtol=1e-9, atol=1e-9),
              f'exact regular polygon spectrum n={n}')
        check(abs(squared_condition(regular) - target) < 1e-8*target,
              f'optimal condition n={n}')
        check(abs(w[0]-w[-1]) < 1e-12, f'balanced endpoint n={n}')
        for h in (0.75, 0.85, 0.95, 1.05, 1.15, 1.25):
            wc = np.exp(log_weights(n, x*h))
            check(float(wc.max()/wc.min()) > target*(1-1e-11),
                  f'unimodal radius optimum n={n}, multiplier={h}')
        for j in range(20):
            newx = x * exp(rng.uniform(-0.5, 0.5))
            phases = np.sort(rng.uniform(0, 2*pi, size=N))
            weights = rng.lognormal(0, 0.45, size=N)
            weights *= N / weights.sum()
            A = matrix(n, newx, phases, weights)
            observed = squared_condition(A)
            check(observed >= target*(1-1e-8), f'global condition n={n}, trial={j}')
            diagonal_bound = float(np.exp(log_weights(n, newx)).max() /
                                   np.exp(log_weights(n, newx)).min())
            check(observed >= diagonal_bound*(1-1e-8),
                  f'Rayleigh diagonal n={n}, trial={j}')
    for n in (20, 40, 80, 160, 320, 640, 1280, 2560):
        x = optimum_x(n)
        k = int(x)
        logM = k*log(x) - lgamma(k+1)
        asymp = n/(2*exp(1)) + 0.25 + (1/exp(1)-1)/4 * log(2*pi*n)
        err = abs(0.5*logM - asymp)
        check(err < 0.12 / sqrt(n), f'asymptotic remainder n={n}, error={err}')
    print(f'PASS: {ASSERTIONS} finite assertions; proof supplies all-degree result.')

if __name__ == '__main__':
    main()
