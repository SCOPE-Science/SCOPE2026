#!/usr/bin/env python3
"""Exact modular witnesses for maximal algebraic-degree Nash facility optima.

Python 3 standard library only. Finite verification complements, and does not
replace, the all-size theorem proved in RESULT.md.
"""
from fractions import Fraction
from math import isqrt


def prime(p):
    if p < 2:
        return False
    for d in range(2, isqrt(p) + 1):
        if p % d == 0:
            return False
    return True


def elementary_next_last(a):
    # e_{n-1}(a_1,...,a_n), computed over exact integers.
    v = [1] + [0] * len(a)
    for z in a:
        for k in range(len(a), 0, -1):
            v[k] += z * v[k-1]
    return v[-2]


def polynomial_coefficients(t, Q):
    # Ascending coefficients of F(Y)=product(QY-t_i).
    c = [1]
    for z in t:
        nxt = [0] * (len(c) + 1)
        for k, a in enumerate(c):
            nxt[k] -= z * a
            nxt[k + 1] += Q * a
        c = nxt
    return c


def sign_at(t, Q, y):
    # Exact logarithmic derivative at the central gap.
    j = len(t) // 2
    return sum((-1 if i < j else 1) / abs(y - Fraction(z, Q))
               for i, z in enumerate(t))


def witness(n):
    p = n + 1
    while not (prime(p) and (p - 1) % n == 0):
        p += 1
    roots = [u for u in range(1, p) if pow(u, n, p) == 1]
    assert len(roots) == n
    j = n // 2
    # Fix distinct rational targets in the two allowed bands.
    targets = ([Fraction(101, 100) + Fraction(i+1, 100*(j+1)) for i in range(j)]
               + [Fraction(-4, 100) + Fraction(i+1, 100*((n-j)+1))
                  for i in range(n-j)])
    Q = 1 + 1000000 * p * p
    residues = roots[:]
    # Make e_(n-1) p-divisible but not p^2-divisible.
    assert elementary_next_last(residues) % p == 0
    for k in range(p):
        test = residues[:]
        test[0] += p * k
        if elementary_next_last(test) % (p*p):
            residues = test
            break
    else:
        raise AssertionError('No lift')
    t = []
    for r, a in zip(targets, residues):
        ideal = r * Q
        m = round((ideal - a) / (p * p))
        t.append(a + m * p * p)
    assert all(t[i] % p == roots[i] for i in range(n))
    assert elementary_next_last(t) % p == 0
    assert elementary_next_last(t) % (p*p) != 0
    assert all(Fraction(1,1) < Fraction(t[i],Q) < Fraction(21,20)
               for i in range(j))
    assert all(Fraction(-1,20) < Fraction(t[i],Q) < 0
               for i in range(j,n))
    assert len(set(t)) == n
    assert sign_at(t,Q,Fraction(1,4)) > 0
    assert sign_at(t,Q,Fraction(3,4)) < 0
    c = polynomial_coefficients(t,Q)
    dc = [k*c[k] for k in range(1,len(c))]
    assert len(dc) == n
    assert dc[-1] % p != 0
    assert all(z % p == 0 for z in dc[:-1])
    assert dc[0] % p == 0 and dc[0] % (p*p) != 0
    return p, Q, t


def run():
    count = 0
    for n in range(3,21):
        p, Q, t = witness(n)
        count += 1
        print(f'n={n}, prime={p}, Q={Q}: Eisenstein, intervals, signs PASS')
    # Separate small exact witness stated in RESULT.md.
    Q = 25001
    t = [25506, 25502, -496, -497]
    c = polynomial_coefficients(t, Q)
    dc = [k*c[k] for k in range(1, len(c))]
    assert list(reversed(dc)) == [
        1562750015000400004, -2344734470628525045,
        750121981158099160, 15833802072249820]
    assert all(z % 5 == 0 for z in dc[:-1]) and dc[0] % 25 == 20
    assert sign_at(t, Q, Fraction(1,4)) > 0
    assert sign_at(t, Q, Fraction(3,4)) < 0
    count += 1
    print(f'PASS: {count} independent exact finite witnesses; infinite theorem requires proof')


if __name__ == '__main__':
    run()
