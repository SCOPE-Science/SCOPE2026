#!/usr/bin/env python3
"""Finite-matrix checks for a dimer-chain spectral pinning theorem.
Run: python verify.py
Requires numpy and scipy. No network access or external data files.
"""
import numpy as np
from scipy.linalg import eigh


def matrices(alpha, beta, a, b):
    n = len(alpha)
    assert n >= 2 and len(beta) == n and len(a) == n and len(b) == n - 1
    masses = np.empty(2*n)
    masses[0::2], masses[1::2] = alpha, beta
    K = np.zeros((2*n, 2*n))
    for j, stiffness in enumerate(np.ravel(np.column_stack((a[:-1], b)))):
        K[j, j] += stiffness
        K[j+1, j+1] += stiffness
        K[j, j+1] -= stiffness
        K[j+1, j] -= stiffness
    j = 2*n-2
    K[j, j] += a[-1]
    K[j+1, j+1] += a[-1]
    K[j, j+1] -= a[-1]
    K[j+1, j] -= a[-1]
    return K, masses


def pinned_mode(alpha, beta):
    n = len(alpha)
    x = np.empty(2*n)
    x[0] = 1.0
    for j in range(n):
        x[2*j+1] = -(alpha[j]/beta[j])*x[2*j]
        if j+1 < n:
            x[2*j+2] = x[2*j+1]
    return x


def main():
    rng = np.random.default_rng(192714)
    counts = {'pinned':0,'shape':0,'rank':0,'changed_coupling':0,'sensitivity':0,'detuned':0,'uniform_localization':0}
    max_residual = 0.0
    max_relative_error = 0.0
    max_absolute_error = 0.0
    for _ in range(900):
        n = int(rng.integers(2, 10))
        alpha = np.exp(rng.uniform(-0.6, 0.6, n))
        beta = np.exp(rng.uniform(-0.6, 0.6, n))
        target = float(np.exp(rng.uniform(-0.5, 1.2)))
        a = target/(1/alpha+1/beta)
        b = np.exp(rng.uniform(-2, 2, n-1))
        K, masses = matrices(alpha, beta, a, b)
        eig, vec = eigh(K, np.diag(masses), check_finite=True)
        # There are N sign changes, so the 0-indexed spectral position is N.
        assert abs(eig[n] - target) <= 2e-12*max(1, target, eig[-1])
        assert eig[n-1] < target-1e-12 and eig[n+1] > target+1e-12
        counts['pinned'] += 1
        counts['rank'] += 1
        z = pinned_mode(alpha, beta)
        z /= np.sqrt(np.sum(masses*z*z))
        max_residual = max(max_residual, np.linalg.norm(K@z-target*masses*z))
        assert np.linalg.norm(K@z-target*masses*z) < 1e-11
        assert abs(np.vdot(vec[:, n]*masses,z)) > 1-1e-10
        assert np.linalg.norm(z[1:-1:2]-z[2::2]) < 1e-14
        counts['shape'] += 1
        b2 = b * np.exp(rng.uniform(-1.5, 1.5, n-1))
        K2, _ = matrices(alpha,beta,a,b2)
        eig2 = eigh(K2, np.diag(masses), eigvals_only=True)
        assert abs(eig2[n]-target) < 1e-10
        counts['changed_coupling'] += 1
        # One defective dimer generically destroys exact spectral pinning.
        a_bad=a.copy()
        t=int(rng.integers(n))
        a_bad[t] *= 1.03
        K_bad,_=matrices(alpha,beta,a_bad,b)
        bad=eigh(K_bad,np.diag(masses),eigvals_only=True)
        assert bad[n] > target+1e-11
        counts['detuned'] += 1
        # Hellmann-Feynman sensitivity for a generic (untuned) system.
        i=int(rng.integers(n-1))
        lam,v=eigh(K_bad,np.diag(masses))
        j=int(rng.integers(1,2*n-1))
        diff=v[2*i+1,j]-v[2*i+2,j]
        predicted=diff*diff
        eps=1e-5*min(1,b[i])
        b_right=b.copy(); b_left=b.copy()
        b_right[i]+=eps; b_left[i]-=eps
        right=eigh(matrices(alpha,beta,a_bad,b_right)[0],np.diag(masses),eigvals_only=True)[j]
        left=eigh(matrices(alpha,beta,a_bad,b_left)[0],np.diag(masses),eigvals_only=True)[j]
        err=abs((right-left)/(2*eps)-predicted)
        max_relative_error=max(max_relative_error,err/max(1,predicted))
        max_absolute_error=max(max_absolute_error,err)
        assert err < 4e-7
        counts['sensitivity'] += 1
    for _ in range(100):
        n=int(rng.integers(3,30))
        ratio=float(np.exp(rng.uniform(-1.1,1.1)))
        alpha=np.ones(n)
        beta=np.full(n,1/ratio)
        z=pinned_mode(alpha,beta)
        assert np.allclose(z[0::2], np.array([(-ratio)**k for k in range(n)]), rtol=5e-14, atol=1e-11)
        counts['uniform_localization']+=1
    print({'tests':counts,'max_residual':max_residual,
           'max_sensitivity_absolute_error':max_absolute_error,
           'max_sensitivity_normalized_error':max_relative_error, 'status':'PASS'})

if __name__=='__main__':
    main()
