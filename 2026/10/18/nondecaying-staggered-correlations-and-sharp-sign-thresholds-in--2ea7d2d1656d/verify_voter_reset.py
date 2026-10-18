"""Independent finite-state and recurrence checks for a reset voter ring.

Requires Python 3, NumPy and SciPy. Run: python voter_reset_verification.py.
The infinite-lattice statements follow from the accompanying proof, not these tests.
"""
import itertools
import math
import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve
from scipy.optimize import brentq
from scipy.special import lambertw


def q_of_r(r):
    return (2 + r - math.sqrt(r * (r + 4))) / 2


def predictions(n, r):
    q = q_of_r(r)
    means = np.array([(-1)**j * r/(r+2) for j in range(n)])
    moments = np.array([
        (-1)**d * r/(r+4) + 4/(r+4) *
        (q**d + q**(n-d))/(1+q**n)
        for d in range(1, n)
    ])
    return means, moments


def solve_full_chain(n, r):
    assert n % 2 == 0 and n >= 4
    dim = 2**n
    generator = lil_matrix((dim, dim), dtype=float)
    checker = sum(1 << j for j in range(0, n, 2))
    for state in range(dim):
        transitions = {}
        for j in range(n):
            old = (state >> j) & 1
            for neigh in ((j-1) % n, (j+1) % n):
                copied = (state >> neigh) & 1
                if copied != old:
                    target = state ^ (1 << j)
                    transitions[target] = transitions.get(target, 0) + 0.5
        if state != checker:
            transitions[checker] = transitions.get(checker, 0) + r
        for target, rate in transitions.items():
            generator[state, target] += rate
            generator[state, state] -= rate
    system = generator.T.tolil()
    system[0, :] = 1
    rhs = np.zeros(dim)
    rhs[0] = 1
    weights = spsolve(system.tocsc(), rhs)
    assert min(weights) > -1e-11
    assert abs(sum(weights) - 1) < 1e-10
    means = np.zeros(n)
    moments = np.zeros(n-1)
    for state, p in enumerate(weights):
        spins = np.array([1 if ((state >> j)&1) else -1 for j in range(n)])
        means += p * spins
        for d in range(1, n):
            moments[d-1] += p * spins[0]*spins[d]
    return means, moments


def main():
    solved = 0
    for n in (4, 6, 8, 10):
        for rate in (0.07, 0.4, 1.0, 3.0, 13.0):
            actual_m, actual_c = solve_full_chain(n, rate)
            expect_m, expect_c = predictions(n, rate)
            assert np.max(np.abs(actual_m-expect_m)) < 3e-10
            assert np.max(np.abs(actual_c-expect_c)) < 3e-10
            solved += 1
    recurrences = 0
    for r in (0.001, 0.02, 0.4, 2.0, 45.0):
        q = q_of_r(r)
        for d in range(1, 301):
            def c(x):
                if x == 0:
                    return 1.0
                return (-1)**x*r/(r+4)+4/(r+4)*q**x
            residual = c(d-1)+c(d+1)-(2+r)*c(d)+r*(-1)**d
            assert abs(residual) < 2e-11
            recurrences += 1
    for k in range(1, 41):
        root=brentq(lambda q:q**k*(1+q*q)+q-1,1e-14,1-1e-14)
        threshold=(1-root)**2/root
        for r, expected_positive in ((threshold*0.99,True),(threshold*1.01,False)):
            q=q_of_r(r)
            covariance=4/(r+4)*(q**(2*k+1)-r/(r+2)**2)
            assert (covariance>0) == expected_positive
    for k in (100, 1000, 10000):
        root=brentq(lambda q:q**k*(1+q*q)+q-1,0.5,1-1e-15)
        rate=(1-root)**2/root
        leading=float(lambertw(2*k).real/k)**2
        assert 0.75 < rate/leading < 1.20
    print(f'PASS: {solved} full-state stationary systems; {recurrences} recurrence identities; 80 sign tests; 3 scaling checks')

if __name__ == '__main__':
    main()
