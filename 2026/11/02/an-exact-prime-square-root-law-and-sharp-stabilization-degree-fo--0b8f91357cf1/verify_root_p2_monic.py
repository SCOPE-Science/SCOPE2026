"""Exact checks for the prime-square monic polynomial root-count law.

Pure Python 3 standard library. Brute force is limited to explicitly listed
small rings; the universal result is proved separately, not inferred here.
"""
from collections import Counter
from fractions import Fraction
from itertools import product


def multiply(a, b):
    out = {}
    for i, x in a.items():
        for j, y in b.items():
            out[i + j] = out.get(i + j, Fraction()) + x * y
    return {k: v for k, v in out.items() if v}


def predicted(p, d):
    # Coefficients in the degree variable, each a polynomial in the PGF variable.
    b = {0: Fraction(1) - Fraction(1, p),
         1: Fraction(-1), p: Fraction(1, p)}
    if p == 1:
        raise ValueError("p must be prime")
    local = [{0: Fraction(1)}, {0: Fraction(-1), 1: Fraction(1)}, b]
    current = [{} for _ in range(d + 1)]
    current[0] = {0: Fraction(1)}
    for _ in range(p):
        following = [{} for _ in range(d + 1)]
        for i in range(d + 1):
            for j in range(min(2, d - i) + 1):
                for k, v in multiply(current[i], local[j]).items():
                    target = following[i + j]
                    target[k] = target.get(k, Fraction()) + v
        current = following
    answer = {}
    for j in range(d + 1):
        for k, v in current[j].items():
            answer[k] = answer.get(k, Fraction()) + v / p**j
    return {k: v for k, v in answer.items() if v}


def exhaustive(p, d):
    mod = p * p
    counts = Counter()
    for coefficients in product(range(mod), repeat=d):
        roots = 0
        for x in range(mod):
            value = 1
            for a in reversed(coefficients):
                value = (value*x + a) % mod
            roots += value == 0
        counts[roots] += 1
    return {k: Fraction(v, mod**d) for k, v in counts.items()}


def conditional(p, d):
    # Enumerate reductions over F_p and, independently, each repeated-root lift.
    outcome = {}
    for coefficients in product(range(p), repeat=d):
        simple = repeated = 0
        for x in range(p):
            value = 1
            derivative = 0
            for a in reversed(coefficients):
                derivative = (derivative*x + value) % p
                value = (value*x + a) % p
            if value == 0:
                if derivative:
                    simple += 1
                else:
                    repeated += 1
        dist = {simple: Fraction(1)}
        for _ in range(repeated):
            nxt = {}
            for k, prob in dist.items():
                nxt[k] = nxt.get(k, Fraction()) + prob*(1-Fraction(1,p))
                nxt[k+p] = nxt.get(k+p, Fraction()) + prob*Fraction(1,p)
            dist = nxt
        for k, prob in dist.items():
            outcome[k] = outcome.get(k, Fraction()) + prob / p**d
    return {k: v for k, v in outcome.items() if v}


def main():
    brute_cases = [
        (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6),
        (3, 1), (3, 2), (3, 3), (3, 4), (3, 5),
        (5, 2), (5, 3), (7, 2), (11, 2), (13, 2),
    ]
    for p, d in brute_cases:
        expected = predicted(p, d)
        observed = exhaustive(p, d)
        assert expected == observed, (p, d, expected, observed)
    conditional_cases = [(2, 7), (2, 8), (3, 5), (3, 6), (5, 4)]
    for p, d in conditional_cases:
        assert predicted(p, d) == conditional(p, d), (p, d)
    for p in (2, 3, 5, 7, 11, 13):
        left = predicted(p, 2*p - 1)
        at = predicted(p, 2*p)
        right = predicted(p, 2*p + 1)
        assert left != at and at == right, (p, "stabilization")
        for d in (1, 2, 3, 2*p, 2*p + 1):
            v = predicted(p, d)
            assert sum(v.values()) == 1, (p, d)
            mean = sum(k*prob for k, prob in v.items())
            assert mean == 1, (p, d, mean)
            if d >= 2:
                variance = sum(k*k*prob for k, prob in v.items()) - 1
                assert variance == 2-Fraction(2,p), (p, d, variance)
    print("VERIFY_OK exhaustive_cases=%d conditional_cases=%d stability_primes=6" % (
        len(brute_cases), len(conditional_cases)))


if __name__ == "__main__":
    main()
