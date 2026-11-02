"""Exact independent checks for equal-quota coupon-completion ordering.

Run: python3 verify.py
All comparisons use fractions, with no floating point assumptions.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import factorial

CHECKS = 0


def check(statement):
    global CHECKS
    CHECKS += 1
    assert statement, f'Assertion {CHECKS} failed'


def convolution(a, b, degree):
    return [sum((a[k] * b[n-k] for k in range(n+1)), Q(0))
            for n in range(degree+1)]


def tail_exp(p, q, degree):
    return [Q(0) if k < q else p**k / factorial(k)
            for k in range(degree+1)]


def completion_formula(p, p0, q, tmax):
    m = len(p)
    result = [[Q(0) for _ in p] for _ in range(tmax+1)]
    for i in range(m):
        degree = tmax - q
        a = [p0**k / factorial(k) for k in range(degree+1)]
        for j in range(m):
            if i != j:
                a = convolution(a, tail_exp(p[j], q, degree), degree)
        for t in range(m*q, tmax+1):
            result[t][i] = factorial(t-1)*p[i]**q / factorial(q-1)*a[t-q]
    return result


def completion_dp(p, p0, q, tmax):
    m = len(p)
    initial = (0,)*m
    alive = {initial: Q(1)}
    result = [[Q(0) for _ in p] for _ in range(tmax+1)]
    for t in range(1, tmax+1):
        nxt = {}
        for state, probability in alive.items():
            if p0:
                nxt[state] = nxt.get(state, Q(0)) + probability*p0
            for i in range(m):
                state2 = list(state)
                state2[i] += 1
                if state2[i] > q:
                    state2[i] = q
                state2 = tuple(state2)
                mass = probability * p[i]
                if all(v == q for v in state2):
                    check(state[i] == q-1)
                    result[t][i] += mass
                else:
                    nxt[state2] = nxt.get(state2,Q(0)) + mass
        alive=nxt
        check(sum(alive.values())+sum(sum(result[s]) for s in range(1,t+1)) == 1)
    return result


def run():
    profiles = [
        ([1, 2], 0), ([1, 3, 6], 0), ([1, 1, 1], 0),
        ([1, 1, 2, 4], 0), ([2, 3, 5, 7], 1),
        ([1, 1], 8), ([1, 2, 3], 4), ([1, 3, 3, 5], 2),
        ([1, 1, 1, 1], 7), ([1, 2], 7),
    ]
    for weights, null_weight in profiles:
        denom = sum(weights) + null_weight
        p = tuple(Q(x, denom) for x in weights)
        p0 = Q(null_weight, denom)
        m = len(p)
        for q in (1, 2, 3, 4):
            tmax = m*q+7
            f=completion_formula(p,p0,q,tmax)
            g=completion_dp(p,p0,q,tmax)
            for t in range(tmax+1):
                for i in range(m):
                    check(f[t][i] == g[t][i])
                if t >= m*q:
                    check(sum(f[t]) > 0)
            initial = f[m*q]
            check(len(set(initial)) == 1)
            for i in range(m):
                check(f[m*q+1][i]/f[m*q][i] == Q(m*q,q+1)*(1+q*p0-p[i]))
            for i,j in combinations(range(m),2):
                for t in range(m*q, tmax):
                    a=f[t][i]*f[t+1][j]
                    b=f[t+1][i]*f[t][j]
                    check((a>b) if p[i]>p[j] else (a<b) if p[i]<p[j] else (a==b))
            for t in range(m*q,tmax+1):
                by_type = sum((p[i]*f[t][i] for i in range(m)),Q(0)) / sum(f[t])
                check(min(p) <= by_type <= max(p))
    print(f'PASS {CHECKS} exact rational assertions')

if __name__=='__main__':
    run()
