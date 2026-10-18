"""Finite tests for the one-constant single-agent knowing-value signature theorem.

Run: python check_signature.py
The mathematical argument for arbitrary formulas and models is in RESULT.md.
"""
from itertools import combinations
from functools import lru_cache
import random


def signature(values, pointed_value, k):
    u = set(range(k))
    support = set(values)
    t = frozenset(support & u)
    outside = len(support - u)
    delta = min(2, outside)
    tau = pointed_value if pointed_value in u else '*'
    return tau, t, delta


def eval_actual(formula, world, values):
    kind = formula[0]
    if kind == 'top':
        return True
    if kind == 'eq':
        return values[world] == formula[1]
    if kind == 'not':
        return not eval_actual(formula[1], world, values)
    if kind == 'and':
        return eval_actual(formula[1], world, values) and eval_actual(formula[2], world, values)
    if kind == 'k':
        return all(eval_actual(formula[1], j, values) for j in range(len(values)))
    if kind == 'kv':
        selected = {values[j] for j in range(len(values)) if eval_actual(formula[1], j, values)}
        return len(selected) < 2
    raise AssertionError(kind)


def eval_signature(formula, sig):
    tau, present, delta = sig
    kind = formula[0]
    if kind == 'top':
        return True
    if kind == 'eq':
        return tau == formula[1]
    if kind == 'not':
        return not eval_signature(formula[1], sig)
    if kind == 'and':
        return eval_signature(formula[1], sig) and eval_signature(formula[2], sig)
    if kind in ('k', 'kv'):
        representatives = [(x, 1) for x in sorted(present)]
        if delta:
            representatives += [('*', delta)]
        selected = [(x, count) for x, count in representatives
                    if eval_signature(formula[1], (x, present, delta))]
        if kind == 'k':
            return len(selected) == len(representatives)
        return sum(count for _, count in selected) < 2
    raise AssertionError(kind)


def gen_formula(rng, depth, k):
    if depth == 0:
        return ('eq', rng.randrange(k)) if k else ('top',)
    choice = rng.randrange(4)
    if choice == 0:
        return ('not', gen_formula(rng, depth - 1, k))
    if choice == 1:
        return ('and', gen_formula(rng, depth - 1, k), gen_formula(rng, depth - 1, k))
    if choice == 2:
        return ('k', gen_formula(rng, depth - 1, k))
    return ('kv', gen_formula(rng, depth - 1, k))


def main():
    rng = random.Random(260631891)
    checked = 0
    for k in range(4):
        formulas = [gen_formula(rng, d, k) for d in range(1, 5) for _ in range(20)]
        signatures = set()
        universe = list(range(k + 3))
        # Complete nonempty supports, including one/two/three unnamed values.
        for n in range(1, len(universe) + 1):
            for values in combinations(universe, n):
                for pointed, v in enumerate(values):
                    sig = signature(values, v, k)
                    signatures.add(sig)
                    for f in formulas:
                        assert eval_actual(f, pointed, values) == eval_signature(f, sig), (k, values, pointed, f)
                        checked += 1
        expected = (3 * k * 2 ** (k - 1) + 2 ** (k + 1)) if k else 2
        assert len(signatures) == expected, (k, len(signatures), expected)
        for tau, t, delta in signatures:
            # Canonical set contains exactly |T|+delta worlds and preserves the pointed signature.
            canonical = tuple(sorted(t)) + tuple(range(k, k + delta))
            distinguished = tau if tau != '*' else k
            assert len(canonical) == len(t) + delta
            assert signature(canonical, distinguished, k) == (tau, t, delta)
        # Duplicate-value worlds do not alter any formula.
        for _ in range(150):
            vals = tuple(rng.choice(universe) for _ in range(6))
            for pointed, v in enumerate(vals):
                sig = signature(vals, v, k)
                for f in formulas[::5]:
                    assert eval_actual(f, pointed, vals) == eval_signature(f, sig)
                    checked += 1
        print(f'k={k}: signatures={len(signatures)} optimal_max_worlds={k+2}')
    print('KNOWING_VALUE_SIGNATURE_VERIFY_OK', checked)


if __name__ == '__main__':
    main()
