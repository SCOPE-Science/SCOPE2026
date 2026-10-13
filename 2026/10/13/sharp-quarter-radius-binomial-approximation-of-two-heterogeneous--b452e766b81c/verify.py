"""Exact rational checks for a sharp two-trial Poisson-binomial binomial-cover radius.

These finite checks corroborate identities in RESULT.md; the universal theorem
is established by its analytic proof, not by enumeration.
Run: python3 verify.py
"""
from fractions import Fraction as F
from math import comb


def tv(left, right):
    length = max(len(left), len(right))
    return sum(abs((left[i] if i < len(left) else 0) -
                   (right[i] if i < len(right) else 0))
               for i in range(length)) / 2


def two_bernoulli(p, q):
    return [(1-p)*(1-q), p*(1-q)+q*(1-p), p*q]


def binomial(m, r):
    return [F(comb(m, k)) * r**k * (1-r)**(m-k) for k in range(m+1)]


def test():
    low_count = high_count = middle_count = 0
    for i in range(33):
        for j in range(33):
            p, q = F(i, 32), F(j, 32)
            w = p*q
            if w <= F(1,4):
                r = p+q-w
                d = tv(two_bernoulli(p,q), binomial(1,r))
                assert d == w and d <= F(1,4), (i,j,d,w)
                low_count += 1
    # Squared grid makes sqrt(pq) rational, so the high branch uses no floats.
    for i in range(33):
        for j in range(33):
            p, q = F(i*i,1024), F(j*j,1024)
            if p*q >= F(1,4):
                r = F(i*j,1024)
                d = tv(two_bernoulli(p,q), binomial(2,r))
                assert d == p+q-2*r == (F(i-j,32))**2, (i,j,d)
                assert d <= F(1,4), (i,j,d)
                if d == F(1,4):
                    assert sorted([p,q]) == [F(1,4),F(1)]
                high_count += 1
    extremal = two_bernoulli(F(1),F(1,4))
    assert extremal == [F(0), F(3,4), F(1,4)]
    for m in range(1,51):
        if m>=2:
            # mode at success probability 1/m, exact rational maximum
            singleton_max = F(m-1,m)**(m-1)
            assert singleton_max <= F(1,2)
        for k in range(65):
            r=F(k,64)
            d = tv(extremal, binomial(m,r))
            assert d >= F(1,4), (m,k,d)
            middle_count += 1
    assert tv(extremal,binomial(1,F(1))) == F(1,4)
    assert tv(extremal,binomial(2,F(1,2))) == F(1,4)
    print(f'VERIFY_OK low_rational={low_count} high_square_rational={high_count} extremal_tests={middle_count}')


if __name__ == '__main__':
    test()
