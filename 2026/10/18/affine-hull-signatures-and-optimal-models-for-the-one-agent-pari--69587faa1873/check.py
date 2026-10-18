"""Independent finite semantic checks for the affine one-agent S5 theorem.

Runs on Python 3 without third-party dependencies. All S5 classes are represented
by nonempty sets of distinct propositional truth vectors. Formula evaluation
uses the Kripke clauses, independently of the affine-hull proof.
"""
import itertools
import random


def affine_hull(X, n):
    X = frozenset(X)
    pivot = min(X)
    differences = {v ^ pivot for v in X}
    span = {0}
    for d in differences:
        span |= {x ^ d for x in tuple(span)}
    # span closure of all generators: one pass with every element is sufficient
    return frozenset(pivot ^ d for d in span)


def affine_value(mask, c, v):
    return ((mask & v).bit_count() & 1) ^ c


def evaluate(formula, X, a):
    op = formula[0]
    if op == 'p':
        return (a >> formula[1]) & 1
    if op == 'one':
        return 1
    if op == 'zero':
        return 0
    if op == 'neg':
        return 1 ^ evaluate(formula[1], X, a)
    if op == 'xor':
        return evaluate(formula[1], X, a) ^ evaluate(formula[2], X, a)
    if op == 'dia':
        return int(any(evaluate(formula[1], X, b) for b in X))
    if op == 'box':
        return int(all(evaluate(formula[1], X, b) for b in X))
    raise AssertionError(formula)


def generate(rng, n, depth):
    if depth == 0 or rng.randrange(5) == 0:
        k = rng.randrange(n + 2)
        return ('p', k) if k < n else (('zero',) if k == n else ('one',))
    op = rng.choice(['neg', 'xor', 'dia', 'box'])
    if op == 'xor':
        return ('xor', generate(rng, n, depth - 1), generate(rng, n, depth - 1))
    return (op, generate(rng, n, depth - 1))


def affine_signature(X, a, n):
    return (a, tuple(int(any(affine_value(mask, c, b) for b in X))
                     for mask in range(1 << n) for c in (0, 1)))


def gaussian(n, d):
    if d == 0 or d == n:
        return 1
    product = 1
    for j in range(d):
        product *= (2 ** n - 2 ** j)
    denominator = 1
    for j in range(d):
        denominator *= (2 ** d - 2 ** j)
    assert product % denominator == 0
    return product // denominator


def run():
    rng = random.Random(27612026)
    total_lemma = total_formulas = total_point_comparisons = 0
    class_counts = {}
    for n in (1, 2, 3):
        universe = tuple(range(1 << n))
        seen_types = {}
        sample_formulas = [generate(rng, n, 4) for _ in range(160)]
        sample_formulas += [('dia', ('xor', ('p', i), ('p', j)))
                            for i in range(n) for j in range(n)]
        sample_formulas += [('box', ('p', i)) for i in range(n)]
        total_formulas += len(sample_formulas)
        for bits in range(1, 1 << len(universe)):
            X = frozenset(v for v in universe if (bits >> v) & 1)
            H = affine_hull(X, n)
            # Brute-force all affine truth tables in the modal operand.
            for mask in range(1 << n):
                for c in (0, 1):
                    a = any(affine_value(mask, c, v) for v in X)
                    b = any(affine_value(mask, c, v) for v in H)
                    assert a == b, (n, X, H, mask, c)
                    total_lemma += 1
            for a in X:
                sig = affine_signature(X, a, n)
                pair = (a, H)
                old = seen_types.setdefault(sig, pair)
                assert old == pair
                for formula in sample_formulas:
                    assert evaluate(formula, X, a) == evaluate(formula, H, a), (formula, X, H, a)
                    total_point_comparisons += 1
        predicted = (1 << n) * sum(gaussian(n, d) for d in range(n + 1))
        assert len(seen_types) == predicted, (n, len(seen_types), predicted)
        class_counts[n] = len(seen_types)
    # Check the finite Gaussian-binomial type counts beyond the exhaustive classes.
    assert {n: (1 << n) * sum(gaussian(n, d) for d in range(n + 1)) for n in (1,2,3,4,5)} == {
        1: 4, 2: 20, 3: 128, 4: 1072, 5: 11968}
    assert class_counts == {1: 4, 2: 20, 3: 128}
    print('AFFINE_S5_VERIFY_OK')
    print('affine_existence_comparisons', total_lemma)
    print('random_and_structured_formula_templates', total_formulas)
    print('pointed_truth_comparisons', total_point_comparisons)
    print('exhaustive_pointed_type_counts', class_counts)


if __name__ == '__main__':
    run()
