"""Reproducible finite matrix and asymptotic checks for polynomial weighted dilations.

All infinite-dimensional statements require the analytic proof and are not certified
by the finite checks in this script.
"""
import math
import cmath
from fractions import Fraction


def polyphase(p, q):
    return [[p[j] for j in range(r, len(p), q)] for r in range(q)]


def inner(x, y):
    return sum(a.conjugate() * b for a, b in zip(x, y))


def coeffs(beta1, beta2, order, q, p, ell):
    source = (ell + order + 1) ** ((beta1 - 1) / 2)
    deriv = math.prod(range(ell + 1, ell + order + 1))
    return [(j + q * ell, c * source * deriv * (j + q * ell + 1) ** ((1-beta2)/2))
            for j, c in enumerate(p) if c]


def critical_gram(p, q, N):
    # H^2 -> H^2, order zero: exact coefficient matrix without radicals.
    columns = [dict(coeffs(1, 1, 0, q, p, ell)) for ell in range(N)]
    return [[sum(columns[k].get(t, 0) * columns[l].get(t, 0).conjugate()
                 for t in columns[k].keys() | columns[l].keys())
             for l in range(N)] for k in range(N)]


def check_critical():
    checks = 0
    for p, q, expected in [([1,1],2,(2,0)), ([1,0,1],2,(2,1)),
                           ([1,1,0,0,2],3,(6,2))]:
        G=critical_gram(p,q,30)
        # Toeplitz: G[k,l] is a function only of k-l.
        for k in range(30):
            for l in range(30):
                assert abs(G[k][l]-G[abs(k-l)][0])<1e-12
                checks += 1
        assert abs(G[0][0]-expected[0]) < 1e-12
        assert abs(G[0][1]-expected[1]) < 1e-12
        checks += 2
    # Unlike P=1+z^2, P=1+z gives an exactly isometric multiplier up to sqrt(2).
    Ga=critical_gram([1,1],2,12)
    Gb=critical_gram([1,0,1],2,12)
    assert Ga==[[2 if k==l else 0 for l in range(12)] for k in range(12)]
    assert Gb==[[2 if k==l else 1 if abs(k-l)==1 else 0 for l in range(12)] for k in range(12)]
    checks += 2
    return checks


def check_weight_exponents():
    checks=0
    for b1,b2,n,q in [(1,1,0,2), (1,3,1,3), (0,4,1,2), (2,1,0,4),(-1,2,0,3)]:
        gamma=n+(b1-b2)/2
        c=q**((1-b2)/2)
        for k in (200,1000,5000):
            a=coeffs(b1,b2,n,q,[1],k)[0][1]
            ratio=abs(a)/(c*k**gamma)
            assert abs(ratio-1) < 0.045, (b1,b2,n,q,k,ratio)
            checks += 1
    return checks


def check_fourier_gram():
    checks=0
    for p, q in [([2,1,3,0,2],2), ([1,2,-1,4,5,3],3), ([1,0,1,1,2,2],4)]:
        phases=polyphase(p,q)
        G=critical_gram(p,q,12)
        for d in range(6):
            # Fourier coefficient of h(t)=sum_r |P_r(t)|^2 at exponent -d.
            expected=sum(sum(ph[k+d]*ph[k].conjugate()
                             for k in range(len(ph)-d)) for ph in phases)
            assert abs(G[d][0]-expected)<1e-12, (p,q,d,G[d][0],expected)
            checks+=1
    return checks


if __name__ == '__main__':
    counts=[check_critical(),check_weight_exponents(),check_fourier_gram()]
    print('PASS:',sum(counts),'deterministic coefficient/Gram checks; groups',counts)
