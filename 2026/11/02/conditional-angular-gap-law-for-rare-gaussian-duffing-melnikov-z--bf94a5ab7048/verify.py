"""Supplementary elementary checks for the conditional Melnikov gap theorem.
Finite computations support (but never replace) the analytic proof.
"""
import math
import random

C = 2 * math.sqrt(2) / (3 * math.pi)

def w(k, omega):
    z = .5 * math.pi * omega * k
    return omega * k * 2 * math.exp(-z) / (1 + math.exp(-2*z))

def qtail(omega):
    q = math.exp(-math.pi * omega / 2)
    return 2 * omega * q*q*(2-q)/(1-q)**2

def gap_cdf(d, t):
    u = math.cos(d/2)
    return 1 - u*math.sqrt(1+t*t)/math.sqrt(1+t*t*u*u)

for omega in (1.0, 1.7, 2.5, 4.0, 6.0):
    weights = [w(k,omega) for k in range(1,101)]
    assert abs(w(1,omega)-omega/math.cosh(math.pi*omega/2)) < 1e-12
    assert sum(weights[1:]) <= qtail(omega) * (1 + 1e-12)
    ratio = sum(k*weights[k-1] for k in range(2,101))/weights[0]
    assert ratio > 0 and ratio < 200*math.exp(-math.pi*omega/2)
    t = weights[0]/C
    assert gap_cdf(0,t) == 0
    assert abs(gap_cdf(math.pi,t)-1) < 2e-16
    assert 0 < gap_cdf(math.pi/2,t) < 1

rng = random.Random(261033620)
for t in (0.15,0.55,1.1):
    n = 190_000
    accepted = 0
    counted = [0,0,0]
    for _ in range(n):
        delta, a, b = rng.gauss(0,1),rng.gauss(0,1),rng.gauss(0,1)
        R = math.hypot(a,b)
        if abs(delta)<=t*R:
            accepted += 1
            d=2*math.acos(min(1,abs(delta)/(t*R)))
            for j,threshold in enumerate((math.pi/3,math.pi/2,2*math.pi/3)):
                counted[j] += (d<=threshold)
    p=t/math.sqrt(1+t*t)
    assert abs(accepted/n-p)<0.011, (t,accepted/n,p)
    for j,threshold in enumerate((math.pi/3,math.pi/2,2*math.pi/3)):
        empirical=counted[j]/accepted
        expected=gap_cdf(threshold,t)
        assert abs(empirical-expected) < 0.025,(t,threshold,empirical,expected)
print('PASS: weight bounds; exact one-harmonic gap CDF; 9 conditional Monte Carlo checks')
