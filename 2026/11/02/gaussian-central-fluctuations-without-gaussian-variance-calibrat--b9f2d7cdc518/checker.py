"""Reproducible finite checks for the two-temperature thermal-wall tracer.

This checks analytic one-cycle moments and Pareto-tail constants. It is not a
proof of distributional or second-moment asymptotics.
"""
import math
import numpy as np
from scipy.integrate import quad


def params(beta_h, beta_c, length):
    mu = length * math.sqrt(math.pi / 2) * (math.sqrt(beta_h) + math.sqrt(beta_c))
    nu = 1/beta_h - 1/beta_c
    c = (beta_h + beta_c) * length * length / 2
    return mu, nu, c


def tail_of_sum(t, beta_h, beta_c, length):
    a = beta_h * length*length/2
    b = beta_c * length*length/2
    # W = tau_h+tau_c.  The first term covers tau_h >= t.
    def kernel(u):
        if u <= 0:
            return 0.0
        f_h = 2*a/u**3*math.exp(-a/u**2)
        return f_h * (-math.expm1(-b/(t-u)**2))
    integral = quad(kernel, 0, t, points=[t/3, 2*t/3], epsabs=2e-11,
                    epsrel=5e-10, limit=220)[0]
    return -math.expm1(-a/t**2) + integral


def run_checks():
    rng = np.random.default_rng(928151)
    cases = [(1.0, 2.0, 1.0), (2.0, 2.0, 1.5), (0.65, 3.0, 0.7)]
    tests = 0
    for bh,bc,L in cases:
        mu,nu,c = params(bh,bc,L)
        n=1_200_000
        eh=rng.exponential(1/bh, n)
        ec=rng.exponential(1/bc, n)
        vh=np.sqrt(2*eh)
        vc=np.sqrt(2*ec)
        w=L/vh+L/vc
        r=eh-ec
        # 7 sigma confidence is a deliberately loose finite-sample tolerance.
        for empirical, expected, tol in [
            (float(w.mean()),mu, 0.025*mu),
            (float(r.mean()),nu,0.018),
            (float(r.var()),1/bh**2+1/bc**2,0.06*(1/bh**2+1/bc**2)),
        ]:
            if abs(empirical-expected) > tol:
                raise AssertionError((bh,bc,L,empirical,expected,tol))
            tests+=1
        # Direct convolution quadrature, not a stochastic estimate.
        for t in (100*L, 400*L):
            actual = tail_of_sum(t,bh,bc,L)
            ratio = t*t*actual/c
            if not (0.97 <= ratio <= 1.07):
                raise AssertionError((bh,bc,L,t,ratio))
            tests+=1
        sigma_gaussian=(c*nu**2/mu**3) if nu!=0 else (2/bh**2)/mu
        if sigma_gaussian <= 0:raise AssertionError('invalid CLT variance')
        tests+=1
        print(f'beta_h={bh}, beta_c={bc}, L={L}: mu={mu:.7f}, nu={nu:.7f}, tail_c={c:.7f}, central_var_coeff={sigma_gaussian:.8f}')
    print(f'PASS: {tests} independent moment, convolution-tail and positivity comparisons')

if __name__=='__main__':
    run_checks()
