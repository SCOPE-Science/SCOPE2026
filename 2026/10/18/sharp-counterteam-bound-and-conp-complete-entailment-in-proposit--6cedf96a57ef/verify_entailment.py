"""Direct finite semantics tests for PL(NE) entailment.

Run: python verify_entailment.py

This is a finite test, not a substitute for the general proof.
"""
from functools import lru_cache
import random


def atom(kind, i=None):
    return (kind,) if i is None else (kind, i)


def ne_count(formula):
    if formula[0] == 'ne':
        return 1
    if formula[0] in ('and', 'or'):
        return ne_count(formula[1]) + ne_count(formula[2])
    return 0


def semantic_table(formula, nvars):
    """Truth table indexed by a bit mask representing a team of valuations."""
    nvals = 1 << nvars
    nteams = 1 << nvals

    @lru_cache(None)
    def ev(node, team):
        tag = node[0]
        if tag == 'top':
            return True
        if tag == 'bot':
            return team == 0
        if tag == 'ne':
            return team != 0
        if tag in ('p', 'not'):
            for val in range(nvals):
                if (team >> val) & 1:
                    bit = (val >> node[1]) & 1
                    if bit != (1 if tag == 'p' else 0):
                        return False
            return True
        if tag == 'and':
            return ev(node[1], team) and ev(node[2], team)
        if tag == 'or':
            # Lax split: two (possibly overlapping) subteams must cover the team.
            left = team
            while True:
                if ev(node[1], left):
                    right = team
                    while True:
                        if left | right == team and ev(node[2], right):
                            return True
                        if right == 0:
                            break
                        right = (right - 1) & team
                if left == 0:
                    break
                left = (left - 1) & team
            return False
        raise AssertionError(tag)

    return tuple(ev(formula, team) for team in range(nteams))


def subteams(team):
    a = team
    while True:
        yield a
        if a == 0:
            return
        a = (a - 1) & team


def check_universe(nvars, num_random=1600):
    nvals = 1 << nvars
    nteams = 1 << nvals
    bases = [atom('top'), atom('bot'), atom('ne')]
    for i in range(nvars):
        bases += [atom('p', i), atom('not', i)]
    rng = random.Random(73000 + nvars)
    formulas = list(bases)
    for _ in range(num_random):
        a = rng.choice(formulas if rng.random() < .65 else bases)
        b = rng.choice(formulas if rng.random() < .65 else bases)
        # Avoid unbounded depth: randomly mix in base formulas.
        if len(str(a)) > 100: a = rng.choice(bases)
        if len(str(b)) > 100: b = rng.choice(bases)
        formulas.append((rng.choice(('and', 'or')), a, b))

    unique = {}
    for f in formulas:
        table = semantic_table(f, nvars)
        m = ne_count(f)
        if table not in unique or m < unique[table][0]:
            unique[table] = (m, f)

    checked_models = 0
    checked_closure = 0
    for table, (m, f) in unique.items():
        for t, true in enumerate(table):
            if not true:
                continue
            checked_models += 1
            # The published small-subteam lemma, tested against raw semantics.
            assert any(table[s] and s.bit_count() <= m for s in subteams(t)), (f, t, m)
        sat = [t for t in range(nteams) if table[t]]
        for a in sat:
            for b in sat:
                assert table[a | b], ('union', f, a, b)
                if (a & b) == a:
                    for between in range(nteams):
                        if (a & between) == a and (between & b) == between:
                            assert table[between], ('convexity', f, a, between, b)
                checked_closure += 1

    checked_pairs = 0
    for left, (m, _) in unique.items():
        for right in unique:
            counter = [t for t in range(nteams) if left[t] and not right[t]]
            if counter:
                assert min(t.bit_count() for t in counter) <= m + 1, (m, counter)
            checked_pairs += 1

    return {'nvars': nvars, 'formulas_generated': len(formulas),
            'distinct_semantics': len(unique), 'satisfying_teams_checked': checked_models,
            'closure_pairs_checked': checked_closure, 'entailment_pairs_checked': checked_pairs}


def char_valuation(v, nvars):
    terms = [atom('p', i) if ((v >> i) & 1) else atom('not', i) for i in range(nvars)]
    f = terms[0]
    for t in terms[1:]:
        f = ('and', f, t)
    return f


def split_many(formulas):
    f = formulas[0]
    for s in formulas[1:]:
        f = ('or', f, s)
    return f


def sharpness(m):
    nvars = max(1, (m + 1 - 1).bit_length())
    required = list(range(m))
    clauses = [('and', char_valuation(v, nvars), atom('ne')) for v in required]
    antecedent = ('or', split_many(clauses), atom('top'))
    consequent = split_many([char_valuation(v, nvars) for v in required])
    left = semantic_table(antecedent, nvars)
    right = semantic_table(consequent, nvars)
    counter = [t for t in range(len(left)) if left[t] and not right[t]]
    assert ne_count(antecedent) == m
    assert counter, (m, 'no counterexample')
    assert min(t.bit_count() for t in counter) == m + 1, (m, 'bound not sharp')
    return {'m': m, 'variables': nvars, 'least_counterteam': m + 1,
            'counterteams': len(counter)}


if __name__ == '__main__':
    for n in (1, 2):
        print('Finite universe:', check_universe(n))
    for m in (1, 2, 3):
        print('Sharpness:', sharpness(m))
    print('VERIFY_OK')
