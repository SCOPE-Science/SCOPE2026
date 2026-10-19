#!/usr/bin/env python3
"""Reproduce finite-phase renewal-age covariance and independent renewal simulations."""
import numpy as np
from scipy.linalg import expm
from numpy.random import default_rng

def renewal_cov(k, tau):
    g = np.array([(2*j + 1 - k)/(2*k) for j in range(k)], dtype=float)
    f = np.array([(j+1)*(2*j+3-k)/(2*k) for j in range(k)], dtype=float)
    m = np.zeros((2*k, 2*k))
    for j in range(k):
        m[j, j] -= 1
        m[j, (j-1) % k] += 1
        m[k+j, j] = 1
        m[k+j, k+j] = -1
        if j:
            m[k+j, k+j-1] = 1
    return (expm(m*tau) @ np.r_[g, f])[k:].sum()

def closed(k, t):
    if k == 1: return np.exp(-t)
    if k == 2: return 2*np.exp(-t)-np.exp(-2*t)/4
    if k == 3: return 3*np.exp(-t)-2*np.exp(-1.5*t)*np.cos(np.sqrt(3)*t/2+np.pi/3)/3
    if k == 4: return (4+np.sin(t))*np.exp(-t)-np.exp(-2*t)/4
    raise ValueError(k)

def stationary_renewal_sample(k, t, n, seed):
    # Independent alternative to the matrix-generator calculation: construct
    # the age from completed exponential stages in the current stationary cycle.
    rng = default_rng(seed)
    j = rng.integers(k, size=n)
    a0 = rng.gamma(j+1, 1.)
    rest = rng.gamma(k-j, 1.)
    a1 = a0+t
    remaining = t-rest
    mask = remaining>=0
    while np.any(mask):
        rows = np.flatnonzero(mask)
        cycle = rng.gamma(k, 1., size=len(rows))
        remaining[rows] -= cycle
        # If cycle finishes after remaining time, current age = time since last reset.
        done = remaining[rows]<0
        a1[rows[done]] = remaining[rows[done]]+cycle[done]
        mask[rows[done]] = False
    return np.mean((a0-np.mean(a0))*(a1-np.mean(a1)))

def main():
    for k in range(1, 5):
        for t in np.linspace(0, 12, 31):
            x = renewal_cov(k, t)
            y = closed(k, t)
            assert abs(x-y)<4e-11, (k,t,x,y)
            assert y > 0
    print('124 closed-form phase-generator comparisons passed')
    for k,t in [(5,4.75),(6,4.6),(8,5.)]:
        actual = renewal_cov(k,t)
        print('phase-generator C(%d,%.2f) = %.9f' % (k,t,actual))
        assert actual<0
    for k,t in [(2,1.0),(4,2.0),(8,5.0)]:
        pred = renewal_cov(k,t)
        mc = stationary_renewal_sample(k,t,400000,103+k)
        print('renewal MC k=%d t=%.2f: %.6f versus matrix %.6f' % (k,t,mc,pred))
        assert abs(pred-mc)<0.11, (k,t,mc,pred)
    for k in [5,6,8,12]:
        z = np.exp(2j*np.pi/k)
        g = np.array([(2*j+1-k)/(2*k) for j in range(k)])
        a = sum(z**j*g[j] for j in range(k))/k
        amp = a*sum((j+1)*z**(-j-1) for j in range(k))
        assert abs(amp+1/(z-1)**2)<1e-11
    print('dominant complex-mode residue identities passed')
if __name__=='__main__': main()
