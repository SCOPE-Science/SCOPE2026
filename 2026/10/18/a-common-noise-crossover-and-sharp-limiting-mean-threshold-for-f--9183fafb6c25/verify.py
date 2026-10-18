#!/usr/bin/env python3
"""Numerical consistency checks for the common-noise fastest-search crossover.

All computations concern the published mathematical model and use deterministic
random seeds. Numerical tests supplement but do not replace the analytic proof.
"""
import math
import numpy as np
from scipy.special import ndtr, ndtri, roots_hermitenorm, erfc

D = 1.0
ell = 1.0
T = 0.5
A = 1.0


def exact_fixed_time_survival(n, a, t, threshold=0., nodes=240):
    eta = min(1., a / math.log(n))
    rho = 1. - eta
    xs, ws = roots_hermitenorm(nodes)
    mu = ell + math.sqrt(2*D*rho*t)*xs
    sigma = math.sqrt(2*D*eta*t)
    return float(np.dot(ws, ndtr((mu-threshold)/sigma)**n)/math.sqrt(2*math.pi))


def limiting_fixed_time_survival(a, t, threshold=0.):
    mean = ell - 2*math.sqrt(D*a*t)
    return float(ndtr((mean-threshold)/math.sqrt(2*D*t)))


def extrema_tail(n, eps, t=1.0):
    # Y_n(t) = max(-B_i(t))/sqrt(2 log n); correct standard-normal scale.
    threshold_low = (1-eps)*math.sqrt(2*math.log(n))
    threshold_high = (1+eps)*math.sqrt(2*math.log(n))
    p_below = ndtr(threshold_low)**n
    p_above = 1-ndtr(threshold_high)**n
    return p_below, p_above


def run():
    print('Fixed-time common-factor Gaussian-mixture check')
    last_error = float('inf')
    for n in [128, 1024, 8192, 65536]:
        actual = exact_fixed_time_survival(n, A, T)
        asymptotic = limiting_fixed_time_survival(A, T)
        err = abs(actual-asymptotic)
        print(n, 'exact', format(actual, '.9f'), 'limit', format(asymptotic, '.9f'), 'error', format(err, '.9f'))
        assert 0 < actual < 1
        assert err < last_error, ('expected trend did not hold', n, err, last_error)
        last_error = err

    print('Independent Brownian extreme tails (finite n)')
    for n in [100, 1000, 10000, 1000000]:
        p_low,p_high=extrema_tail(n, .5)
        print(n, 'P(Y<0.5)', p_low, 'P(Y>1.5)', p_high)
        assert 0 <= p_low <= 1 and 0 <= p_high <= 1

    print('Pathwise min process against critical random envelope')
    rng=np.random.default_rng(20261015)
    nsteps=240
    horizon=1.5
    dt=horizon/nsteps
    for n in (128, 1024, 4096):
        eta=A/math.log(n)
        rho=1-eta
        rms=[]
        for _ in range(12):
            common=0.
            private=np.zeros(n, dtype=float)
            squared_errors=[]
            for j in range(1,nsteps+1):
                common += rng.normal(0,math.sqrt(dt))
                private += rng.normal(0,math.sqrt(dt),size=n)
                t=j*dt
                actual=ell+math.sqrt(2*D*rho)*common+math.sqrt(2*D*eta)*np.min(private)
                asymptotic=ell+math.sqrt(2*D)*common-2*math.sqrt(D*A*t)
                squared_errors.append((actual-asymptotic)**2)
            rms.append(math.sqrt(sum(squared_errors)/len(squared_errors)))
        print(n,'mean path RMS error',format(np.mean(rms),'.6f'))
        assert np.isfinite(rms).all()

    print('Zero-crossover boundary limit')
    for t in [0.05,0.3,1.,4.]:
        exact_BM_hit=erfc(ell/math.sqrt(4*D*t))
        normal_BM_hit=2*(1-ndtr(ell/math.sqrt(2*D*t)))
        assert abs(exact_BM_hit-normal_BM_hit)<1e-14
    print('All tests passed')

if __name__=='__main__':
    run()


def spectral_crossing_check():
    """Check killed OU ground energy by a conjugate Schrödinger discretization."""
    from scipy.linalg import eigh_tridiagonal
    from scipy.special import ndtr
    h = 0.015
    print('OU killed half-line principal eigenvalues')
    vals=[]
    for b in [0., 0.6, 1., 1.4, 2.]:
        count = int((10-b)/h)
        x = b + h * np.arange(1, count)
        diagonal = np.full(len(x), 1/h**2) + x*x/8 - .25
        off = np.full(len(x)-1, -.5/h**2)
        lam = eigh_tridiagonal(diagonal,off,select='i',select_range=(0,0),check_finite=False)[0][0]
        print(b, lam)
        vals.append(lam)
    assert vals == sorted(vals)
    assert abs(vals[2]-1)<5e-4
    assert abs(vals[0]-.5)<5e-4
    assert vals[1]<1<vals[3]
    print('OU threshold checks passed')

if __name__ == '__main__':
    spectral_crossing_check()
