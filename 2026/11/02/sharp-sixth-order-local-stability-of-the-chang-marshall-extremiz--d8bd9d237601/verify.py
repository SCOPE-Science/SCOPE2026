"""Exact finite Taylor-coefficient checks for the monomial stability calculation.

Python 3 standard library only. These are finite checks; the theorem's
all-degree and infinite-dimensional assertions follow from the proof.
"""
from collections import defaultdict
from fractions import Fraction as Q
from math import isqrt

K = 6

def mult(A, B):
    out = defaultdict(Q)
    for (t, f), a in A.items():
        for (u, g), b in B.items():
            if t + u <= K:
                out[(t + u, f + g)] += a*b
    return {k: v for k, v in out.items() if v}

def coeffs(m, c, d):
    root = isqrt(m)
    assert root*root == m
    a = {0: Q(1, root), 1: Q(1), 2: c, 3: d}
    den = {0: Q(1), 2: Q(m + 1), 4: Q(m + 2)*c*c,
           6: Q(m + 3)*d*d}
    inv = {0: Q(1)}
    for j in (2,4,6):
        inv[j] = -sum(den.get(k,Q()) * inv.get(j-k,Q())
                      for k in range(2,j+1,2))
    power = defaultdict(Q)
    for i, ai in a.items():
        for j, aj in a.items():
            power[(i+j,i-j)] += ai*aj
    x = defaultdict(Q)
    for (i, j), aij in power.items():
        for k, ik in inv.items():
            if i+k <= K:
                x[(i+k,j)] += aij*ik
    x[(0,0)] -= Q(1,m)
    p = {(0,0):Q(1)}
    coeff = defaultdict(Q)
    coeff[(0,0)] = Q(1)
    fac = 1
    for k in range(1,K+1):
        p = mult(p,x)
        fac *= k
        for key,val in p.items():
            coeff[key] += val/fac
    return coeff[(2,0)], coeff[(4,0)], coeff[(6,0)]

def main():
    cases = 0
    for root in range(1,9):
        m = root*root
        c = Q(2*m+1,2*root)
        d = Q(m)+Q(5,4)+Q(1,3*m)
        a2,a4,a6 = coeffs(m,c,d)
        assert (a2,a4,a6) == (0,0,-Q(1,24*m)), (m,a2,a4,a6)
        _,v4,_ = coeffs(m,c+1,d)
        assert v4 == -Q(1,m), (m,v4)
        _,v4,v6 = coeffs(m,c,d+1)
        assert v4 == 0 and v6 == -Q(1,24*m)-Q(2,m), (m,v4,v6)
        cases += 3
    print('CHECK_OK: %d exact Fourier/Taylor coefficient cases across m=1,4,...,64; finite algebra checks only' % cases)

if __name__ == '__main__':
    main()
