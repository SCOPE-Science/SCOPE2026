"""Finite checks for pointwise three-valued Kleene disagreement loci.

0 = false, 1 = unknown, 2 = true; conjunction=min, disjunction=max.
These tests support, but do not replace, the all-arity proof.
"""
from itertools import product


def neg(x):
    return 2 - x


def info_leq(a, b):
    return all(x == 1 or x == y for x, y in zip(a, b))


def term_closure(k):
    points = tuple(product(range(3), repeat=k))
    funcs = {tuple(p[i] for p in points) for i in range(k)}
    while True:
        new = set(funcs)
        for f in funcs:
            new.add(tuple(neg(x) for x in f))
            for g in funcs:
                new.add(tuple(min(x, y) for x, y in zip(f, g)))
                new.add(tuple(max(x, y) for x, y in zip(f, g)))
        if new == funcs:
            return points, funcs
        funcs = new


def values_from_upset(points, up):
    if not up:
        raise ValueError('The primary upset must be nonempty')
    out = []
    for x in points:
        monomials = []
        for a in up:
            literals = []
            for ai, xi in zip(a, x):
                if ai == 2:
                    literals.append(xi)
                elif ai == 0:
                    literals.append(neg(xi))
            assert literals
            monomials.append(min(literals))
        out.append(max(monomials))
    return tuple(out)


def realization(points, chosen):
    chosen = set(chosen)
    if not chosen:
        return set()
    U = {x for x in points if any(info_leq(d, x) for d in chosen)}
    V = U - chosen
    A = values_from_upset(points, U)
    B = values_from_upset(points, V) if V else tuple(min(a, neg(a)) for a in A)
    assert all(b <= a for a, b in zip(A, B))
    f = tuple(max(a, neg(a)) for a in A)
    g = tuple(max(b, neg(a)) for a, b in zip(A, B))
    return {x for x, a, b in zip(points, f, g) if a != b}


def convex(points, subset):
    return all((b in subset) for a in subset for c in subset
               for b in points if info_leq(a, b) and info_leq(b, c))


# The 2026 dependence-like conditional is classically material on crisp inputs
# and infectious on unknown inputs.
for a, b in product(range(3), repeat=2):
    value = min(max(neg(a), b), max(a, neg(a)), max(b, neg(b)))
    expected = 1 if a == 1 or b == 1 else max(neg(a), b)
    assert value == expected

for k, expected_funcs, expected_sets in [(1, 4, 4), (2, 82, 256)]:
    points, functions = term_closure(k)
    assert len(functions) == expected_funcs
    disagreement = {frozenset(x for x, a, b in zip(points, f, g) if a != b)
                    for f in functions for g in functions}
    assert len(disagreement) == expected_sets
    other = [x for x in points if x != (1,) * k]
    for mask in range(1 << len(other)):
        subset = {other[i] for i in range(len(other)) if mask & (1 << i)}
        assert convex(points, subset)
        assert realization(points, subset) == subset
        assert frozenset(subset) in disagreement
    assert all(convex(points, set(d)) and (1,) * k not in d for d in disagreement)
    print(f'arity={k} term_functions={len(functions)} disagreement_sets={len(disagreement)}')

# Explicit arity-three nonconvex obstruction; necessity rules it out.
points = tuple(product(range(3), repeat=3))
nonconvex = {(0, 1, 1), (0, 0, 0)}
assert not convex(points, nonconvex)
assert (0, 0, 1) not in nonconvex
assert info_leq((0, 1, 1), (0, 0, 1)) and info_leq((0, 0, 1), (0, 0, 0))

# Test many three-variable convex sets, without claiming to enumerate all.
import random
rng = random.Random(11703)
for _ in range(1000):
    seed = {x for x in points if x != (1, 1, 1) and rng.randrange(3) == 0}
    U = {x for x in points if any(info_leq(d, x) for d in seed)}
    Vseed = {x for x in U if rng.randrange(2) == 0}
    V = {x for x in U if any(info_leq(d, x) for d in Vseed)}
    D = U - V
    assert convex(points, D)
    assert realization(points, D) == D
print('KLEENE_DISAGREEMENT_VERIFY_OK')
