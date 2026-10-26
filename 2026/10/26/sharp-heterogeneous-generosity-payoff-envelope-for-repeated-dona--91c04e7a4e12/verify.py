#!/usr/bin/env python3
"""Exact-rational checks for heterogeneous repeated-donation GTFT payoffs.

Requires only the Python standard library. Analytical infinite-dimensional
and convex-order assertions are proved in RESULT.md, not by these finite checks.
"""
from fractions import Fraction as Q
from itertools import product
from math import comb

COUNT = 0

def check(assertion, context):
    global COUNT
    if not assertion:
        raise AssertionError(context)
    COUNT += 1

def payoff(g, h, benefit, cost, continuation):
    x, y = 1-g, 1-h
    return ((benefit-cost)/(1-continuation)
            + (cost*continuation*x - benefit*continuation*y + cost-benefit)
            / (2*(1-continuation*continuation*x*y)))

def solve(A, z):
    n = len(z)
    B = [list(map(Q, A[i])) + [Q(z[i])] for i in range(n)]
    for i in range(n):
        j = next(j for j in range(i,n) if B[j][i] != 0)
        B[i], B[j] = B[j], B[i]
        v = B[i][i]
        B[i] = [t/v for t in B[i]]
        for j in range(n):
            if j != i:
                v = B[j][i]
                B[j] = [B[j][u] - v*B[i][u] for u in range(n+1)]
    return [B[i][-1] for i in range(n)]

def independent_payoff(g,h,benefit,cost,continuation):
    M = [[Q(1),Q(0),Q(0),Q(0)],
         [g,Q(0),1-g,Q(0)],
         [h,1-h,Q(0),Q(0)],
         [g*h,g*(1-h),h*(1-g),(1-g)*(1-h)]]
    V = [benefit-cost,-cost,benefit,Q(0)]
    A = [[Q(i==j)-continuation*M[i][j] for j in range(4)] for i in range(4)]
    r = solve(A,V)
    return sum(r)/4

def heterogeneity_gap(g_values,weights,benefit,cost,continuation):
    mean = sum(g*w for g,w in zip(g_values,weights))
    mixture = sum(weights[i]*weights[j]*payoff(g_values[i],g_values[j],benefit,cost,continuation)
                  for i in range(len(weights)) for j in range(len(weights)))
    return payoff(mean,mean,benefit,cost,continuation)-mixture

def endpoint_gap(L,U,mean,benefit,cost,continuation):
    if L == U:
        return Q(0)
    theta = (mean-L)/(U-L)
    return heterogeneity_gap([1-L,1-U],[1-theta,theta],benefit,cost,continuation)

pairs = [Q(i,5) for i in range(6)]
for benefit,cost,delta in [(Q(3),Q(2),Q(1,2)), (Q(7),Q(1),Q(3,4)),
                            (Q(5),Q(2),Q(1,3))]:
    for g,h in product(pairs,pairs):
        check(payoff(g,h,benefit,cost,delta)
              == independent_payoff(g,h,benefit,cost,delta), ('matrix',g,h,delta))
    for a,b,c in product(range(6),repeat=3):
        if a+b+c != 5:
            continue
        probabilities = [Q(a,5),Q(b,5),Q(c,5)]
        levels = [Q(0),Q(1,2),Q(1)]
        mean_g = sum(levels[i]*probabilities[i] for i in range(3))
        mean_x = 1-mean_g
        variance = sum(probabilities[i]*(1-levels[i]-mean_x)**2 for i in range(3))
        gap = heterogeneity_gap(levels,probabilities,benefit,cost,delta)
        lower = (benefit-cost)*delta**3*mean_x*variance/2
        upper = endpoint_gap(Q(0),Q(1),mean_x,benefit,cost,delta)
        check(gap >= lower, ('lower', probabilities, gap, lower))
        check(gap <= upper, ('upper', probabilities, gap, upper))
        check((gap == Q(0)) == (variance == Q(0)), ('strict', probabilities))
        if probabilities[1]==0:
            check(gap == upper, ('endpoint',probabilities))
for k in range(2,8):
    for beta in [Q(1,4),Q(1,3),Q(1,2),Q(2,3),Q(3,4)]:
        lam = (1-beta)/beta
        Z = sum(lam**j for j in range(k))
        weights = [lam**j/Z for j in range(k)]
        gs = [Q(j,k-1) for j in range(k)]
        gap = heterogeneity_gap(gs,weights,Q(3),Q(2),Q(1,2))
        check(gap>0, ('IGT',k,beta,gap))
example = heterogeneity_gap([Q(0),Q(1)],[Q(1,2),Q(1,2)],Q(3),Q(2),Q(1,2))
check(example == Q(1,48), ('exact-example',example))
print('VERIFIED',COUNT,'exact-rational assertions; illustration gap =',example)
