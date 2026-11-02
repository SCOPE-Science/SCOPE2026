"""Deterministic checks for the two-pilot oracle log-determinant example.

The checks verify finite algebraic instances. Infinite claims require the
analytical arguments in RESULT.md, not finite enumeration.
"""
import math
from fractions import Fraction


def parameters(k):
    assert isinstance(k, int) and k >= 1
    ell, j, l, h = 48*k, 27*k, 36*k, 12*k
    p, m = ell*ell, 3
    return ell, j, l, h, p, l+p, m, 4*k+1


def grouped_spectrum(k, epsilon=None):
    ell, j, l, h, p, n, m, probes = parameters(k)
    delta = 0.25
    if epsilon is None:
        return [(delta, l), (delta/math.sqrt(p), p)]
    assert 0 < epsilon < 1/math.sqrt(p)
    large = delta*math.sqrt((1-(p-h)*epsilon*epsilon)/h)
    return [(delta, l), (large, h), (delta*epsilon, p-h)]


def tail_sum(groups, rank, f):
    total, removed = 0.0, rank
    for value, count in groups:
        take = min(removed, count)
        removed -= take
        total += (count-take)*f(value)
    assert removed == 0
    return total


def risk(groups, rank, probes):
    return 2*tail_sum(groups, rank, lambda x: math.log1p(x)**2)/probes


def check():
    checks = 0
    for k in list(range(1, 101)) + [250, 500, 1000]:
        ell,j,l,h,p,n,m,probes = parameters(k)
        assert ell==48*k and j==27*k and l==36*k
        assert h==12*k and p==ell**2 and n==l+p
        assert ell+m==l+m*probes
        assert Fraction(3, 9*k+3)*Fraction(9*k+1)>1
        checks += 4
        b=grouped_spectrum(k)
        assert sum(c for _,c in b)==n
        assert b[0][0] >= b[1][0] > 0
        assert abs(tail_sum(b,l,lambda x:x*x)-1/16)<1e-13
        assert abs(tail_sum(b,j,lambda x:x*x)-(9*k+1)/16)<1e-11
        ratio= risk(b,ell,1)/risk(b,l,probes)
        assert math.isclose(ratio,probes*(1-h/p),rel_tol=1e-12)
        checks+=5
        for eps in [1e-2/math.sqrt(p),1e-3/math.sqrt(p),1e-4/math.sqrt(p)]:
            c=grouped_spectrum(k,eps)
            assert sum(t for _,t in c)==n
            assert 0<c[-1][0]<c[1][0]<c[0][0]<=0.25
            assert abs(tail_sum(c,l,lambda x:x*x)-1/16)<1e-13
            assert abs(tail_sum(c,j,lambda x:x*x)-(9*k+1)/16)<1e-11
            assert risk(c,ell,1)<risk(c,l,probes)
            checks+=5
        assert Fraction(probes)*(1-Fraction(h,p))>k
        checks+=1
    for k in range(1,1001):
        _,j,l,h,p,_,_,probes=parameters(k)
        assert Fraction(3,l-j+3)*Fraction(9*k+1)>1
        assert Fraction(h,p)==Fraction(1,192*k)
        assert Fraction(probes)*(1-Fraction(h,p))>k
        checks+=3
    print('PASS:',checks,'finite arithmetic checks')
    for k in (1,20,100):
        b=grouped_spectrum(k)
        c=grouped_spectrum(k,1e-8/math.sqrt(parameters(k)[4]))
        ell,j,l,h,p,n,m,probes=parameters(k)
        print('k=',k,'diffuse one/mixed=',risk(b,ell,1)/risk(b,l,probes),
              'concentrated mixed/one=',risk(c,l,probes)/risk(c,ell,1))


if __name__=='__main__':
    check()
