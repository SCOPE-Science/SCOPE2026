"""Exact rational checks for edge-order greedy maximal matchings in radius-two trees.

Run with Python 3.9+; only standard-library modules are used.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import product, permutations
from collections import defaultdict
from math import prod, factorial


def edges_for(arms):
    edges = []
    for i, a in enumerate(arms):
        edges.append(((('root',), ('branch', i)), ('central', i)))
        for j in range(a):
            edges.append(((('branch', i), ('leaf', i, j)), ('outer', i, j)))
    return edges


def forecast(arms):
    d = len(arms)
    if d == 0:
        return {frozenset(): Fraction(1)}
    pzero = prod((Fraction(a, a + 1) for a in arms), start=Fraction(1))
    out = defaultdict(Fraction)
    if pzero:
        all_choices = [range(a) for a in arms]
        for pick in product(*all_choices):
            M = frozenset(('outer', i, j) for i, j in enumerate(pick))
            out[M] += pzero / prod(arms)
    for k, ak in enumerate(arms):
        # Exact integral of y^ak times product (a_j + y^(a_j+1))/(a_j+1).
        poly = [Fraction(0)] * ak + [Fraction(1)]
        for j, a in enumerate(arms):
            if j == k:
                continue
            q = [Fraction(a, a + 1)] + [Fraction(0)] * a + [Fraction(1, a + 1)]
            nxt = [Fraction(0)] * (len(poly) + len(q) - 1)
            for t, ct in enumerate(poly):
                if ct:
                    for u, cu in enumerate(q):
                        if cu:
                            nxt[t + u] += ct * cu
            poly = nxt
        pk = sum((coeff / (j + 1) for j, coeff in enumerate(poly)), Fraction(0))
        other = [j for j in range(d) if j != k and arms[j] > 0]
        ways = prod(arms[j] for j in other)
        for pick in product(*(range(arms[j]) for j in other)):
            M = frozenset([('central', k)] + [('outer', j, l) for j, l in zip(other, pick)])
            out[M] += pk / ways
    assert sum(out.values()) == 1, arms
    return dict(out)


def first_edge_law(arms):
    edges = edges_for(arms)
    m = len(edges)
    incidence = []
    for i, (e, _) in enumerate(edges):
        incidence.append(sum(1 << j for j, (f, _) in enumerate(edges)
                             if not set(e).isdisjoint(f)))

    @lru_cache(None)
    def solve(mask):
        if mask == 0:
            return {0: Fraction(1)}
        chosen = [i for i in range(m) if mask & (1 << i)]
        out = defaultdict(Fraction)
        for i in chosen:
            r = mask & ~incidence[i]
            for part, p in solve(r).items():
                out[part | (1 << i)] += p / len(chosen)
        return dict(out)

    return {frozenset(edges[i][1] for i in range(m) if mask & (1 << i)): p
            for mask, p in solve((1 << m) - 1).items()}


def direct_permutations(arms):
    edges = edges_for(arms)
    m = len(edges)
    counts = defaultdict(int)
    for order in permutations(range(m)):
        matched = set()
        M = []
        for i in order:
            e, label = edges[i]
            if not matched.intersection(e):
                M.append(label)
                matched.update(e)
        counts[frozenset(M)] += 1
    return {M: Fraction(n, factorial(m)) for M, n in counts.items()}, factorial(m)


def check_all():
    cases = 0
    output_states = 0
    permutation_orders = 0
    uniform_shapes = []
    for d in range(1, 6):
        for arms in product(range(4), repeat=d):
            if sum(a + 1 for a in arms) > 10:
                continue
            expected = forecast(arms)
            computed = first_edge_law(arms)
            assert expected == computed, ('recurrence disagreement', arms, expected, computed)
            assert all(prob > 0 for prob in expected.values())
            if len(set(expected.values())) == 1:
                uniform_shapes.append(arms)
                positive = [a for a in arms if a > 0]
                assert len(positive) == 0 or (len(positive) == 1 and
                          (len(arms) == 1 or (positive[0] == 2 and len(arms) == 3))), \
                          ('unpredicted uniformity', arms)
            if len(arms) <= 4 and sum(a + 1 for a in arms) <= 7:
                brute, n_orders = direct_permutations(arms)
                assert brute == expected, ('permutation disagreement', arms, brute, expected)
                permutation_orders += n_orders
            cases += 1
            output_states += len(expected)
    # Confirm symbolic nonuniformity witness for all-positive branch sizes.
    all_positive_checks = 0
    for d in range(2, 8):
        for arms in product(range(1, 5), repeat=d):
            actual = prod((Fraction(a, a + 1) for a in arms), start=Fraction(1))
            flat = 1 / (1 + sum(Fraction(1, a) for a in arms))
            assert actual < flat
            all_positive_checks += 1
    # Double-star exceptional and bias formula.
    double_star_checks = 0
    for a in range(1, 18):
        for b in range(1, 18):
            law = forecast((a,) + (0,) * b)
            bridge = frozenset({('central', 0)})
            assert law[bridge] == Fraction(1, a + b + 1)
            assert all(p == Fraction(a + b, a * b * (a + b + 1))
                       for M, p in law.items() if M != bridge)
            tv = sum(abs(p - Fraction(1, 1 + a * b)) for p in law.values()) / 2
            assert tv == Fraction(abs(a * b - a - b), (a + b + 1) * (a * b + 1))
            assert (tv == 0) == (a == b == 2)
            double_star_checks += 1
    print('VERIFY_OK profiles=%d support_points=%d brute_permutations=%d '
          'positive_obstructions=%d double_stars=%d' %
          (cases, output_states, permutation_orders, all_positive_checks, double_star_checks))


if __name__ == '__main__':
    check_all()
