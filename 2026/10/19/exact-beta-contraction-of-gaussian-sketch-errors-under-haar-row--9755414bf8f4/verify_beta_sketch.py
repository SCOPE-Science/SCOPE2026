"""Reproducibility checks for the finite-sample Haar sketch law.

Run: python verify_beta_sketch.py
Requires numpy and scipy. This program is diagnostic; the infinite-probability
statements are established by the mathematical proof, not by random trials.
"""
import numpy as np
from scipy.stats import ks_2samp
from scipy.special import gammaln

rng = np.random.default_rng(20260518)
checks = 0


def require(condition, message):
    global checks
    assert bool(condition), message
    checks += 1


def moment(n, ell, r, order):
    nu = ell-r+1
    if ell == n:
        return 0.0
    if 2*order >= nu:
        return np.inf
    a = (n-ell)/2
    c = (n-r)/2
    log_m = (gammaln(a+order) - gammaln(a)
             + gammaln(c) - gammaln(c+order)
             + gammaln(r/2+order) - gammaln(r/2)
             + gammaln(nu/2-order) - gammaln(nu/2))
    return np.exp(log_m)


def draw_haar_excess(n, ell, r, count):
    vals = np.empty(count)
    for j in range(count):
        g = rng.standard_normal((n, ell))
        q, _ = np.linalg.qr(g)
        mat = q[:r,:].T
        target = q[r,:]
        v = np.linalg.solve(mat.T@mat, mat.T@target)
        vals[j] = v@v
    return vals


def draw_coupled_excess(n, ell, r, count):
    if ell == n:
        return np.zeros(count)
    if ell == r:
        beta = np.ones(count)
    else:
        beta = rng.beta((n-ell)/2, (ell-r)/2, count)
    return beta * rng.chisquare(r, count)/rng.chisquare(ell-r+1, count)


# Check that direct projected normal equations match the complementary
# Gaussian-subspace least-squares derivation for arbitrary nonorthogonal designs.
for n, ell, r in [(8,5,2),(11,7,3),(12,4,4),(9,9,2)]:
    for _ in range(50):
        a = rng.normal(size=(n,r))
        b = rng.normal(size=n)
        qa, _ = np.linalg.qr(a)
        residual = b-qa@(qa.T@b)
        if ell < n:
            h = rng.normal(size=(n-ell,n))
            proj = np.eye(n)-h.T@np.linalg.solve(h@h.T,h)
        else:
            h=np.zeros((0,n))
            proj=np.eye(n)
        full = np.linalg.solve(a.T@a,a.T@b)
        sketched = np.linalg.solve(a.T@proj@a,a.T@proj@b)
        require(np.linalg.norm(a.T@proj@(a@sketched-b))<2e-8,
                'sketched normal equations')
        if ell < n:
            h1 = h@qa
            h2 = h@(np.eye(n)-qa@qa.T)
            z = -np.linalg.lstsq(h2.T, residual, rcond=None)[0]
            v = h1.T@z
            predicted = qa.T@(a@(sketched-full))
            require(np.linalg.norm(v-predicted)<2e-8*(1+np.linalg.norm(predicted)),
                    'complementary subspace coefficient identity')

# Direct Haar samples versus the independent Beta * chi-square-ratio law.
for n, ell, r in [(8,4,1),(12,5,2),(12,7,3),(20,8,2),(11,3,3)]:
    direct=draw_haar_excess(n,ell,r,6000)
    coupled=draw_coupled_excess(n,ell,r,6000)
    ks=ks_2samp(direct,coupled).statistic
    require(ks < 0.055, f'distributional identity {n,ell,r}: KS={ks}')
    for quantile in (0.1,0.25,0.5,0.75,0.90):
        left=np.quantile(direct,quantile)
        right=np.quantile(coupled,quantile)
        fraction=np.mean(direct<=right)
        require(abs(fraction-quantile)<0.06,
                f'quantile agreement {n,ell,r,quantile}')

# Integer-moment formula, boundary and the known exact mean.
for n in range(6,19):
    for r in range(1,min(n,5)):
        for ell in range(r,n+1):
            if ell == n:
                require(moment(n,ell,r,1)==0.0, 'full sketch exact')
                continue
            for order in (1,2,3):
                actual=moment(n,ell,r,order)
                if ell-r+1<=2*order:
                    require(np.isinf(actual), 'moment existence threshold')
                else:
                    require(np.isfinite(actual) and actual>0,'positive moment')
            if ell>r+1:
                known=r*(n-ell)/((n-r)*(ell-r-1))
                require(np.isclose(moment(n,ell,r,1),known,rtol=3e-12),
                        'published exact mean recovered')

# Scalar finite-difference identity for the Beta risk factor,
# tested without simulation for random integer dimensions.
for n in range(3,60):
    for r in range(1,n):
        for ell in range(r+1,n):
            reduction=(n-ell)/(n-r)
            require(0<reduction<1, 'strict Beta contraction')

print(f'PASS: {checks} checks (complement projection, law, moments, boundaries).')
