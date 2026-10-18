"""Exact finite checks for the short-chord/crossing transfer identity.

No scientific claim beyond the finite tested sizes is established by enumeration.
The accompanying proof establishes the identity for all sizes.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import factorial


def matchings(vertices):
    if not vertices:
        yield ()
        return
    a = vertices[0]
    for i, b in enumerate(vertices[1:], 1):
        remaining = vertices[1:i] + vertices[i+1:]
        for tail in matchings(remaining):
            yield ((a, b),) + tail


def count_statistics(matching, n):
    simple = sum(b == a + 1 or (a == 0 and b == 2*n-1)
                 for a, b in matching)
    crossings = sum(a < c < b < d or c < a < d < b
                    for (a, b), (c, d) in combinations(matching, 2))
    return simple, crossings


def falling(x, k):
    p = 1
    for j in range(k):
        p *= x-j
    return p


def alpha(n, k):
    return Fraction(2*n, 2*n-k) * Fraction(2**k * falling(n,k), falling(2*n,k))


def double_factorial_odd(n):
    p = 1
    for q in range(1, 2*n, 2):
        p *= q
    return p


def check():
    hist = {0: Counter({(0,0):1})}
    checks = 0
    for n in range(1,8):
        h = Counter()
        for m in matchings(tuple(range(2*n))):
            if n == 1:
                h[(1,0)] += 1
            else:
                h[count_statistics(m,n)] += 1
        hist[n] = h
        total = sum(h.values())
        assert total == double_factorial_odd(n)
        checks += 1
        if n == 1:
            continue
        for k in range(n+1):
            lhs = Counter()
            for (s,x),v in h.items():
                lhs[x] += v*falling(s,k)
            rhs_distribution = Counter()
            for (s,x),v in hist[n-k].items():
                rhs_distribution[x] += v
            target_factor = Fraction(total, sum(hist[n-k].values()))*alpha(n,k)
            for x in set(lhs)|set(rhs_distribution):
                assert lhs[x] == target_factor*rhs_distribution[x], (n,k,x)
                checks += 1
            assert alpha(n,k) <= 2
            checks += 1
        es = Fraction(sum(s*v for (s,x),v in h.items()),total)
        ex = Fraction(sum(x*v for (s,x),v in h.items()),total)
        ess = Fraction(sum(s*s*v for (s,x),v in h.items()),total)
        esx = Fraction(sum(s*x*v for (s,x),v in h.items()),total)
        exx = Fraction(sum(x*x*v for (s,x),v in h.items()),total)
        assert es == Fraction(2*n,2*n-1)
        assert ex == Fraction(n*(n-1),6)
        assert ess-es*es == Fraction(4*n*(n-1),(2*n-1)**2)
        assert esx-es*ex == -Fraction(2*n*(n-1),3*(2*n-1))
        assert exx-ex*ex == Fraction(n*(n-1)*(n+3),45)
        assert (esx-es*ex)**2 == Fraction(5,n+3) * (ess-es*es) * (exx-ex*ex)
        checks += 6
        print(f'n={n}: {total} matchings, {len(h)} joint support points, verified all k=0..{n}')
    print(f'PASS: {checks} exact-rational/equality assertions; all perfect matchings through n=7 checked.')

if __name__ == '__main__':
    check()
