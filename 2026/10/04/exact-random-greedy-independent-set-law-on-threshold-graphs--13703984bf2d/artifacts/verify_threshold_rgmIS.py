from collections import Counter
from fractions import Fraction
from itertools import permutations, product
from math import factorial


def adjacency(bits):
    n = len(bits)
    adj = [set() for _ in range(n)]
    for j in range(1, n):
        if bits[j] == 1:
            for i in range(j):
                adj[i].add(j)
                adj[j].add(i)
    return adj


def greedy_output(bits, perm):
    adj = adjacency(bits)
    chosen = set()
    for v in perm:
        if not (adj[v] & chosen):
            chosen.add(v)
    return frozenset(chosen)


def predicted_law(bits):
    n = len(bits)
    zeros = [i for i, b in enumerate(bits) if b == 0]
    ones = [i for i, b in enumerate(bits) if b == 1]
    law = {}

    p0 = Fraction(1, 1)
    for j in ones:
        p0 *= Fraction(j, j + 1)
    law[frozenset(zeros)] = p0

    for i in ones:
        p = Fraction(1, i + 1)
        for j in ones:
            if j > i:
                p *= Fraction(j, j + 1)
        support = frozenset([i] + [z for z in zeros if z > i])
        law[support] = p
    return law


def pgf_from_law(law):
    out = Counter()
    for support, p in law.items():
        out[len(support)] += p
    return dict(out)


def pgf_recurrence(bits):
    # coefficient dictionary degree -> exact probability
    pgf = {1: Fraction(1, 1)}
    for pos in range(2, len(bits) + 1):
        if bits[pos - 1] == 0:
            pgf = {d + 1: c for d, c in pgf.items()}
        else:
            nxt = {d: c * Fraction(pos - 1, pos) for d, c in pgf.items()}
            nxt[1] = nxt.get(1, Fraction(0, 1)) + Fraction(1, pos)
            pgf = {d: c for d, c in nxt.items() if c}
    return pgf


def predicted_optimal_probability(bits):
    n = len(bits)
    second_zero = next((j for j in range(2, n + 1) if bits[j - 1] == 0), n + 1)
    p = Fraction(1, 1)
    for j in range(second_zero + 1, n + 1):
        if bits[j - 1] == 1:
            p *= Fraction(j - 1, j)
    return p


def verify():
    sequences = 0
    permutation_checks = 0
    for n in range(1, 8):
        for tail in product((0, 1), repeat=n - 1):
            bits = (0,) + tail
            sequences += 1
            counts = Counter(greedy_output(bits, perm) for perm in permutations(range(n)))
            permutation_checks += factorial(n)
            denom = factorial(n)
            actual = {s: Fraction(c, denom) for s, c in counts.items()}
            predicted = predicted_law(bits)
            assert actual == predicted, (bits, actual, predicted)
            assert sum(predicted.values(), Fraction(0, 1)) == 1
            assert pgf_from_law(predicted) == pgf_recurrence(bits)

            alpha = sum(1 for b in bits if b == 0)
            actual_opt = sum(p for s, p in actual.items() if len(s) == alpha)
            assert actual_opt == predicted_optimal_probability(bits), (bits, actual_opt)

    print(f"VERIFY_OK sequences={sequences} permutation_checks={permutation_checks}")


if __name__ == "__main__":
    verify()
