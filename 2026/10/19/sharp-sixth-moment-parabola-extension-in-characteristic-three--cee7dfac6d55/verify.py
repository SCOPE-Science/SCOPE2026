#!/usr/bin/env python3
"""Exact finite-field incidence checks and illustrative sixth-moment tests.
The all-field theorem is proved separately by a nonnegative-inequality argument.
This script uses only the Python standard library.
"""
from __future__ import annotations
import cmath
import random
from fractions import Fraction


def finite_field(power: int):
    """F_{3^power} in a fixed polynomial basis, powers 1,2,3."""
    mod = {1: (0, 1), 2: (1, 0, 1), 3: (2, 2, 0, 1)}[power]
    q = 3 ** power
    def dig(v):
        return [(v // (3 ** i)) % 3 for i in range(power)]
    def fromdig(v):
        return sum((x % 3) * 3 ** i for i, x in enumerate(v))
    digits = [dig(t) for t in range(q)]
    add = [[fromdig([(digits[a][i] + digits[b][i]) % 3 for i in range(power)]) for b in range(q)] for a in range(q)]
    minus = [fromdig([-v for v in digits[a]]) for a in range(q)]
    def product(a, b):
        c = [0] * (2 * power - 1)
        for i, ai in enumerate(digits[a]):
            for j, bj in enumerate(digits[b]):
                c[i + j] = (c[i + j] + ai * bj) % 3
        for k in range(len(c) - 1, power - 1, -1):
            val = c[k]
            for j in range(power):
                c[k - power + j] = (c[k - power + j] - val * mod[j]) % 3
        return fromdig(c[:power])
    mul = [[product(a,b) for b in range(q)] for a in range(q)]
    return q, add, minus, mul


def counts_and_moments(power: int):
    q, add, neg, mul = finite_field(power)
    sq = [mul[t][t] for t in range(q)]
    fibers = [[] for _ in range(q*q)]
    for a in range(q):
        for b in range(q):
            ab = add[a][b]
            w_ab = add[sq[a]][sq[b]]
            for c in range(q):
                s = add[ab][c]
                w = add[w_ab][sq[c]]
                fibers[s*q+w].append((a,b,c))
    freq = [len(fiber) for fiber in fibers]
    assert sum(freq) == q**3
    assert all(freq[s*q+w] == q for s in range(1,q) for w in range(q))
    assert freq[0] == q
    assert sorted(freq[w] for w in range(1,q)) == ([0] * ((q-1)//2) + [2*q] * ((q-1)//2))
    T1 = sum(v*v for v in freq)
    assert T1 == q**4 + q**3 - q**2
    print(f'F_{q}: {q**3} triples, all {q*q} fibers, constant moment {T1}; exact target {Fraction(q*q+q-1,q*q)}')

    def moment(f):
        return sum(abs(sum(f[a]*f[b]*f[c] for a,b,c in fiber))**2 for fiber in fibers)
    def bound_chain(f):
        F = sum(abs(z)**2 for z in f)
        if not F: return
        T = moment(f)
        c = []
        sd = []
        for d in range(q):
            terms = [f[add[a][neg[d]]] * f[a] * f[add[a][d]] for a in range(q)]
            c.append(sum(terms))
            sd.append(sum(abs(z)**2 for z in terms))
        assert abs(sum(sd) - sum(abs(f[a]*f[b]*f[c0])**2 for fiber in fibers[:q] for a,b,c0 in fiber)) < 1e-7 * max(1,F**3)
        lhs_1 = q * (F**3 - sum(sd)) + abs(c[0])**2 + 2*sum(abs(z)**2 for z in c[1:])
        lhs_2 = q * F**3 + sum(abs(z)**2 for z in c[1:])
        lhs_3 = q * F**3 + F*(F**2 - sum(abs(z)**4 for z in f))
        lhs_4 = (q+1-1/q) * F**3
        eps = 2e-7 * max(1, lhs_4)
        assert T <= lhs_1 + eps, (T,lhs_1)
        assert lhs_1 <= lhs_2 + eps, (lhs_1,lhs_2)
        assert lhs_2 <= lhs_3 + eps, (lhs_2,lhs_3)
        assert lhs_3 <= lhs_4 + eps, (lhs_3,lhs_4)
    rng = random.Random(3_000+q)
    for i in range(60):
        f = [complex(rng.randrange(-2,3),rng.randrange(-2,3)) for _ in range(q)]
        bound_chain(f)
    bound_chain([1+0j]*q)
    # An additive quadratic phase character supplies a second equality witness.
    # For all t, Tr(t^2) is computed by Frobenius and the integer-valued
    # constant coefficient in the polynomial basis.
    def trace(a):
        cur=a; acc=0
        for _ in range(power):
            acc=add[acc][cur]
            cur=mul[mul[cur][cur]][cur]
        assert all(v==0 for v in ([acc//(3**i)%3 for i in range(1,power)]))
        return acc % 3
    omega=cmath.exp(2j*cmath.pi/3)
    f=[omega**trace(sq[t]) for t in range(q)]
    bound_chain(f)
    ratio=moment(f)/(q*(sum(abs(z)**2 for z in f)**3))
    assert abs(ratio - (1+1/q-1/q**2)) < 1e-9
    print(f'F_{q}: 60 complex inputs and two equality witnesses passed all four inequality steps')

if __name__ == '__main__':
    for p in (1,2,3): counts_and_moments(p)
    print('All tests passed. Finite tests are corroboration; the proof covers every power of three.')
