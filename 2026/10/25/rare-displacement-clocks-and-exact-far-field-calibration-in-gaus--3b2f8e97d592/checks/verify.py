#!/usr/bin/env python3
"""Deterministic numerical checks for a geometric-Gaussian renewal model.

Requires only the Python standard library. These checks corroborate finite
parameter identities; they do not replace the mathematical proof of limits.
"""
import cmath
import math

checks = 0

def close(actual, expected, tol, label):
    global checks
    if not abs(actual - expected) <= tol:
        raise AssertionError(f'{label}: got {actual!r}, expected {expected!r}, tolerance {tol}')
    checks += 1

def stable_posterior(p, r, n_max=None):
    a = -math.log1p(-p)
    beta = math.sqrt(2*a)
    if n_max is None:
        n_max = max(600, int(8*r/beta)+200)
    logs = [-a*n - .5*math.log(n) - r*r/(2*n) for n in range(1,n_max+1)]
    z = max(logs)
    w = [math.exp(x-z) for x in logs]
    total = math.fsum(w)
    weights = [x/total for x in w]
    density_log = math.log(p)-.5*math.log(2*math.pi)+z+math.log(total)
    mean = math.fsum((i+1)*v for i,v in enumerate(weights))
    var = math.fsum(((i+1)-mean)**2 *v for i,v in enumerate(weights))
    return density_log, mean, var, weights

for p in [0.15, 0.30, 0.60, 0.85]:
    q = 1-p
    a = -math.log(q)
    beta = math.sqrt(2*a)
    close(math.fsum(p*q**n for n in range(1200)), 1.0, 2e-14, 'geometric normalization')
    for k in [0., 0.2, 0.6, 1.1, 2.]:
        direct = math.fsum(p*q**n*math.exp(-.5*n*k*k) for n in range(1200))
        formula = p/(1-q*math.exp(-.5*k*k))
        close(direct, formula, 2e-13, 'stationary characteristic function')
    for r in [20., 30., 45., 70., 100.]:
        logf, mean, var, weights = stable_posterior(p,r)
        close(math.exp(logf-(math.log(p)-math.log(beta)-beta*r)), 1., 5e-6, 'density far-field prefactor')
        close(mean, r/beta + 1/(2*a), .01, 'conditioned count mean and constant')
        close(var, r/beta**3 + 1/(2*a*a), .1, 'conditioned count variance and constant')
        close(sum(weights), 1., 1e-11, 'conditioned count normalization')
    r = 100.
    _, _, _, weights = stable_posterior(p, r)
    sd = math.sqrt(r/beta**3)
    mid = r/beta
    for z in [-1.5, -0.5, 0.5, 1.5]:
        posterior_cdf = math.fsum(v for i,v in enumerate(weights) if ((i+1)-mid)/sd <= z)
        norm_cdf = (1+math.erf(z/math.sqrt(2)))/2
        close(posterior_cdf, norm_cdf, .12, 'conditioned count central limit profile')

# Independent exponential jump/reset clocks: observation-age transform.
for jump_rate, reset_rate in [(0.9,0.4), (1.7,0.8), (0.5,1.6)]:
    total_rate = jump_rate + reset_rate
    q = jump_rate/total_rate
    p = reset_rate/total_rate
    for s in [0.,0.1,0.4,1.5]:
        b_hat = total_rate/(total_rate+s)
        jump_hat = b_hat
        for k in [0.,0.3,0.8]:
            direct = p*b_hat * math.fsum((q*jump_hat*math.exp(-.5*k*k))**n for n in range(1500))
            formula = reset_rate/(reset_rate+s+jump_rate*(1-math.exp(-.5*k*k)))
            close(direct, formula, 2e-13, 'exponential-clock position-age transform')
    for r in [25.,50.,100.]:
        _, mean, var, _ = stable_posterior(p,r)
        clock_mean = (mean+1)/total_rate
        clock_var = (mean+1+var)/total_rate**2
        aa=-math.log(q)
        bb=math.sqrt(2*aa)
        clock_mean_asym=(r/bb+1/(2*aa)+1)/total_rate
        clock_var_asym=(r/bb**3+1/(2*aa**2)+r/bb+1/(2*aa)+1)/total_rate**2
        close(clock_mean,clock_mean_asym,.01,'conditional reset-age mean')
        close(clock_var,clock_var_asym,.15,'conditional reset-age variance')
    s=.5
    b_hat=total_rate/(total_rate+s)
    close(p*b_hat/(1-q*b_hat), reset_rate/(reset_rate+s), 2e-13, 'reset age marginal')

# A non-exponential competition: jump clock Uniform(0,2), reset clock 1.
# Here q=p=1/2, T=min(J,1), mean(T)=3/4,
# conditional jump time Uniform(0,1), and equilibrium current age has
# transform (1-E[exp(-s*T)])/(s*mean(T)).
for s in [0.1,0.4,1.2]:
    et=(1-math.exp(-s))/(2*s)+.5*math.exp(-s)
    b_hat=(1-et)/(.75*s)
    jump_hat=(1-math.exp(-s))/s
    for k in [0.,.2,.9]:
        direct=.5*b_hat*math.fsum((.5*jump_hat*math.exp(-.5*k*k))**n for n in range(500))
        formula=.5*b_hat/(1-.5*jump_hat*math.exp(-.5*k*k))
        close(direct,formula,2e-13,'non-exponential-clock transform')

print('PASS:',checks,'deterministic comparisons')
