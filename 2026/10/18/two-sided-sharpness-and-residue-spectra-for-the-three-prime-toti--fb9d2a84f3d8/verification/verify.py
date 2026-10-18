#!/usr/bin/env python3
"""Exact independent checks of the fixed-support totient discrepancy theorem.
All arithmetic is integer arithmetic; this program does not prove prime infinitude.
"""
from math import gcd, isqrt


def is_prime(n):
    return n > 1 and all(n % d for d in range(2, isqrt(n) + 1))


def S(n):
    # Count admissible residues, independent of any factorization formula.
    return sum(gcd(u, n) == gcd(u-1, n) == 1 for u in range(1, n+1))


def T(n):
    # Literal definition, with explicit odd representatives.
    return sum(gcd(m, n) == gcd((m-1)//2, n) == 1 for m in range(1, n+1, 2))


def B(P, a):
    return sum(gcd(j, P) == gcd(a*j-1, P) == 1 for j in range(1, P+1, 2))


def verify():
    checks = 0
    p65 = [j for j in range(1,66,2) if gcd(j,65)==gcd(24*j-1,65)==1]
    p119 = [j for j in range(1,120,2) if gcd(j,119)==gcd(31*j-1,119)==1]
    assert (S(65),T(65),B(65,24)) == (33,15,19)
    assert (S(119),T(119),B(119,31)) == (75,38,35)
    assert p65 == [1,3,7,11,17,21,23,27,31,33,37,41,43,47,51,53,57,61,63]
    assert p119 == [1,3,9,13,15,23,25,27,29,31,37,39,41,43,53,55,57,59,65,67,69,71,73,81,83,87,93,95,97,99,101,107,109,111,115]
    checks += 4
    for P in range(3,101,2):
        SP=S(P)
        TP=T(P)
        for a in range(1,P):
            if gcd(a,P)==1:
                assert B(P,a)+B(P,-a)==SP, (P,a)
                checks += 1
        for r in range(3,110,2):
            if is_prime(r) and gcd(r,P)==1:
                n=P*r
                rhs=(r-1)//2*SP+TP-2*B(P,r)
                assert T(n)==rhs, (P,r,n,T(n),rhs)
                assert S(n)==(r-2)*SP, (P,r,n)
                d = 2*T(n)-S(n)+1
                assert d == SP+1+2*TP-4*B(P,r), (P,r,d)
                checks += 3
    for P,a,expected in [(65,24,-6),(119,31,6)]:
        for r in range(3,2500,2):
            if is_prime(r) and r%P==a:
                n=P*r
                # Efficient witness via exact fixed-support theorem, with literal check of modest n.
                discrepancy = (S(P)+1)//2+T(P)-2*B(P,r)
                assert discrepancy==expected
                if n <= 220000:
                    assert 2*T(n)-S(n)+1 == 2*expected
                    checks += 1
                checks += 1
    from collections import Counter
    for P,expected in [
        (65, {-6:1, -4:5, -2:18, 0:18, 2:5, 4:1}),
        (119, {-4:1, -2:10, 0:37, 2:37, 4:10, 6:1})
    ]:
        counts=Counter((S(P)+1)//2+T(P)-2*B(P,a)
                       for a in range(1,P) if gcd(a,P)==1)
        assert dict(counts)==expected, (P,counts)
        checks += sum(counts.values())
    small_supports=[]
    for P in range(15,120,2):
        factors=[p for p in range(3,P+1,2) if is_prime(p) and P%p==0]
        if len(factors)!=2 or factors[0]*factors[1]!=P:
            continue
        vals=[(S(P)+1)//2+T(P)-2*B(P,a)
              for a in range(1,P) if gcd(a,P)==1]
        small_supports.append((P,min(vals),max(vals)))
        checks += len(vals)
    assert next(P for P,lo,hi in small_supports if lo == -6) == 65
    assert next(P for P,lo,hi in small_supports if hi == 6) == 119
    checks += 2
    assert (T(5785),S(5785)) == (1429,2871)
    assert (T(3689),S(3689)) == (1093,2175)
    checks += 2
    print('PASS:',checks,'exact integer checks')
    print('P65:',S(65),T(65),B(65,24),len(p65))
    print('P119:',S(119),T(119),B(119,31),len(p119))
    print('Witnesses: n=5785, D=-6 and n=3689, D=+6')
    print('Boundary support minima: first negative at P=65; first positive at P=119')

if __name__ == '__main__':
    verify()
