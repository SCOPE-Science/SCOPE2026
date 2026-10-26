"""Exact finite arithmetic checks for Bernoulli Fourier-zero census.

Run with Python 3.10+; no third-party dependencies. Only finite examples
are checked. Universal assertions are established in the accompanying proof.
"""
from collections import Counter
from fractions import Fraction
from math import isqrt


def rational_zeros(p, q, X):
    assert 0 < p < q
    result = Counter()
    j = 0
    while Fraction(q, p) ** j <= X:
        scale = Fraction(q, p) ** j
        max_u = X * scale.denominator // scale.numerator
        for u in range(1, max_u + 1, 2):
            result[scale * u] += 1
        j += 1
    return result


def predicted_for_rational(p, q, X):
    lam = p / q
    if p % 2 and q % 2:
        D = (q - 1) / (2 * q * (1 - lam))
        return {m: D * (1 - 1 / q) / q ** (m - 1) * X
                for m in range(1, 6)}
    return {1: X / (2 * (1 - lam))}


def sqrt_third_zeros(X):
    # lambda = 1/sqrt(3). Even and odd scaling chains never overlap.
    out = Counter()
    j = 0
    while 3 ** j <= X ** 2:
        r = j % 2
        z = 3 ** (j // 2)
        if not r:
            mx = X // z
        else:
            mx = isqrt(X * X // (3 * z * z))
        for u in range(1, mx + 1, 2):
            out[(r, z * u)] += 1
        j += 1
    return out




def quadratic_odd_power_zeros(a, b, X):
    """lambda=sqrt(a/b); exact frequencies as parity + rational coefficient."""
    assert a % 2 == b % 2 == 1 and a < b
    out = Counter()
    j = 0
    while True:
        r, h = j % 2, j // 2
        base = Fraction(b, a) ** h
        sq_scale = base * base * (Fraction(b, a) if r else 1)
        if sq_scale > X * X:
            # Subsequent levels are larger, so no more zero factors up to X.
            break
        lim_sq = Fraction(X * X, 1) / sq_scale
        mx = isqrt(lim_sq.numerator // lim_sq.denominator)
        for u in range(1, mx + 1, 2):
            out[(r, base * u)] += 1
        j += 1
    return out

def check():
    X = 50000
    for p, q in ((1, 3), (3, 5), (3, 7), (2, 5), (3, 8), (1, 4)):
        ct = rational_zeros(p, q, X)
        dist = Counter(ct.values())
        model = predicted_for_rational(p, q, X)
        assert abs(len(ct) - ((q-1)/(2*q*(1-p/q))*X)) < 15 if p % 2 and q % 2 else abs(len(ct) - model[1]) < 15
        if p % 2 and q % 2:
            for m in range(1, 5):
                assert abs(dist[m] - model[m]) < 15, (p, q, m, dist[m], model[m])
            for m in range(1, 6):
                special = Fraction(q ** (m - 1), 1)
                assert ct[special] == m
                assert all(x >= special for x, mult in ct.items() if mult >= m)
        else:
            assert max(ct.values()) == 1
        print(f'rational lambda={p}/{q}, distinct={len(ct)}, '
              f'multiplicity_profile={dict(sorted(dist.items()))}, '
              f'model={[round(model[m], 3) for m in sorted(model)]}')
    ct = sqrt_third_zeros(X)
    dist = Counter(ct.values())
    lam = 1 / (3 ** .5)
    d1 = (3 - 1) / (2 * 3 * (1 - lam)) * (1 - 1 / 3) * X
    assert abs(dist[1] - d1) < 15
    for m in range(1, 6):
        assert ct[(0, 3 ** (m - 1))] == m
        assert all(key[1] >= 3 ** (m - 1) or key[0] == 1 and key[1] * 3 ** .5 >= 3 ** (m - 1)
                   for key, mult in ct.items() if mult >= m)
    print(f'algebraic lambda=1/sqrt(3), distinct={len(ct)}, '
          f'multiplicity_profile={dict(sorted(dist.items()))}, '
          f'predicted_simple_count={d1:.3f}')
    for a,b in ((1,3),(3,5)):
        sample = quadratic_odd_power_zeros(a,b,X)
        hist=Counter(sample.values())
        lam=(a/b)**0.5
        for m in range(1,5):
            pred=X*(b-1)**2/(2*b**(m+1)*(1-lam))
            assert abs(hist[m]-pred)<15,(a,b,m,hist[m],pred)
            assert sample[(0,Fraction(b**(m-1),1))]==m
        print(f'algebraic lambda=sqrt({a}/{b}), order counts={dict(sorted(hist.items()))}')
    print('All finite exact-arithmetic census checks passed.')

if __name__ == '__main__':
    check()
