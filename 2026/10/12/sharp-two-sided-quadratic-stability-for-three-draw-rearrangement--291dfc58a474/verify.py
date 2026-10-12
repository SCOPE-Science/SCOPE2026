"""Exact rational sanity checks for a sharp three-draw permutation diversity theorem.

Run: python verify.py   (Python standard library only).
All universal claims rest on the accompanying algebraic proof.
"""
from fractions import Fraction as Q
from itertools import combinations, product
from math import factorial


def compositions(n, k):
    if k == 1:
        yield (n,)
        return
    for a in range(n + 1):
        for rest in compositions(n - a, k - 1):
            yield (a,) + rest


def score(p):
    sq = sum(x * x for x in p)
    cube = sum(x * x * x for x in p)
    return 6 - 9 * sq + 4 * cube


def schur(a, b, c):
    return a * (a - b) * (a - c) + b * (b - a) * (b - c) + c * (c - a) * (c - b)


def remainders(p):
    q = len(p)
    u = Q(1, q)
    variance = sum((x - u) ** 2 for x in p)
    expected_uniform = Q(6) - Q(9, q) + Q(4, q * q)
    deficit = expected_uniform - score(p)
    lower = Q(5) - Q(4, q)
    upper = Q(9) - Q(12, q) + Q(4 * (q - 2), q * (q - 1))
    low_certificate = Q(4, q) * sum(
        (p[i] - p[j]) ** 2 * (1 - p[i] - p[j]) for i, j in combinations(range(q), 2)
    )
    high_certificate = Q(8, q * (q - 1)) * sum(
        schur(p[i], p[j], p[k]) for i, j, k in combinations(range(q), 3)
    )
    assert deficit - lower * variance == low_certificate, (q, p, 'LOW IDENTITY')
    assert upper * variance - deficit == high_certificate, (q, p, 'HIGH IDENTITY')
    assert low_certificate >= 0, (q, p, 'LOW SIGN')
    assert high_certificate >= 0, (q, p, 'HIGH SIGN')
    return variance, deficit, lower, upper, low_certificate, high_certificate


if __name__ == '__main__':
    total = 0
    for q in range(2, 9):
        for denominator in range(1, 8):
            for counts in compositions(denominator, q):
                p = tuple(Q(z, denominator) for z in counts)
                remainders(p)
                total += 1
        uniform = (Q(1, q),) * q
        v, d, lo, hi, lr, hr = remainders(uniform)
        assert v == d == lr == hr == 0
        extreme = (Q(1),) + (Q(0),) * (q-1)
        v, d, lo, hi, lr, hr = remainders(extreme)
        assert v > 0 and d == lo * v and lr == 0
        omit_one = (Q(0),) + (Q(1, q-1),) * (q-1)
        v, d, lo, hi, lr, hr = remainders(omit_one)
        assert v > 0 and d == hi * v and hr == 0
        if q >= 3:
            assert lo < hi
        else:
            assert lo == hi
    # Independent direct enumeration of all q^3 ordered outcomes, a different
    # calculation from the power-sum identity used in the proof.
    brute = 0
    for q in range(2, 7):
        for counts in compositions(4, q):
            p = tuple(Q(z,4) for z in counts)
            total_expectation = Q(0)
            for word in product(range(q), repeat=3):
                multiplicities = [word.count(k) for k in range(q)]
                m = factorial(3)
                for r in multiplicities:
                    m //= factorial(r) if r else 1
                # For d=3, denominators divide 3!, but using sequential // after
                # each factorial does preserve exactness for the possible patterns.
                mass = p[word[0]] * p[word[1]] * p[word[2]]
                total_expectation += m * mass
            assert total_expectation == score(p), (q, counts)
            brute += 1
    print(f'VERIFY_OK exact_simplex_cases={total} independent_expectation_cases={brute}')
