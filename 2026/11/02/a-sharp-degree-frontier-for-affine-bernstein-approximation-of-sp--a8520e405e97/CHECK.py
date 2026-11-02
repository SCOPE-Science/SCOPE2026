#!/usr/bin/env python3
"""Exact rational checks for spherical Bernstein/Gegenbauer coefficient identities.

Only Python standard-library arithmetic is used. Finite checks do not prove
positivity at every Legendre order or dimension.
"""
from fractions import Fraction as F
from math import comb, factorial


def plus(p, q):
    r = [F(0)] * max(len(p), len(q))
    for i, x in enumerate(p): r[i] += x
    for i, x in enumerate(q): r[i] += x
    return r


def scale(p, c):
    return [c * x for x in p]


def mul(p, q):
    r = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q): r[i+j] += a * b
    return r


def power(p, n):
    r = [F(1)]
    for _ in range(n): r = mul(r, p)
    return r


def eval_poly(p, x):
    s = F(0)
    for c in reversed(p): s = x * s + c
    return s


def gegenbauer(m, lam):
    if m == 0: return [F(1)]
    p = [F(1)]
    q = [F(0), 2 * lam]
    for k in range(2, m+1):
        r = plus(scale([F(0)] + q, 2*(k-1+lam)/k),
                 scale(p, -(k-2+2*lam)/k))
        p, q = q, r
    return q


def bernstein(p, n):
    result = [F(0)] * (n+1)
    for j in range(n+1):
        node = F(2*j-n, n)
        v = eval_poly(p, node)
        basis = mul(power([F(1,2), F(1,2)], j),
                    power([F(1,2), F(-1,2)], n-j))
        result = plus(result, scale(basis, comb(n,j)*v))
    return result


def in_basis(p, basis):
    arr = p[:] + [F(0)]*(len(basis)-len(p))
    out = [F(0)]*len(basis)
    for k in reversed(range(len(basis))):
        coeff = arr[k]/basis[k][k]
        out[k] = coeff
        for i in range(k+1): arr[i] -= coeff*basis[k][i]
    assert all(v == 0 for v in arr)
    return out


def main():
    count = 0
    for d in range(2, 10):
        lam = F(d-1, 2)
        for n in range(1, 13):
            Cn = gegenbauer(n,lam)
            Cm = gegenbauer(n+2,lam)
            Qn_lead = Cn[n]/eval_poly(Cn,F(1))
            Qm = scale(Cm, 1/eval_poly(Cm,F(1)))
            got = bernstein(Qm,n)[n]/Qn_lead
            want = (F(factorial(n),n**n) * (n+lam) *
                    F(d+1-n,3*n) * F((n+1)*(n+2),(n+d-1)*(n+d)))
            assert got == want, (d,n,got,want)
            count += 1
    assert (bernstein(gegenbauer(6,F(1,2)),4)[4]/
            gegenbauer(4,F(1,2))[4]) == F(-9,256)
    count += 1
    basis = [gegenbauer(k,F(1,2)) for k in range(4)]
    for n in (1,2,3):
        for m in range(0, 65):
            p = gegenbauer(m,F(1,2))
            out = bernstein(p,n)
            coeffs = in_basis(out,basis[:n+1])
            assert all(z >= 0 for z in coeffs), (n,m,coeffs)
            count += 1
    print('PASS: %d exact rational assertions' % count)

if __name__ == '__main__':
    main()
