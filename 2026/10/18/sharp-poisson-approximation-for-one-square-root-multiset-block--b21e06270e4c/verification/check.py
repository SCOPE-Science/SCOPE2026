"""Standalone exact finite verification of multiset fixed-point asymptotics.

Requires Python 3 standard library only. Finite tests do not replace the proof.
"""
from fractions import Fraction
from itertools import permutations
from math import comb, exp, factorial, floor, sqrt


def distribution(n, m):
    assert 1 <= m <= n
    t = n - m
    b = []
    denominator = 1
    for h in range(n + 1):
        if h:
            denominator *= n - h + 1
        numerator = 0
        for s in range(max(0, h - t), min(m, h) + 1):
            r = h - s
            falling = 1
            for u in range(s):
                falling *= m - u
            numerator += comb(t, r) * comb(m, s) * falling
        b.append(Fraction(numerator, denominator))
    mass = [sum(((-1) ** (h-j)) * comb(h, j) * b[h]
                for h in range(j, n+1)) for j in range(n+1)]
    assert min(mass) >= 0
    assert sum(mass) == 1
    mu = Fraction(n - m + m*m, n)
    assert sum(j * mass[j] for j in range(n+1)) == mu
    f2 = sum(j*(j-1)*mass[j] for j in range(n+1))
    expected_f2_cumulant = Fraction(
        m*(m-1)*(m*m-2*m*n-m+n), n*n*(n-1))
    assert f2 - mu*mu == expected_f2_cumulant
    return mass


def direct_enumeration(n, m):
    reference = (0,)*m + tuple(range(1, n-m+1))
    counts = [0]*(n+1)
    words = set(permutations(reference))
    for word in words:
        counts[sum(word[i] == reference[i] for i in range(n))] += 1
    return [Fraction(count, len(words)) for count in counts]


def poisson_mass(k, lam):
    from math import lgamma, log
    return exp(-lam + k*log(lam) - lgamma(k+1))


def total_variation(mass, lam):
    n = len(mass)-1
    subtotal = sum(abs(float(p) - poisson_mass(j, lam)) for j,p in enumerate(mass))
    # Sum the remaining Poisson tail without unstable subtraction from one.
    j = n+1
    p = poisson_mass(j, lam)
    while p > 1e-17:
        subtotal += p
        j += 1
        p *= lam/j
    return subtotal/2


def main():
    for n, m in ((4,2), (6,2), (9,3)):
        assert distribution(n,m) == direct_enumeration(n,m)
    target = 5*exp(-2)/3
    assert abs(target - 0.2255588053943545) < 1e-14
    for k in range(2, 13):
        n = k*k
        m = k
        mass = distribution(n,m)
        lam = (n-m+m*m)/n
        scaled = sqrt(n)*total_variation(mass,lam)
        print(f'n={n:3d} m={m:2d} scaled_TV={scaled:.12f}')
    print(f'asymptotic_target={target:.12f}')
    print('PASS: exact finite distributions, mixed moment identities, and direct enumeration')

if __name__ == '__main__':
    main()
