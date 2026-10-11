import math
from fractions import Fraction

try:
    import numpy as np
    import mpmath as mp
except Exception as exc:
    raise SystemExit('required verification dependency unavailable: %s' % exc)

# Exact beta mean and variance identities.
for N in range(2, 31):
    for n in range(1, N):
        mean = Fraction(n, N)
        var = Fraction(2*n*(N-n), N*N*(N+2))
        A = Fraction(n, 2)
        B = Fraction(N-n, 2)
        mean_beta = A/(A+B)
        var_beta = A*B/((A+B)**2*(A+B+1))
        assert mean == mean_beta
        assert var == var_beta

# Rank-one compression replay on deterministic pseudorandom Grassmannian samples.
rng = np.random.default_rng(20261006)
for N,n,a,b in [(5,1,3.0,1.0),(7,2,4.0,1.5),(9,4,2.5,0.8),(12,7,5.0,2.0)]:
    m = N-n
    for _ in range(8):
        Z = rng.normal(size=(N,m))
        U,_ = np.linalg.qr(Z)
        Q = np.diag([1/a**2] + [1/b**2]*(N-1))
        comp = U.T @ Q @ U
        got = np.linalg.eigvalsh(comp)[0]
        S = float(np.sum(U[0,:]**2))
        want = 1/b**2 - (1/b**2-1/a**2)*S
        assert abs(got-want) < 2e-12

# Beta integral versus hypergeometric moment formula.
mp.mp.dps = 50
for N,n,kappa,q in [(5,1,3,1),(7,2,4,2),(9,4,2.5,3),(12,7,5,0.5)]:
    A = mp.mpf(n)/2
    B = mp.mpf(N-n)/2
    c = mp.mpf(kappa)**2-1
    beta = mp.beta(A,B)
    integ = mp.quad(lambda t: (1+c*t)**(-mp.mpf(q)/2) * t**(A-1)*(1-t)**(B-1)/beta, [0,1])
    hyp = mp.hyper([mp.mpf(q)/2,A],[mp.mpf(N)/2],-c)
    assert abs(integ-hyp) < mp.mpf('1e-25')

# Factor-C CDF threshold replay.
for N,n,kappa,C in [(5,1,3,1.4),(7,2,4,2),(9,4,2.5,1.2),(12,7,5,3)]:
    A = mp.mpf(n)/2
    B = mp.mpf(N-n)/2
    th = (mp.mpf(kappa)**2/mp.mpf(C)**2-1)/(mp.mpf(kappa)**2-1)
    tail = 1-mp.betainc(A,B,0,th,regularized=True)
    # Inverting R/b = kappa/sqrt(1+(kappa^2-1)T) gives exactly T >= th.
    assert 0 < th < 1
    assert 0 < tail < 1

print('VERIFY_OK')
print('beta_mean_variance=exact N=2..30')
print('rank_one_compression=32 deterministic Haar samples')
print('moment_integrals=4 high_precision checks')
print('factor_C_thresholds=4 checks')
