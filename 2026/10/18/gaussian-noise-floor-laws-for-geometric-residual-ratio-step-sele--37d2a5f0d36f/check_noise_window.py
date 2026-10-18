"""Deterministic checks and seeded numerical comparisons for Gaussian window ratios.
No finite test is a proof of the universal distributional statements.
"""
import math
import numpy as np
from scipy.special import betainc

rng = np.random.default_rng(7162927)
checks = 0

def close(a, b, tol=1e-11):
    global checks
    assert abs(a-b) <= tol, (a,b,tol)
    checks += 1

# Exact Cauchy / beta correspondence, exact symmetry and analytic moment identities.
for d in range(1, 11):
    a = d/2
    for w in range(1, 7):
        for t in (0.15,0.5,1.0,2.0,6.0):
            F = betainc(a,a,t**(2*w)/(1+t**(2*w)))
            G = betainc(a,a,(1/t)**(2*w)/(1+(1/t)**(2*w)))
            close(F+G,1,3e-10)
            if t == 1:close(F,0.5,2e-12)
            if d==1:close(F,2/math.pi*math.atan(t**w),2e-12)
        for q in (0.1,0.25,0.5,1.0,1.5,2.0,3.0):
            if q >= d*w:continue
            m = math.exp(math.lgamma(a+q/(2*w)) + math.lgamma(a-q/(2*w)) - 2*math.lgamma(a))
            assert m > 1
            checks += 1

# Independent Gaussian residual pairs, finite-sample F-CDF and moments.
for d,w in [(1,1),(1,2),(2,2),(3,1),(3,2),(5,2),(8,1)]:
    samples=100000
    x = np.sum(rng.normal(size=(samples,d))**2,axis=1)
    y = np.sum(rng.normal(size=(samples,d))**2,axis=1)
    q=(x/y)**(0.5/w)
    for threshold in (0.75,1.0,1.5,2.0):
        empirical=np.mean(q<=threshold)
        exact=betainc(d/2,d/2,threshold**(2*w)/(1+threshold**(2*w)))
        assert abs(empirical-exact) < 0.012,(d,w,threshold,empirical,exact)
        checks+=1
    assert abs(np.mean(q>1)-0.5)<0.012
    checks+=1
    # Use a low exponent for numerical robustness against exceptionally rare tails.
    moment_exp=min(0.4,d*w*0.35)
    empirical=float(np.mean(q**moment_exp))
    exact=math.exp(math.lgamma(d/2+moment_exp/(2*w))+math.lgamma(d/2-moment_exp/(2*w))-2*math.lgamma(d/2))
    assert abs(empirical-exact) < 0.025,(d,w,empirical,exact)
    checks+=1

# Exact Gaussian small-ball coefficient, limiting chi-ratio tail constant.
for d in range(1,11):
    gamma_const = math.exp(math.lgamma(d)-math.lgamma(d/2+1)-math.lgamma(d/2))
    small_ball_coeff=1/(2**(d/2)*math.gamma(d/2+1))
    num_moment=2**(d/2)*math.gamma(d)/math.gamma(d/2)
    close(small_ball_coeff*num_moment,gamma_const,1e-9)

print(f'passed {checks} distributional algebra, symmetry and seeded Gaussian checks')
