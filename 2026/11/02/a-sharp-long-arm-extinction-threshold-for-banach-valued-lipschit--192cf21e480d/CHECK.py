"""Exact-rational checks for the one-long-arm star extension formula.
Run: python CHECK.py. No third-party packages are needed.
These finite tests supplement, and do not replace, the proof.
"""
from fractions import Fraction as F
from itertools import product


def predicted(m, r):
    r = F(r)
    cut = F(m, m-2)
    if r <= cut:
        den = m*r*r + 2*r + m
        a = r*(r+1)/den
        value = m*(r+1)*(r+1)/den
    else:
        a = F(1, m)
        value = F(2*(m-1), m)
    return value, a


def actual_row_norm(m, r, a, leaf):
    weights = [F(1)]*m + [F(r)]
    coords = [F(a)]*m + [F(1)-m*F(a)]
    mu = [int(k == leaf)-coords[k] for k in range(m+1)]
    assert sum(mu) == 0
    # Dual Lipschitz ball: independent values f(v_j) in [-w_j,w_j]
    # after fixing hub f(o)=0 on the weighted star.
    bruteforce = max(abs(sum(mu[k]*sgn[k]*weights[k]
                             for k in range(m+1)))
                     for sgn in product((-1, 1), repeat=m+1))
    tree_norm = sum(abs(mu[k])*weights[k] for k in range(m+1))
    assert bruteforce == tree_norm
    return tree_norm / weights[leaf]


def all_norm(m,r,a):
    # Algebraic weighted-tree transport formula, independently verified
    # with signed potentials only at the proposed optimum.
    b = F(1)-m*F(a)
    short = abs(F(1)-a) + (m-1)*abs(F(a)) + F(r)*abs(b)
    longrow = (m*abs(F(a))+F(r)*abs(F(1)-b))/F(r)
    return max(F(1),short,longrow)


r_values = list(map(F, ['1', '5/4', '3/2', '2', '7/3', '3', '4', '8', '20']))
checks = 0
for m in range(3, 9):
    rs = sorted(set(r_values + [F(m,m-2)]))
    for r in rs:
        value, a = predicted(m,r)
        assert F(0) <= a <= F(1,m)
        assert all_norm(m,r,a) == value
        for leaf in (0,m):
            assert actual_row_norm(m,r,a,leaf) == (
                abs(F(1)-a)+(m-1)*abs(a)+r*abs(F(1)-m*a)
                if leaf == 0 else m*abs(a)*(1+F(1)/r))
        checks += 1
        # Exact one-variable global reduction: symmetric affine coordinates
        # can have any sign, including beyond the probability simplex.
        for j in range(-20, 61):
            cand = F(j,20*m)
            assert all_norm(m,r,cand) >= value, (m,r,cand)
            checks += 1
        # At the transition, the long-leaf mass vanishes exactly.
        if r == F(m,m-2):
            assert a == F(1,m)
        if r < F(m,m-2):
            assert F(1)-m*a > 0
        else:
            assert F(1)-m*a == 0
print('PASS exact rational tests:',checks)
