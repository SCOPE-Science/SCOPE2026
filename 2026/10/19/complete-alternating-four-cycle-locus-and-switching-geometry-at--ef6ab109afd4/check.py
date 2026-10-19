"""Exact rational checks of the alternating-four-cycle classification.

Run with Python 3 (standard library only). These checks sample rational
parameters; the theorem for all real parameters is proved separately.
"""
from fractions import Fraction as Q
from itertools import product


def mm(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)) for i in range(2))


def mv(A, x):
    return tuple(sum(A[i][j] * x[j] for j in range(2)) for i in range(2))


def check(a, d, e):
    b = -(1 - d) * (1 - e) / a
    if not (a > abs(1 + d) and b < -abs(1 + e)):
        return 0
    assert d < 1 and e < 1 and 1 + d * e > 0
    p = (b + e + 1) / (2 * (1 + d * e))
    q = (a + d + 1) / (2 * (1 + d * e))
    s = a / (1 - e)
    radius = min(-p, q / s)
    P, v, w = (p, -e*q), (Q(1), e*a/(1-e)), (s, -d)
    assert p < 0 and q > 0 and radius > 0

    AL, AR = ((a, Q(1)), (-d, Q(0))), ((b, Q(1)), (-e, Q(0)))
    B = mm(AR, AL)
    assert mm(B, B)[0][0] + mm(B, B)[1][1] == 1 + (d*e)**2
    assert mv(B, v) == tuple(-x for x in v)
    assert mv(B, (Q(1), -a/(1-d))) == tuple(-d*e*x for x in (Q(1), -a/(1-d)))
    assert (a*b + (d-1)*(e-1)) == 0
    assert (q/s + p) == (a+d*(1-e))/(a*(1+d*e))

    def F(z):
        x, y = z
        M = AL if x <= 0 else AR
        return (M[0][0]*x + y + 1, M[1][0]*x)

    for t in (-radius, -radius/2, Q(0), radius/2, radius):
        z = tuple(P[i] + t*v[i] for i in range(2))
        z1 = F(z)
        z2 = F(z1)
        assert z[0] <= 0 and z1[0] >= 0 and z2[0] <= 0
        assert z2 == tuple(P[i] - t*v[i] for i in range(2))
        assert F(F(z2)) == z
        if t != 0:
            assert z2 != z

    for t in (-radius*Q(7,10), Q(0), radius*Q(7,10)):
        zbase = tuple(P[i] + t*v[i] for i in range(2))
        if d*e != 1:
            for u in (Q(0), Q(1,10000), Q(-1,10000)):
                ws=(Q(1),-a/(1-d))
                z=tuple(zbase[i]+u*ws[i] for i in range(2))
                if not (z[0]<0 and F(z)[0]>0 and F(F(z))[0]<0 and F(F(F(z)))[0]>0):
                    continue
                z4=F(F(F(F(z))))
                target=tuple(zbase[i]+u*(d*e)**2*ws[i] for i in range(2))
                assert z4 == target
    return 1


def main():
    N=0
    vals=[Q(-3),Q(-2),Q(-1),Q(-1,2),Q(0),Q(1,4),Q(1,2)]
    avals=[Q(1,4),Q(1,2),Q(3,4),Q(1),Q(5,4),Q(3,2),Q(2),Q(3),Q(4),Q(6),Q(9)]
    for d,e,a in product(vals, vals, avals):
        if d>=1 or e>=1: continue
        N+=check(a,d,e)
    assert N>100
    print('PASS: %d admissible exact-rational parameter triples; five four-cycle phases per triple; multiplier, switching, and local transverse identities checked.'%N)

if __name__=='__main__':
    main()
