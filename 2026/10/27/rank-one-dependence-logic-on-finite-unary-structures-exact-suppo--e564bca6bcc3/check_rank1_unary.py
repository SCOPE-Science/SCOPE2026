#!/usr/bin/env python3
"""Finite checks for rank-one dependence semantics on unary structures.

Run with Python 3. Uses only the standard library. Checks are finite
and do not establish the unrestricted theorem.
"""
from functools import lru_cache
from itertools import product

# Quantifier-free syntax with one free variable x:
# ('const',), ('type', t), ('not_type', t), ('true',), ('false',)
# or ('and', left, right), ('or', left, right).

def mk_or(forms):
    assert forms
    out = forms[0]
    for form in forms[1:]:
        out = ('or', out, form)
    return out


def upper_formula(color, k):
    assert k >= 0
    return mk_or([('not_type', color)] + [('const',)] * k)


def team_truth(ast, team):
    """Truth by the split-team clause; team is a tuple of (color, index)."""
    tag = ast[0]
    if tag == 'const':
        return len(team) <= 1
    if tag == 'type':
        return all(c == ast[1] for c, _ in team)
    if tag == 'not_type':
        return all(c != ast[1] for c, _ in team)
    if tag == 'true':
        return True
    if tag == 'false':
        return not team
    if tag == 'and':
        return team_truth(ast[1], team) and team_truth(ast[2], team)
    if tag == 'or':
        # Downward closure permits disjoint splitting without loss.
        for mask in range(1 << len(team)):
            left = tuple(x for i, x in enumerate(team) if mask >> i & 1)
            right = tuple(x for i, x in enumerate(team) if not (mask >> i & 1))
            if team_truth(ast[1], left) and team_truth(ast[2], right):
                return True
        return False
    raise ValueError(ast)


def model_team(counts):
    return tuple((color, index) for color, n in enumerate(counts)
                 for index in range(n))


def all_models(num_colors, maximum):
    for counts in product(range(maximum + 1), repeat=num_colors):
        if sum(counts):
            yield counts


def color_support(counts):
    return frozenset(i for i, n in enumerate(counts) if n)


def in_downset(counts, obstacles_by_support):
    sup = color_support(counts)
    return not any(all(counts[i] >= a[i] for i in sup)
                   for a in obstacles_by_support.get(sup, ()))


def synthesized_truth(counts, obstacles_by_support):
    sup = color_support(counts)
    # Exact-support guard is verified independently of the obstruction formula.
    if not sup:
        return False
    for a in obstacles_by_support.get(sup, ()):
        # Sentence-level or is ordinary Boolean or on the singleton empty assignment.
        if not any(team_truth(upper_formula(i, a[i] - 1), model_team(counts))
                   for i in sup):
            return False
    return True


def formula_capacity(ast):
    """0,1,...,None (=infinity), for one-colored universes."""
    tag = ast[0]
    if tag == 'const':
        return 1
    if tag in ('true', 'type'):
        return None
    if tag in ('false', 'not_type'):
        return 0
    a, b = formula_capacity(ast[1]), formula_capacity(ast[2])
    if tag == 'and':
        if a is None:
            return b
        if b is None:
            return a
        return min(a, b)
    if tag == 'or':
        return None if a is None or b is None else a + b
    raise ValueError(ast)


def constancy_occurrences(ast):
    if ast[0] == 'const':
        return 1
    if ast[0] in ('and', 'or'):
        return constancy_occurrences(ast[1]) + constancy_occurrences(ast[2])
    return 0


def main():
    total_upper = 0
    for counts in all_models(2, 3):
        team = model_team(counts)
        for color in (0, 1):
            for k in range(5):
                got = team_truth(upper_formula(color, k), team)
                assert got == (counts[color] <= k), (counts, color, k, got)
                total_upper += 1
    print('UPPER_TEAM_SEMANTICS_OK', total_upper)

    # Every support has its own finite minimal forbidden vector antichain.
    obstacles = {
        frozenset((0,)): [{0: 3}],
        frozenset((1,)): [{1: 2}],
        frozenset((0, 1)): [{0: 2, 1: 3}, {0: 3, 1: 2}],
    }
    tested = 0
    for counts in all_models(2, 4):
        assert synthesized_truth(counts, obstacles) == in_downset(counts, obstacles)
        tested += 1
    print('SUPPORT_FIBER_SYNTHESIS_OK', tested)

    # Direct formula checking versus exact capacity on all one-color teams.
    atoms = [('const',), ('true',), ('false',), ('type', 0), ('not_type', 0)]
    forms = list(atoms)
    for a in atoms:
        for b in atoms:
            forms.append(('or', a, b))
            forms.append(('and', a, b))
    for a in atoms:
        for b in atoms:
            for c in atoms:
                forms.append(('or', ('and', a, b), c))
                forms.append(('and', ('or', a, b), c))
    cases = 0
    for ast in forms:
        cap = formula_capacity(ast)
        if cap is not None:
            assert cap <= constancy_occurrences(ast)
        for n in range(6):
            got = team_truth(ast, model_team((n,)))
            want = (cap is None or n <= cap)
            assert got == want, (ast, n, cap, got)
            cases += 1
    print('QUANTIFIER_FREE_CAPACITY_OK', len(forms), cases)

    # Rank-one preservation: forall clauses shrink by downward closure;
    # exists clauses persist if their witnessing color remains present.
    bases = atoms + forms[5:25]
    clauses = [('forall', ast) for ast in bases] + [('exists', ast) for ast in bases]
    pair_checks = 0
    for upper in all_models(2, 3):
        for lower in all_models(2, 3):
            if color_support(lower) != color_support(upper):
                continue
            if any(a > b for a, b in zip(lower, upper)):
                continue
            hi, lo = model_team(upper), model_team(lower)
            for q, ast in clauses:
                if q == 'forall':
                    p_hi, p_lo = team_truth(ast, hi), team_truth(ast, lo)
                else:
                    p_hi = any(team_truth(ast, (x,)) for x in hi)
                    p_lo = any(team_truth(ast, (x,)) for x in lo)
                assert not p_hi or p_lo, (upper, lower, q, ast)
                pair_checks += 1
    print('RANK_ONE_SUPPORT_THINNING_OK', pair_checks)
    print('RANK_ONE_MONADIC_CHECK_OK')


if __name__ == '__main__':
    main()
