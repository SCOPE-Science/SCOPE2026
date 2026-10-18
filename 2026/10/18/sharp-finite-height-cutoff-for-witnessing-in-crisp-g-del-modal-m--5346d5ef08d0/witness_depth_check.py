#!/usr/bin/env python3
"""Finite stress test for a sharp depth-wise witnessing construction.

Only finite prefixes are evaluated. The infinite failure and universal
quantifiers are established by the accompanying mathematical proof.
"""
from fractions import Fraction
from functools import lru_cache
import random

RNG = random.Random(452701)


def model(depth, cap):
    root = ('root', 0)
    worlds = [root] + [(n, j) for n in range(2, cap+1) for j in range(depth+1)]
    successors = {w: () for w in worlds}
    successors[root] = tuple((n, 0) for n in range(2, cap+1))
    for n in range(2, cap+1):
        for j in range(depth):
            successors[(n, j)] = ((n, j+1),)
    values = {w: Fraction(1) for w in worlds}
    for n in range(2, cap+1):
        values[(n, depth)] = Fraction(1, n)
    return root, successors, values


def evaluator(successors, values):
    @lru_cache(maxsize=None)
    def ev(formula, world):
        tag = formula[0]
        if tag == 'p': return values[world]
        if tag == 'bot': return Fraction(0)
        if tag in ('and', 'or', 'imp'):
            a, b = ev(formula[1], world), ev(formula[2], world)
            if tag == 'and': return min(a, b)
            if tag == 'or': return max(a, b)
            return Fraction(1) if a <= b else b
        if tag in ('box', 'dia'):
            s = successors[world]
            if not s: return Fraction(1) if tag == 'box' else Fraction(0)
            vals = [ev(formula[1], v) for v in s]
            return min(vals) if tag == 'box' else max(vals)
        raise ValueError(tag)
    return ev


def box_iter(n):
    formula = ('p',)
    for _ in range(n): formula = ('box', formula)
    return formula


def random_formula(depth, size):
    if size == 0 or (depth == 0 and RNG.randrange(5)==0):
        return ('p',) if RNG.randrange(3) else ('bot',)
    choices = ['and', 'or', 'imp'] + (['box', 'dia'] if depth else [])
    tag = RNG.choice(choices)
    if tag in ('box','dia'):
        return (tag, random_formula(depth-1, size-1))
    i = RNG.randint(0, size-1)
    return (tag, random_formula(depth, i), random_formula(depth, size-1-i))


def check():
    samples = 0
    for depth in range(0, 6):
        for cap in range(4, 12):
            root, successors, values = model(depth, cap)
            ev = evaluator(successors, values)
            target = ev(box_iter(depth+1), root)
            assert target == Fraction(1, cap), (depth, cap, target)
            # Each immediate child has its particular, positive inner value.
            assert [ev(box_iter(depth), (n, 0)) for n in range(2, cap+1)] == [Fraction(1,n) for n in range(2, cap+1)]
            # Below the first varying leaf, all branches have the same profile.
            if depth:
                for _ in range(200):
                    formula = random_formula(depth-1, 7)
                    observed = {ev(formula, (n,0)) for n in range(2, cap+1)}
                    assert len(observed) == 1, (depth, cap, formula, observed)
                    samples += 1
        print('depth',depth,'checked finite caps 4..11; root box^(depth+1) = 1/cap')
    print('WITNESS_DEPTH_FINITE_STRESS_OK', 'shallow_formula_comparisons=', samples)


if __name__ == '__main__':
    check()
