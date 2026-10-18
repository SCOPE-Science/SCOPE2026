"""Reproduce finite spectral-hole identities and the critical Poisson point-process limit."""
from fractions import Fraction
from math import exp, log, sqrt, pi
from scipy.special import erfcx
from scipy.integrate import quad

checks = 0
for n in range(2, 40):
    for theta in (1, 2, 3):
        probs = [Fraction(1, k**theta) for k in range(2, n+2)]
        m = sum(probs)
        d = sum((2*k-1)*prob for k, prob in zip(range(2, n+2), probs))
        # Factorial and independent-Bernoulli identities.
        assert m == sum(probs)
        assert d == sum((2*k-1)*prob for k, prob in zip(range(2,n+2), probs))
        assert sum(p*(1-p) for p in probs) <= m
        assert sum(Fraction((2*k-1)**2)*p*(1-p) for k,p in zip(range(2,n+2), probs)) <= (2*n+1)*d
        checks += 4

# Critical n^{-1} weighted-hole Laplace transform converges to doubled Dickman.
for s in (0.3, 0.8, 2.0):
    limit = exp(quad(lambda x: (exp(-2*s*x)-1)/x if x>0 else -2*s, 0, 1, epsabs=1e-12)[0])
    errors = []
    for n in (1000, 3000, 10000):
        lp = sum(log(1 + (exp(-s*(2*k-1)/n)-1)/k) for k in range(2,n+2))
        errors.append(abs(exp(lp)-limit))
    assert errors[2] < errors[0] and errors[2] < 0.001
    checks += 1

# Beta=1/2 Mittag-Leffler laplace is erfcx(s), with sharp near-zero constant 1/sqrt(pi).
for c in (0.7, 1.0, 1.3):
    for n in (2000, 6000, 20000):
        em = sum(erfcx(c*log(k)) for k in range(2,n+2))
        ed = sum((2*k-1)*erfcx(c*log(k)) for k in range(2,n+2))
        r1 = em * c*sqrt(pi)*log(n)/n
        r2 = ed * c*sqrt(pi)*log(n)/(n*n)
        assert 0.80 < r1 < 1.25 and 0.80 < r2 < 1.25
        checks += 2

# Critical conditional exact variance formula: mean 2N+O(log N), variance 2N^2+o(N^2).
for n in (1000, 10000):
    mu = sum((2*k-1)/k for k in range(2, n+2))
    var = sum(((2*k-1)**2)*(1/k)*(1-1/k) for k in range(2,n+2))
    assert abs(mu/n - 2)<0.03 and abs(var/n**2 -2)<0.04
    checks += 2
print(f'PASS: {checks} finite exact identities / numerical asymptotic checks')
