"""Exact finite regression checks for singular strata of two odd cycles with a joining path.

Only Python standard-library modules are used. Infinite assertions rely on the proof,
not on these bounded checks.
"""
from fractions import Fraction
from itertools import combinations
from math import comb, gcd
import json


def graph_and_relation(a, b, length):
    assert a >= 1 and b >= 1 and length >= 0
    A = [f'A{i}' for i in range(2 * a + 1)]
    B = [f'B{i}' for i in range(2 * b + 1)]
    if length == 0:
        B[0] = A[0]
    edges = {}
    ca = []
    cb = []
    path = []
    for i in range(len(A)):
        name = f'a{i}'
        edges[name] = (A[i], A[(i + 1) % len(A)])
        ca.append(name)
    for i in range(len(B)):
        name = f'b{i}'
        edges[name] = (B[i], B[(i + 1) % len(B)])
        cb.append(name)
    if length:
        nodes = [A[0]] + [f'P{i}' for i in range(1, length)] + [B[0]]
        for i in range(length):
            name = f'p{i+1}'
            edges[name] = (nodes[i], nodes[i+1])
            path.append(name)
    walk = ca + path + cb + list(reversed(path))
    relation = {e: 0 for e in edges}
    for pos, e in enumerate(walk):
        relation[e] += 1 if pos % 2 == 0 else -1
    assert all(relation.values())
    assert gcd(*relation.values()) == 1
    assert sum(relation.values()) == 0
    for v in set(x for endpoints in edges.values() for x in endpoints):
        assert sum(relation[e] for e, pair in edges.items() if v in pair) == 0
    return edges, relation


def monomial_gradient_vanishes(exp, zero):
    # Evaluate each partial derivative of the monomial at the binary point:
    # all coordinates are 1 except those in 'zero', which are 0.
    for variable, power in exp.items():
        if power == 0:
            continue
        d = power
        for other, other_power in exp.items():
            exponent = other_power - (1 if variable == other else 0)
            if exponent and other in zero:
                d = 0
                break
        if d:
            return False
    return True


def expected_minimals(relation):
    one = []
    two = []
    for sign in (1, -1):
        vals = [(e, abs(v)) for e, v in relation.items() if v * sign > 0]
        squares = [frozenset((e,)) for e, p in vals if p == 2]
        linear = [e for e, p in vals if p == 1]
        pairs = [frozenset(pair) for pair in combinations(linear, 2)]
        assert all(p in (1, 2) for _, p in vals)
        (one if sign == 1 else two).extend(squares + pairs)
    return {a | b for a in one for b in two}


def actual_minimals(relation):
    names = list(relation)
    pos = {e: v for e, v in relation.items() if v > 0}
    neg = {e: -v for e, v in relation.items() if v < 0}
    ans = set()
    for mask in range(1 << len(names)):
        zero = frozenset(names[i] for i in range(len(names)) if mask & (1 << i))
        if not (monomial_gradient_vanishes(pos, zero) and monomial_gradient_vanishes(neg, zero)):
            continue
        if all(not (monomial_gradient_vanishes(pos, zero - {e}) and
                    monomial_gradient_vanishes(neg, zero - {e})) for e in zero):
            ans.add(zero)
    return ans


def run():
    cases = [(1, 1, ell) for ell in range(6)] + \
            [(1, 2, ell) for ell in range(5)] + \
            [(2, 2, ell) for ell in range(4)]
    results = []
    checked_patterns = 0
    for a, b, ell in cases:
        edges, relation = graph_and_relation(a, b, ell)
        up = sum(v == 2 for v in relation.values())
        um = sum(v == -2 for v in relation.values())
        sp = sum(v == 1 for v in relation.values())
        sm = sum(v == -1 for v in relation.values())
        if ell % 2 == 0:
            assert sp == sm == a + b + 1
            assert up == um == ell // 2
        else:
            assert sp == a + b + 2 and sm == a + b
            assert up == (ell-1)//2 and um == (ell+1)//2
        predicted = expected_minimals(relation)
        observed = actual_minimals(relation)
        assert predicted == observed, (a, b, ell, predicted - observed, observed - predicted)
        counts = {j: sum(len(z) == j for z in observed) for j in (2, 3, 4)}
        assert counts[2] == up * um == ell*ell // 4
        assert counts[3] == up*comb(sm, 2) + um*comb(sp, 2)
        assert counts[4] == comb(sp, 2)*comb(sm, 2)
        checked_patterns += 1 << len(edges)
        results.append({'a': a, 'b': b, 'length': ell, 'edges': len(edges),
                        'singular_components_codim_1_2_3': [counts[2], counts[3], counts[4]]})
    return {'checked_cases': len(cases), 'binary_support_patterns': checked_patterns,
            'verified': True, 'cases': results}


if __name__ == '__main__':
    print(json.dumps(run(), separators=(',', ':')))
