#!/usr/bin/env python3
"""Reproduce exact positivity identities and Monte Carlo scale diagnostics."""
from fractions import Fraction as F
import math
import random


def forward_operator(gaps, tau):
    n = len(gaps)
    M = [ (gaps[i] + gaps[i+1]) / 2 for i in range(n-1)]
    mat = [[F(0) for _ in range(n-1)] for _ in range(n-1)]
    for i in range(n-1):
        mat[i][i] = 1 - tau * (1/gaps[i] + 1/gaps[i+1]) / M[i]
        if i > 0:
            mat[i][i-1] = tau / (M[i]*gaps[i])
        if i < n-2:
            mat[i][i+1] = tau / (M[i]*gaps[i+1])
    return mat


def exact_checks():
    cases = 0
    for n in range(2, 10):
        for j in range(1, 26):
            w = [F(1 + (k*k + 3*j*k + j*j) % 13, 1) for k in range(n)]
            s = sum(w)
            h = [x/s for x in w]
            lim = min(h[i] * h[i+1] / 2 for i in range(n-1))
            for tau in (F(0), lim/F(2), lim, lim*F(101,100)):
                P = forward_operator(h, tau)
                nonnegative = all(v>=0 for row in P for v in row)
                assert nonnegative == (tau<=lim), (n,j,tau,lim)
                if tau<=lim:
                    assert all(sum(row)<=1 for row in P)
                cases+=1
    return cases


def random_limit_checks():
    rng = random.Random(173)
    diagnostics=[]
    for n,reps in ((60,2500),(240,2500),(960,2000)):
        vals=[]
        for _ in range(reps):
            e = [rng.expovariate(1) for _ in range(n)]
            z = min(e[i]*e[i+1] for i in range(n-1))
            vals.append(n*math.log(n)*z)
        vals.sort()
        # CDF at the limiting Exp(1) 50th percentile log 2
        threshold=math.log(2)
        pct=sum(x<=threshold for x in vals)/len(vals)
        diagnostics.append((n,reps,round(pct,4),round(vals[len(vals)//2],5)))
        assert 0.25 < pct < 0.85
    return diagnostics


if __name__ == '__main__':
    ec=exact_checks()
    print('VERIFY_OK exact_positive_operator_cases=',ec)
    print('EXTREME_VALUE_SCALE_DIAGNOSTICS n,reps, empirical_CDF_at_log2, empirical_median:')
    for v in random_limit_checks():print(*v)
