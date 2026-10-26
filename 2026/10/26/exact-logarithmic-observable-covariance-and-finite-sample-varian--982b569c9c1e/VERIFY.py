"""Numerical cross-checks for exact logarithmic covariance formulas.

Run with: python VERIFY.py
Requires mpmath, available in standard scientific Python installations.
The computations test finite cases; the all-time claims are proved analytically.
"""
from math import isfinite
import mpmath as mp
mp.mp.dps = 45

def lag_covariance_gamma(q):
    Q = mp.mpf(q)
    L = mp.log(Q)
    val = mp.quad(lambda t: mp.log(t)*(mp.loggamma(Q+t)-mp.loggamma(t)-Q*L)/Q,
                  [0, mp.mpf('0.5'), 1])
    return val - 1

def lag_covariance_direct(q):
    Q = mp.mpf(q)
    return (sum(mp.quad(lambda t, j=j: mp.log((j+t)/Q)*mp.log(t),
                        [0, mp.mpf('0.5'), 1]) for j in range(q))/Q -1)

J = mp.quad(lambda t:mp.loggamma(t)*mp.log(t),[0, mp.mpf('0.5'),1])
c = -mp.log(2*mp.pi)/2-J
assert abs(lag_covariance_gamma(2)-(1-mp.pi**2/24)) < mp.mpf('1e-32')
for q in (2,4,8,16):
    a,b=lag_covariance_gamma(q),lag_covariance_direct(q)
    assert abs(a-b)<mp.mpf('1e-28'), (q,a,b)
    assert a>0
for k in (1,2,3,4,6,8,10,12):
    q=2**k
    exact=lag_covariance_gamma(q)
    leading=(mp.log(q)/4+c)/q
    assert abs(exact-leading)<1/mp.mpf(q)**2, (k,exact,leading)

# Exact covariance identity gives the finite-N variance.
C={k:lag_covariance_gamma(2**k) for k in range(1,15)}
for N in range(1,8):
    by_cov = N+2*sum((N-k)*C[k] for k in range(1,N))
    # Piecewise analytic interval integrals, not Monte Carlo.
    def s_integrand(x):
        s = sum(-mp.log(mp.frac((2**j)*x))-1 for j in range(N))
        return s*s
    by_direct = sum(mp.quad(s_integrand,[mp.mpf(j)/(2**(N-1)),
                                             mp.mpf(j+1)/(2**(N-1))])
                    for j in range(2**(N-1)))
    assert abs(by_cov-by_direct) < mp.mpf('1e-23'), (N,by_cov,by_direct)

for K in (8,12):
    partial=1+2*sum(C[k] for k in range(1,K+1))
    approx=partial + ((K+2)*mp.log(2)/2+2*c)/(2**K)
    bound=mp.mpf(2)/(3*(4**K))
    assert mp.mpf('3.705485920780') > approx-bound
    assert mp.mpf('3.705485920781') < approx+bound

print('VERIFY_OK direct_covariance_q=2,4,8,16 sharp_lag_bounds=8 direct_variance_N=1..7')
print('sigma2_approx=',mp.nstr(approx,17),'rigorous_series_tail_bound=',mp.nstr(bound,5))
