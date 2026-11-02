"""Exact and independent checks of normalized moment bounds for rectangular flat tori.
Run: python3 verify_metric_torus.py. Uses only Python standard library.
"""
from fractions import Fraction as F
from itertools import product
from random import Random


def moment(a, s):
    """Exact E max(U[0,a_i])**s, positive integer s and rational a_i."""
    a = sorted(F(x) for x in a)
    assert a and all(x > 0 for x in a) and s > 0
    n = len(a)
    out = a[-1] ** s
    left = F(0)
    for j, right in enumerate(a):
        active = n - j
        prod = F(1)
        for x in a[j:]:
            prod *= x
        out -= F(s, s + active) * (right ** (s + active) - left ** (s + active)) / prod
        left = right
    return out


def test():
    checks = 0
    for d in range(2, 8):
        for a in product(range(1, 5), repeat=d):
            # Symmetry reduction retains all unordered profiles over these lengths.
            if tuple(sorted(a)) != a:
                continue
            m1, m2, m3, m4 = (moment(a, s) for s in (1, 2, 3, 4))
            for p, q, mp, mq in [(2, 1, m2, m1), (3, 1, m3, m1),
                                  (4, 2, m4, m2), (3, 2, m3, m2),
                                  (4, 3, m4, m3)]:
                # Raise the fractional moment ratio to q to keep exact rationals.
                ratq = mp**q / mq**p
                loq = F(d,d+p)**q / F(d,d+q)**p
                hiq = F(1,p+1)**q / F(1,q+1)**p
                assert loq <= ratq < hiq, (d,a,p,q,ratq,loq,hiq)
                checks += 1
            if len(set(a)) == 1:
                assert m1 == F(d, d + 1) * a[0]
                assert m2 == F(d, d + 2) * a[0]**2
    # Independent integrand quadrature against the polynomial-integral implementation.
    import math
    for a in [(F(1), F(3, 2)), (F(1), F(2), F(5)), (F(1, 2), F(1), F(5, 2), F(4))]:
        b = max(a)
        num = 50000
        h = float(b) / num
        def CDF(t):
            prod = 1.0
            for x in a:
                prod *= min(t / float(x), 1.0)
            return prod
        for s in (1, 2, 3, 4):
            # Midpoint approximation of survival-integral, independent of segment formula.
            val = sum(s*(i+0.5)**(s-1)*h**s*(1-CDF((i+.5)*h)) for i in range(num))
            assert abs(val - float(moment(a, s))) < 1e-7, (a, s, val, moment(a, s))
            checks += 1
    # Two-point torus distance distribution: independent Haar coordinates induce
    # uniform coordinate geodesic distances up to half-circumference.
    rng = Random(321789)
    a = [1.0, 1.8, 2.7]
    total = 180000
    s1 = s2 = 0.
    for _ in range(total):
        displacements=[]
        for ai in a:
            x,y=rng.random(),rng.random()
            delta=abs(x-y)
            displacements.append(ai*min(delta,1-delta))
        z=max(displacements)
        s1+=z
        s2+=z*z
    assert abs(s1/total-float(moment([F(str(x))/2 for x in a],1)))<0.009
    assert abs(s2/total-float(moment([F(str(x))/2 for x in a],2)))<0.009
    checks += 2
    # Sharp upper-limit sequence and lower equality.
    for d in range(2,8):
        assert moment([1]*d,2)/moment([1]*d,1)**2 == F((d+1)**2,d*(d+2))
        seq=[F(1,10000)]*(d-1)+[F(1)]
        rr=moment(seq,2)/moment(seq,1)**2
        assert abs(float(rr)-4/3)<0.001
        checks+=2
    print(f'VERIFY_OK exact_moment_profiles={checks} independent_quadratures=12 simulation_draws={total}')

if __name__=='__main__':
    test()
