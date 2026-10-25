"""Finite cross-checks for three-one binary Lyndon-factor statistics.

Standard-library only. All-length conclusions require the separate symbolic proof.
"""
from collections import Counter
from fractions import Fraction
from math import comb


def is_lyndon(s):
    return len(s) == 1 or (len(s) > 1 and all(s < s[i:] + s[:i] for i in range(1, len(s))))


def brute_lyndon_count(a, b, c, d):
    w = '0' * a + '1' + '0' * b + '1' + '0' * c + '1' + '0' * d
    return len({w[i:j] for i in range(len(w)) for j in range(i + 1, len(w) + 1)
                if is_lyndon(w[i:j])})


def count_formula(a, b, c, d):
    m = a + b + c + d
    return (1 + int(m > 0) + max(a, b, c) + max(a-b, 0) + max(b-c, 0)
            + max(a - max(b, c), 0) + int(a >= b > c))


def add(X, Y):
    result = X.copy()
    for term, value in Y.items():
        result[term] = result.get(term, 0) + value
    return {term: v for term, v in result.items() if v}


def mul(X, Y, bound):
    result = {}
    for (m, j), v in X.items():
        for (n, k), w in Y.items():
            if m+n <= bound:
                term = (m+n, j+k)
                result[term] = result.get(term, 0) + v*w
    return {term: v for term, v in result.items() if v}


def scale(X, value):
    return {term: value*v for term, v in X.items() if value*v}


def monomial(a, b):
    return {(a, b): 1}


def geo(a, b, bound):
    if a <= 0:
        raise ValueError('positive z degree required')
    return {(a*i, b*i): 1 for i in range(bound//a+1)}


def generating_coefficients(bound):
    one = monomial(0, 0)
    powers = {
        'E': geo(3, 1, bound),
        'R22': geo(2, 2, bound), 'R21': geo(2, 1, bound),
        'R13': geo(1, 3, bound), 'R12': geo(1, 2, bound),
        'R11': geo(1, 1, bound), 'D': geo(1, 0, bound)
    }

    def term(zdeg, ydeg, *geometries):
        p = monomial(zdeg, ydeg)
        for name in geometries:
            p = mul(p, powers[name], bound)
        return p

    # Seven weak-order cases for (a,b,c), including the diagonal.
    Q = one
    for a, b, g in [(2,3,'R22'), (2,2,'R22'), (2,1,'R21'),
                    (1,3,'R13'), (1,1,'R11'), (1,2,'R12')]:
        Q = add(Q, term(a,b,g))
    # The six strict-order cases; a>b>c contributes the extra exponent one.
    for a, b, left, right in [
        (3,6,'R22','R13'), (3,5,'R22','R13'),
        (3,4,'R22','R12'), (3,3,'R21','R12'),
        (3,3,'R22','R11'), (3,2,'R21','R11')
    ]:
        Q = add(Q, term(a,b,left,right))
    S = mul(Q, powers['E'], bound)
    # F=y + y^2/(1-z) [ S-1+z ].
    correction = add(add(S, scale(one,-1)), monomial(1,0))
    return add(monomial(0,1), mul(monomial(0,2),mul(powers['D'],correction,bound),bound))


def main():
    checked = 0
    for m in range(12):
        for a in range(m+1):
            for b in range(m-a+1):
                for c in range(m-a-b+1):
                    d = m-a-b-c
                    assert brute_lyndon_count(a,b,c,d) == count_formula(a,b,c,d), (a,b,c,d)
                    checked += 1
    print('Individual-word direct Lyndon-substring checks:', checked)

    upto = 25
    gf = generating_coefficients(upto)
    compared = 0
    for m in range(upto+1):
        d = Counter()
        for a in range(m+1):
            for b in range(m-a+1):
                for c in range(m-a-b+1):
                    d[count_formula(a,b,c,m-a-b-c)] += 1
        coeffs = {ell: v for (r,ell),v in gf.items() if r == m and v}
        assert coeffs == d, (m, coeffs, d)
        assert sum(d.values()) == comb(m+3,3)
        compared += sum(d.values())
    print('Full bivariate coefficient checks: m=0..', upto, ', words=',compared)

    # Exact uniform-simplex sector first and second moments, independent of finite checks.
    cs = [
        (Fraction(1,3),1,3,0), (Fraction(1,3),1,3,0),
        (Fraction(1,3),1,2,0), (Fraction(1,3),Fraction(1,2),2,0),
        (Fraction(1,3),1,1,0), (Fraction(1,3),Fraction(1,2),1,0)
    ]
    e = sum((sum(c) / 4 for c in cs), Fraction(0))/6
    e2 = sum(((sum(c)**2 + sum(v*v for v in c))/20 for c in cs), Fraction(0))/6
    assert e == Fraction(19,24)
    assert e2 == Fraction(37,45)
    assert e2-e*e == Fraction(563,2880)
    print('Uniform-simplex moment identities: mean=19/24, second=37/45, variance=563/2880')
    print('All finite and exact-rational computational checks passed.')


if __name__ == '__main__':
    main()
