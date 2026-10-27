"""Finite direct-power checks for nilpotent restricted-range operators.

Run: python verify.py. Pure Python standard library, no external dependencies.
For q=4, arithmetic is in F_2[u]/(u^2+u+1).
"""
from itertools import product
from fractions import Fraction
from math import prod


def partitions(n, cap=None):
    if n == 0:
        yield ()
        return
    for d in range(min(n, n if cap is None else cap), 0, -1):
        for tail in partitions(n-d, d):
            yield (d,) + tail


def orbit_size(q, k, lam):
    conjugate = [sum(a >= j for a in lam) for j in range(1, lam[0]+1)]
    multiplicities = [lam.count(j) for j in set(lam)]
    centralizer = Fraction(q ** sum(a*a for a in conjugate), 1)
    for r in multiplicities:
        for i in range(1, r+1):
            centralizer *= Fraction(q**i-1, q**i)
    gl_order = prod(q**k-q**i for i in range(k))
    size = Fraction(gl_order, 1)/centralizer
    assert size.denominator == 1
    return size.numerator


def theoretical(q, k, c):
    counts = {}
    for lam in partitions(k):
        d, r = lam[0], lam.count(lam[0])
        n = orbit_size(q, k, lam)
        counts[d] = counts.get(d, 0)+n*q**((k-r)*c)
        counts[d+1] = counts.get(d+1, 0)+n*(q**(k*c)-q**((k-r)*c))
    return {t: v for t,v in counts.items() if v}


def operations(q):
    if q != 4:
        return (lambda a,b:(a+b)%q), (lambda a,b:(a*b)%q)
    def f4mul(a,b):
        out = 0
        for bit in range(2):
            if (b >> bit) & 1:
                out ^= a << bit
        if out & 8:
            out ^= 0b1110
        if out & 4:
            out ^= 0b111
        return out
    return lambda a,b:a ^ b, f4mul


def direct(q, k, c):
    n = k+c
    add, mul = operations(q)
    counts = {}
    for vals in product(range(q), repeat=k*n):
        rows = [list(vals[i*n:(i+1)*n]) for i in range(k)] + [[0]*n for _ in range(c)]
        def matmul(a,b):
            return [[reduce_add((mul(a[i][s], b[s][j]) for s in range(n)), add)
                     for j in range(n)] for i in range(n)]
        index, power = 1, rows
        while any(any(row) for row in power):
            index += 1
            if index > k+1:
                break
            power = matmul(power, rows)
        if not any(any(row) for row in power):
            counts[index] = counts.get(index, 0)+1
    return counts


def reduce_add(items, add):
    out = 0
    for x in items:
        out = add(out,x)
    return out


def main():
    cases = [(2,1,1),(2,2,1),(2,2,3),(2,3,2),
             (3,2,2),(4,2,1),(5,1,2)]
    total = 0
    for q,k,c in cases:
        prediction = theoretical(q,k,c)
        observation = direct(q,k,c)
        assert observation == prediction, (q,k,c,observation,prediction)
        assert sum(observation.values()) == q**(k*(k+c-1))
        total += q**(k*(k+c))
        print('OK', q,k,c, sorted(observation.items()))
    print('VERIFY_OK',len(cases),'field/truncation cases;',total,'direct matrices')


if __name__ == '__main__':
    main()
