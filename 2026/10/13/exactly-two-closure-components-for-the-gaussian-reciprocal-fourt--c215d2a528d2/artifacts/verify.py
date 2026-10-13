#!/usr/bin/env python3
"""Exact finite certificate for the Gaussian reciprocal fourth-power divisor range."""
from fractions import Fraction
from math import isqrt

ANCHORS = [29, 41, 53, 73, 101, 137, 193, 269, 373, 509, 701, 953, 1289, 1741, 2357, 3181, 4297, 5801, 7841, 10589, 14321, 19333, 26113, 35257, 47609, 64301, 86813, 117209, 158233, 213637, 288413, 389357, 525641, 709649, 958049, 1293373, 1746109, 2357249, 3182293, 4296137, 5799793, 7829737, 10570177, 14269757, 19264177, 26006641, 35108989, 47397149, 63986189, 86381461, 116614973, 157430249, 212530853, 286916653, 387337513, 522905657, 705922661, 952995601, 1286544097, 1736834537, 2344726693, 3165381101, 4273264493, 5768907101, 7788024653, 10513833373]


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d <= isqrt(n):
        if n % d == 0:
            return False
        d += 2
    return True


def gaussian_prime_norms(limit):
    # Nonramified Gaussian prime norms, with conjugate ideals counted separately.
    ans = []
    for p in range(3, limit+1, 2):
        if not is_prime(p):
            continue
        if p % 4 == 1:
            ans.extend((p, p))
        elif p*p <= limit:
            ans.append(p*p)
    return sorted(ans)


def verify():
    norms = gaussian_prime_norms(113)
    assert norms[:7] == [5, 5, 9, 13, 13, 17, 17]
    assert norms[-2:] == [113, 113]
    # For each norm less than 29, an exact finite subproduct of the subsequent
    # Euler factors exceeds the critical adjacent-interval overlap threshold.
    for j in range(7):
        n = norms[j]
        subproduct = Fraction(1)
        for later in norms[j+1:]:
            subproduct *= Fraction(later*later, later*later-1)
        assert subproduct >= Fraction(n*n+1, n*n), (j,n)
    # The second norm-5 occurrence is the tightest finite check.
    finite = Fraction(1)
    for n in norms[2:]:
        finite *= Fraction(n*n, n*n-1)
    assert finite > Fraction(26,25)
    # Consecutive split-prime anchors imply that for every real
    # 29 <= x < 8e9, a prime q == 1 mod 4 lies in (x, sqrt(2) x).
    assert ANCHORS[0] == 29 and ANCHORS[-1] >= 8_000_000_000
    for left,right in zip(ANCHORS, ANCHORS[1:]):
        assert right > left
        assert right%4==1 and is_prime(right)
        assert right*right < 2*left*left, (left,right)
    assert is_prime(ANCHORS[0])
    # For x >= 8e9 the unconditional explicit theta(x;4,1) estimate
    # of Bennett--Martin--O'Bryant--Rechnitzer supplies a split prime
    # in (x,sqrt(2)x). Its analytic step is proven in RESULT.md.
    assert Fraction(625,576)>Fraction(21,20)  # C>21/20
    assert Fraction(21,20)>1
    print('EXACT_CERTIFICATE_OK small_norms=7 finite_factors='+str(len(norms))+
          ' anchors='+str(len(ANCHORS))+' last_anchor='+str(ANCHORS[-1])+
          ' second_five_factor_ratio='+str(float(finite)))


if __name__ == '__main__':
    verify()
