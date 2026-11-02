"""Direct finite checks for binary periodic two-run cyclic k-mer reconstruction.
Run with Python 3.9+; no nonstandard dependencies.
"""
from collections import defaultdict
from itertools import product
from math import comb, gcd
from random import Random


def rotations(s):
    return (s[i:] + s[:i] for i in range(len(s)))


def canonical(s):
    return min(rotations(s))


def spectrum(s, k):
    # Literal overlapping circular windows, retaining multiplicity.
    n = len(s)
    extended = s + s[:k - 1]
    return tuple(sorted(extended[i:i + k] for i in range(n)))


def totient(d):
    return sum(gcd(i, d) == 1 for i in range(1, d + 1))


def fiber_formula(a, b, t, k):
    A, B = max(a - k + 1, 0), max(b - k + 1, 0)
    numerator = 0
    for d in range(1, t + 1):
        if t % d == 0:
            s = t // d
            numerator += totient(d) * comb(s * (A + 1) - 1, s - 1) * comb(s * (B + 1) - 1, s - 1)
    assert numerator % t == 0
    return numerator // t


def exhaustive_check(max_n=16):
    tests = 0
    necklaces_checked = 0
    for n in range(4, max_n + 1):
        # Full class partition for every k, assembled independently of formula.
        groups = {k: defaultdict(int) for k in range(2, n + 1)}
        for bits in product('01', repeat=n):
            s = ''.join(bits)
            if canonical(s) != s:
                continue
            necklaces_checked += 1
            for k in groups:
                groups[k][spectrum(s, k)] += 1
        for a in range(1, n):
            for b in range(1, n):
                if n % (a + b):
                    continue
                t = n // (a + b)
                if t < 2:
                    continue
                target = ('0' * a + '1' * b) * t
                for k in range(2, n + 1):
                    found = groups[k][spectrum(target, k)]
                    expected = fiber_formula(a, b, t, k)
                    assert found == expected, (a, b, t, k, found, expected)
                    tests += 1
    return tests, necklaces_checked


def weak_composition(total, count, rng):
    if count == 1:
        return (total,)
    bars = sorted(rng.sample(range(total + count - 1), count - 1))
    ends = [-1] + bars + [total + count - 1]
    return tuple(ends[i + 1] - ends[i] - 1 for i in range(count))


def alternative_runs(a, t, k, rng):
    if a < k - 1:
        return (a,) * t
    extra = weak_composition(t * (a - k + 1), t, rng)
    return tuple(k - 1 + x for x in extra)


def random_construction_checks():
    rng = Random(1729)
    trials = 0
    for t in range(2, 7):
        for a in range(1, 9):
            for b in range(1, 9):
                target = ('0' * a + '1' * b) * t
                for k in range(2, max(a, b) + 3):
                    target_spectrum = spectrum(target, k)
                    for _ in range(12):
                        za = alternative_runs(a, t, k, rng)
                        ob = alternative_runs(b, t, k, rng)
                        candidate = ''.join('0' * u + '1' * v for u, v in zip(za, ob))
                        assert len(candidate) == len(target)
                        assert spectrum(candidate, k) == target_spectrum, (a, b, t, k, za, ob)
                        trials += 1
    return trials


def main():
    exhaustive, necklaces = exhaustive_check(16)
    constructed = random_construction_checks()
    examples = [(3, 2, 2, (8, 2, 1)), (4, 2, 3, (184, 10, 4, 1))]
    for a, b, t, sequence in examples:
        assert tuple(fiber_formula(a, b, t, k) for k in range(2, 2 + len(sequence))) == sequence
    print('VERIFY_OK', 'exhaustive_parameter_k_cases=' + str(exhaustive),
          'cyclic_necklaces_examined=' + str(necklaces),
          'independent_constructed_words=' + str(constructed),
          'max_exhaustive_n=16', 'max_constructed_t=6')


if __name__ == '__main__':
    main()
