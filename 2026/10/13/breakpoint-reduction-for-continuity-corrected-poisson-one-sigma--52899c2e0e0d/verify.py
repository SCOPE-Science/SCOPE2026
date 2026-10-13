import math
from scipy.stats import poisson

def bounds(lam):
    return max(0, math.floor(lam-math.sqrt(lam))), math.ceil(lam+math.sqrt(lam))

def J(lam):
    ell, u = bounds(lam)
    return poisson.cdf(u, lam) - (poisson.cdf(ell-1, lam) if ell else 0.0)

def derivative_formula(lam, ell, u):
    left = 0.0 if ell == 0 else math.exp(-lam + (ell-1)*math.log(lam) - math.lgamma(ell))
    right = math.exp(-lam + u*math.log(lam) - math.lgamma(u+1))
    return left-right

for lam in [0.1, 0.5, 1.2, 2.0, 3.0, 5.5, 10.3, 25.4, 100.7]:
    ell, u = bounds(lam)
    h = 1e-6
    if bounds(lam-h) == (ell,u) and bounds(lam+h) == (ell,u):
        fd = (J(lam+h)-J(lam-h))/(2*h)
        assert abs(fd-derivative_formula(lam,ell,u)) < 2e-7

for s in range(2,101):
    x = s*s
    eps = 1e-8
    assert J(x) < J(x-eps)
    assert J(x) < J(x+eps)

print("VERIFY_OK derivative_formula squares=2..100")
