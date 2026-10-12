#!/usr/bin/env python3
"""Exact rational, finite checks for common-shock Poisson conditional laws.

The universal claims depend on the analytic proof; these bounded checks
are independent reproducibility diagnostics, not infinite certificates.
"""
from fractions import Fraction as Q
from itertools import product
from math import comb, factorial, prod


def binom_mass(m, k, n):
    if not 0 <= k <= m:
        return Q(0)
    return Q(comb(m, k) * (n-1)**(m-k), n**m)


def conditional_mass(n, a, b, s):
    """P(X_1=x | sum X_i=s), exact for positive rational a,b."""
    a, b = Q(a), Q(b)
    options = []
    for z in range(s//n + 1):
        m = s - n*z
        weight = b**z / factorial(z) * (n*a)**m / factorial(m)
        options.append((z, m, weight))
    norm = sum((w for _, _, w in options), Q(0))
    out = []
    for x in range(s+1):
        numerator = sum((w * binom_mass(m, x-z, n) for z,m,w in options), Q(0))
        out.append(numerator / norm)
    assert sum(out) == 1
    return out


def joint_unnormalized(x, a, b):
    return sum((b**z/Q(factorial(z)) * prod(a**(u-z)/Q(factorial(u-z)) for u in x)
                for z in range(min(x)+1)), Q(0))


def pair_joint_unnormalized(x, s, a, b):
    if x < 0 or s < x:
        return Q(0)
    return sum((a**(s-2*z)/Q(factorial(x-z)*factorial(s-x-z))
                * b**z/Q(factorial(z)) for z in range(min(x,s-x)+1)), Q(0))


def test_exact_thresholds():
    count = 0
    for a in [Q(1,2),Q(1),Q(2),Q(5,3)]:
        for k in [Q(1,5),Q(1),Q(2),Q(3),Q(6),Q(7),Q(12)]:
            b = a**3*k
            p2, p3 = conditional_mass(3,a,b,2), conditional_mass(3,a,b,3)
            w = Q(9)*a**3/(Q(9)*a**3+2*b)
            assert p2 == [Q(4,9),Q(4,9),Q(1,9)]
            assert p3 == [8*w/27, 1-5*w/9, 2*w/9, w/27]
            st = all(sum(p2[t:]) <= sum(p3[t:]) for t in range(1,4))
            assert st == (b <= 6*a**3)
            lr = all(p3[i]*p2[i+1] <= p3[i+1]*p2[i] for i in range(0,2))
            assert lr == (b <= 2*a**3)
            count += 1
    return count


def test_dimension_thresholds():
    count = 0
    for n in range(3,13):
        r = sum((binom_mass(n-1,k,n) for k in range(2,n)),Q(0))
        delta = Q(n-1,n*n)*Q(n-1,n)**(n-2)
        assert r > 0 and delta>0
        for a in [Q(1,2), Q(1), Q(7,4)]:
            amp = (n*a)**n/Q(factorial(n))
            crit = amp*delta/r
            for q in [Q(1,3),Q(1),Q(3,2)]:
                b = crit*q
                prev = conditional_mass(n,a,b,n-1)
                after = conditional_mass(n,a,b,n)
                assert sum(prev[2:]) == r
                assert sum(after[2:]) == amp/(amp+b)*(r+delta)
                assert (sum(after[2:]) < sum(prev[2:])) == (b > crit)
                count += 1
    return count


def test_bivariate_total_positivity():
    count=0
    for a,b in [(Q(1),Q(7)),(Q(1,5),Q(1,2)),(Q(7),Q(1,8)),(Q(1),Q(100))]:
        for x in range(13):
            for s in range(13):
                d=(pair_joint_unnormalized(x,s,a,b)*pair_joint_unnormalized(x+1,s+1,a,b)
                   -pair_joint_unnormalized(x,s+1,a,b)*pair_joint_unnormalized(x+1,s,a,b))
                assert d>=0
                count+=1
    return count


def test_mtp2():
    count=0
    for n in [2,3,4]:
        for a,b in [(Q(1),Q(7)),(Q(1,3),Q(10)),(Q(3),Q(1,5))]:
            pts=list(product(range(4), repeat=n))
            mass={x:joint_unnormalized(x,a,b) for x in pts}
            for i,x in enumerate(pts):
                for y in pts[i+1:]:
                    meet=tuple(min(s,t) for s,t in zip(x,y))
                    join=tuple(max(s,t) for s,t in zip(x,y))
                    assert mass[x]*mass[y] <= mass[meet]*mass[join]
                    count+=1
    return count


def main():
    print('Exact trivariate thresholds:',test_exact_thresholds(),'parameter cases')
    print('General-dimension tail transitions:',test_dimension_thresholds(),'parameter cases')
    print('Adjacent bivariate TP2 determinants:',test_bivariate_total_positivity(),'exact inequalities')
    print('MTP2 finite-lattice comparisons:',test_mtp2(),'exact inequalities')
    print('All bounded checks passed; universal theorems require the written proof.')


if __name__=='__main__':
    main()
