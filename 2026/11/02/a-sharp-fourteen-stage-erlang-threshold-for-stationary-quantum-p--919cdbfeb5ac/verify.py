"""Exact rational certificate for Erlang renewal qubit purity/fidelity sign thresholds.
Run with Python 3; only the standard library is required.
"""
from fractions import Fraction as F
from math import comb


def trim(p):
    p = list(p)
    while len(p) > 1 and not p[-1]:
        p.pop()
    return p


def rem(p, q):
    p, q = trim(p), trim(q)
    if q == [0]:
        raise ZeroDivisionError
    while len(p) >= len(q) and p != [0]:
        a = p[-1] / q[-1]
        shift = len(p) - len(q)
        for i, z in enumerate(q):
            p[i + shift] -= a * z
        p = trim(p)
    return p


def sign(z):
    return (z > 0) - (z < 0)


def variations(signs):
    s = [t for t in signs if t]
    return sum(a != b for a, b in zip(s, s[1:]))


def sturm_variations(p):
    p = [F(c) for c in trim(p)]
    if len(p) == 1:
        return 0, 0
    d = [F(i) * p[i] for i in range(1, len(p))]
    seq = [p, trim(d)]
    while seq[-1] != [0] and len(seq[-1]) > 1:
        nxt = [-c for c in rem(seq[-2], seq[-1])]
        if nxt == [0]:
            break
        # Divide by positive scalar without changing Sturm signs.
        scale = max(abs(c) for c in nxt)
        nxt = trim([c / scale for c in nxt])
        seq.append(nxt)
    # Values at 0+ use the lowest nonzero coefficient if zero occurs at 0.
    v0 = variations([sign(next((c for c in p if c), F(0))) for p in seq])
    vinf = variations([sign(p[-1]) for p in seq])
    return v0, vinf


def coeffs(k):
    """Coefficients of N_k(y)/y^2, ascending powers, all integers."""
    assert k >= 2
    out = []
    for j in range(2, k + 1):
        c = -comb(k, j)
        if 2 * j <= k:
            c += 2 * (-1)**j * comb(k, 2*j)
        if 2*j-1 <= k:
            c += k * (-1)**(j-1) * comb(k, 2*j-1)
        out.append(c)
    return out


def check():
    checks=0
    for k in range(2, 14):
        p = coeffs(k)
        v0, vinf = sturm_variations(p)
        assert v0 == vinf, (k, v0, vinf)
        assert p[0] < 0 and p[-1] < 0
        print('shape=%02d degree=%02d signs_at_0=%d signs_at_infinity=%d positive_roots=0' %
              (k, len(p)-1, v0, vinf))
        checks += 3
    p14 = coeffs(14)
    v0, vinf = sturm_variations(p14)
    assert v0-vinf == 2
    print('shape=14 degree=12 positive_roots=2, variations=(%d,%d)' % (v0,vinf))
    checks += 1
    a = F(3,4)**7
    witness = 8*a - 1 - a*a
    assert witness == F(13436039,268435456) and witness > 0
    checks += 2
    u = F(22,45)
    L = 1 - u*u/2 + u**4/25
    assert L > 0 and L**15 > F(3,20)
    checks += 2
    assert (F(35,6)+1)*F(3,20) - F(3,20)**2 - 1 == F(1,400)
    checks += 1
    def evalpoly(p,y):
        out=F(0)
        for c in reversed(p):
            out=out*y+c
        return out
    assert evalpoly(p14,F(29,100)) < 0 < evalpoly(p14,F(3,10))
    assert evalpoly(p14,F(7,20)) > 0 > evalpoly(p14,F(9,25))
    checks += 2
    # Independent exact characteristic-transform checks using rational complex arithmetic.
    # A+Bi is stored as pair of Fractions to avoid floating-point error.
    def mul(a,b):
        return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]
    def sub(a,b):
        return a[0]-b[0], a[1]-b[1]
    for k in (1,2,3,7,13,14,15,20):
        for x in (F(1,3), F(1), F(3)):
            z = (1/(1+x*x), x/(1+x*x))
            zk=(F(1),F(0));sumz=(F(0),F(0))
            for _ in range(k):
                zk=mul(zk,z)
                sumz=(sumz[0]+zk[0],sumz[1]+zk[1])
            rep=sub((F(1),F(0)),zk)
            other=(-rep[1]/(k*x), rep[0]/(k*x))
            assert (sumz[0]/k,sumz[1]/k) == other
            d=(sumz[0]/k) - ((sumz[0]/k)**2+(sumz[1]/k)**2)
            if k>=2:
                y=x*x
                polynomial=evalpoly(coeffs(k),y)
                assert d == y*polynomial/(k*k*(1+y)**k)
            checks += 2
    print('All %d exact assertions passed.' % checks)

if __name__ == '__main__':
    check()
