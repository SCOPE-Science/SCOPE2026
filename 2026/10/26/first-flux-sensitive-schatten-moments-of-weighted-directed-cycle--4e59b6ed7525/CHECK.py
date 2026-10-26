"""Finite reproducibility checks for the phase-onset theorem; requires NumPy.
These tests are not a replacement for the general proof.
"""
import numpy as np

rng = np.random.default_rng(26261018)
assertions = 0
for n in range(3, 11):
    k = n // np.gcd(n, 2)
    r = 2 * k // n
    for trial in range(9):
        weights = rng.uniform(.15, 1.5, n)*np.exp(1j*rng.uniform(-3, 3, n))
        if trial == 0:
            weights[0] = 0
        if trial == 1:
            weights = np.full(n, 1/np.sqrt(n), dtype=complex)
        W = np.zeros((n, n), dtype=complex)
        for j, weight in enumerate(weights):
            W[(j+1)%n, j] = weight
        t = (trial+1)/11
        s = 1-t
        Q = np.prod(weights)
        H = float(np.sum(abs(weights)**2))
        def phase_value(j, theta):
            R = t*np.exp(1j*theta)*W+s*np.exp(-1j*theta)*W.conj().T
            B = R.conj().T @ R
            return float(np.trace(np.linalg.matrix_power(B,j)).real)
        C = phase_value(k, 0)-2*n*(t*s)**k * (Q**r).real
        for theta in [0, .18, .579, 1.2, 2.4, 3.1]:
            observed = phase_value(k, theta)
            predicted = C+2*n*(t*s)**k*np.real(np.exp(2j*k*theta)*Q**r)
            assert abs(observed-predicted) < 3e-7*max(1,abs(observed))
            assertions += 1
            for j in range(1,k):
                observed_low = phase_value(j,theta)
                reference = phase_value(j,0)
                assert abs(observed_low-reference) < 3e-7*max(1,abs(reference))
                assertions += 1
        osc = 4*n*(t*s)**k*abs(Q)**r
        bound = 4*float(n)**(1-k)*(t*s)**k*H**k
        assert osc <= bound+2e-10*max(1,bound)
        assertions+=1
        if trial == 1:
            assert abs(osc-bound) < 1e-9*max(1,bound)
            assertions+=1
print(f"CHECK_OK {assertions} finite assertions")
