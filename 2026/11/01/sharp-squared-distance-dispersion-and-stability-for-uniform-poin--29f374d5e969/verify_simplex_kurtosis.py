#!/usr/bin/env python3
"""Exact finite diagnostics for simplex interpoint squared-distance moments.

The accompanying mathematical proof establishes the dimension-uniform claims;
this program independently checks the Dirichlet integration, formulas, and
selected sharp limiting examples, using only integer/rational arithmetic.
"""
from fractions import Fraction as F
from itertools import product
from math import factorial


def gram_data(vertices):
    n = len(vertices)
    d = len(vertices[0])
    assert n == d + 1
    ctr = [F(sum(p[k] for p in vertices), n) for k in range(d)]
    w = [[F(p[k]) - ctr[k] for k in range(d)] for p in vertices]
    g = [[sum(w[i][k] * w[j][k] for k in range(d))
          for j in range(n)] for i in range(n)]
    t = sum(g[i][i] for i in range(n))
    u = sum(g[i][j]**2 for i in range(n) for j in range(n))
    z = sum(g[i][i]**2 for i in range(n))
    return g, t, u, z


def formula(vertices):
    n = len(vertices)
    d = n - 1
    g, t, u, z = gram_data(vertices)
    a = n * (n + 1)
    b = a * (n + 2) * (n + 3)
    m2 = F(2 * t, a)
    m4 = F(2 * (t*t + 2*u + 6*z), b) + F(2*t*t + 4*u, a*a)
    q = m4 / (m2*m2)
    c = F(n*(n+1), (n+2)*(n+3))
    qmin = F((d+1)*(d+2)*(d+7), d*(d+3)*(d+4))
    qmax = F(6*(d+1)**3, d*(d+3)*(d+4))
    remainder = ((1+c)*(u-F(t*t,d)) + 3*c*(z-F(t*t,n))) / (t*t)
    assert q-qmin == remainder
    assert qmin <= q < qmax
    return m2, m4, q


def direct_integration(vertices):
    """Enumerate every Dirichlet monomial in squared distance squared."""
    g, _, _, _ = gram_data(vertices)
    n = len(vertices)
    def monomial(idx):
        counts = [0] * n
        for i in idx:
            counts[i] += 1
        den = 1
        for k in range(len(idx)):
            den *= n + k
        num = 1
        for c in counts:
            num *= factorial(c)
        return F(num, den)
    q2 = F(0)
    q4 = F(0)
    for i,j in product(range(n), repeat=2):
        q2 += g[i][j] * (2*monomial([i,j]) - 2*monomial([i])*monomial([j]))
    for inds in product(range(n),repeat=4):
        i,j,k,l = inds
        e = F(0)
        for mask in range(16):
            left = [inds[t] for t in range(4) if not (mask >> t) & 1]
            right = [inds[t] for t in range(4) if (mask >> t) & 1]
            e += (-1)**len(right) * monomial(left) * monomial(right)
        q4 += g[i][j] * g[k][l] * e
    return q2, q4


def verify():
    total = 0
    for d in (2,3,4):
        base = [[0]*d] + [[int(i==j) for j in range(d)] for i in range(d)]
        for shear in (0,1,3):
            vertices = [[p[j] + (shear*p[0] if j == 1 else 0)
                         for j in range(d)] for p in base]
            m2, m4, q = formula(vertices)
            exact2, exact4 = direct_integration(vertices)
            assert m2 == exact2 and m4 == exact4
            total += 3
        for epsilon in (F(1,2),F(1,5),F(1,20),F(1,100)):
            vertices = [[int(j==0) for j in range(d)]] + [
                [epsilon*int(i==j) for j in range(d)] for i in range(d)]
            _, _, q = formula(vertices)
            if epsilon == F(1,100):
                qmax = F(6*(d+1)**3,d*(d+3)*(d+4))
                assert q < qmax
            total += 2
        n = d+1
        centered = [[F(int(i==j)) - F(1,n) for j in range(n)] for i in range(n)]
        # This is an isometric regular d-simplex in the zero-sum hyperplane.
        g = [[sum(centered[i][k]*centered[j][k] for k in range(n))
              for j in range(n)] for i in range(n)]
        t = sum(g[i][i] for i in range(n))
        u = sum(g[i][j]**2 for i in range(n) for j in range(n))
        z = sum(g[i][i]**2 for i in range(n))
        assert u == t*t/d and z == t*t/n
        total += 2
    for n in range(3,11):
        bound = F(n*n-3*n+3,n*(n-1))
        for vals in product((-2,-1,0,1,2),repeat=n):
            if sum(vals) != 0 or not any(vals):
                continue
            s2 = sum(x*x for x in vals)
            s4 = sum(x**4 for x in vals)
            assert F(s4,s2*s2) <= bound
            total += 1
            if total > 90000:
                break
        if total > 90000:
            break
    print('PASS:', total, 'exact rational diagnostics')


if __name__ == '__main__':
    verify()
