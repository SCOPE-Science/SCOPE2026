"""Finite arithmetic checks for a high-resetting active-diffusion first-passage formula."""
import math
import numpy as np
from scipy.special import roots_hermitenorm

D = 0.8
L = 2.0
X = 0.75


def exponents(rate, drift):
    s = np.sqrt(drift * drift + 4.0 * D * rate)
    return (s + drift) / (2.0 * D), (s - drift) / (2.0 * D)


def u(rate, drift, x=X):
    aa, bb = exponents(rate, drift)
    q = (aa / bb) * np.exp(-(aa + bb) * L)
    return (np.exp(-aa * x) + q * np.exp(bb * x)) / (1.0 + q)


def derivatives(rate, drift, x=X):
    aa, bb = exponents(rate, drift)
    q = (aa / bb) * np.exp(-(aa + bb) * L)
    ux = (-aa * np.exp(-aa*x) + q*bb*np.exp(bb*x)) / (1+q)
    uxx = (aa*aa*np.exp(-aa*x) + q*bb*bb*np.exp(bb*x)) / (1+q)
    return ux, uxx


checks = 0
for rate in (1.0, 3.0, 12.0, 170.0):
    for drift in (-2.5, -0.7, 0.0, 0.7, 2.5):
        assert abs(u(rate, drift, 0) - 1) < 1e-13
        checks += 1
        assert abs(derivatives(rate, drift, L)[0]) < 3e-12
        checks += 1
        for x in (0.21, 0.75, 1.54):
            ux, uxx = derivatives(rate, drift, x)
            residual = D*uxx + drift*ux - rate*u(rate,drift,x)
            assert abs(residual) <= 4e-11*max(1.0, rate*u(rate,drift,x))
            checks += 1

# The full reflected solution has the correct protocol-dependent prefactor.
for drift in (-1.9, -0.6, 0.0, 0.8, 2.4):
    rate = 50000.0
    pred = math.exp(-X*drift/(2*D))
    actual = math.exp(X*math.sqrt(rate/D))*float(u(rate, drift))
    assert abs(actual/pred-1) < .007
    checks += 1

# For Gaussian redraws, integrate the exact constant-drift resolvent;
# in the colored-noise theorem its limit equals this frozen initial drift.
sigma = math.sqrt(.6)
nodes, weights = roots_hermitenorm(84)
weights = weights / math.sqrt(2*math.pi)
expected = math.exp(X*X*sigma*sigma/(8*D*D))
ratios = []
for rate in (400., 1600., 6400., 25600.):
    probs = u(rate, sigma*nodes)
    normalized = math.exp(X*math.sqrt(rate/D))*float(np.dot(weights, probs))
    assert abs(normalized/expected-1) < .018
    checks += 1
    ratios.append(normalized)
assert abs(ratios[-1]-expected) < abs(ratios[0]-expected)
checks += 1

# Sampled-path upper Skorokhod map, testing the comparison lemma.
rng = np.random.default_rng(20261020)
for seed in range(12):
    dt = 0.001
    n = 1500
    increments = rng.normal(0, math.sqrt(2*D*dt), n)
    vel_increments = rng.normal(0, math.sqrt(dt), n)
    v = np.empty(n+1)
    v[0] = rng.normal()
    for i in range(n):
        v[i+1] = v[i] * math.exp(-dt/1.3) + math.sqrt(.6*(1-math.exp(-2*dt/1.3)))*vel_increments[i]/math.sqrt(dt)
    z = np.max(np.abs(v-v[0]))
    low = v[0]-z
    high = v[0]+z
    y = X+np.r_[0,np.cumsum(increments)] + np.r_[0,np.cumsum(v[:-1]*dt)]
    ylow = X+np.r_[0,np.cumsum(increments + low*dt)]
    yhigh = X+np.r_[0,np.cumsum(increments + high*dt)]
    def reflect_upper(path):
        return path-np.maximum.accumulate(np.maximum(path-L,0))
    a, b, c = map(reflect_upper, (ylow, y, yhigh))
    assert np.max(a-b) < 1e-10
    assert np.max(b-c) < 1e-10
    checks += 2

print(f"PASS: {checks} finite assertions; constant-drift, Gaussian mixing, reflection order")
print(f"Gaussian prefactor {expected:.12g}; final normalized finite-rate {ratios[-1]:.12g}")
