"""Standalone numerical sanity checks for the Markov-modulated rare-exit limit.

The check solves an EXACT finite-state killed generator (the asymptotic
big-jump model); it does not simulate the infinite-activity stable process
or replace the analytical small-time exit theorem.
"""
import math
import numpy as np


def stationary(K):
    n = len(K)
    A = K.T - np.eye(n)
    A[-1, :] = 1.0
    rhs = np.zeros(n)
    rhs[-1] = 1.0
    return np.linalg.solve(A, rhs)


def main():
    assertions = 0
    K = np.array([[0.10, 0.90, 0], [0.20, 0.20, 0.60], [0.80, 0.10, 0.10]], dtype=float)
    assert np.allclose(K.sum(axis=1), 1.0)
    pi = stationary(K)
    assert np.all(pi > 0) and np.allclose(pi @ K, pi)
    assertions += 2
    alpha, c, r = 1.3, 1.0, 1.7
    lambdas = [-0.6, 0, 0.35]
    eta = c * math.gamma(alpha) * math.sin(math.pi * alpha / 2) / math.pi
    k = np.array([eta*((1-x)**(-alpha)+(1+x)**(-alpha)) for x in lambdas])
    kbar = pi @ k
    assert np.all(k > 0) and kbar > 0
    assertions += 1
    for L in [50, 250, 2000, 20000]:
        eps = L**(-alpha)
        # Exact finite-state Markov generator for independently occurring
        # killing jumps at rates eps * k_i.
        Q = r*(K-np.eye(3))-eps*np.diag(k)
        mean = np.linalg.solve(-Q, np.ones(3))
        assert np.all(mean > 0)
        assertions += 1
        for theta in [0.25, 1.0, 4.0]:
            F = np.linalg.solve(theta*eps*np.eye(3)-Q, eps*k)
            target = kbar/(theta+kbar)
            assert np.all((F>0) & (F<1))
            assertions += 1
            if L>=2000:
                assert np.max(abs(F-target)) < 0.01
                assertions += 1
        if L >= 2000:
            assert max(abs(mean*eps-1/kbar)) < 0.01
            assertions += 1
    # Second moment from the killed-state generator is exact.
    eps = 20000**(-alpha)
    Q = r*(K-np.eye(3))-eps*np.diag(k)
    mu = np.linalg.solve(-Q, np.ones(3))
    m2 = 2*np.linalg.solve(-Q, mu)
    assert np.max(abs(m2*eps**2-2/kbar**2)) < 0.02
    assertions += 1
    # Same invariant destination law, distinct temporal correlations.
    J = np.ones((3,1)) @ pi[None,:]
    assert np.allclose(pi@J, pi)
    assertions += 1
    eps = 20000**(-alpha)
    Q2 = r*(J-np.eye(3))-eps*np.diag(k)
    mu2 = np.linalg.solve(-Q2, np.ones(3))
    assert max(abs(eps*mu2-1/kbar)) < 0.01
    assertions += 1
    print(f'PASS {assertions} assertions; stationary weights={pi.tolist()}')
    print(f'kappa={k.tolist()}; weighted hazard={kbar:.12f}')
    print('Toy killing generator only; stable-process proof is analytical.')


if __name__ == '__main__':
    main()
