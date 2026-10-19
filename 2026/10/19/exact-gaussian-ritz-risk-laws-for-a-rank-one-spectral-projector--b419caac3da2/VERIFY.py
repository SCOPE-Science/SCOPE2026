"""Reproduce the exact laws for Gaussian Petrov--Galerkin Ritz extraction.

Uses only Python's standard library. Finite numerical checks are not proofs
of the distributional statements, which follow from Gaussian invariance.
"""
import cmath
import math
import random

SEED = 20261013034
rng = random.Random(SEED)


def complex_normal():
    return complex(rng.gauss(0, 1), rng.gauss(0, 1)) / math.sqrt(2)


def solve(a, b):
    """Small nonsingular complex system by partial-pivot elimination."""
    n = len(a)
    a = [list(row) + [b[i]] for i, row in enumerate(a)]
    for j in range(n):
        p = max(range(j, n), key=lambda i: abs(a[i][j]))
        if abs(a[p][j]) < 1e-12:
            raise ArithmeticError('rare nearly singular test matrix')
        a[j], a[p] = a[p], a[j]
        z = a[j][j]
        a[j] = [x / z for x in a[j]]
        for i in range(n):
            if i != j:
                z = a[i][j]
                a[i] = [u - z * v for u, v in zip(a[i], a[j])]
    return [a[i][-1] for i in range(n)]


def mean_formula(k, alpha):
    beta = 1 - alpha
    return k * alpha / beta**k * (
        -math.log(alpha) - sum(beta**j / j for j in range(1, k))
    )


def mean_integral(k, alpha, count=10000):
    assert count % 2 == 0
    def f(u):
        return k * alpha * (1-u)**(k-1) / (alpha + (1-alpha)*u)
    step = 1 / count
    sm = f(0) + f(1)
    for i in range(1, count):
        sm += (4 if i % 2 else 2) * f(i*step)
    return sm * step / 3


def cdf_formula(k, alpha, t):
    if t <= alpha:
        return 0.0
    if t >= 1:
        return 1.0
    return ((t - alpha) / ((1-alpha)*t))**k


def algebra_tests():
    samples = 0
    for m in (2, 3, 5, 7):
        n = m + 1
        for alpha in (0.015, 0.09, 0.47):
            s = math.sqrt(alpha)
            c = math.sqrt(1-alpha)
            for _ in range(36):
                # G is the conjugate transpose of an n-by-m Gaussian sketch.
                G = [[complex_normal() for _ in range(n)] for _ in range(m)]
                h = solve([row[:m] for row in G], [-row[m] for row in G]) + [1.0]
                assert max(abs(sum(a*b for a,b in zip(row,h))) for row in G) < 2e-8
                mu = s*h[0] / (s*h[0] - c*h[m])
                z = [s*h[j]/h[m] for j in range(1,m)]
                x = [c] + z + [s]
                Ax_minus_mux = [-mu*c] + [(1-mu)*u for u in z] + [(1-mu)*s]
                pg = [sum(row[j]*Ax_minus_mux[j] for j in range(n)) for row in G]
                assert max(map(abs, pg)) <= 3e-8 * (1 + abs(mu) + sum(map(abs,z)))
                rho = (alpha + sum(abs(q)**2 for q in z)) / (1 + sum(abs(q)**2 for q in z))
                U = abs(h[m])**2 / (abs(h[m])**2 + sum(abs(h[j])**2 for j in range(1,m)))
                assert abs(rho - alpha/(alpha + (1-alpha)*U)) < 3e-12
                v = s*h[0] - c*h[m]
                xi = c*h[0] + s*h[m]
                assert abs(mu - (alpha+s*c*xi/v)) < 3e-11*(1+abs(mu))
                samples += 1
    return samples


def distribution_tests():
    total = 0
    for m, alpha in ((2,.03), (3,.10), (5,.04), (10,.20)):
        k = m-1
        values = []
        for _ in range(50000):
            # A complex isotropic null vector has independent exponential
            # squared coordinate magnitudes. This bypasses matrix inversion.
            y = rng.expovariate(1)
            x = sum(rng.expovariate(1) for _ in range(k))
            U = y/(x+y)
            values.append(alpha/(alpha+(1-alpha)*U))
        av = sum(values)/len(values)
        target = mean_formula(k, alpha)
        stderr_bound = 5 * math.sqrt(max(target*(1-target),1e-5)/len(values))
        assert abs(av-target) <= max(stderr_bound,.008), (m,alpha,av,target)
        for t in (alpha+0.03*(1-alpha), alpha+0.4*(1-alpha), alpha+0.8*(1-alpha)):
            observed = sum(x <= t for x in values)/len(values)
            expected = cdf_formula(k,alpha,t)
            assert abs(observed-expected) < .018, (m,t,observed,expected)
            total += 1
        quadrature = mean_integral(k, alpha)
        assert abs(quadrature-target) < 2e-8, (m,alpha,quadrature,target)
    return total


def asymptotic_checks():
    for k in (1,2,4,8):
        a = 1e-6
        predicted = k*a*(-math.log(a)-sum(1/j for j in range(1,k)))
        true = mean_formula(k,a)
        assert abs(true-predicted) < 1e-8
    tau = 1.0
    for k in (100,1000,10000):
        a = tau/k
        for t in (.3,.5,.8):
            got = cdf_formula(k,a,t)
            target = math.exp(-tau*(1-t)/t)
            assert abs(got-target) < 0.028, (k,t,got,target)
    return True


if __name__ == '__main__':
    count = algebra_tests()
    tests = distribution_tests()
    asymptotic_checks()
    print('PASS: projected generalized-eigenvector identities for',count,'Gaussian matrices')
    print('PASS: exact Beta-law CDF/mean versus independent sampling and quadrature in',tests,'tail checks')
    print('PASS: fixed-dimension logarithmic expansion and critical dimensional limit')
