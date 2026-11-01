"""Exact checks of cardinal-spline endpoint values and finite monotonicity samples.

The proof in RESULT.md applies to all orders. This checker is an independent
finite stress test, not a replacement for the analytic arguments.
"""
from fractions import Fraction as Q
from math import comb, factorial, pi, sqrt


def bspline(n, x):
    assert n >= 2
    x = Q(x)
    return Q(sum((-1)**j * comb(n, j) * max(x-j, 0)**(n-1)
               for j in range(n+1)), factorial(n-1))


def periodized_square(n, x):
    x = Q(x)
    return sum(bspline(n, x+k)**2 for k in range(-n-1, n+2))


def verify():
    cases = {2:(Q(1),Q(1,2)), 3:(Q(1,2),Q(19,32)),
             4:(Q(1,2),Q(265,576)), 5:(Q(61,144),Q(32227,73728)),
             6:(Q(571,1440),Q(1442647,3686400))}
    checks = 0
    for n in range(2, 13):
        v0 = periodized_square(n, 0)
        vh = periodized_square(n, Q(1,2))
        assert (v0 > vh) == (n % 2 == 0); checks += 1
        if n in cases:
            assert (v0,vh) == cases[n]; checks += 1
        last = v0
        for j in range(1,33):
            x=Q(j,64)
            p=periodized_square(n,x)
            if n%2 == 0:
                assert p < last
            else:
                assert p > last
            assert periodized_square(n,1-x)==p
            assert sum(bspline(n,x+k) for k in range(-n-1,n+2))==1
            last=p
            checks += 3
    # Exact rational tests of the partial-fraction identity used in the proof.
    for n in range(2, 11):
        for a in (Q(2), Q(5,2), Q(7)):
            for u in (Q(-3,2), Q(1,3), Q(3,4), Q(7,5), Q(8)):
                if u == 0 or a == u:
                    continue
                lhs = 1/(u**n * (a-u)**n)
                rhs = sum(comb(2*n-j-1,n-1) *
                          (u**(-j) + (a-u)**(-j)) / a**(2*n-j)
                          for j in range(1,n+1))
                assert lhs == rhs
                checks += 1
    # Compare finite-order condition-number excess with its theorem's limit.
    target = 4/sqrt(3*(1-4/pi**2))
    ratios=[]
    for n in (9, 12, 15, 18):
        p0=float(periodized_square(n,0))
        ph=float(periodized_square(n,Q(1,2)))
        ratios.append(abs(p0-ph)/min(p0,ph)*(pi*pi/4)**n)
        checks+=1
    assert all(0.85*target < r < 1.10*target for r in ratios)
    assert ratios[-1] > ratios[0]  # larger-order approach in tested orders
    print(f'CHECK_OK assertions={checks} scaled_ratios={ratios} limit={target:.12f}')


if __name__ == '__main__':
    verify()
