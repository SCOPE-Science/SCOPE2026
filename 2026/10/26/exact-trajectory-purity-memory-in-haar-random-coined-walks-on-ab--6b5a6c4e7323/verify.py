"""Numerical checks of exact two-mode Haar-coin walk moment identities.

This supplementary script tests the theorem at finite sample size; the proof
uses Haar conjugation identities and does not rely on Monte Carlo.
"""
import numpy as np


def haar_unitary(d, rng):
    z = (rng.standard_normal((d, d)) + 1j*rng.standard_normal((d, d)))/np.sqrt(2)
    q, r = np.linalg.qr(z)
    return q * (np.diag(r) / np.abs(np.diag(r)))


def sample(d, phases, steps, trials, seed=48921):
    rng = np.random.default_rng(seed)
    D = np.diag(np.exp(1j*np.asarray(phases)))
    z_values = np.zeros(trials, dtype=complex)
    for n in range(trials):
        psi = np.zeros(d, dtype=complex)
        phi = np.zeros(d, dtype=complex)
        psi[0] = phi[0] = 1
        for _ in range(steps):
            u = haar_unitary(d, rng)
            psi = D @ (u @ psi)
            phi = u @ phi
        z_values[n] = np.vdot(phi, psi)
    lam = np.trace(D)/d
    r = (d*d*abs(lam)**2 - 1)/(d*d-1)
    mean_expected = lam**steps
    second_expected = 1/d + (1-1/d)*r**steps
    mean_empirical = z_values.mean()
    second_empirical = np.mean(abs(z_values)**2)
    mean_err = abs(mean_expected-mean_empirical)
    second_err = abs(second_expected-second_empirical)
    print(dict(d=d, steps=steps, lam=complex(lam), r=float(r), predicted_mean=complex(mean_expected), measured_mean=complex(mean_empirical), predicted_second=float(second_expected), measured_second=float(second_empirical), mean_err=float(mean_err), second_err=float(second_err)))
    assert mean_err < 0.07 and second_err < 0.025


if __name__ == '__main__':
    for cfg in [(2,[0,1.2],1,10000), (2,[0,1.2],4,10000),
                (2,[0,np.pi],4,6000), (3,[0,1.1,-1.7],4,10000),
                (4,[0,1.1,2.1,2.7],3,8000)]:
        sample(*cfg)
    print('All finite-sample checks passed; no infinite conclusion relies on these checks.')
