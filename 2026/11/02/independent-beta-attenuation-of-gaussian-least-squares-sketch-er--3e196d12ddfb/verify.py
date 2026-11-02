"""Checks for a finite-dimensional sketch-and-solve beta attenuation law.

Requires numpy and scipy. Run: python verify.py
"""
import math
import numpy as np
from scipy.special import beta as beta_function
from scipy.special import gamma, gammaln
from scipy.stats import beta as beta_distribution, betaprime, ks_2samp
from scipy.integrate import quad

CHECKS = 0

def check(ok, message):
    global CHECKS
    assert bool(ok), message
    CHECKS += 1


def factor(n, ell, power):
    a = (n - ell) / 2
    s = (n - 1) / 2
    return math.exp(gammaln(a + power) - gammaln(a)
                    + gammaln(s) - gammaln(s + power))

for n in range(4, 17):
    for ell in range(2, n):
        a, b = (n - ell) / 2, (ell - 1) / 2
        for power in (0.25, 0.5, 1, 1.5, 2, 4):
            m = beta_distribution.moment(int(power), a, b) if int(power) == power else factor(n,ell,power)
            check(abs(m - factor(n,ell,power)) < 3e-11,
                  'Beta moment identity')
        check(abs(factor(n,ell,1) - (n-ell)/(n-1)) < 1e-12,
              'Mean attenuation')
        check(0 < factor(n,ell,ell/2) < 1, 'Strict tail attenuation')

# A completely independent sketch construction, including an orthonormal
# frame obtained from QR rather than via the beta/gamma representation.
rng = np.random.default_rng(20261025)
N = 26000
n, ell, p = 10, 4, 3
raw = rng.standard_normal((N, n, ell))
q, _ = np.linalg.qr(raw, mode='reduced')
proj = np.einsum('tik,tk->ti',q[:,1:p+1,:],q[:,0,:])
p00 = np.sum(q[:,0,:]**2, axis=1)
haar_error2 = np.sum((proj/p00[:,None])**2,axis=1)

g = rng.standard_normal((N, n, ell))
xg = np.einsum('tik,tk->ti',g[:,1:p+1,:],g[:,0,:])/np.sum(g[:,0,:]**2, axis=1)[:,None]
gaussian_error2 = np.sum(xg*xg, axis=1)

rad = rng.beta((n-ell)/2,(ell-1)/2,size=N)
base = rng.chisquare(p,size=N)/rng.chisquare(ell,size=N)
coupled_error2 = rad*base
ks = ks_2samp(haar_error2,coupled_error2)
check(ks.statistic < 0.027, f'Direct Haar and beta-Gaussian CDF comparison: {ks.statistic}')
check(abs(np.mean(haar_error2)-p*(n-ell)/((n-1)*(ell-2))) < 0.080,
      'Haar mean matches exact factor')
check(abs(np.mean(gaussian_error2)-p/(ell-2)) < 0.14,
      'Gaussian mean matches exact factor')

# Independent scalar CDF check via Haar sampling and beta-prime mixture.
for t in (0.02,0.2,0.8,4,15):
    a, b = (n-ell)/2, (ell-1)/2
    analytic = quad(lambda z: beta_distribution.pdf(z,a,b)*betaprime.cdf(t/z,.5,ell/2),
                    0,1,epsabs=2e-9)[0]
    # Direct Haar scalar error uses first coordinate of the multi-output vector.
    empirical = np.mean((proj[:,0]/p00)**2 <= t)
    check(abs(empirical-analytic) < 0.019, 'Scalar direct Haar CDF vs integral')

# The large-threshold tail ratio is an explicit beta moment. Evaluate CDFs
# using positive survival probabilities; the limiting constant is nonzero.
a,b=(n-ell)/2,(ell-1)/2
for t in (2e4,1e6,1e8):
    pmix = quad(lambda z: beta_distribution.pdf(z,a,b)*betaprime.sf(t/z,.5,ell/2),
                0,1,epsabs=1e-15,epsrel=3e-9)[0]
    pg = betaprime.sf(t,.5,ell/2)
    check(abs(pmix/pg-factor(n,ell,ell/2)) < .002,
          'Sharp catastrophic-tail coefficient ratio')

# Exact identity in a representative instance.
check(abs(factor(10,4,1) - 2/3) < 1e-14, 'example mean ratio')
check(abs(factor(10,4,2) - 16/33) < 1e-14, 'example tail ratio')
print(f'PASS: {CHECKS} analytical, matrix, and seeded statistical checks; '
      f'direct-Haar KS={ks.statistic:.5f}, '
      f'tail ratio={factor(10,4,2):.12f}')
