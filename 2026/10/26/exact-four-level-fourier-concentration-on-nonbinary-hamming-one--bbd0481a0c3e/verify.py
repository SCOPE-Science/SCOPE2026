"""Reproducible finite checks for radius-one Fourier concentration; not an infinite proof."""
import itertools
import math
from fractions import Fraction
import numpy as np


def points(q, d):
    pts = [(0,) * d]
    for i in range(d):
        for a in range(1, q):
            z = [0] * d
            z[i] = a
            pts.append(tuple(z))
    return pts


def matrix(q, d):
    pts = points(q, d)
    n = len(pts)
    return np.array([[n-q*sum(a != b for a,b in zip(x,y)) for y in pts] for x in pts], dtype=np.int64)


checks = 0
for q in range(3, 10):
    for d in range(3, 10):
        mat = matrix(q,d)
        L = d*(q-1)
        N = L+1
        T = q*q + 1 + d*(d-2)*(q-1)**2
        assert N == len(mat)
        assert int(np.trace(mat)) == N*N
        assert T*T > 4*q*q
        mu_plus = (T+math.sqrt(T*T-4*q*q))/2
        mu_minus = q*q/mu_plus
        assert 0 < mu_minus < q < q*q < mu_plus < q**d, (q,d,mu_plus,q**d)
        checks += 5
        # Contrasts internal to a single coordinate axis.
        for i in range(d):
            for a in range(2, q):
                v = np.zeros(N, dtype=np.int64)
                v[1+i*(q-1)] = 1
                v[1+i*(q-1)+(a-1)] = -1
                assert np.array_equal(mat@v, q*v)
                checks += 1
        # Contrasts between axis-constant vectors.
        for i in range(1,d):
            v = np.zeros(N, dtype=np.int64)
            v[1:1+q-1] = 1
            v[1+i*(q-1):1+(i+1)*(q-1)] = -1
            assert np.array_equal(mat@v,q*q*v)
            checks += 1
        # Two-dimensional residual block, in the nonnormalized radial basis.
        zero = np.zeros(N,dtype=np.int64); zero[0]=1
        one = np.ones(N,dtype=np.int64); one[0]=0
        assert np.array_equal(mat@zero, N*zero + (N-q)*one)
        assert np.array_equal(mat@one, L*(N-q)*zero + (T-N)*one)
        assert N*(T-N)-L*(N-q)**2 == q*q
        checks += 3
        # Exact characteristic polynomial from invariant decomposition.
        # trace(M^2) = mu_+^2 + mu_-^2 + (d-1)q^4 + d(q-2)q^2.
        assert int(np.trace(mat@mat)) == T*T-2*q*q+(d-1)*q**4+d*(q-2)*q*q
        checks += 1

# The character kernel agrees with the combinatorial matrix on cyclic groups.
for q,d in [(3,3),(3,4),(4,3),(4,4),(5,3),(6,3)]:
    pts = points(q,d)
    Fourier = np.array([[np.exp(-2j*np.pi*sum(a*b for a,b in zip(x,xi))/q) for x in pts] for xi in pts],dtype=complex)/q**(d/2)
    Gram = Fourier.conj().T @ Fourier
    expected = matrix(q,d)/q**d
    assert np.max(np.abs(Gram-expected)) < 3e-13, (q,d)
    expected_spectrum = np.array([
        (q*q+1+d*(d-2)*(q-1)**2-math.sqrt((q*q+1+d*(d-2)*(q-1)**2)**2-4*q*q))/(2*q**d),
        *([q**(1-d)]*(d*(q-2))),
        *([q**(2-d)]*(d-1)),
        (q*q+1+d*(d-2)*(q-1)**2+math.sqrt((q*q+1+d*(d-2)*(q-1)**2)**2-4*q*q))/(2*q**d)
    ])
    assert np.max(np.abs(np.sort(np.linalg.eigvalsh(Gram))-np.sort(expected_spectrum))) < 2e-12
    checks += 2

# Noncyclic four-element alphabet: A = (Z/2Z)^2.
q,d = 4,3
pts = points(q,d)
chi = lambda a,b: (-1)**((a&1)*(b&1)+((a>>1)&1)*((b>>1)&1))
F = np.array([[np.prod([chi(a,b) for a,b in zip(x,xi)]) for x in pts] for xi in pts], dtype=float)/q**(d/2)
assert np.max(np.abs(F.T@F-matrix(q,d)/q**d)) < 1e-12
checks += 1
print(f'VERIFY_OK exact_block_and_contrast_checks={checks-13} direct_fourier_tests=13 total_assertion_units={checks}')
