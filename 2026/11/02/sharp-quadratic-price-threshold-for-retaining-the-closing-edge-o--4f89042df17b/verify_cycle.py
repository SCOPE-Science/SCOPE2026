"""Reproducible checks for a price-induced support transition on weighted cycles.

Requires Python 3, NumPy, SciPy and SymPy. This script provides finite
checks only; the full parameter theorem uses an analytic convexity proof.
"""
from math import sqrt, pi
import numpy as np
from scipy.optimize import minimize
import sympy as sp


def critical(n):
    assert n >= 3
    k = np.arange(1, n, dtype=float)
    a = 1.0 / np.sqrt(k * (n - k))
    t = np.r_[0.0, np.cumsum(a)]
    return float(n * np.sum((t - t.mean())**2))


def path_weights(n, B=1.0):
    k = np.arange(1, n, dtype=float)
    b = k * (n - k)
    s = np.sqrt(b).sum()
    return np.r_[B*np.sqrt(b)/s, 0.0], float(s*s/B)


def laplacian(w):
    n = len(w)
    L = np.zeros((n,n))
    for e, weight in enumerate(w):
        a,b = e, (e+1)%n
        L[a,a] += weight
        L[b,b] += weight
        L[a,b] -= weight
        L[b,a] -= weight
    return L


def value_gradient(w):
    n = len(w)
    Q = laplacian(w) + np.ones((n,n))/n
    X = np.linalg.inv(Q)
    F = n * (np.trace(X)-1)
    deriv = np.zeros(n)
    for e in range(n):
        b = (e+1)%n
        v = X[:,e]-X[:,b]
        deriv[e] = -n*np.dot(v,v)
    return float(F), deriv


def independent_resistance_sum(w):
    n = len(w)
    total = 0.0
    if w[-1] == 0:
        for a in range(n):
            for b in range(a+1,n):
                total += sum(1/w[k] for k in range(a,b))
        return total
    res = 1/np.asarray(w)
    T = sum(res)
    for a in range(n):
        for b in range(a+1,n):
            A = sum(res[a:b])
            total += A*(T-A)/T
    return float(total)


def optimizer(n,r):
    prices = np.r_[np.ones(n-1), r]
    y,_ = path_weights(n)
    # A feasible interior starting point ensures a stable numerical comparison.
    x0 = .90*y
    x0[-1] = .1/r
    cons = [{'type':'eq', 'fun':lambda w: np.dot(prices,w)-1,
             'jac':lambda w:prices}]
    res = minimize(lambda w:value_gradient(w), x0, jac=True,
                   bounds=[(1e-6,None)]*(n-1)+[(0,None)], constraints=cons, method='SLSQP',
                   options={'ftol':1e-11,'maxiter':1400})
    return res


def main():
    n3 = critical(3)
    assert abs(n3-3) < 1e-12
    a = sp.sqrt(sp.Rational(1,3))
    seq = [0,a,a+sp.Rational(1,2),2*a+sp.Rational(1,2)]
    mean = sum(seq)/4
    r4_exact = sp.simplify(4*sum((t-mean)**2 for t in seq))
    assert sp.simplify(r4_exact-(sp.Rational(11,3)+4/sp.sqrt(3))) == 0
    assert abs(critical(4)-float(r4_exact))<1e-12
    print('Exact small-order thresholds: n=3 is 3, n=4 is', r4_exact)

    signed_checks = 0
    independent_checks = 0
    optimization_checks = 0
    for n in range(3,11):
        pc, Fp = path_weights(n)
        rc = critical(n)
        mu = Fp
        fp, gradient = value_gradient(pc)
        assert abs(fp-Fp)<max(1e-7,1e-9*Fp)
        assert abs(-gradient[-1]/mu-rc)<1e-8*rc
        assert max(abs(gradient[:-1]/mu+1))<1e-9
        assert abs(independent_resistance_sum(pc)-fp)<max(1e-7,1e-9*fp)
        independent_checks += 1
        for r in ((0.30*rc, 0.75*rc, 1.20*rc) if n <= 7 else ()):
            z = optimizer(n,r)
            assert z.success or (np.isfinite(z.fun) and abs(z.fun-Fp) < 1e-4), (n,r,z.message)
            assert z.x.min() >= -1e-10, (n,r,z.x)
            assert abs(np.dot(np.r_[np.ones(n-1),r],z.x)-1)<1e-6
            if r < rc:
                assert z.fun < Fp - 1e-6, (n,r,z.fun,Fp)
                assert z.x[-1]>1e-6, (n,r,z.x)
                assert min(z.x[:-1])>1e-6
            else:
                assert abs(z.fun-Fp) < max(3e-5,2e-6*Fp), (n,r,z.fun,Fp)
                assert z.x[-1]<2e-4, (n,r,z.x)
            if z.x[-1] > 1e-7:
                independent = independent_resistance_sum(z.x)
                assert abs(independent-z.fun)<max(5e-5,2e-6*z.fun)
                independent_checks += 1
            optimization_checks += 1
        # Directional gradient of the deleted edge equals mu*(r-rc).
        for r in (0.5*rc, rc, 1.5*rc):
            directional = gradient[-1] + mu*r
            assert abs(directional/mu-(r-rc))<1e-8*rc
            signed_checks += 1
    asymptotic = pi*pi/4-2
    vals = [(n,critical(n)/(n*n)) for n in (20,100,500)]
    assert abs(vals[-1][1]-asymptotic)<0.007
    assert abs(vals[2][1]-asymptotic)<abs(vals[1][1]-asymptotic)<abs(vals[0][1]-asymptotic)
    print('Edge threshold derivative identities:', signed_checks)
    print('Independent pairwise-resistance comparisons:', independent_checks)
    print('Full-dimensional constrained numerical comparisons:', optimization_checks)
    print('Asymptotic normalized thresholds:',vals)
    print('Proved limiting constant:',asymptotic)
    print('ALL FINITE CHECKS PASSED')

if __name__=='__main__': main()
