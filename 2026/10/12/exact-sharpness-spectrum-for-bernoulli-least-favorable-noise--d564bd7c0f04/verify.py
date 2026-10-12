from fractions import Fraction
from math import comb


def binom_prob(n, k, p):
    q = 1 - p
    return Fraction(comb(n, k), 1) * p**k * q**(n-k)


def check(p, m):
    q = 1 - p
    sigma2 = p*q
    probs = [binom_prob(m+1, s, p) for s in range(m+2)]
    cond = [Fraction(s, m+1) for s in range(m+2)]
    assert sum(probs) == 1
    mean = sum(w*x for w, x in zip(probs, cond))
    var = sum(w*(x-mean)**2 for w, x in zip(probs, cond))
    assert mean == p
    assert var == sigma2 / (m+1)
    v = m*sigma2
    assert var == sigma2*sigma2/(sigma2+v)
    a = sigma2/(sigma2+v) if sigma2+v else Fraction(1,1)
    assert (1-a) == a*m


count = 0
for p in [Fraction(1,7), Fraction(1,3), Fraction(2,5), Fraction(1,2), Fraction(4,5), Fraction(6,7)]:
    for m in range(0, 9):
        check(p, m)
        count += 1
print('VERIFY_OK', count)
