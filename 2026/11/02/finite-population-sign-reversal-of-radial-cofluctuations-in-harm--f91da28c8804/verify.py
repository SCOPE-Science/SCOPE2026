#!/usr/bin/env python3
"""Exact rational checks for centered active-particle squared-radius correlations.

Run with Python 3 (standard library only): python verify.py
The proof of the all-parameter identity is supplied separately; finite
enumeration here is an independent consistency check, not that proof.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product


def single_moments(model, alpha):
    """Stationary polynomial-generator recurrence, independent of closed formulas."""
    alpha = F(alpha)
    assert alpha > 0 and model in ("RTP", "ABP")

    @lru_cache(None)
    def moment(p, q, k):
        if p == 0 and q == 0:
            return F(1) if k == 0 else F(0)
        orientation_eigenvalue = alpha * (k * k if model == "ABP" else int(k != 0))
        numerator = (p * moment(p - 1, q, k + 1) if p else 0)
        numerator += (q * moment(p, q - 1, k - 1) if q else 0)
        return numerator / (p + q + orientation_eigenvalue)

    return moment(1, 1, 0), moment(2, 2, 0)


def closed_moments(model, a):
    a = F(a)
    m2 = 1 / (1 + a)
    if model == "RTP":
        m4 = 2 / ((1 + a) * (2 + a))
    else:
        m4 = (4 * a + 3) / ((1 + a) * (2 * a + 1) * (a + 3))
    return m2, m4


def centered_covariance_direct(n, m2, m4):
    """Compute cumulant contraction from explicit projection rows."""
    a = [F(int(k == 0)) - F(1, n) for k in range(n)]
    b = [F(int(k == 1)) - F(1, n) for k in range(n)]
    cross = sum(x * y for x, y in zip(a, b))
    collision = sum(x*x*y*y for x, y in zip(a, b))
    return m2*m2*cross*cross + (m4-2*m2*m2)*collision


def centered_covariance_closed(model, n, alpha):
    m2, m4 = closed_moments(model, alpha)
    c = F(2*n-3, n)
    a = F(alpha)
    if model == "RTP":
        deficit = 2 / (a+2)
    else:
        deficit = (7*a+3) / ((a+3)*(2*a+1))
    return (m2*m2 / (n*n)) * (1-c*deficit)


def enumerated_cardinal_covariance(n):
    """Exhaustive independent, isotropic four-direction law, n <= 6."""
    directions = ((1,0),(-1,0),(0,1),(0,-1))
    total_r1, total_r2, total_prod = 0, 0, 0
    cases = 0
    for configuration in product(directions, repeat=n):
        sx = sum(t[0] for t in configuration)
        sy = sum(t[1] for t in configuration)
        x1, y1 = configuration[0]
        x2, y2 = configuration[1]
        # Squared radii multiplied by n**2, stored as integers.
        r1 = (n*x1-sx)**2 + (n*y1-sy)**2
        r2 = (n*x2-sx)**2 + (n*y2-sy)**2
        total_r1 += r1
        total_r2 += r2
        total_prod += r1*r2
        cases += 1
    mean_product = F(total_prod, cases*n**4)
    mean1 = F(total_r1, cases*n*n)
    mean2 = F(total_r2, cases*n*n)
    return mean_product - mean1*mean2


def main():
    checks = 0
    for model in ("RTP", "ABP"):
        for a in (F(1,20),F(1,3),F(1),F(5,4),F(2),F(3),F(4),F(10),F(100)):
            p = single_moments(model, a)
            q = closed_moments(model, a)
            assert p == q, (model, a, p, q)
            checks += 2
            for n in range(2,65):
                cov = centered_covariance_direct(n, *p)
                closed = centered_covariance_closed(model,n,a)
                assert cov == closed, (model,a,n,cov,closed)
                checks += 1
    for n in range(2,7):
        cov_enum = enumerated_cardinal_covariance(n)
        predicted = centered_covariance_direct(n,F(1),F(1))
        assert cov_enum == predicted, (n,cov_enum,predicted)
        checks += 1
    for n in range(4,65):
        delta = F(n-3,n)
        rt = 2*delta
        # At the RTP transition, ABP remains negative; at alpha=4 both positive.
        assert centered_covariance_closed("RTP",n,rt)==0
        assert centered_covariance_closed("ABP",n,rt)<0
        assert centered_covariance_closed("RTP",n,F(4))>0
        assert centered_covariance_closed("ABP",n,F(4))>0
        checks += 4
    assert centered_covariance_closed("RTP",4,F(1)) == F(1,384)
    assert centered_covariance_closed("ABP",4,F(1)) == -F(1,1536)
    checks += 2
    print("PASS: %d exact rational assertions, including complete finite-state examples" % checks)

if __name__ == "__main__":
    main()
