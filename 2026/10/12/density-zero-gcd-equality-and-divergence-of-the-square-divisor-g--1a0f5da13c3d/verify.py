"""Exact finite checks accompanying the gcd-of-squared-divisor-sums density theorem.

This program does not certify the infinite Dirichlet-series or density limits;
those steps are proved in the accompanying mathematical argument.
"""
from math import gcd
from fractions import Fraction


def smallest_prime_factors(n):
    spf = list(range(n + 1))
    for p in range(2, int(n**0.5) + 1):
        if spf[p] == p:
            for x in range(p*p, n+1, p):
                if spf[x] == x:
                    spf[x] = p
    return spf


def sigma_square(m, spf):
    x, product = m, 1
    while x > 1:
        p, e = spf[x], 0
        while x % p == 0:
            x //= p
            e += 1
        product *= (p ** (2*e+1) - 1) // (p-1)
    return product


def roots(p, power):
    first = [r for r in range(1, p) if (r*r+r+1) % p == 0]
    assert len(first) == 2
    results = []
    for r in first:
        for j in range(2, power+1):
            previous = p ** (j-1)
            lifts = [r+t*previous for t in range(p)
                     if ((r+t*previous)**2 + (r+t*previous)+1) % (previous*p) == 0]
            assert len(lifts) == 1
            r = lifts[0]
        results.append(r)
    assert all((r*r+r+1) % (p**power) == 0 for r in results)
    return tuple(results)


def exact_exponent_once(n, p):
    return n % p == 0 and n % (p*p) != 0


def main():
    bound = 100000
    spf = smallest_prime_factors(bound)
    counts, targets = {}, {10,100,1000,10000,100000}
    equal = 0
    for m in range(1,bound+1):
        s = sigma_square(m, spf)
        a, b = gcd(m,s), gcd(m*m,s)
        assert b % a == 0
        if a == b:
            equal += 1
        if m in targets:
            counts[m] = equal
    expected = {10:10,100:99,1000:974,10000:9561,100000:93845}
    assert counts == expected, (counts,expected)
    print('GCD_EQUALITY_PREFIX_COUNTS',counts)
    for p in (7,13,19,31):
        for B in (1,2,3):
            rr = roots(p,B)
            assert len(set(rr)) == 2
            assert all(gcd(r,p) == 1 for r in rr)
            print('HENSEL_ROOTS',p,B,rr)
    Q = (7,13)
    modulus = 1
    predicted = Fraction(1,1)
    for q in Q:
        modulus *= q*q
        predicted *= (1-Fraction(q-1,q*q))
    actual = sum(1 for m in range(1,modulus+1)
                 if all(not exact_exponent_once(m,q) for q in Q))
    assert Fraction(actual,modulus) == predicted
    print('FINITE_CRT_AVOID_ALL',Q,actual,modulus,str(predicted))
    for p in (7,13,19):
        rr = roots(p,2)
        witnesses = [q for q in range(2,bound+1)
                     if spf[q] == q and q % (p*p) in rr]
        assert len(witnesses) > 2
        assert all((q*q+q+1) % (p*p) == 0 for q in witnesses)
        print('AP_PRIME_WITNESSES',p,len(witnesses),witnesses[:5])
    print('VERIFY_OK exact finite tests; infinite conclusions rely on symbolic proof')

if __name__ == '__main__':
    main()
