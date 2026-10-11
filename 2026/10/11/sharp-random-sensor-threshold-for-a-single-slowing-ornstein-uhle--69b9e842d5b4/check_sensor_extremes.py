"""Finite diagnostic identities for independent random-direction OU sensors.

All infinite assertions in RESULT.md require their analytical proofs. This
script checks special exact CDFs, general special-function identities, and
finite-size numerical consistency with the stated limiting formulas.
"""
import math
from scipy.special import betainc
from scipy.stats import chi2

checks = 0

def near(got, want, tol=2e-11):
    global checks
    assert abs(got-want) <= tol, (got, want, tol)
    checks += 1

# In dimension three the squared first coordinate is Beta(1/2,1): F(w)=sqrt(w).
for m in range(1, 13):
    for w in (0.04, 0.25, 0.49, 0.81):
        near(betainc(.5, 1, w)**m, w**(m/2), 4e-14)

# In dimension two the squared first coordinate has the arcsine law.
for m in range(1, 6):
    for w in (0.01, 0.125, 0.5, 0.875, 0.99):
        near(betainc(.5, .5, w)**m, (2*math.asin(math.sqrt(w))/math.pi)**m, 2e-13)

# Exact finite-n identity: probability at least one random sensor has a
# larger critical-mode than stable-mode variance.
for n in (3, 10, 64, 256):
    for m in (1, 3, 10):
        for eps in (.02, .1, .5):
            threshold = eps/(1+eps)
            p = -math.expm1(m*math.log(betainc(.5,(n-1)/2,threshold)))
            tail = betainc((n-1)/2,.5,1-threshold)
            slow_probability = -math.expm1(m*math.log1p(-tail))
            near(p, slow_probability)

# Finite-parameter OU identities and normalized variance transform.
for n in (3, 16, 100):
    for eps in (.02, .15, .6):
        for w in (.0003, .02, .3):
            v = .5*(1+(1/eps-1)*w)
            near(n*eps/(1-eps)*(2*v-1), n*w, 1e-11)
            for t in (.2, 2.0):
                acf = ((w/eps)*math.exp(-eps*t)+(1-w)*math.exp(-t))/(w/eps+1-w)
                numerator = w*math.exp(-eps*t)/eps+(1-w)*math.exp(-t)
                near(acf, numerator/(2*v), 3e-14)

# Quantile-window convergence: exact Beta formula vs limiting Gumbel.
# These are numerical diagnostics with tolerance; not a proof.
for n, m in ((20000, 200), (50000, 300), (100000, 400)):
    b = 2*math.log(m)-math.log(math.log(m))-math.log(math.pi)
    for x in (-1.0, 0.0, 1.0):
        eps = (b+2*x)/n
        cdf = betainc(.5,(n-1)/2,eps/(1+eps))**m
        target = math.exp(-math.exp(-x))
        assert abs(cdf-target) < .2, (n,m,x,cdf,target)
        checks += 1

# Gumbel centering has correct Gaussian-square tail asymptotics.
for m in (1000, 10000, 1000000):
    b = 2*math.log(m)-math.log(math.log(m))-math.log(math.pi)
    for x in (-1,0,1):
        mp = m*chi2.sf(b+2*x, 1)
        assert abs(mp-math.exp(-x))/math.exp(-x)<.22, (m,x,mp)
        checks += 1

print(f"PASS: {checks} finite diagnostics; no claim of numerical proof for infinite limits")
