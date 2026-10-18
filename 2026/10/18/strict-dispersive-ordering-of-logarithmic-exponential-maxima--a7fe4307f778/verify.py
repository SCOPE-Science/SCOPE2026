#!/usr/bin/env python3
"""Numerical diagnostics for exact quantile contraction.

Python standard library only. This finite verification is not an infinite proof.
"""
import math


def quantile(a, u):
    assert a > 0 and 0 < u < 1
    z = math.exp(math.log(u) / a)
    return math.log(-math.log1p(-z))


def cdf(a, y):
    return (-math.expm1(-math.exp(y))) ** a


def slope(a, u):
    z = math.exp(math.log(u) / a)
    return z / (a * u * (1-z) * (-math.log1p(-z)))


def h_log_slope(z):
    return (1 - (1-z)/(-math.log(z)) - z/(-math.log1p(-z))) / (z * (1-z))


def run():
    count = 0
    params = [0.125, 0.5, 1, 1.25, 2, 3, 4.75, 10, 30]
    us = [0.0005, 0.002, 0.01, 0.04, 0.10, 0.25, 0.5, 0.75, 0.9, 0.96, 0.99]
    for a in params:
        for u in us:
            q = quantile(a,u)
            assert math.isclose(cdf(a,q),u,rel_tol=1e-11,abs_tol=1e-12), (a,u)
            count += 1
            epsilon=min(1e-6, u / 5, (1-u)/5)
            numeric = (quantile(a,u+epsilon)-quantile(a,u-epsilon))/(2*epsilon)
            assert math.isclose(numeric,slope(a,u),rel_tol=2e-6,abs_tol=1e-6),(a,u,numeric,slope(a,u))
            count += 1
    for i,a in enumerate(params):
        for b in params[i+1:]:
            for j,u in enumerate(us):
                assert slope(b,u) < slope(a,u), (a,b,u)
                count +=1
                for v in us[j+1:]:
                    span_a=quantile(a,v)-quantile(a,u)
                    span_b=quantile(b,v)-quantile(b,u)
                    assert span_b < span_a, (a,b,u,v)
                    count += 1
    for z in [0.0001,0.001,0.01,0.1,0.2,0.35,0.5,0.7,0.9,0.99,0.999]:
        assert h_log_slope(z)<0, z
        count += 1
    print(f"PASS: {count} numerical consistency assertions. Universal conclusion requires analytic proof.")


if __name__=='__main__':
    run()
