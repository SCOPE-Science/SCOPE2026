"""Finite diagnostics for modal support-announcement normal forms.

No finite test is used as a proof of the all-cardinality classification.
Run: python3 checker.py
"""
from itertools import product
from random import Random


def atom(t, k):
    return ('and', tuple(('p', j) if (t >> j) & 1 else ('not', ('p', j)) for j in range(k)))


def disj(parts):
    return ('or', tuple(parts)) if parts else ('false',)


def conj(parts):
    return ('and', tuple(parts)) if parts else ('true',)


def type_test(t, k):
    return atom(t, k)


def diamond_test(t, k):
    return ('dia', type_test(t, k))


def truth_support_test(s, m, k):
    return conj(diamond_test(j, k) if s & (1 << j) else ('not', diamond_test(j, k))
                for j in range(m))


def normal_form(table, k):
    m = 1 << k
    clauses = []
    for t in range(m):
        supports = [truth_support_test(s, m, k) for s in range(1 << m) if (table[s] >> t) & 1]
        clauses.append(conj((type_test(t, k), disj(supports))))
    return disj(clauses)


def ev(formula, world, support, k):
    tag = formula[0]
    if tag == 'p': return bool(world & (1 << formula[1]))
    if tag == 'true': return True
    if tag == 'false': return False
    if tag == 'not': return not ev(formula[1], world, support, k)
    if tag == 'and': return all(ev(child, world, support, k) for child in formula[1])
    if tag == 'or': return any(ev(child, world, support, k) for child in formula[1])
    if tag == 'dia': return any(ev(formula[1], v, support, k) for v in range(1 << k) if support & (1 << v))
    raise ValueError(tag)


def update(formula, support, k):
    return sum((1 << t) for t in range(1 << k) if (support & (1 << t)) and ev(formula, t, support, k))


def chain_formula(k):
    m = 1 << k
    return disj(conj((type_test(t, k), ('dia', disj(type_test(j, k) for j in range(t)))))
                for t in range(1, m))


def all_contractives(m):
    # All contractive functions represented by coordinate bits.
    choices = [[s] for s in range(1 << m)]
    out = set()
    for mask in range(1 << (m * (1 << (m-1)))):
        bits = mask
        images = []
        for s in range(1 << m):
            target = 0
            for t in range(m):
                if s & (1 << t):
                    if bits & 1: target |= 1 << t
                    bits >>= 1
            images.append(target)
        out.add(tuple(images))
    return out


def is_monotone(table, m):
    return all((table[s] & ~table[u]) == 0
               for s in range(1 << m) for u in range(1 << m) if s & ~u == 0)


def all_monotone_boolean_functions(v):
    return [bits for bits in range(1 << (1 << v))
            if all(not ((bits >> a) & 1) or ((bits >> b) & 1)
                   for a in range(1 << v) for b in range(1 << v) if a & ~b == 0)]


def main():
    rng = Random(20261023)
    tests = 0
    # Exhaust complete m=2 transformation class, matching the 2^(m 2^(m-1)) formula.
    maps = all_contractives(2)
    assert len(maps) == 16
    for table in maps:
        f = normal_form(table, 1)
        for s in range(4):
            assert update(f, s, 1) == table[s]
            tests += 1
    # Larger support families: random direct Kripke-semantics cross-checks.
    for k, samples in [(1, 40), (2, 180)]:
        m = 1 << k
        for _ in range(samples):
            table = tuple(s & rng.randrange(1 << m) for s in range(1 << m))
            f = normal_form(table, k)
            for s in range(1 << m):
                assert update(f, s, k) == table[s]
                tests += 1
    # The exact positive-modal landscape is counted by Dedekind numbers.
    for v, expected in [(0, 2), (1, 3), (2, 6), (3, 20)]:
        n = len(all_monotone_boolean_functions(v))
        assert n == expected, (v,n)
        tests += n
    for m in (1, 2, 3):
        maps = all_contractives(m)
        direct = sum(is_monotone(f, m) for f in maps)
        ded = len(all_monotone_boolean_functions(m-1)) ** m
        assert direct == ded, (m,direct,ded)
        tests += len(maps)
    # Positive-diamond depth-one witnesses realize the longest possible chains.
    for k in range(0, 5):
        m = 1 << k
        formula = chain_formula(k)
        full = (1 << m) - 1
        s = full
        for r in range(m):
            nxt = update(formula, s, k)
            assert nxt != s
            assert nxt == s & ~(1 << r), (k,r,nxt,s)
            s = nxt
            tests += 1
        assert s == 0 and update(formula, 0, k) == 0
    print('ALL_CHECKS_OK', tests)

if __name__ == '__main__': main()
