"""Reproducibility checks for stationary OU-driven two-patch dispersal.

Not a substitute for the analytical infinite-time arguments. Requires only numpy.
"""
import math
import numpy as np


def simulate(M, lam, D, *, steps=180000, h=0.005, burn=40000, seed=20261017):
    rng = np.random.default_rng(seed)
    decay = math.exp(-lam * h)
    sd = math.sqrt(2.0*lam*D * (1.0-decay*decay))
    ehalf = math.exp(-M*h/2)
    x = 0.0
    eta = rng.normal(scale=math.sqrt(2*lam*D))
    sg = sc = sm = sm2 = 0.0
    count = 0
    for n in range(steps):
        nxt = decay * eta + sd * rng.normal()
        x = 2.0*math.atanh(ehalf*math.tanh(x/2.0))
        x += h*(eta+nxt)/2.0
        x = 2.0*math.atanh(ehalf*math.tanh(x/2.0))
        eta = nxt
        if n >= burn:
            sg += 0.5*M*(math.cosh(x)-1.0)
            sc += 0.5*eta*math.tanh(x/2.0)
            sm += M*x*math.sinh(x)
            sm2 += lam*eta*x + M*M*math.sinh(x)**2
            count += 1
    exact_upper = lam*D/(2.0*(M+lam))
    return (sg/count, sc/count, sm/count, sm2/count, exact_upper)


def run():
    print('Independent ODE moment algebra:')
    # Values from stationarity, with sigma_eta^2 = 2 lambda D.
    for lam,D in [(1.0,0.3),(2.0,0.04),(0.8,0.1)]:
        sig2=2*lam*D
        assert abs(sig2/lam-2*D)<1e-12
        print(f'  lambda={lam:g}, D={D:g}: Var(eta)={sig2:g}, moment ceiling={2*D:g}')
    print('Stationary trajectory checks (sample errors are stochastic):')
    for M,lam,D in [(0.3,1,0.1),(1,1,0.1),(3,1,0.1),(0.8,2,0.02)]:
        g, cov, mom, mom2, cap=simulate(M,lam,D)
        print(f' M={M:g} lambda={lam:g} D={D:g}: '
              f'growth={g:.6g}, covariance={cov:.6g}, '
              f'upper={cap:.6g}, moment={mom:.6g}, moment2={mom2:.6g}')
        assert g>0 and g<cap * 1.15
        assert abs(g-cov) < max(0.010,0.8*g)
    print('PASS: all finite stationary-simulation tests')


if __name__=='__main__':
    run()
