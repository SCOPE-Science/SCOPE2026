"""Exact rational checks for gap-resolved inversions in uniform involutions.

Run with Python 3 standard library: python verify_involution_filtration.py
Finite checks support (but do not replace) the all-n algebraic proofs.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations

COUNT = 0


def check(condition, label):
    global COUNT
    COUNT += 1
    if not condition:
        raise AssertionError(label)


def involutions(n):
    """Yield all size-n involutions, as zero-indexed one-line tuples."""
    def rec(remaining, p):
        if not remaining:
            yield tuple(p)
            return
        a = remaining[0]
        q = p.copy()
        q[a] = a
        yield from rec(remaining[1:], q)
        for b in remaining[1:]:
            q = p.copy()
            q[a] = b
            q[b] = a
            yield from rec([t for t in remaining[1:] if t != b], q)
    yield from rec(list(range(n)), [None] * n)


def inv(p):
    return sum(p[i] > p[j] for i in range(len(p))
               for j in range(i + 1, len(p)))


def des(p):
    return sum(p[i] > p[i + 1] for i in range(len(p) - 1))


def conditional_pair_probability(n, k, gap):
    if n == 2:
        return Fraction(k)  # only gap is 1, k in {0,1}
    return (Fraction(2 * k * k, n * (n - 1))
            + Fraction(2 * k * (n - 2 * k) * (n - gap - 1),
                       n * (n - 1) * (n - 2)))


def explicit_finite_check(n):
    classes = defaultdict(list)
    for p in involutions(n):
        k = sum(p[i] != i for i in range(n)) // 2
        classes[k].append(p)
    for k in range(n // 2 + 1):
        ps = classes[k]
        check(len(ps) > 0, ('nonempty class', n, k))
        check(len(ps) == __import__('math').factorial(n) //
              (2 ** k * __import__('math').factorial(k) *
               __import__('math').factorial(n - 2 * k)),
              ('class cardinality', n, k))
        check(Fraction(sum(inv(p) for p in ps), len(ps)) ==
              Fraction(k * (2 * n - k), 3),
              ('inversion regression', n, k))
        check(Fraction(sum(des(p) for p in ps), len(ps)) ==
              Fraction(2 * k * (n - k), n),
              ('descent regression', n, k))
        for i in range(n):
            for j in range(i + 1, n):
                observed = Fraction(sum(p[i] > p[j] for p in ps), len(ps))
                predicted = conditional_pair_probability(n, k, j - i)
                check(observed == predicted, ('local inversion', n, k, i, j))
        if k == n // 2:
            continue
        target = defaultdict(int)
        for p in ps:
            fixed = [i for i, x in enumerate(p) if x == i]
            for i, j in combinations(fixed, 2):
                q = list(p)
                q[i] = j
                q[j] = i
                q = tuple(q)
                delta = inv(q) - inv(p)
                predicted_delta = 1 + 2 * sum(
                    i < p[t] < j for t in range(i + 1, j))
                check(delta == predicted_delta, ('increment identity', n, k, p, i, j))
                check(delta >= 1 and delta % 2 == 1,
                      ('strict odd increment', n, k, p, i, j))
                target[q] += 1
        next_class = classes[k + 1]
        check(set(target) == set(next_class), ('onto', n, k))
        check(set(target.values()) == {k + 1},
              ('constant preimage multiplicity', n, k))
        check(len(ps) * (n - 2 * k) * (n - 2 * k - 1) // 2 ==
              len(next_class) * (k + 1), ('double count', n, k))


for n in range(2, 11):
    explicit_finite_check(n)

# Separate exact arithmetic checks of the analytic formula, its spatial slope,
# and its strict monotonicity in k for a nontrivial infinite-looking sample.
# The all-size conclusion is proved by algebra in the accompanying text.
for n in range(3, 121):
    for k in range(n // 2 + 1):
        total = sum((n - gap) * conditional_pair_probability(n, k, gap)
                    for gap in range(1, n))
        check(total == Fraction(k * (2 * n - k), 3),
              ('pair sum', n, k))
        if k:
            check(conditional_pair_probability(n, k, 1) ==
                  Fraction(2 * k * (n - k), n * (n - 1)),
                  ('short distance', n, k))
        for gap in range(1, n - 1):
            check(conditional_pair_probability(n, k, gap)
                  - conditional_pair_probability(n, k, gap + 1)
                  == Fraction(2 * k * (n - 2 * k),
                              n * (n - 1) * (n - 2)),
                  ('gap slope', n, k, gap))
        if k < n // 2:
            for gap in range(1, n):
                check(conditional_pair_probability(n, k + 1, gap) >
                      conditional_pair_probability(n, k, gap),
                      ('class monotonicity', n, k, gap))

print(f'PASS: {COUNT} exact assertions; enumerated all involutions for n=2..10')
