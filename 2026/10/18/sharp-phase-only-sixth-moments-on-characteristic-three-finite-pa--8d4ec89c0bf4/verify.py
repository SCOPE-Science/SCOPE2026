"""Exact finite checks for the characteristic-three parabola phase-only sixth moment.

Run: python verify.py. Standard library only; exhaustive finite tests supplement the proof.
"""
from collections import Counter, defaultdict
from itertools import product


def field(degree):
    q = 3 ** degree
    modulus = {1: None, 2: [1, 0, 1], 3: [2, 2, 0, 1]}[degree]
    def add(a, b):
        return sum((((a // (3 ** k)) + (b // (3 ** k))) % 3) * 3 ** k
                   for k in range(degree))
    def mul(a, b):
        c = [0] * (2 * degree - 1)
        for i in range(degree):
            for j in range(degree):
                c[i + j] = (c[i + j] + (a // (3 ** i) % 3) * (b // (3 ** j) % 3)) % 3
        if degree > 1:
            for k in range(len(c) - 1, degree - 1, -1):
                v = c[k]
                for j in range(degree):
                    c[k - degree + j] = (c[k - degree + j] - v * modulus[j]) % 3
        return sum(c[i] * (3 ** i) for i in range(degree))
    def power(a, k):
        r = 1
        while k:
            if k & 1:
                r = mul(r, a)
            a = mul(a, a)
            k >>= 1
        return r
    def tr(a):
        r, v = 0, a
        for _ in range(degree):
            r = add(r, v)
            v = power(v, 3)
        assert r < 3
        return r
    return q, add, mul, tr


def rank_mod3(rows, q):
    pivots = {}
    for row in rows:
        v = row[:]
        for k in sorted(pivots):
            if v[k]:
                fac = v[k]
                p = pivots[k]
                v = [(x - fac * y) % 3 for x, y in zip(v, p)]
        nz = next((i for i, x in enumerate(v) if x), None)
        if nz is not None:
            fac = 1 if v[nz] == 1 else 2
            pivots[nz] = [(x * fac) % 3 for x in v]
    return len(pivots)


def run(degree):
    q, add, mul, tr = field(degree)
    sq = [mul(x, x) for x in range(q)]
    fib = defaultdict(list)
    for a, b, c in product(range(q), repeat=3):
        key = (add(add(a, b), c), add(add(sq[a], sq[b]), sq[c]))
        fib[key].append((a, b, c))
    hist = Counter(len(v) for v in fib.values())
    assert hist == {q: q * (q - 1) + 1, 2 * q: (q - 1) // 2}
    energy = sum(len(v) ** 2 for v in fib.values())
    assert energy == q ** 4 + q ** 3 - q ** 2

    # All fiber-alignment constraints for ternary phases, modulo 3.
    def constraint_rows():
        for triples in fib.values():
            baseline = triples[0]
            for triple in triples[1:]:
                r = [0] * q
                for t in triple:
                    r[t] += 1
                for t in baseline:
                    r[t] -= 1
                yield [x % 3 for x in r]
    rank = rank_mod3(constraint_rows(), q)
    assert rank == q - (1 + 2 * degree), (q, rank)

    # Verify every quadratic additive-character phase for q <= 9, and
    # representative phases for q=27, without floating point arithmetic.
    params = list(product(range(q), repeat=2)) if q <= 9 else [(0, 0), (1, 0), (0, 1), (3, 6), (5, 13)]
    for alpha, beta in params:
        phases = [tr(add(mul(alpha, t), mul(beta, sq[t]))) for t in range(q)]
        for triples in fib.values():
            t = triples[0]
            target = sum(phases[x] for x in t) % 3
            assert all(sum(phases[x] for x in e) % 3 == target for e in triples)
    print('q=%d; fibers=%d; rank=%d; phase-nullity=%d; energy=%d; '
          'phase-tests=%d; all exact checks passed' %
          (q, len(fib), rank, q - rank, energy, len(params)))


if __name__ == '__main__':
    for d in (1, 2, 3):
        run(d)
    print('All exact finite checks passed; the theorem for all extension degrees is proved separately.')
