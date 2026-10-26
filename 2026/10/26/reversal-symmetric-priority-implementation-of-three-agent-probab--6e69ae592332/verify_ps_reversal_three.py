"""Exact finite verification of a three-agent reversal-balanced priority implementation.

Uses Python 3 standard library only; all probabilities are fractions.
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations, product


def probabilistic_serial(profile):
    """Independent event-driven simulation of simultaneous unit-rate eating."""
    n = len(profile)
    remaining = [Fraction(1) for _ in range(n)]
    matrix = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    elapsed = Fraction(0)
    while elapsed < 1:
        eating = [next(obj for obj in ranking if remaining[obj] > 0)
                  for ranking in profile]
        multiplicity = Counter(eating)
        step = min(remaining[obj] / count
                   for obj, count in multiplicity.items())
        assert step > 0
        for i, obj in enumerate(eating):
            matrix[i][obj] += step
        for obj, count in multiplicity.items():
            remaining[obj] -= step * count
        elapsed += step
    assert elapsed == 1 and all(value == 0 for value in remaining)
    assert all(sum(row) == 1 for row in matrix)
    assert all(sum(matrix[i][j] for i in range(n)) == 1
               for j in range(n))
    return tuple(tuple(row) for row in matrix)


def serial_dictatorship(profile, priority):
    remaining = set(range(len(profile)))
    allocation = [-1] * len(profile)
    for agent in priority:
        chosen = next(obj for obj in profile[agent] if obj in remaining)
        remaining.remove(chosen)
        allocation[agent] = chosen
    assert not remaining
    return tuple(allocation)


def priority_rule(profile):
    """Return a profile-contingent reversal-symmetric law on priorities."""
    n = len(profile)
    orders = tuple(permutations(range(n)))
    assert n <= 3
    if n == 3:
        firsts = [ranking[0] for ranking in profile]
        groups = [[i for i in range(3) if firsts[i] == x]
                  for x in range(3)]
        shared = next((g for g in groups if len(g) == 2), None)
        if shared is not None and profile[shared[0]] != profile[shared[1]]:
            solo = next(i for i in range(3) if i not in shared)
            retained = [order for order in orders
                        if order[0] == solo or order[-1] == solo]
            assert len(retained) == 4
            return {order: Fraction(1, 4) for order in retained}
    return {order: Fraction(1, len(orders)) for order in orders}


def priority_matrix(profile, probabilities):
    n = len(profile)
    result = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    for order, prob in probabilities.items():
        matching = serial_dictatorship(profile, order)
        for agent, obj in enumerate(matching):
            result[agent][obj] += prob
    return tuple(tuple(row) for row in result)


def dec_ef(profile, probabilities):
    for i in range(len(profile)):
        pos = {obj: k for k, obj in enumerate(profile[i])}
        for j in range(len(profile)):
            if j == i:
                continue
            envy = sum((prob for priority, prob in probabilities.items()
                        if pos[serial_dictatorship(profile, priority)[j]]
                        < pos[serial_dictatorship(profile, priority)[i]]),
                       Fraction(0))
            assert envy <= Fraction(1, 2), (profile, i, j, envy)


def relabel(profile, agents, objects):
    return tuple(tuple(objects[x] for x in profile[agents[i]])
                 for i in range(len(profile)))


def canonical(profile):
    n = len(profile)
    return min(relabel(profile, agents, objects)
               for agents in permutations(range(n))
               for objects in permutations(range(n)))


def three_agent_tests():
    prefs = tuple(permutations(range(3)))
    counts, exceptional_classes = Counter(), Counter()
    unusual = 0
    for profile in product(prefs, repeat=3):
        probabilities = priority_rule(profile)
        for order, weight in probabilities.items():
            assert probabilities.get(order[::-1], Fraction(0)) == weight
        assert sum(probabilities.values()) == 1
        target = probabilistic_serial(profile)
        implemented = priority_matrix(profile, probabilities)
        assert target == implemented, (profile, target, implemented)
        dec_ef(profile, probabilities)
        key = canonical(profile)
        counts[key] += 1
        baseline = priority_matrix(profile, {
            order: Fraction(1, 6) for order in permutations(range(3))
        })
        is_special = len(probabilities) == 4
        assert (target != baseline) == is_special
        if is_special:
            unusual += 1
            exceptional_classes[key] += 1
            distances = [sum(abs(target[i][j] - baseline[i][j])
                             for j in range(3)) / 2 for i in range(3)]
            assert sorted(distances) == [0, Fraction(1, 12), Fraction(1, 12)]
    assert len(counts) == 10
    assert sorted(counts.values()) == [6, 12, 18, 18, 18, 18, 18, 36, 36, 36]
    assert unusual == 72 and sorted(exceptional_classes.values()) == [36, 36]
    assert sum(counts.values()) == 216
    print('3x3: 216 strict profiles; 10 symmetry classes; 72 four-priority cases')
    for k in sorted(counts):
        kind = 'four' if k in exceptional_classes else 'six'
        print('   ', ''.join(''.join(str(x) for x in p) + ' ' for p in k),
              'size', counts[k], 'priority law', kind)


def two_agent_tests():
    prefs = tuple(permutations(range(2)))
    for profile in product(prefs, repeat=2):
        law = priority_rule(profile)
        assert probabilistic_serial(profile) == priority_matrix(profile, law)
        dec_ef(profile, law)
    print('2x2: 4 strict profiles all implemented')


def four_agent_obstruction():
    # Example 5 of Kawase, Suksompong, Sumita and Yokoi (2026).
    profile = ((0, 1, 2, 3), (0, 1, 2, 3),
               (0, 2, 1, 3), (2, 0, 1, 3))
    matrix = probabilistic_serial(profile)
    assert matrix[2][0] == Fraction(1, 3)
    assert matrix[2][1] == Fraction(1, 12)
    assert matrix[2][0] + matrix[2][1] == Fraction(5, 12)
    paired = set()
    for order in permutations(range(4)):
        if order in paired:
            continue
        reverse = order[::-1]
        paired.add(order)
        paired.add(reverse)
        left = serial_dictatorship(profile, order)[2]
        right = serial_dictatorship(profile, reverse)[2]
        assert (left in (0, 1)) + (right in (0, 1)) == 1
    assert len(paired) == 24
    # Thus any reversal-symmetric priority law would give probability 1/2,
    # in contradiction with the PS probability 5/12.
    print('4x4: source obstruction independently checked (12 reversal pairs)')


if __name__ == '__main__':
    two_agent_tests()
    three_agent_tests()
    four_agent_obstruction()
    print('ALL EXACT CHECKS PASSED')
