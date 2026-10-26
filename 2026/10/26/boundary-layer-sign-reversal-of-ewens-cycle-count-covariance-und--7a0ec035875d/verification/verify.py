"""Reproducible exact checks for the near-maximal-cycle Ewens covariance theorem.
Run: python3 verification/verify.py (standard library only).
"""
from fractions import Fraction
from itertools import permutations
from math import factorial


def g(k, theta):
    if k < 0:
        return Fraction(0)
    z = Fraction(1)
    for j in range(k):
        z *= Fraction(theta + j, j + 1)
    return z


def a(n, r, s, theta):
    k = n - s
    z = g(k, theta)
    for j in range(max(0, r - s)):
        z -= theta * g(j, theta) / (k - j)
    return z


def covariance(n, r, theta):
    assert n >= max(4, 2*r + 4) and theta > 0
    v = [a(n, r, s, theta) for s in range(4)]
    assert v[0] > 0
    return theta**2 * (v[0]*v[3] - v[1]*v[2]) / (2*v[0]**2)


def cycle_lengths(perm):
    seen = set(); lengths = []
    for i in range(len(perm)):
        if i in seen:
            continue
        k = 0; j = i
        while j not in seen:
            seen.add(j); k += 1; j = perm[j]
        lengths.append(k)
    return lengths


def exhaustive(n, r, theta):
    total = ef = et = eft = Fraction(0)
    for perm in permutations(range(n)):
        ll = cycle_lengths(perm)
        if max(ll) > n-r:
            continue
        w = theta**len(ll)
        f, t = ll.count(1), ll.count(2)
        total += w; ef += w*f; et += w*t; eft += w*f*t
    assert total
    actual = eft/total - ef*et/total**2
    expected = covariance(n, r, theta)
    assert actual == expected, (n, r, theta, actual, expected)


def main():
    count = 0
    for theta in [Fraction(s) for s in ('1/5','1/2','3/4','1','3/2','2','3','5')]:
        for r in range(1, 8):
            for n in range(max(4,2*r+4), 56):
                c = covariance(n,r,theta)
                if theta == 1 or theta > 1 or r <= 2:
                    assert c < 0, (n,r,theta,c)
                if theta < 1 and r == 3:
                    assert c > 0, (n,r,theta,c)
                count += 1
    exhaustive_checks=0
    for theta in (Fraction(1,2),Fraction(1),Fraction(2)):
        for r in (1,2):
            for n in range(max(4,2*r+4),9):
                exhaustive(n,r,theta); exhaustive_checks+=1
    for theta in (Fraction(1,2),Fraction(1),Fraction(2)):
        for n in range(6,9):
            # r=1 formula works already when n >= 4.
            c = covariance(n,1,theta)
            v = [g(n-s,theta) for s in range(4)]
            an = v[0] - theta/n
            factored = theta**2 * v[3] / (2*n*an**2) * (
                2*(1-theta)*v[1]/(n-2)-theta)
            assert c == factored
            if theta==1:
                assert c==Fraction(-n,2*(n-1)**2)
            if theta==2:
                assert c==Fraction(-8*n,(n+2)**2*(n-1))
    # Coefficient identity for the rare-event covariance contribution.
    for theta in [Fraction(1,3),Fraction(1,2),Fraction(1),Fraction(3,2),Fraction(2),Fraction(3)]:
        for r in range(1,13):
            h=Fraction(0)
            for j in range(r):
                gj=g(j,theta)
                ef=theta*g(j-1,theta)/gj if j>=1 else 0
                et=theta*g(j-2,theta)/(2*gj) if j>=2 else 0
                eft=theta**2*g(j-3,theta)/(2*gj) if j>=3 else 0
                h+=gj*(eft-theta*et-theta*ef/2+theta**2/2)
            assert h == theta**2*(g(r-1,theta)-g(r-3,theta))/2,(theta,r,h)
    print('PASS: %d exact finite formula/sign checks; %d full Ewens permutation enumerations; 15 special-form checks; 72 rare-event coefficient identities' % (count,exhaustive_checks))

if __name__ == '__main__':
    main()
