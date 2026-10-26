#!/usr/bin/env python3
"""Exact-fraction check of finite reversible binary-switch spectral realization.

Uses only the Python standard library. The theorem is proved independently;
these finite checks are reproducibility examples, not an infinite certificate.
"""
from fractions import Fraction as F
from itertools import product
from math import factorial, exp


def check(mean, rates, weights, allocations):
    assert len(rates) == len(weights) == len(allocations)
    n = len(rates)
    assert n >= 1 and all(v > 0 for v in rates+weights+allocations)
    assert sum(allocations) < mean
    prob = [h*h/(h*h+w) for h, w in zip(allocations, weights)]
    amp = [(h*h+w)/h for h, w in zip(allocations, weights)]
    base = mean-sum(allocations)
    states = list(product((0,1), repeat=n))
    idx = {s:i for i,s in enumerate(states)}
    pi = [F(1) for _ in states]
    dvals = []
    for i,s in enumerate(states):
        for j, bit in enumerate(s):
            pi[i] *= prob[j] if bit else 1-prob[j]
        dvals.append(base+sum(amp[j]*bit for j,bit in enumerate(s)))
    q = [[F(0) for _ in states] for _ in states]
    for i,s in enumerate(states):
        for j,bit in enumerate(s):
            s2=list(s);s2[j]=1-bit
            v = (prob[j] if not bit else (1-prob[j]))*rates[j]
            k=idx[tuple(s2)]
            q[i][k]+=v
            q[i][i]-=v
    assert min(dvals) == base > 0
    assert sum(pi)==1
    assert sum(pi[i]*dvals[i] for i in range(len(states)))==mean
    assert all(sum(row)==0 for row in q)
    assert all(pi[i]*q[i][k]==pi[k]*q[k][i] for i in range(len(states)) for k in range(len(states)))
    modes = [[amp[j]*(s[j]-prob[j]) for s in states] for j in range(n)]
    for j in range(n):
        assert all(sum(q[i][k]*modes[j][k] for k in range(len(states)))==-rates[j]*modes[j][i] for i in range(len(states)))
        for k in range(n):
            inner=sum(pi[i]*modes[j][i]*modes[k][i] for i in range(len(states)))
            assert inner == (weights[j] if j==k else F(0))
    assert all(dvals[i]-mean==sum(modes[j][i] for j in range(n)) for i in range(len(states)))
    for t in (F(1,4), F(1), F(3)):
        c=sum(float(weights[j])*exp(-float(rates[j]*t)) for j in range(n))
        # This is the exact eigenbasis semigroup expression, evaluated in floats.
        c2=0.0
        for j in range(n):
            pj=sum(float(pi[i])*float(modes[j][i])*float(dvals[i]-mean) for i in range(len(states)))
            c2+=pj*exp(-float(rates[j]*t))
        assert abs(c-c2)<1e-11*max(1,abs(c))
    print('EXACT_VERIFY_OK states=',len(states),'modes=',n,'mean=',mean,'minD=',base)


if __name__=='__main__':
    check(F(2), [F(1,2),F(3,2),F(5,2)], [F(2),F(1,3),F(5)], [F(1,3)]*3)
    check(F(3,2), [F(1),F(4)], [F(1,10),F(17,4)], [F(1,5),F(1,5)])
    check(F(7), [F(2)], [F(1000)], [F(1)])
