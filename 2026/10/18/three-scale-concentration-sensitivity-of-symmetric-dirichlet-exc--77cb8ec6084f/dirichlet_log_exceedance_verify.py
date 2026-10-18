"""Numerical cross-checks for a Dirichlet log-product/exceedance theorem.

Requires mpmath, scipy. Does not purport to prove infinite-dimensional claims.
"""
import math
import mpmath as mp
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import betaln, digamma, betainc

mp.mp.dps = 48
checks = 0


def cov(m, a, t):
    """Beta score integral for Cov(sum log X_i, count{X_i>t})."""
    c = (-digamma(a) - (m-1)*digamma((m-1)*a) + m*digamma(m*a))
    lb = betaln(a, (m-1)*a)
    def integrand(x):
        if x <= 0 or x >= 1:
            return 0.0
        h = math.log(x)+(m-1)*math.log1p(-x)+c
        f = math.exp((a-1)*math.log(x)+((m-1)*a-1)*math.log1p(-x)-lb)
        return h*f
    # Total expectation of the score is zero. Choose the safer endpoint.
    if t <= 0.5:
        power=max(1.0, 2/a)
        def transformed(u):
            if u<=0: return 0.0
            return integrand(t*u**power)*t*power*u**(power-1)
        return -m*quad(transformed, 0, 1, epsabs=3e-10, limit=250)[0]
    power=max(1.0, 2/((m-1)*a))
    def transformed(u):
        if u<=0: return 0.0
        x=1-(1-t)*u**power
        return integrand(x)*(1-t)*power*u**(power-1)
    return m*quad(transformed, 0, 1, epsabs=3e-10, limit=250)[0]


def assert_close(x, y, atol=1e-7, rtol=1e-7):
    global checks
    assert abs(float(x)-float(y)) < atol+rtol*abs(float(y)), (x,y)
    checks += 1

# Separate numerical-method check: finite-difference derivative of incomplete beta.
for m in (2,3,4,6,9):
    for a in (0.7,1.0,2.5):
        for t in (.12,.27,.43,.62,.8):
            d = 2e-5
            b0 = lambda z: 1 - betainc(z,(m-1)*z,t)
            derivative = m*(b0(a-2*d)-8*b0(a-d)+8*b0(a+d)-b0(a+2*d))/(12*d)
            assert_close(cov(m,a,t),derivative,atol=2e-7,rtol=3e-6)

# A single zero, with the signs predicted by the exact score-shape argument.
for m in (2,3,4,6,9,25,75):
    for a in (0.7, 1.0, 2.5):
        t_star = brentq(lambda t: cov(m,a,t), max(1e-5,0.0005/m), min(0.75,3/m),xtol=1e-10)
        assert cov(m,a,t_star*.75)>0, (m,a,t_star, cov(m,a,t_star*.75), cov(m,a,t_star))
        assert cov(m,a,t_star*1.1 if t_star*1.1 <1 else (t_star+1)/2)<0
        checks += 2
        if m==2:
            assert_close(t_star,.5,atol=3e-7)

# Small-precision limit: high-precision differentiation of Beta tails.
for m in (2,3,5):
    for t in (.2,.35,.65,.8):
        a = mp.mpf('0.003')
        target=(m-1)*math.log((1-t)/t)
        probability=lambda z: 1-mp.betainc(z,(m-1)*z,0,mp.mpf(t),regularized=True)
        actual=float(m*mp.diff(probability,a))
        assert abs(actual-target) < .07+abs(target)*.06, (m,t,actual,target)
        checks += 1

# The fixed-shape high-dimensional limit and the exponential closed form.
gamma = float(mp.euler)
def G1(y):
    return math.exp(-y)*(math.log(y)+gamma-y)+float(mp.e1(y))
root = brentq(G1,1.01,3,xtol=1e-13)
assert_close(root,1.3714020181783595,atol=1e-10)
for y in (.5,1,1.2,1.6,2,3):
    if y == root: continue
    limit = G1(y)
    # for X_1 ~ Beta(1,m-1), use threshold y/m
    approxim = cov(250,1,y/250)/250
    assert_close(approxim,limit,atol=.004,rtol=.17)

print('PASS',checks,'checks; gamma-alpha-one crossover',format(root,'.13f'))
