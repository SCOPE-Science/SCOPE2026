#!/usr/bin/env python3
"""Standalone exact checks for star transmission control formulas."""
from fractions import Fraction as Q
from itertools import product
from functools import reduce
from math import sqrt


def determinant(rows):
    n = len(rows)
    if n == 0:
        return Q(1)
    total = Q(0)
    for j in range(n):
        if rows[0][j] != 0:
            minor = [row[:j] + row[j+1:] for row in rows[1:]]
            total += ((-1) ** j) * rows[0][j] * determinant(minor)
    return total


def schur_certificate(a, ds, bs, cs, xs, ys):
    n = len(ds)
    matrix = [[Q(0) for _ in range(n+1)] for _ in range(n+1)]
    matrix[0][0] = a
    for i in range(n):
        matrix[i+1][i+1] = ds[i]
        matrix[0][i+1] = bs[i] * xs[i]
        matrix[i+1][0] = cs[i] * ys[i]
    identity_minus = [[Q(int(i == j)) - matrix[i][j]
                       for j in range(n+1)] for i in range(n+1)]
    w = [bs[i] * cs[i] / (1-ds[i]) for i in range(n)]
    H = 1-a
    scalar = H - sum((w[i]*xs[i]*ys[i] for i in range(n)), Q(0))
    assert determinant(identity_minus) == scalar * reduce(
        lambda x, y: x*y, (1-d for d in ds), Q(1))
    return w, H, scalar


def cheapest_directional(w, p, q, H):
    budget = sum(w)-H
    priority = sorted(range(len(w)), key=lambda i: w[i]/min(p[i], q[i]),
                      reverse=True)
    r = [Q(0)]*len(w)
    for i in priority:
        take = min(Q(1), budget/w[i])
        r[i] = take
        budget -= w[i]*take
        if budget == 0:
            break
    assert budget == 0
    cost = sum((min(p[i], q[i])*r[i] for i in range(len(w))), Q(0))
    return r, cost


def reciprocal_solution(w, p, q, H):
    h = [p[i]+q[i] for i in range(len(w))]
    def weighted_squares(lam):
        return sum(float(w[i])*min(1.0, float(h[i])/(2*lam*float(w[i])))**2
                   for i in range(len(w)))
    lo, hi = 0.0, 1.0
    while weighted_squares(hi) > float(H):
        hi *= 2
    for _ in range(105):
        mid = (lo+hi)/2
        if weighted_squares(mid) > float(H):
            lo = mid
        else:
            hi = mid
    t = [min(1.0, float(h[i])/(2*hi*float(w[i]))) for i in range(len(w))]
    assert all(0 < v <= 1 for v in t)
    assert abs(sum(float(w[i])*t[i]*t[i] for i in range(len(w)))-float(H)) < 1e-10
    return t, sum(float(h[i])*(1-t[i]) for i in range(len(w)))


# Every attenuation combination in three rational parameter settings and
# stars with two, three, and four spokes. Determinants are exact Fractions.
count=0
for m in (2, 3, 4):
    for shift in range(3):
        a=Q(shift+1,6)
        ds=[Q((i+shift)%3,5) for i in range(m)]
        bs=[Q(i+1,3) for i in range(m)]
        cs=[Q(i+2,2) for i in range(m)]
        for xs in product((Q(0), Q(1,2), Q(1)), repeat=m):
            for ys in product((Q(0), Q(1,2), Q(1)), repeat=m):
                schur_certificate(a,ds,bs,cs,xs,ys)
                count+=1
assert count==22113

# Exact nontrivial policy contrast: 3 spokes, threshold mass 3/4.
w,H,_=schur_certificate(Q(1,4),[Q(0)]*3,[Q(1)]*3,[Q(1)]*3,
                        [Q(1)]*3,[Q(1)]*3)
r,direct=cheapest_directional(w,[Q(1)]*3,[Q(1)]*3,H)
t,reciprocal=reciprocal_solution(w,[Q(1)]*3,[Q(1)]*3,H)
assert r==[Q(1),Q(1),Q(1,4)]
assert direct==Q(9,4)
assert all(abs(z-0.5)<1e-11 for z in t)
assert abs(reciprocal-3.0)<1e-10
assert sum(w[i]*(1-r[i]) for i in range(3))==H

# The exact sharp price law on two equal spokes.
for u in (Q(1,10000),Q(1,4),Q(1,2),Q(9999,10000)):
    W=Q(1,2); H=W*u
    w=[Q(1,4),Q(1,4)]
    rr,cd=cheapest_directional(w,[Q(1)]*2,[Q(1)]*2,H)
    t,cr=reciprocal_solution(w,[Q(1)]*2,[Q(1)]*2,H)
    assert abs(cr/float(cd)-2/(1+sqrt(float(u))))<1e-10
    assert cr+1e-10>=float(cd)
    assert cr<=2*float(cd)+1e-10

# Unequal-cost price is unbounded already on the same two-spoke family.
for M in (Q(1),Q(3),Q(11),Q(101)):
    w=[Q(1,4),Q(1,4)]; H=Q(1,8)
    rr,cd=cheapest_directional(w,[Q(1)]*2,[M]*2,H)
    t,cr=reciprocal_solution(w,[Q(1)]*2,[M]*2,H)
    assert cd==Q(3,2)
    assert abs(cr-float(M+1))<1e-10

print('VERIFY_OK: %d exact Schur determinants, sharp directional and reciprocal cost certificates' % count)
