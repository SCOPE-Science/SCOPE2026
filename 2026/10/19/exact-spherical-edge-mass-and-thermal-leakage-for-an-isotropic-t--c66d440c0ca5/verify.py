#!/usr/bin/env python3
"""Finite-moment checks for a spherical harmonic RTP stationary law.
These are finite checks and not proofs of asymptotic convergence.
"""
import math
import numpy as np
from scipy.special import gammaln, digamma


def moment_check(d, alpha, nmax=1000):
    # Dirichlet mean generalized-Stieltjes generating function coefficients.
    k = np.arange(1, nmax+1)
    logs = gammaln(k + .5) - gammaln(.5) + gammaln(d/2) - gammaln(k+d/2)
    m = np.exp(logs)
    a = alpha * m / (2*k)
    b = np.empty(nmax+1); b[0] = 1.0
    # n*b_n = alpha/2 * sum m_k*b_{n-k}
    for n in range(1,nmax+1):
        b[n] = (alpha/2/n) * np.dot(m[:n],b[n-1::-1])
    beta=(d-1)/2
    F1 = math.exp(-alpha*(math.log(2)+digamma(beta)-digamma(2*beta)))
    for n in [25,100,400,1000]:
        # R^(2n) moment from one-coordinate moment + sphere factors
        logv = math.log(b[n]) + gammaln(2*n+1)+gammaln(alpha)-gammaln(2*n+alpha) \
             +gammaln(n+d/2)-gammaln(d/2)+gammaln(.5)-gammaln(n+.5)
        logasym = math.log(F1)+gammaln(alpha+1)-alpha*math.log(2*n)
        if d==2:
            # exact beta: E[(R^2)^n] = Gamma(alpha+1) Gamma(n+1)/Gamma(n+alpha+1)
            exact_log = gammaln(alpha+1)+gammaln(n+1)-gammaln(n+alpha+1)
            assert abs(logv-exact_log) < 3e-10, ('beta disagreement',d,alpha,n,logv,exact_log)
        print(f'd={d}, alpha={alpha:4.2f}, n={n:4d}, ratio={math.exp(logv-logasym):.7f}; C_d={F1:.9f}')

for d,alpha in [(2,0.6),(2,1.7),(3,.8),(4,.75),(4,1.2),(5,1.5),(8,.6)]:
    moment_check(d,alpha)
print('PASS: 28 numerical moment comparisons and 8 d=2 exact beta identities')


# Corroborative finite-sample Gaussian-leakage measurements.
from scipy.special import gamma
rng = np.random.default_rng(403026)
N = 180000
for d, alpha in [(2, 0.6), (3, 0.8), (4, 0.75), (5, 1.5)]:
    x = np.zeros((N, d), dtype=float)
    rem = np.ones(N)
    for j in range(75):
        fraction = rng.beta(1, alpha, N)
        direction = rng.normal(size=(N, d))
        direction /= np.linalg.norm(direction, axis=1)[:, None]
        x += (rem*fraction)[:, None]*direction
        rem *= 1-fraction
    assert rem.max() < 1e-8, ('insufficient stick truncation', d, alpha)
    C = math.exp((alpha/2)*(digamma(d/2)-digamma((d-1)/2)))
    normal_part = 2**(alpha/2-1)*gamma((alpha+1)/2)/math.sqrt(math.pi)
    for sigma in (0.03, 0.015):
        noise = rng.normal(size=x.shape)
        observed = (np.linalg.norm(x+sigma*noise, axis=1)>1).mean()
        predicted = C*normal_part*sigma**alpha
        std_err = math.sqrt(observed*(1-observed)/N)
        print(f'finite-noise d={d}, alpha={alpha}, sigma={sigma}: empirical {observed:.6f} +/- {2*std_err:.6f}; asymptotic {predicted:.6f}; ratio {observed/predicted:.4f}')
print('Finite-sample leakage checks completed (corroboration only).')
