"""Exact small-instance checks for temporal repetition-count variance.

Run with Python 3 standard library only. The general inequality and normal
limit require the analytic arguments in RESULT.md.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product


def step_matrix(neighbors, noise):
    n = len(neighbors)
    states = list(product((-1, 1), repeat=n))
    matrix = {}
    for state in states:
        pos = [noise / 2 + (1 - noise) * sum(state[j] == 1 for j in neighbors[v]) / len(neighbors[v]) for v in range(n)]
        matrix[state] = {other: _prod(pos[v] if other[v] == 1 else 1 - pos[v] for v in range(n)) for other in states}
        assert sum(matrix[state].values()) == 1
    return states, matrix


def _prod(vals):
    ans = Fraction(1)
    for val in vals:
        ans *= val
    return ans


def finite_variance(neighbors, noise, lag, length):
    states, trans = step_matrix(neighbors, noise)
    dist = {(state, (), 0): Fraction(1, len(states)) for state in states}
    for moment in range(1, length + lag + 1):
        nxt = defaultdict(Fraction)
        for (state, window, successes), probability in dist.items():
            for other, weight in trans[state].items():
                if not weight:
                    continue
                count = successes + (moment > lag and other[0] == window[-lag])
                window2 = (window + (other[0],))[-lag:]
                nxt[other, window2, count] += probability * weight
        dist = nxt
    mean = sum(Fraction(count) * p for (_, _, count), p in dist.items())
    var = sum((count - mean) ** 2 * p for (_, _, count), p in dist.items())
    return mean, var


def walsh_formula(ancestors, lag):
    pairs = Counter()
    const = 0
    for t in range(len(ancestors) - lag):
        a, b = ancestors[t], ancestors[t + lag]
        if a == b:
            const += 1
        else:
            pairs[tuple(sorted((a, b)))] += 1
    conditional_var = Fraction(sum(m * m for m in pairs.values()), 4)
    vals = []
    for symbols in product((-1, 1), repeat=max(ancestors) + 1):
        successes = sum(symbols[ancestors[t]] == symbols[ancestors[t + lag]] for t in range(len(ancestors) - lag))
        vals.append(successes)
    avg = Fraction(sum(vals), len(vals))
    direct_var = Fraction(sum((v - avg) ** 2 for v in vals), len(vals))
    assert avg == Fraction(len(ancestors) - lag + const, 2)
    assert direct_var == conditional_var
    return 1


def main():
    checks = 0
    for lag in (1, 2):
        for ancestors in product(range(4), repeat=5):
            checks += walsh_formula(ancestors, lag)
    examples = (
        (((1,), (0,)), Fraction(1, 2)),
        (((1, 2), (0, 2), (0, 1)), Fraction(1, 2)),
        (((1, 2), (0, 2), (0, 1)), Fraction(1, 3)),
    )
    for neighbors, noise in examples:
        for lag in (1, 2):
            for length in (1, 2, 3, 4):
                _, var = finite_variance(neighbors, noise, lag, length)
                assert var >= Fraction(length, 4) * noise ** 2, (neighbors, noise, lag, length, var)
                checks += 1
    for lag in (1, 2, 3):
        for length in (1, 2, 3, 4):
            _, var = finite_variance(((1,), (0,)), Fraction(1), lag, length)
            assert var == Fraction(length, 4), (lag, length, var)
            checks += 1
    print(f"PASS: {checks} exact checks (Walsh identities and finite voter distributions)")


if __name__ == "__main__":
    main()
