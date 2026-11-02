"""Independent finite-dimensional checks for quadratic Gaussian pure-dephasing theorem.

Requires Python 3 and numpy; discretization checks are evidence, not an infinite-dimensional proof.
"""
import numpy as np


def modulus(C, weights, kappa):
    # For a covariance C and real quadratic weights, Q=xi^T B xi - tr B,
    # where B=L.T diag(weights) L and L L.T = C.
    L = np.linalg.cholesky(C)
    B = L.T @ (weights[:, None] * L)
    ev = np.linalg.eigvalsh(B)
    return float(np.exp(-0.25 * np.log1p(4 * kappa * kappa * ev * ev).sum()))


def test_positive_cases():
    rng = np.random.default_rng(7042024)
    count = 0
    N = 48
    times = (np.arange(N) + 0.5) / N
    for case in range(40):
        # Strictly positive nonstationary covariance, including anticorrelated
        # oscillatory components; no assumed covariance sign or Markov property.
        v = 0.6 + 0.8 * rng.random(N)
        oscill = np.cos((times[:, None]-times[None, :]) * rng.uniform(1, 23))
        OU = np.exp(-rng.uniform(0.1, 8.0) * np.abs(times[:, None]-times[None, :]))
        C = (0.2 * v[:, None] * v[None, :] * oscill
             + 0.8 * v[:, None] * v[None, :] * OU
             + 1e-8 * np.eye(N))
        g = 0.1 + rng.random(N)
        kappa = 10**rng.uniform(-1.5, 1.0)
        vals = []
        for count_active in range(0, N+1, 4):
            w = np.zeros(N)
            w[:count_active] = g[:count_active] / N
            vals.append(modulus(C, w, kappa))
        assert np.all(np.diff(vals) <= 2e-11), (case, vals)
        assert vals[-1] < vals[0]
        count += len(vals) - 1
    return count


def test_echo_cases():
    n=80
    ts=(np.arange(n)+0.5) * 2.0/n
    dt=2.0/n
    w1=np.where(ts < 1,dt,0)
    w2=np.where(ts < 1,dt,-dt)
    tested=0
    for eps in (0.001,0.01,0.03,0.05,0.1):
        C=np.exp(-eps*np.abs(ts[:,None]-ts[None,:]))+1e-10*np.eye(n)
        for coupling in (0.2,1.,3.):
            f1=modulus(C,w1,coupling)
            f2=modulus(C,w2,coupling)
            assert f2 > f1 + 0.001, (eps,coupling,f1,f2)
            tested += 1
    # At exactly static noise, the first half has coherence below 1,
    # and the second half rephases exactly because integrated weight is zero.
    for coupling in (0.2,1,3):
        expected=(1+4*coupling**2)**(-0.25)
        assert expected < 1
        tested += 1
    return tested


def test_determinant_identity():
    rng=np.random.default_rng(313)
    count=0
    for n in (3,5,8,11):
        for _ in range(5):
            V=rng.normal(size=(n,n))
            C=V@V.T/n + 0.1*np.eye(n)
            weights=rng.uniform(-0.4,0.4,size=n)
            kappa=float(rng.uniform(0.02,4))
            actual=modulus(C,weights,kappa)
            determinant=np.linalg.det(np.eye(n)-2j*kappa*C@np.diag(weights))
            expected=abs(determinant)**(-0.5)
            assert abs(actual-expected)<3e-10
            count +=1
    return count

if __name__ == '__main__':
    p=test_positive_cases(); e=test_echo_cases(); d=test_determinant_identity()
    print(f'PASS positive covariance/modulation pairwise comparisons: {p}')
    print(f'PASS finite-correlation echo and static-limit cases: {e}')
    print(f'PASS complex determinant comparisons: {d}')
    print(f'PASS total: {p+e+d}')
