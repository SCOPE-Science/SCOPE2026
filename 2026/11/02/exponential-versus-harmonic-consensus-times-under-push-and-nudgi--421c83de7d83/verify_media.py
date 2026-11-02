#!/usr/bin/env python3
"""Exact checks for push/nudging consensus-time formulas on complete graphs.

This program uses only the Python standard library. The finite checks do not
establish the all-population limit; the accompanying proof does.
"""
from fractions import Fraction as Q
from itertools import product
from math import log, log1p, exp


def probabilities(n, alpha, field, push):
    h, c = alpha * field, 1 - alpha
    up = [Q(n - i, n) * (c * Q(i, n - 1) + h) for i in range(n)]
    down = [Q(0)] + [
        Q(i, n) * (Q(n-i, n-1) if push else
                   max(Q(0), c * Q(n-i, n-1) - h))
        for i in range(1, n)
    ]
    return up, down


def expected_times(n, up, down):
    # From first-step equations, p_i Delta_i-q_i Delta_{i-1}=1.
    delta = []
    for i in range(n):
        delta.append((1 + (down[i]*delta[i-1] if i else 0))/up[i])
    times = [Q(0)]*(n+1)
    for i in range(n-1, -1, -1):
        times[i] = times[i+1]+delta[i]
    return times


def linear_system_times(n, up, down):
    # Separate route: solve the original tridiagonal hitting-time equations.
    m = [[Q(0) for _ in range(n+1)] for _ in range(n)]
    for i in range(n):
        m[i][i] = up[i]+down[i]
        if i: m[i][i-1] = -down[i]
        if i < n-1: m[i][i+1] = -up[i]
        m[i][n] = Q(1)
    for j in range(n):
        pivot = next(k for k in range(j, n) if m[k][j])
        m[j], m[pivot] = m[pivot], m[j]
        v = m[j][j]
        for k in range(j, n+1): m[j][k] /= v
        for i in range(j+1, n):
            v = m[i][j]
            for k in range(j, n+1): m[i][k] -= v*m[j][k]
    for i in range(n-1, -1, -1):
        for j in range(i+1, n): m[i][n] -= m[i][j]*m[j][n]
    return [m[i][n] for i in range(n)] + [Q(0)]


def logadd(a, b):
    if a < b: a, b = b, a
    return a+log1p(exp(b-a))


def log_push_time(n, alpha, field, start):
    c, h = 1-alpha, alpha*field
    last_delta, last_sum = None, None
    for j in range(n):
        p = (n-j)/n * (c*j/(n-1)+h)
        z = -log(p)
        if j:
            q = j*(n-j)/(n*(n-1))
            z = logadd(z, log(q/p) + last_delta)
        last_delta = z
        if j >= start:
            last_sum = z if last_sum is None else logadd(last_sum, z)
    return last_sum


def check():
    tests = transitions = harmonic = 0
    for n in range(2, 13):
        for alpha in (Q(1,4), Q(1,2), Q(3,4), Q(1)):
            for field in (Q(1,5), Q(2,5), Q(3,5), Q(4,5)):
                for push in (False, True):
                    up, down = probabilities(n, alpha, field, push)
                    t = expected_times(n, up, down)
                    assert t == linear_system_times(n, up, down)
                    assert all(Q(0) <= up[i] <= 1 and
                               Q(0) <= down[i] <= 1-up[i]
                               for i in range(n))
                    if not push:
                        for i in range(n):
                            H = sum((Q(1, j) for j in range(1, n-i+1)), Q(0))
                            assert n*H <= t[i] <= n*H/(alpha*field)
                            harmonic += 1
                    tests += 1
    for n in range(2, 8):
        for bits in product((0,1), repeat=n):
            i = sum(bits)
            if i == n: continue
            for alpha in (Q(1,4), Q(3,4), Q(1)):
                for field in (Q(1,3), Q(2,3)):
                    for push in (True,False):
                        h,c = alpha*field, 1-alpha
                        up,down = probabilities(n,alpha,field,push)
                        up_direct=Q(0);down_direct=Q(0)
                        for state in bits:
                            if state==0:
                                up_direct += (c*Q(i,n-1)+h)/n
                            else:
                                down_direct += (Q(n-i,n-1) if push else
                                                max(Q(0),c*Q(n-i,n-1)-h))/n
                        assert up[i]==up_direct and down[i]==down_direct
                        transitions+=1
    for alpha,field in ((0.5,0.4),(1.0,0.3),(0.7,0.6)):
        # Midpoint Riemann estimate used only as a numerical consistency check.
        steps = 20000
        rate = (1-field)/steps * sum(
            log(x / ((1-alpha)*x+alpha*field))
            for x in (field+(k+0.5)*(1-field)/steps for k in range(steps)))
        last = float('inf')
        for n in (100, 300, 1000, 3000):
            errs=[]
            for i in (0,n-1):
                estimate=log_push_time(n,alpha,field,i)/n
                errs.append(abs(estimate-rate))
            error=max(errs)
            assert error < last
            last=error
    print('PASS: exact hitting-time linear systems:', tests)
    print('PASS: direct configuration transitions:', transitions)
    print('PASS: harmonic expectation bounds:', harmonic)
    print('PASS: large-N log-rate convergence trends: 3 parameter sets x 4 sizes x 2 starts')

if __name__ == '__main__': check()
