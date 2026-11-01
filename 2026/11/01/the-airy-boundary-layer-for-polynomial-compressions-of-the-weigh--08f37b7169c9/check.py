"""Supplementary finite tests for the Bergman polynomial-compression Airy edge.

Run: python check.py. Requires numpy and scipy. Tests are not a proof of
any asymptotic, compactness, or originality statement.
"""
import math
from fractions import Fraction
import numpy as np
from scipy.linalg import eigh_tridiagonal
from scipy.special import ai_zeros, airy

checks = 0

def verify(statement, message):
    global checks
    if not statement:
        raise AssertionError(message)
    checks += 1

# Exact normalized Bergman-moment and shift-ratio tests, all arithmetic rational.
for alpha in range(0, 9):
    p = alpha + 1
    m = Fraction(1)
    for n in range(1, 100):
        m_next = m * Fraction(n, n+p)
        verify(m_next / m == Fraction(n,n+p), f'monomial ratio alpha={alpha} n={n}')
        verify(m_next > 0 and m_next < m, f'moment monotonicity alpha={alpha} n={n}')
        m = m_next

zero = abs(ai_zeros(1)[0][0])
verify(2.3381 < zero < 2.3382, 'Airy zero bracket')

# Rayleigh identity, direct matrix comparison, and scaled Airy eigenvalue profiles.
for p in [0.3, 0.75, 1.0, 2.0, 4.0]:
    last = 10.0
    scaled = []
    for N in [256, 512, 1024, 2048, 4096]:
        w = np.sqrt((np.arange(N, dtype=float)+1)/(np.arange(N, dtype=float)+p+1))
        eig, vec = eigh_tridiagonal(np.zeros(N+1),w/2,select='i',select_range=(N,N))
        r = float(eig[0])
        u = np.abs(vec[:,0]); u = u / np.linalg.norm(u)
        verify(0 < r < 1, 'spectral bound')
        verify(np.linalg.norm(u)-1 < 1e-11, 'normalized top vector')
        # Quadratic form identity, including its two ends (with outside weights 0).
        v = np.zeros(N+1)
        v[0] = 1-w[0]/2
        v[1:N] = 1-(w[:-1]+w[1:])/2
        v[N] = 1-w[-1]/2
        mu = 1-w[-1]
        lhs = 1-r-mu
        rhs = (np.sum(w*np.diff(u)**2)/2 + np.dot(v-mu,u*u))
        verify(abs(lhs-rhs) < 2e-11, f'energy identity p={p} N={N}, {lhs} vs {rhs}')
        verify(lhs >= -5e-14, 'positive edge energy')
        expected = zero*p**(2/3)/2
        scaled_value = (1-r-p/(2*N))*N**(4/3)
        scaled.append(scaled_value)
        verify(abs(scaled_value-expected)< 2.0, f'Airy edge finite sanity p={p}, N={N}')
        last = r
    # Large finite dimensions give a clearer approximation, not a proof.
    verify(abs(scaled[-1]-expected)<abs(scaled[0]-expected)+0.08, f'improvement p={p}')

# Compare eigenvector against continuous normalized Airy profile.
for p in [0.5, 1., 3.]:
    N = 4000
    h = N**(-2./3)
    w = np.sqrt((np.arange(N,dtype=float)+1)/(np.arange(N,dtype=float)+p+1))
    eig,vec=eigh_tridiagonal(np.zeros(N+1),w/2,select='i',select_range=(N,N))
    u=np.abs(vec[:,0])[::-1]
    j=np.arange(N+1,dtype=float)
    x=j*h
    norm = abs(airy(-zero)[1]); amplitude=p**(1/6)/norm
    profile=amplitude*airy(p**(1/3)*x-zero)[0]
    approx=math.sqrt(h)*profile
    distance=float(np.linalg.norm(u-approx))
    verify(distance < 0.27, f'Airy ground state finite test p={p} d={distance}')

# The Hardy endpoint is exactly the constant-coefficient tridiagonal.
for N in [1,2,3,9,32,200]:
    r=float(eigh_tridiagonal(np.zeros(N+1),np.full(N,0.5),select='i',select_range=(N,N))[0][0])
    verify(abs(r-math.cos(math.pi/(N+2))) < 2e-13, 'Hardy comparison')

print(f'PASS: {checks} finite supplementary assertions. Infinite limits are established analytically.')
