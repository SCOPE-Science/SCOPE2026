"""Independent finite checks of a geometric covariance inversion identity."""
import math
import numpy as np

def root(a):
    eigenvalues, q = np.linalg.eigh(a)
    assert np.all(eigenvalues > 0)
    return (q * np.sqrt(eigenvalues)) @ q.T

def inverse_root(a):
    eigenvalues, q = np.linalg.eigh(a)
    assert np.all(eigenvalues > 0)
    return (q * (eigenvalues ** -0.5)) @ q.T

def check():
    rng = np.random.default_rng(719333)
    for d in range(1, 8):
        m = d + 1
        c = (m * np.eye(d) - np.ones((d, d))) / (m*m*(m+1))
        assert np.allclose(np.linalg.inv(c), m*(m+1)*(np.eye(d)+np.ones((d,d))), atol=1e-10)
        for _ in range(8):
            v = rng.normal(size=(d,d)) + (d+1)*np.eye(d)
            g = v.T @ v
            s = 4 * g @ c @ g
            rec = 0.5 * inverse_root(c) @ root(root(c) @ s @ root(c)) @ inverse_root(c)
            assert np.allclose(rec, g, rtol=1e-9, atol=1e-8)
            volume = abs(np.linalg.det(v)) / math.factorial(d)
            predicted = (np.linalg.det(s) * m**(d+1) * (m+1)**d / (4**d * math.factorial(d)**4))**0.25
            assert math.isclose(volume, predicted, rel_tol=1e-9, abs_tol=1e-8)
        if d < 5:
            v = rng.normal(size=(d,d)) + 2*np.eye(d)
            g = v.T@v
            lam = rng.dirichlet(np.ones(m), size=600000)[:,1:]
            y = np.diag(g)[None,:] - 2 * lam @ g
            empirical = np.cov(y, rowvar=False)
            assert np.allclose(np.atleast_2d(empirical), 4*g@c@g, rtol=0.035, atol=0.035)
    print('PASS: d=1..7, 56 SPD inversion/volume checks; Monte Carlo covariance d=1..4 (600000 samples each).')

if __name__ == '__main__': check()
