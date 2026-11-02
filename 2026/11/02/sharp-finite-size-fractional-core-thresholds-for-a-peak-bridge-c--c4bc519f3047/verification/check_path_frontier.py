#!/usr/bin/env python3
"""Exact rational primal/dual witnesses for a peak--bridge committee election.

Requires Python 3.9+. The optional optimization cross-check requires scipy.
The universal theorem is established by the accompanying analytical proof,
not by these finite tests.
"""
from fractions import Fraction as F
from itertools import combinations


def frontier(k, v):
    assert k >= 1 and F(1, 2) < v < 1
    if k % 2:
        h = k // 2
        return v * k / (h + v)
    h = k // 2
    return v * (2*h - 1 + 2*v) / (h - 1 + 2*v)


def primal(k, v):
    r = frontier(k, v)
    p, q = [F(0)] * k, [F(0)] * (k-1)
    if k == 1:
        p[0] = F(1)
    elif k % 2:
        for i in range(k-1):
            q[i] = r / (2*v)
        p[0] = p[-1] = r/2
    else:
        h = k//2
        z = F(h) / (h-1+2*v)
        for i in range(k-1):
            q[i] = F(1) if i % 2 == 0 else z
        p[0] = p[-1] = v*z
    return p, q


def dual(k, v):
    if k % 2:
        h = k//2
        a = v/(h+v)
        b = (1-v)/(h+v)
        lam = [a if i % 2 == 0 else b for i in range(k)]
        exceptional = None
    else:
        h = k//2
        a = v/(h-1+2*v)
        b = (1-v)/(h-1+2*v)
        lam = [a if i % 2 == 0 or i == k-1 else b for i in range(k)]
        exceptional = k-2
    return lam, a, exceptional


def verify_exact(k, v):
    r = frontier(k, v)
    p, q = primal(k, v)
    assert len(p) == k and len(q) == k-1
    assert all(F(0) <= x <= 1 for x in p+q)
    assert sum(p+q) == k
    utilities = [p[i] + v*( (q[i-1] if i else F(0)) + (q[i] if i < k-1 else F(0))) for i in range(k)]
    assert all(u == r for u in utilities), (k,v,utilities,r)
    lam, mu, exceptional = dual(k, v)
    assert sum(lam) == 1
    assert all(F(0) <= x <= mu for x in lam)
    assert all(v*(lam[i]+lam[i+1]) <= mu for i in range(k-1) if i != exceptional)
    if exceptional is None:
        assert r == mu*k
    else:
        assert v*(lam[exceptional]+lam[exceptional+1])-mu == mu*(2*v-1)
        assert r == mu*(k+2*v-1)
    assert v*lam[0] <= mu and v*lam[-1] <= mu
    return r


def opt_lp(k, v, S):
    from scipy.optimize import linprog
    n = 2*k-1
    A, rhs = [], []
    for i in S:
        row = [0.]*(n+1)
        row[-1] = 1.
        row[2*i] = -1.
        if i: row[2*i-1] = -float(v)
        if i<k-1: row[2*i+1] = -float(v)
        A.append(row); rhs.append(0.)
    A.append([1.]*n+[0.]); rhs.append(float(len(S)))
    obj = [0.]*n+[-1.]
    sol = linprog(obj, A_ub=A, b_ub=rhs, bounds=[(0.,1.)]*n+[(0.,None)],method='highs')
    assert sol.success, sol.message
    return -sol.fun


def main():
    values = [F(51,100), F(3,5), F(3,4), F(9,10), F(99,100)]
    exact_cases=0; lp_cases=0
    for v in values:
        last=F(0)
        for k in range(1,17):
            r=verify_exact(k,v)
            assert r >= last
            last=r
            exact_cases += 1
        for k in range(2,9):
            r=frontier(k,v)
            for s in range(1,k+1):
                for S in combinations(range(k),s):
                    optimum=opt_lp(k,v,S)
                    assert optimum <= float(r)+1e-8, (k,v,S,optimum,r)
                    lp_cases += 1
            grand=opt_lp(k,v,tuple(range(k)))
            assert abs(grand-float(r)) < 1e-8, (k,v,grand,r)
    print(f'VERIFY_OK exact_primal_dual={exact_cases} numerical_coalition_LPs={lp_cases}')

if __name__ == '__main__':
    main()
