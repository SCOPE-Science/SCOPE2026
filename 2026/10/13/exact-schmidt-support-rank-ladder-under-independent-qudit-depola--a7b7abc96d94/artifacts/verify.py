"""Independent finite-dimensional checks for a closed-form local-noise negativity theorem."""
from fractions import Fraction
from math import sqrt
import numpy as np


def closed_negativity(d, k, p, q):
    delta = d*d*(1-p)*(1-q)-d*(p*(1-q)+q*(1-p))
    return (k-1)*max(0, delta-k*p*q)/(2*d*d)


def matrix_negativity(d, k, p, q):
    """Construct full physical state, partial transpose, then eigenspectrum."""
    psi = np.zeros(d*d, dtype=np.complex128)
    for j in range(k):
        psi[d*j+j] = 1/sqrt(k)
    original = np.outer(psi, psi.conj())
    rho_a = np.diag([1/k if j < k else 0 for j in range(d)])
    rho_b = rho_a.copy()
    sigma = ((1-p)*(1-q)*original
             + p*(1-q)*np.kron(np.eye(d)/d, rho_b)
             + (1-p)*q*np.kron(rho_a, np.eye(d)/d)
             + p*q*np.eye(d*d)/(d*d))
    assert abs(np.trace(sigma).real-1) < 1e-12
    assert np.linalg.eigvalsh(sigma).min() > -1e-12
    transpose_b = sigma.reshape(d,d,d,d).transpose(0,3,2,1).reshape(d*d,d*d)
    eigenvalues = np.linalg.eigvalsh(transpose_b)
    return float(-sum(z for z in eigenvalues if z < 0))

# Full spectral computation for all flat ranks and multiple rational/noise endpoints.
for d in range(2, 8):
    for k in range(1, d+1):
        for p,q in [
            (0.0,0.0), (0.0,0.6), (1.0,1.0),
            (0.17,0.39), (0.5,0.5), (0.62,0.42), (0.91,0.88)
        ]:
            observed = matrix_negativity(d,k,p,q)
            expected = closed_negativity(d,k,p,q)
            assert abs(observed-expected) < 2e-11, (d,k,p,q,observed,expected)

# Exact rational witness: partially supported qutrit pair is NPT but the
# maximally supported pair has vanishing negativity at identical noise.
qutrit_two = closed_negativity(3,2,Fraction(1,2),Fraction(1,2))
qutrit_three = closed_negativity(3,3,Fraction(1,2),Fraction(1,2))
assert qutrit_two == Fraction(1,72)
assert qutrit_three == 0

# At each predicted symmetric-noise switch, the two adjacent ranks tie
# and beat all other ranks (when the switch belongs to the domain).
for d in range(3,13):
    thresholds = [d/(d+1+sqrt(2*k+1)) for k in range(2,d)]
    assert all(a>b for a,b in zip(thresholds,thresholds[1:]))
    for k in range(2,d):
        t=d/(d+1+sqrt(2*k+1))
        vals=[closed_negativity(d,j,t,t) for j in range(1,d+1)]
        best=max(vals)
        assert best>0
        assert abs(vals[k-1]-best)<1e-11
        assert abs(vals[k]-best)<1e-11
        for j in range(1,d+1):
            if j not in (k,k+1):
                assert vals[j-1] < best - 1e-12
    death=d/(d+1+sqrt(3))
    assert all(closed_negativity(d,j,death,death)<1e-11 for j in range(1,d+1))
    for k in range(2,d+1):
        if k == d:
            t=(d/(d+1+sqrt(2*(d-1)+1)))*0.5
        elif k == 2:
            t=(d/(d+1+sqrt(2*k+1))+death)/2
        else:
            t=(d/(d+1+sqrt(2*k+1))+d/(d+1+sqrt(2*(k-1)+1)))/2
        vals=[closed_negativity(d,j,t,t) for j in range(1,d+1)]
        assert vals[k-1] > 0
        assert vals[k-1] == max(vals)
        assert all(vals[k-1]>v+1e-12 for j,v in enumerate(vals,1) if j!=k)

print('VERIFY_OK')
