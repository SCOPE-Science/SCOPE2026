#!/usr/bin/env python3
"""Exact rational Fourier perturbation check for the sine-forced circle-map invariant density."""
from fractions import Fraction as F
from math import comb, factorial


def P(q, b):
    return {k // b: v for k, v in q.items() if k % b == 0 and v}


def add(dst, k, v):
    if v:
        dst[k] = dst.get(k, F(0)) + v
        if not dst[k]: del dst[k]


def coeffs(b, order=3):
    q = [{0: F(1)}]
    for n in range(1, order + 1):
        rhs = {}
        for r in range(1, n + 1):
            prev = P(q[n-r], b)
            for j in range(r+1):
                shift = r-2*j
                for k0, value in prev.items():
                    k = k0 + shift
                    add(rhs, k, F((-1)**(r+j)*comb(r,j)*k**r, factorial(r))*value)
        term, cur = rhs, {}
        # Finite support and zero constant mode force eventual annihilation by P.
        for _ in range(30):
            for k, v in term.items(): add(cur, k, v)
            term = P(term, b)
            if not term: break
        else: raise AssertionError('Series inversion failed')
        assert 0 not in cur and all(cur.get(-k) == v for k,v in cur.items())
        q.append(cur)
    return q

for b in [2, 3, 4, 5, 6, 8, 10, 20]:
    q = coeffs(b)
    expect = F(-7,2) if b==2 else F(-4) if b==3 else F(1,2)
    assert q[1][1] == -1
    assert q[2].get(1,0) == (2 if b==2 else 0)
    assert q[3].get(1,0) == expect, (b,q)
    print('b=',b,'M/pi normal coeffs:',q[1][1],q[2].get(1,0),q[3].get(1,0))
print('EXACT_FOURIER_COEFFICIENTS_PASS')
