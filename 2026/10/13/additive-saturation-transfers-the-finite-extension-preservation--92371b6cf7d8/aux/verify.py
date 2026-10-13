#!/usr/bin/env python3
"""Finite independent consistency checks for capped-counting semiring semantics.

No finite census is offered as proof of a statement about all finite models.
"""
import itertools
import random


def add(a, b, cap):
    return min(cap, a + b)


def mul(a, b, cap):
    return min(cap, a * b)


def val(formula, semiring, n, annotations, env):
    tag = formula[0]
    if tag == 'lit':
        _, relation, variable, negative = formula
        positive_value, negative_value = annotations[(relation, env[variable])]
        z = negative_value if negative else positive_value
        return z if semiring else z > 0
    if tag == 'eq':
        _, x, y, negative = formula
        truth = env[x] != env[y] if negative else env[x] == env[y]
        return int(truth) if semiring else truth
    if tag in ('and', 'or'):
        left = val(formula[1], semiring, n, annotations, env)
        right = val(formula[2], semiring, n, annotations, env)
        if not semiring:
            return (left and right) if tag == 'and' else (left or right)
        return mul(left, right, semiring) if tag == 'and' else add(left, right, semiring)
    if tag in ('all', 'exists'):
        _, variable, subformula = formula
        result = 1 if tag == 'all' else 0
        for a in range(n):
            env_next = dict(env)
            env_next[variable] = a
            z = val(subformula, semiring, n, annotations, env_next)
            if semiring:
                result = mul(result, z, semiring) if tag == 'all' else add(result, z, semiring)
            else:
                result = (result and z) if tag == 'all' else (result or z)
        return result
    raise ValueError(tag)


def verify():
    semiring_cases = 0
    for k in range(1, 9):
        universe = range(k + 1)
        for a, b, c in itertools.product(universe, repeat=3):
            assert add(add(a, b, k), c, k) == add(a, add(b, c, k), k)
            assert mul(mul(a, b, k), c, k) == mul(a, mul(b, c, k), k)
            assert mul(a, add(b, c, k), k) == add(mul(a, b, k), mul(a, c, k), k)
            assert add(a, b, k) == add(b, a, k)
            assert mul(a, b, k) == mul(b, a, k)
            semiring_cases += 1
        for a in universe:
            assert add(a, 0, k) == a and mul(a, 1, k) == a
            assert mul(a, 0, k) == 0
            assert add(a, k, k) == k
            if a:
                assert sum([a] * k) >= k
                assert min(k, k*a) == k
    P = lambda v, neg=False: ('lit', 'P', v, neg)
    Q = lambda v, neg=False: ('lit', 'Q', v, neg)
    EQ = lambda x, y, neg=False: ('eq', x, y, neg)
    AND = lambda a,b: ('and', a, b)
    OR = lambda a,b: ('or', a, b)
    ALL = lambda v,f: ('all', v, f)
    EX = lambda v,f: ('exists', v, f)
    formulas = (
        EX('x', AND(P('x'), Q('x', True))),
        ALL('x', OR(P('x'), P('x', True))),
        EX('x', ALL('y', OR(P('x'), Q('y')))),
        ALL('x', EX('y', OR(AND(P('x'), Q('y')), AND(P('y', True), Q('x', True))))),
        ALL('x', EX('y', AND(EQ('x','y'), OR(Q('y'), Q('x',True))))),
        EX('x', EX('y', AND(EQ('x','y',True), AND(P('x'), P('y',True))))),
    )
    valuation_cases = 0
    formula_cases = 0
    randomizer = random.Random(1729)
    for k in range(1, 5):
        for n in range(0, 4):
            atoms = list(itertools.product(('P','Q'), range(n)))
            options = [(z,0) for z in range(1,k+1)] + [(0,z) for z in range(1,k+1)]
            size = len(options)**len(atoms)
            if size <= 5000:
                valuations = itertools.product(options, repeat=len(atoms))
            else:
                valuations = (tuple(randomizer.choice(options) for _ in atoms) for _ in range(2000))
            for chosen in valuations:
                annotations = dict(zip(atoms, chosen))
                valuation_cases += 1
                for f in formulas:
                    s = val(f, k, n, annotations, {})
                    b = val(f, False, n, annotations, {})
                    assert (s > 0) == b
                    saturation = 0
                    for _ in range(k):
                        saturation = add(saturation, s, k)
                    assert saturation == (k if b else 0)
                    formula_cases += 1
    print('SEMIRING_AXIOM_TRIPLES', semiring_cases)
    print('MODEL_DEFINING_VALUATIONS', valuation_cases)
    print('FORMULA_SUPPORT_AND_SATURATION_TESTS', formula_cases)
    print('ALL_FINITE_CHECKS_PASSED')

if __name__ == '__main__':
    verify()
