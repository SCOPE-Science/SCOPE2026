"""Reproducibility checks for sparse binary Lyndon-factor formulas.

Requires only Python 3.10+ standard library. Finite checking supplements, and
is not a substitute for, the symbolic all-length proofs in RESULT.md.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb


def is_lyndon(word):
    if len(word) == 1:
        return True
    return all(word < word[i:] + word[:i] for i in range(1, len(word)))


def brute_count(word):
    factors = set()
    for i in range(len(word)):
        for j in range(i + 1, len(word) + 1):
            factor = word[i:j]
            if is_lyndon(factor):
                factors.add(factor)
    return len(factors)


def gap_count(a, b, c, d):
    m = a+b+c+d
    if m == 0:
        return 1
    return (2 + max(a,b,c) + max(0,a-b) + max(0,b-c)
            + max(0,a-max(b,c)) + int(a >= b > c))


def coefficient_list_rational(num, den, end):
    # If G(z) = N(z)/D(z) and D(0)=1, recover coefficients recursively.
    assert den[0] == 1
    out = []
    for k in range(end+1):
        s = num[k] if k < len(num) else 0
        s -= sum(den[j]*out[k-j] for j in range(1,min(k,len(den)-1)+1))
        out.append(s)
    return out


def poly_mul(p,q):
    r = [0]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):r[i+j] += a*b
    return r


def main():
    total_brute = 0
    for n in range(3,21):
        for idx in combinations(range(n),3):
            a,b,c,d = idx[0],idx[1]-idx[0]-1,idx[2]-idx[1]-1,n-1-idx[2]
            word = ''.join('1' if i in idx else '0' for i in range(n))
            assert brute_count(word) == gap_count(a,b,c,d), (word,(a,b,c,d))
            total_brute += 1

    # Rational series for aggregate Lyndon count at binary weight three.
    numerator = [1,11,4,3,-1,1,2,-3,1]
    denominator = [1]
    for f in ([1,-1],)*5 + ([1,1], [1,1,1]):
        denominator = poly_mul(denominator,f)
    coeffs = coefficient_list_rational(numerator, denominator, 25)
    aggregate_checked = 0
    for m in range(26):
        hist = Counter()
        for a in range(m+1):
            for b in range(m-a+1):
                for c in range(m-a-b+1):
                    d = m-a-b-c
                    hist[gap_count(a,b,c,d)] += 1
                    aggregate_checked += 1
        assert sum(k*v for k,v in hist.items()) == coeffs[m], (m, coeffs[m], hist)
        assert sum(hist.values()) == comb(m+3,3)
        if m >= 3:
            assert hist[3*m+2] == 1
            assert hist[3*m+1] == hist[3*m] == 0
            assert hist[3*m-1] == (3 if m == 3 else 2)
            assert hist[2] == 1
        if m >= 4:
            second = [(a,b,c,d)
                      for a in range(m+1)
                      for b in range(m-a+1)
                      for c in range(m-a-b+1)
                      for d in [m-a-b-c]
                      if gap_count(a,b,c,d) == 3*m-1]
            assert second == [(m-1,0,0,1),(m-1,1,0,0)]

    # Exact simplex integration of each quadratic polynomial
    # (1+p*u+q*v)/3 over the ordered three-coordinate simplex.
    # The normalized density is 4 on {(u,v): u>=0,v>=0,2u+v<=1}.
    eu, ev = Fraction(1,6), Fraction(1,3)
    eu2, euv, ev2 = Fraction(1,24), Fraction(1,24), Fraction(1,6)
    forms = [(4,8),(4,8),(4,5),(1,5),(4,2),(1,2)]
    cond_mean = sum(((1+p*eu+q*ev)/3 for p,q in forms), Fraction())/6
    cond_second = sum(((1+2*p*eu+2*q*ev+p*p*eu2+2*p*q*euv+q*q*ev2)/9
                      for p,q in forms), Fraction())/6
    assert cond_mean == Fraction(19,18), cond_mean
    assert cond_second == Fraction(37,27), cond_second
    # Beta(3,1) radial component independent of shape: E[S]=3/4,
    # E[S^2]=3/5. This gives the all-four-gap simplex moments.
    mean = cond_mean * Fraction(3,4)
    second = cond_second * Fraction(3,5)
    assert mean == Fraction(19,24)
    assert second == Fraction(37,45)
    assert second - mean*mean == Fraction(563,2880)

    print('PASS independent brute words:', total_brute)
    print('PASS gap compositions through m=25:', aggregate_checked)
    print('PASS full rational series through m=25, isolation through m=25')
    print('PASS conditional continuous first and second moments:', mean, second)

if __name__ == '__main__':
    main()
