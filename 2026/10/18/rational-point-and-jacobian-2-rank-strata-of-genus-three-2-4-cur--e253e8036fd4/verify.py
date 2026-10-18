"""Exact classification of smooth (2,4) divisors over F_2 on P1 x P1.

Only Python's standard library is needed. Coordinates are [U:V] and [S:T].
Bit i of a binary quartic is the coefficient of S^(4-i) T^i.
"""
from collections import Counter
from itertools import product
from pathlib import Path
import csv
import json

HERE = Path(__file__).resolve().parent


def mul(a, b):
    c = 0
    while b:
        if b & 1:
            c ^= a
        a <<= 1
        b >>= 1
    return c


def derivative(a):
    return sum(((a >> i) & 1) << (i - 1)
               for i in range(1, a.bit_length(), 2))


def remainder(a, b):
    while a and a.bit_length() >= b.bit_length():
        a ^= b << (a.bit_length() - b.bit_length())
    return a


def gcd(a, b):
    while b:
        a, b = b, remainder(a, b)
    return a


def reverse_quartic(a):
    return sum(((a >> i) & 1) << (4 - i) for i in range(5))


def D(a, b, c):
    term = mul(c, derivative(a)) ^ mul(a, derivative(c))
    return mul(term, term) ^ mul(mul(a, c), mul(derivative(b), derivative(b)))


def smooth(a, b, c):
    if b == 0:
        return False
    return (gcd(b, D(a, b, c)) == 1 and
            gcd(reverse_quartic(b), D(reverse_quartic(a),
                                      reverse_quartic(b),
                                      reverse_quartic(c))) == 1)


def val_at_rational_base(a, j):
    return (a & 1) if j == 0 else ((a >> 4) & 1) if j == 1 else a.bit_count() % 2


def rational_points(a, b, c):
    count = 0
    for j in range(3):
        aa, bb, cc = (val_at_rational_base(f, j) for f in (a, b, c))
        count += (aa == 0) + (cc == 0) + (aa ^ bb ^ cc == 0)
    return count


IRREDUCIBLES = ((2, 3), (7,), (11, 13), (19, 25, 31))


def factors(b):
    """Triples (irreducible polynomial, geometric degree, multiplicity)."""
    assert b
    f = b
    result = []
    for degree, ps in enumerate(IRREDUCIBLES, start=1):
        for p in ps:
            mult = 0
            while f and f.bit_length() >= p.bit_length() and gcd(f, p) == p:
                quotient = 0
                r = f
                while r and r.bit_length() >= p.bit_length():
                    shift = r.bit_length() - p.bit_length()
                    quotient ^= 1 << shift
                    r ^= p << shift
                assert r == 0
                f = quotient
                mult += 1
            if mult:
                result.append((p, degree, mult))
    assert f == 1
    infinity_mult = 4 - (b.bit_length() - 1)
    if infinity_mult:
        result.append((0, 1, infinity_mult))
    assert sum(degree * mult for _, degree, mult in result) == 4
    return result


def p_rank_from_branch(b):
    # Deuring--Shafarevich for a degree-two Artin--Schreier cover of P^1.
    return sum(degree for _, degree, _ in factors(b)) - 1


MATRICES = [(a, b, c, d) for a, b, c, d in product((0, 1), repeat=4)
            if (a * d) ^ (b * c)]
assert len(MATRICES) == 6


def polynomial_power(p, n):
    q = 1
    for _ in range(n):
        q = mul(q, p)
    return q


def base_transform(f, m):
    a, b, c, d = m
    p, q = a | (b << 1), c | (d << 1)
    return _base_transform(f, p, q)


def _base_transform(f, p, q):
    result = 0
    for i in range(5):
        if (f >> i) & 1:
            result ^= mul(polynomial_power(p, 4 - i), polynomial_power(q, i))
    return result


BASE_ACTIONS = [[base_transform(f, m) for f in range(32)] for m in MATRICES]


def transform(triple, base_action_index, fiber_matrix):
    a, b, c = triple
    A, B, C = (BASE_ACTIONS[base_action_index][f] for f in (a, b, c))
    p, q, r, s = fiber_matrix
    return ((A if p else 0) ^ (B if p * r else 0) ^ (C if r else 0),
            B,
            (A if q else 0) ^ (B if q * s else 0) ^ (C if s else 0))


def pack(t):
    return t[0] | (t[1] << 5) | (t[2] << 10)


def unpack(i):
    return (i & 31, (i >> 5) & 31, (i >> 10) & 31)


def classify():
    remaining = set(range(1, 1 << 15))
    representatives = []
    while remaining:
        representative = min(remaining)
        triple = unpack(representative)
        orbit = {pack(transform(triple, bi, fm))
                 for bi in range(6) for fm in MATRICES}
        assert orbit <= remaining
        remaining.difference_update(orbit)
        if not smooth(*triple):
            continue
        assert all(smooth(*unpack(other)) for other in orbit)
        representatives.append({'a': triple[0], 'b': triple[1], 'c': triple[2],
                                'orbit': len(orbit),
                                'N': rational_points(*triple),
                                'p_rank': p_rank_from_branch(triple[1])})
    return representatives


def main():
    reps = classify()
    count = Counter((r['N'], r['p_rank']) for r in reps for _ in range(r['orbit']))
    classes = Counter((r['N'], r['p_rank']) for r in reps)
    total = sum(r['orbit'] for r in reps)
    assert total == 9216 and len(reps) == 294
    assert count[(6, 1)] == 282 and count[(6, 3)] == 801
    assert classes[(6, 1)] == 11 and classes[(6, 3)] == 26
    # Full coefficient-space test, independent of orbit weighting.
    all_counts = Counter()
    for a, b, c in product(range(32), repeat=3):
        if smooth(a, b, c):
            all_counts[(rational_points(a, b, c), p_rank_from_branch(b))] += 1
    assert all_counts == count
    with (HERE / 'data' / 'joint_table.json').open(encoding='utf-8') as f:
        expected = json.load(f)
    got = [{'N': n, 'p_rank': pr, 'equations': count[n, pr], 'orbits': classes[n, pr]}
           for n in range(7) for pr in range(4)]
    assert got == expected
    with (HERE / 'data' / 'orbit_representatives.csv').open(newline='', encoding='utf-8') as f:
        expected_reps = [{k: int(v) for k, v in row.items()} for row in csv.DictReader(f)]
    assert reps == expected_reps
    print('PASS: 32767 nonzero equations, 9216 smooth, 294 embedding orbits.')
    print('PASS: full independent coefficient and orbit distributions agree.')
    print('PASS: 1083 six-point curves, 37 orbits, p-rank 1/3 split 282/801.')


if __name__ == '__main__':
    main()
