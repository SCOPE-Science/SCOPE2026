#!/usr/bin/env python3
"""Check finite consequences of the rooted-star non-contingency classification.

The all-formula theorem requires the separate structural-induction proof.
"""
from itertools import product
from math import ceil, log2


def supports(n):
    m = 1 << n
    return [frozenset(i for i in range(m) if mask & (1 << i))
            for mask in range(1 << m)]


def label_formula(n, a):
    parts = [('p', i) if ((a >> i) & 1) else ('not', ('p', i))
             for i in range(n)]
    if not parts:
        return ('top',)
    t = parts[0]
    for part in parts[1:]:
        t = ('and', t, part)
    return t


def evaluate(t, n, v, s, root):
    tag = t[0]
    if tag == 'top':
        return True
    if tag == 'p':
        return bool((v >> t[1]) & 1)
    if tag == 'not':
        return not evaluate(t[1], n, v, s, root)
    if tag == 'and':
        return evaluate(t[1], n, v, s, root) and evaluate(t[2], n, v, s, root)
    if tag == 'delta':
        if not root:
            return True
        values = {evaluate(t[1], n, a, frozenset(), False) for a in s}
        return len(values) <= 1
    raise ValueError(tag)


def flatten(t):
    tag = t[0]
    if tag == 'delta':
        return ('top',)
    if tag == 'not':
        return ('not', flatten(t[1]))
    if tag == 'and':
        return ('and', flatten(t[1]), flatten(t[2]))
    return t


def predicted(t, n, v, s):
    tag = t[0]
    if tag == 'delta':
        vals = {evaluate(flatten(t[1]), n, a, frozenset(), False) for a in s}
        return len(vals) <= 1
    if tag == 'not':
        return not predicted(t[1], n, v, s)
    if tag == 'and':
        return predicted(t[1], n, v, s) and predicted(t[2], n, v, s)
    return evaluate(t, n, v, s, True)


def canonical_support(s):
    return ('small',) if len(s) < 2 else ('support', tuple(sorted(s)))


def check_signature_census():
    for n in range(4):
        m = 1 << n
        groups = {}
        ss = supports(n)
        for s in ss:
            signature = tuple(evaluate(('delta', label_formula(n, a)), n, 0, s, True)
                              for a in range(m))
            groups.setdefault(signature, set()).add(canonical_support(s))
        assert all(len(x) == 1 for x in groups.values())
        assert len(groups) == 2**m - m
        for s in ss:
            for v in range(m):
                type_vector = tuple((v >> i) & 1 for i in range(n)) + tuple(
                    evaluate(('delta', label_formula(n, a)), n, v, s, True)
                    for a in range(m))
                assert type_vector[:n] == tuple((v >> i) & 1 for i in range(n))
        if n >= 2:
            assert 2**(m-1) < 2**m - m <= 2**m
        print('n=%d values=%d successor_types=%d pointed_types=%d tests=%d' %
              (n, m, len(groups), m*len(groups),
               ceil(log2(len(groups))) if len(groups)>1 else 0))


def check_nested_formulas():
    n = 2
    # Deterministically cover nested modalities mixed with both Boolean operators.
    formulas = [('p', 0), ('p', 1), ('top',)]
    for round_index in range(3):
        seed = formulas[-15:]
        generated = []
        for i, t in enumerate(seed):
            generated += [('not', t), ('delta', t)]
            generated += [('and', t, seed[(i+1) % len(seed)])]
        formulas.extend(generated)
    for s in supports(n):
        for v in range(1 << n):
            for t in formulas:
                assert evaluate(t, n, v, s, True) == predicted(t, n, v, s)
                for a in range(1 << n):
                    assert evaluate(t, n, a, frozenset(), False) == evaluate(
                        flatten(t), n, a, frozenset(), False)
    print('nested_truth_tables_checked=%d' % (len(formulas)*len(supports(n))*(1<<n)))


if __name__ == '__main__':
    check_signature_census()
    check_nested_formulas()
    print('ROOTED_STAR_NONCONTINGENCY_ENUMERATION_OK')
