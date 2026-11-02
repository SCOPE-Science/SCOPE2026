#!/usr/bin/env python3
"""Numerical cross-checks for the OU endpoint Fourier-bridge selection theorem.

Standard library only. These checks support, but do not replace, the proof.
"""
import math
import random

PI2 = math.pi ** 2


def weight(q, j):
    """Dimensionless coordinate variance: c_j squared divided by sigma^2*h."""
    sign = -1.0 if (j % 2) else 1.0
    return 2.0 * q * q * (sign - math.exp(-q))**2 / (q*q + PI2*j*j)**2


def c_numeric(q, j, panels=2400):
    """Independent Simpson quadrature of the OU kernel's cosine coefficient."""
    assert panels % 2 == 0
    acc = 0.0
    for k in range(panels + 1):
        u = k/panels
        integrand = math.exp(-q*(1.0-u))*math.cos(j*math.pi*u)
        acc += (1.0 if k in (0,panels) else (4.0 if k % 2 else 2.0))*integrand
    return math.sqrt(2.0)*acc/(3.0*panels)


def crossing(q):
    return math.exp(-q)*(2.0*q*q + 13.0*PI2) - 5.0*PI2


def root():
    lo, hi = 0.0, 4.0
    for _ in range(70):
        mid = (lo+hi)/2.0
        if crossing(mid) > 0.0:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2.0


def residual(q, selected):
    # Itô isometry for the full OU stochastic convolution, minus retained cosine modes.
    full = -math.expm1(-2.0*q)/(2.0*q)
    end = -math.expm1(-q)/q
    return full - end*end - sum(weight(q,j) for j in selected)


def main():
    tests = 0
    random.seed(29032026)
    qstar = root()
    assert abs(qstar-0.97007375960154457596) < 1e-13
    tests += 1

    for _ in range(35):
        q = math.exp(random.uniform(math.log(.08), math.log(12.0)))
        j = random.randint(1, 15)
        actual = c_numeric(q, j)
        # cos integral has sign (-1)^j - exp(-q)
        anticipated = math.sqrt(2.0)*q*((-1.0 if j%2 else 1.0)-math.exp(-q))/(q*q+PI2*j*j)
        assert abs(actual-anticipated) < 4e-11, (q,j,actual,anticipated)
        tests += 1

    for q in [0.01,0.1,0.5,0.95,qstar,1.0,2.0,5.0,12.0,50.0]:
        weights = sorted(range(1,151),key=lambda j:weight(q,j),reverse=True)
        assert weights[0] == 1
        for k in [1,2,3,5,7,10,20]:
            chosen = weights[:k]
            r = sum(weight(q,j) for j in chosen)
            assert r >= sum(weight(q,j) for j in range(1,k+1))-2e-15
            # the optimum includes initial segments of each parity
            odd = sorted(j for j in chosen if j%2)
            even = sorted(j for j in chosen if not j%2)
            assert odd == list(range(1,2*len(odd)+1,2))
            assert even == list(range(2,2*len(even)+1,2))
            tests += 1
        if abs(q-qstar)>1e-9:
            assert (weights[1] == 3) == (q < qstar), (q,weights[:3])
            tests+=1

    for q in [0.12,0.5,0.96,1.2,3.0,15.0]:
        selected = [1,3] if q < qstar else [1,2]
        exact = residual(q,selected)
        # independent direct variance summation, with an explicit tail bound
        series = sum(weight(q,j) for j in range(1,7001) if j not in selected)
        tail_upper = 2*q*q*(1+math.exp(-q))**2/(3*math.pi**4*(6999**3))
        assert abs(exact-series) < tail_upper + 2e-12, (q,exact,series)
        assert exact > 0.0
        tests += 1

    e12 = 1/12-8/math.pi**4
    e13 = e12 - 8/(81*math.pi**4)
    improvement = (e12-e13)/e12
    assert abs(improvement-0.8410990891189896)<1e-12
    for q in [0.00002,0.000001,0.0000001]:
        # Avoid direct cancellation in residual by using a high-precision series.
        r12 = sum(weight(q,j) for j in range(3,3001)) / (q*q)
        r13 = sum(weight(q,j) for j in range(2,3001) if j not in (1,3)) / (q*q)
        assert abs(r12-e12)<4e-8
        assert abs(r13-e13)<4e-8
        tests += 2

    print('PASS: %d independent quadrature, ordering, tail and limit checks' % tests)
    print('unique two-mode crossover q* = %.15f' % qstar)
    print('small-q reduction in residual mean-square error = %.12f%%' % (100*improvement))


if __name__ == '__main__':
    main()
