"""Independent relational and displacement checks for proposition-free cycle loop logic.

Run: python3 loop_cycle_verify.py
Requires Python 3 standard library only.
These finite tests corroborate but do not replace the general proof.
"""
from functools import lru_cache
from math import gcd
from random import Random


def word(*letters):
    if not letters:
        return ('test', ('top',))
    p = ('fwd',) if letters[0] == '+' else ('rev',)
    for s in letters[1:]:
        p = ('seq', p, ('fwd',) if s == '+' else ('rev',))
    return p


def power(sign, k):
    if k == 0:
        return ('test', ('top',))
    return word(*(sign for _ in range(k)))


def relation_semantics(n):
    identity = frozenset((i, i) for i in range(n))
    universe = tuple(range(n))

    @lru_cache(None)
    def formula(f):
        op = f[0]
        if op == 'top':
            return frozenset(universe)
        if op == 'bot':
            return frozenset()
        if op == 'not':
            return frozenset(set(universe) - formula(f[1]))
        if op == 'and':
            return formula(f[1]) & formula(f[2])
        if op == 'dia':
            r, target = program(f[1]), formula(f[2])
            return frozenset(a for a, b in r if b in target)
        if op == 'loop':
            return frozenset(a for a, b in program(f[1]) if a == b)
        raise ValueError(f)

    @lru_cache(None)
    def program(p):
        op = p[0]
        if op == 'fwd':
            return frozenset((i, (i + 1) % n) for i in universe)
        if op == 'rev':
            return frozenset((i, (i - 1) % n) for i in universe)
        if op == 'test':
            return frozenset((i, i) for i in formula(p[1]))
        if op == 'union':
            return program(p[1]) | program(p[2])
        if op == 'seq':
            left, right = program(p[1]), program(p[2])
            return frozenset((a, c) for a, b in left for x, c in right if b == x)
        if op == 'star':
            edges = set(program(p[1])) | set(identity)
            for k in universe:
                for i in universe:
                    if (i, k) in edges:
                        for j in universe:
                            if (k, j) in edges:
                                edges.add((i, j))
            return frozenset(edges)
        raise ValueError(p)

    return formula, program


def offset_semantics(n):
    @lru_cache(None)
    def formula(f):
        op = f[0]
        if op == 'top':
            return True
        if op == 'bot':
            return False
        if op == 'not':
            return not formula(f[1])
        if op == 'and':
            return formula(f[1]) and formula(f[2])
        if op == 'dia':
            return bool(program(f[1])) and formula(f[2])
        if op == 'loop':
            return 0 in program(f[1])
        raise ValueError(f)

    @lru_cache(None)
    def program(p):
        op = p[0]
        if op == 'fwd':
            return frozenset((1 % n,))
        if op == 'rev':
            return frozenset(((-1) % n,))
        if op == 'test':
            return frozenset((0,)) if formula(p[1]) else frozenset()
        if op == 'union':
            return program(p[1]) | program(p[2])
        if op == 'seq':
            return frozenset((a + b) % n for a in program(p[1]) for b in program(p[2]))
        if op == 'star':
            generators = program(p[1])
            reached, todo = {0}, [0]
            while todo:
                cur = todo.pop()
                for a in generators:
                    value = (cur + a) % n
                    if value not in reached:
                        reached.add(value)
                        todo.append(value)
            return frozenset(reached)
        raise ValueError(p)

    return formula, program


def random_formula(rng, depth):
    if depth <= 0:
        return rng.choice([('top',), ('bot',)])
    tag = rng.choice(['not', 'and', 'dia', 'loop'])
    if tag == 'not':
        return ('not', random_formula(rng, depth - 1))
    if tag == 'and':
        return ('and', random_formula(rng, depth - 1), random_formula(rng, depth - 1))
    if tag == 'dia':
        return ('dia', random_program(rng, depth - 1), random_formula(rng, depth - 1))
    return ('loop', random_program(rng, depth - 1))


def random_program(rng, depth):
    if depth <= 0:
        return rng.choice([('fwd',), ('rev',), ('test', ('top',)), ('test', ('bot',))])
    tag = rng.choice(['fwd', 'rev', 'test', 'union', 'seq', 'star'])
    if tag in ['fwd', 'rev']:
        return (tag,)
    if tag == 'test':
        return ('test', random_formula(rng, depth - 1))
    if tag == 'star':
        return ('star', random_program(rng, depth - 1))
    return (tag, random_program(rng, depth - 1), random_program(rng, depth - 1))


def check():
    rng = Random(68155)
    sample = [random_formula(rng, 3) for _ in range(240)]
    comparisons = 0
    for n in range(1, 23):
        relational, _ = relation_semantics(n)
        symbolic, _ = offset_semantics(n)
        for f in sample:
            direct = relational(f)
            assert len(direct) in (0, n), (n, f, direct)
            assert bool(direct) == symbolic(f), (n, f, direct, symbolic(f))
            comparisons += 1

    examples = []
    # General regular programs with signed generators.
    examples.append((('loop', ('seq', ('star', power('+', 6)), power('+', 2))),
                     lambda n: gcd(n, 6) == gcd(n, 6, 2)))
    examples.append((('loop', ('seq', ('star', ('union', power('+', 4), power('-', 6))), power('+', 1))),
                     lambda n: n % 2 == 1))
    examples.append((('loop', ('union', power('+', 4), power('+', 9))),
                     lambda n: 4 % n == 0 or 9 % n == 0))
    examples.append((('loop', ('union', ('seq', ('star', power('+', 4)), power('+', 2)), power('+', 8))),
                     lambda n: gcd(n, 4) <= 2 or 8 % n == 0))
    for prime, exp in [(2, 1), (2, 3), (3, 2), (5, 1)]:
        t = prime ** exp
        e = prime ** (exp - 1)
        examples.append((('not', ('loop', ('seq', ('star', power('+', t)), power('+', e)))),
                         lambda n, t=t: n % t == 0))
    for fixed in (1, 2, 6, 12, 35):
        proper = [d for d in range(1, fixed) if fixed % d == 0]
        f = ('loop', power('+', fixed))
        for d in proper:
            f = ('and', f, ('not', ('loop', power('+', d))))
        examples.append((f, lambda n, fixed=fixed: n == fixed))
    example_checks = 0
    for n in range(1, 171):
        formula, _ = offset_semantics(n)
        for f, expected in examples:
            assert formula(f) == expected(n), (n, f)
            example_checks += 1
    print('CYCLE_LOOP_VERIFY_OK formula_semantics=%d arithmetic=%d' % (comparisons, example_checks))


if __name__ == '__main__':
    check()
