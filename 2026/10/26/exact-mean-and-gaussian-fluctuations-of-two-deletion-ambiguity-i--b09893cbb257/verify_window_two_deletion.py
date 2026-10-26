#!/usr/bin/env python3
"""Self-contained checks for overlapping-window exact-two-deletion output counts."""
from itertools import product, combinations
from fractions import Fraction
from math import comb


def windows(x, ell):
    return tuple(x[i:i+ell] for i in range(len(x)-ell+1))


def direct_two_deletion(y):
    m = len(y)
    return len({tuple(y[k] for k in range(m) if k != i and k != j)
                for i, j in combinations(range(m), 2)})


def local_formula(y):
    m = len(y)
    assert m >= 2
    r = 1 + sum(y[i] != y[i+1] for i in range(m-1))
    h = sum(i == 0 or y[i-1] != y[i]
            for i in range(m-1) if y[i] == y[i+1])
    t = sum(y[i] == y[i+2] and y[i] != y[i+1]
            for i in range(m-2))
    return comb(r, 2) + h - t


def exact_mean(q, ell, n):
    m = n-ell+1
    assert m >= 2
    return (Fraction(comb(m,2),1)
            - Fraction(m*(m-2), q**ell)
            + sum((Fraction(m-1-d, q**(ell+min(d,ell)))
                   for d in range(1,m-1)), Fraction(0)))


def sigma2(q, ell):
    p = Fraction(1, q**ell)
    v = p*(1-p) + 2*sum((Fraction(1,q**(ell+d))-p*p
                        for d in range(1,ell)),Fraction())
    return (1-p)**2*v


def run_checks():
    checked = 0
    means = 0
    checks = []
    for q in (2,3,4):
        for ell in (2,3,4):
            # Limit 4-letter exhaustive inputs to 8 sites; binary 9, ternary 8.
            max_n = {2:9, 3:8, 4:8}[q]
            for n in range(ell+1, max_n+1):
                cnt = 0
                total = 0
                # Fully inspect every source word (not sampled).
                for x in product(range(q), repeat=n):
                    y = windows(x, ell)
                    a = direct_two_deletion(y)
                    b = local_formula(y)
                    assert a == b, (q,ell,n,x,a,b)
                    total += a
                    cnt += 1
                actual = Fraction(total,cnt)
                predicted = exact_mean(q,ell,n)
                assert actual == predicted,(q,ell,n,actual,predicted)
                checked += cnt
                means += 1
                checks.append((q,ell,n,cnt))
    for q in (2,3,4,5):
        for ell in (2,3,4,5):
            s = sigma2(q,ell)
            assert s>0
    assert sigma2(4,2) == Fraction(4725,65536)
    assert sigma2(2,2) == Fraction(45,256)
    print(f'word_count={checked}')
    print(f'full_parameter_exhaustions={means}')
    print('first=' + repr(checks[0]))
    print('last=' + repr(checks[-1]))
    print('sigma_squared_q4_ell2=' + str(sigma2(4,2)))
    print('sigma_squared_q2_ell2=' + str(sigma2(2,2)))
    print('VERIFY_OK')


if __name__ == '__main__':
    run_checks()
