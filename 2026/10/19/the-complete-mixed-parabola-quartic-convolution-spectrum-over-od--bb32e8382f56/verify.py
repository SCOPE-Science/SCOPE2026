#!/usr/bin/env python3
"""Exact prime and quadratic-extension checks of an additive-convolution spectrum."""
from collections import Counter
from math import comb


class Field:
    def __init__(self, p, degree=1):
        self.p, self.degree = p, degree
        self.q = p ** degree
        self.d = None
        if degree == 2:
            squares = {a*a % p for a in range(p)}
            self.d = next(a for a in range(2, p) if a not in squares)
        assert degree in (1, 2)

    def add(self, x, y):
        p = self.p
        return (x + y) % p if self.degree == 1 else (x % p + y % p) % p + p * ((x // p + y // p) % p)

    def neg(self, x):
        p = self.p
        return (-x) % p if self.degree == 1 else (-x % p) + p * (-(x // p) % p)

    def sub(self, x, y):
        return self.add(x, self.neg(y))

    def mul(self, x, y):
        p = self.p
        if self.degree == 1:
            return x * y % p
        a, b = x % p, x // p
        c, e = y % p, y // p
        return (a*c + self.d*b*e) % p + p * ((a*e+b*c) % p)

    def power(self, x, n):
        out = 1
        while n:
            if n & 1:
                out = self.mul(out, x)
            x = self.mul(x, x)
            n //= 2
        return out

    def character(self, x):
        if x == 0:
            return 0
        y = self.power(x, (self.q - 1)//2)
        assert y in (1, self.neg(1))
        return 1 if y == 1 else -1

    def integer(self, x):
        return x % self.p


def predicted(field):
    q = field.q
    alpha = field.character(field.integer(2))
    beta = field.character(field.integer(-2))
    gamma = field.character(field.integer(-6))
    numerators = [
        (3*q*q-2*q+1-alpha*q-beta, 8),
        (2*q*q+3*q-5+2*alpha*q-2*gamma, 6),
        (q*q-2*q+7-alpha*q+3*beta+4*gamma, 4),
        (q-3-2*beta-2*gamma, 2),
        (q*q-6*q+11+alpha*q+9*beta+8*gamma, 24),
    ]
    for numerator, denominator in numerators:
        assert numerator % denominator == 0
    return tuple(numerator//denominator for numerator, denominator in numerators)


def measured(field):
    q = field.q
    fadd, fsub, fmul = field.add, field.sub, field.mul
    us = list(range(q))
    quartic = []
    for u in us:
        square = fmul(u,u)
        quartic.append(fmul(square,square))
    hist = Counter()
    for s in us:
        target_count = [0]*q
        for u in us:
            t = fsub(s,u)
            target_count[fadd(quartic[u],fmul(t,t))] += 1
        hist.update(target_count)
    return tuple(hist[j] for j in range(5))



def check_quadratic_sieve(field):
    """Check the quadratic fiber counts underlying the distinctness sieve."""
    q = field.q
    add, mul = field.add, field.mul
    minus_one = field.integer(-1)
    count_ternary = count_pair = count_equal = 0
    elems = range(q)
    for u in elems:
        u2 = mul(u,u)
        six_u2 = 0
        for _ in range(6):
            six_u2 = add(six_u2,u2)
        count_equal += (six_u2 == minus_one)
        for v in elems:
            v2 = mul(v,v)
            q_pair = add(add(add(add(u2,u2),u2),v2),add(mul(u,v),mul(u,v)))
            count_pair += (q_pair == minus_one)
            for w in elems:
                w2 = mul(w,w)
                Q = add(add(add(u2,v2),w2),add(add(mul(u,v),mul(u,w)),mul(v,w)))
                count_ternary += (Q == minus_one)
    alpha = field.character(field.integer(2))
    beta = field.character(field.integer(-2))
    gamma = field.character(field.integer(-6))
    assert count_ternary == q*q + alpha*q
    assert count_pair == q-beta
    assert count_equal == 1+gamma
    return count_ternary, count_pair, count_equal

def main():
    samples = [(p,1) for p in (5,7,11,13,17,19,23,29,31,37,41,43,47)]
    samples += [(p,2) for p in (5,7,11)]
    for p, degree in samples:
        F = Field(p, degree)
        theory, data = predicted(F), measured(F)
        assert data == theory, (F.q, theory, data)
        q = F.q
        assert sum(theory) == q*q
        assert sum(j*theory[j] for j in range(5)) == q*q
        assert sum(comb(j,2)*theory[j] for j in range(5)) == q*(q-1)//2
        assert sum(j*j*theory[j] for j in range(5)) == 2*q*q-q
        if q <= 25:
            sieve = check_quadratic_sieve(F)
            print(f'GF({q}) underlying quadratic sieve counts: {sieve} PASS')
        print(f'GF({q}) p={p}, degree={degree}: {data} PASS')
    print(f'ALL PASS: {len(samples)} fields, including three quadratic extensions')


if __name__ == '__main__':
    main()
