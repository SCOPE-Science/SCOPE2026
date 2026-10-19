"""Standalone numerical cross-checks for a Gaussian-sketched harmonic Ritz law.

The proof is analytic; finite random checks do not certify any tail or moment claim.
"""
import math
import numpy as np
from scipy import integrate, special, stats

rng = np.random.default_rng(273)
A = np.diag([1.0, 4.0])
v = np.array([1.0, 1.0])/math.sqrt(2)
u = A @ v
mu = (v @ u) / (u @ u)
w = v - mu*u
sigma = np.linalg.norm(w) / np.linalg.norm(u)
assert abs(mu-5/17)<1e-14
assert abs(sigma-3/17)<1e-14
assert np.linalg.norm(w) > .1 and abs(w @ u)<1e-14

checks = 0
for s in (2,3,6):
    # Simulate the exact generalized eigenvalue from Section 3.5 of the source.
    batch = 200000
    S = rng.standard_normal((batch, s, 2))
    Su = S @ u
    Sv = S @ v
    Sw = S @ (w / np.linalg.norm(w))
    X = np.linalg.norm(Su, axis=1)
    Z = np.einsum('bs,bs->b',Su,Sw)/X
    R = np.einsum('bs,bs->b',Su,Sv) / X**2
    direct_inverse = 1 / R
    normal_form = mu + sigma*Z / (X/np.linalg.norm(u))
    assert np.max(abs(R - normal_form)) < 1e-11
    assert np.max(abs(direct_inverse * R - 1)) < 1e-11
    checks += 2*batch
    prob = stats.t.cdf(-mu*math.sqrt(s)/sigma,s)
    empirical = np.mean(R<0)
    se = math.sqrt(prob*(1-prob)/batch)
    assert abs(empirical-prob) <= max(6*se, 0.001)
    checks += 1
    coefficient = special.gamma((s+1)/2)/(sigma*math.sqrt(math.pi)*special.gamma(s/2))*(1+(mu/sigma)**2)**(-(s+1)/2)
    def pdf(x):
        return special.gamma((s+1)/2)/(sigma*math.sqrt(math.pi)*special.gamma(s/2))*(1+((x-mu)/sigma)**2)**(-(s+1)/2)
    mass, error = integrate.quad(pdf,-np.inf,np.inf,epsabs=1e-10)
    assert abs(mass-1)<1e-8
    assert abs(coefficient - pdf(0))<1e-12
    checks += 2
    for t in (20.,100.,500.,2000.):
        q,err = integrate.quad(pdf,-1/t,1/t,epsabs=1e-13)
        assert q>0
        if t>=500:
            assert abs(t*q-2*coefficient)<.04*2*coefficient
        checks += 2
    # Norm-screening retains a strictly positive conditional zero-density.
    accepted = (X >= .8*np.linalg.norm(u)*math.sqrt(s)) & (X <= 1.2*np.linalg.norm(u)*math.sqrt(s))
    assert accepted.mean() > .15
    conditional_density_zero = np.mean((X[accepted]/np.linalg.norm(w))/math.sqrt(2*math.pi)
        * np.exp(-.5*(mu*X[accepted]/np.linalg.norm(w))**2))
    assert conditional_density_zero > 0
    checks += 2
    print(f's={s}, negative_probability={prob:.10g}, sampled={empirical:.10g}, '
          f'signed-tail-coefficient={coefficient:.10g}, norm-screen-density={conditional_density_zero:.10g}')
print('PATHWISE_AND_DISTRIBUTION_CHECKS_PASS',checks)
print('NOTE Monte Carlo and quadrature are secondary checks; proofs of moments and tails are analytic.')
