"""Finite diagnostic tests for the acyclic-attack BSAF criterion.

Usage: python checker.py. Requires only Python 3.9+ standard library.
The tests do not establish the theorem for unbounded input sizes.
"""
from itertools import product
from random import Random


def attacks(E, X, attack_rules):
    return any((T & E) == T and bool(X & (1 << h)) for T, h in attack_rules)


def closed_sets(n, support_rules):
    return [E for E in range(1 << n) if all((T & E) != T or E & (1 << h)
                                          for T, h in support_rules)]


def direct_semantics(n, attack_rules, support_rules):
    closed = closed_sets(n, support_rules)
    complete, admissible, stable = [], [], []
    all_nodes = (1 << n) - 1
    for E in closed:
        if attacks(E, E, attack_rules):
            continue
        defended = 0
        for v in range(n):
            attackers = [Y for Y in closed if attacks(Y, 1 << v, attack_rules)]
            if all(attacks(E, Y, attack_rules) for Y in attackers):
                defended |= 1 << v
        if E & ~defended:
            continue
        admissible.append(E)
        if E == defended:
            complete.append(E)
        if all(attacks(E, 1 << v, attack_rules)
               for v in range(n) if not E & (1 << v)):
            stable.append(E)
    return complete, admissible, stable


def proposed_candidate(n, attack_rules, support_rules, order=None):
    if order is None:
        order = list(range(n))
    accepted = 0
    for v in order:
        if not any(h == v and (T & accepted) == T for T, h in attack_rules):
            accepted |= 1 << v
    is_closed = all((T & accepted) != T or (accepted & (1 << h))
                    for T, h in support_rules)
    return accepted if is_closed else None


def main():
    checks = 0
    # All attack hypergraphs compatible with order 0<...<n-1, with
    # every singleton support digraph, including self-support links.
    for n in range(1, 4):
        a_links = [(T, j) for j in range(n)
                   for T in range(1, 1 << j)]
        s_links = [(1 << i, j) for i in range(n) for j in range(n)]
        for ra in range(1 << len(a_links)):
            attack_rules = [edge for bit, edge in enumerate(a_links) if ra >> bit & 1]
            for rs in range(1 << len(s_links)):
                support_rules = [edge for bit, edge in enumerate(s_links) if rs >> bit & 1]
                actual, admissible, stable = direct_semantics(n, attack_rules, support_rules)
                predicted = proposed_candidate(n, attack_rules, support_rules)
                target = [] if predicted is None else [predicted]
                assert actual == target, (n, attack_rules, support_rules, actual, target)
                assert stable == target, (n, attack_rules, support_rules, stable, target)
                checks += 2
    # Random unrestricted collective supports, allowing empty support tails,
    # and collective attacks compatible with a randomly permuted order.
    rng = Random(20261024)
    for n in range(2, 7):
        for _ in range(1800):
            order = list(range(n))
            rng.shuffle(order)
            attacks_allowed = [(T, order[j]) for j in range(1, n)
                               for T in range(1, 1 << j)]
            # Interpret earlier subsets in the permuted labels.
            attack_rules = []
            for mask, head in attacks_allowed:
                if rng.randrange(8) == 0:
                    T = sum(1 << order[i] for i in range(n) if mask >> i & 1)
                    attack_rules.append((T, head))
            support_rules = []
            for h in range(n):
                for _ in range(rng.randrange(5)):
                    T = rng.randrange(1 << n)
                    support_rules.append((T, h))
            actual, _, stable = direct_semantics(n, attack_rules, support_rules)
            predicted = proposed_candidate(n, attack_rules, support_rules, order)
            target = [] if predicted is None else [predicted]
            assert actual == target, (n, order, attack_rules, support_rules, actual, target)
            assert stable == target
            checks += 2
    # Smallest support collision: there are preferred candidates but no complete.
    F = direct_semantics(2, [(1, 1)], [(1, 1)])
    assert F[0] == [] and F[2] == []
    checks += 1
    # Acyclic attacks do not force the preferred extension to coincide
    # with the unique complete extension.
    F = direct_semantics(3, [(1, 1), (2, 2)], [(1, 2)])
    assert F[0] == [5] and F[2] == [5] and 2 in F[1] and 5 in F[1], F
    maximal_admissible = [E for E in F[1] if not any(E != Y and E & Y == E for Y in F[1])]
    assert set(maximal_admissible) == {2, 5}, maximal_admissible
    checks += 2
    print('ALL_CHECKS_OK', checks)


if __name__ == '__main__':
    main()
