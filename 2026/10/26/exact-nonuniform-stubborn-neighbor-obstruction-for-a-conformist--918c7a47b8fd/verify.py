"""Exact, independent finite checks for the two-hub conformist--rebel theorem."""
from itertools import product


def theorem_obstructs(p, q):
    m = len(p)
    assert m >= 2 and len(q) == m
    largest = max(p)
    smallest = min(q)
    peak = {i for i in range(m) if p[i] == largest}
    trough = {i for i in range(m) if q[i] == smallest}
    return len(trough) >= 2 and trough <= peak


def direct_equilibria(p, q):
    m = len(p)
    result = []
    for a, b in product(range(m), repeat=2):
        c_score = [p[i] + (i == b) for i in range(m)]
        r_cost = [q[i] + (i == a) for i in range(m)]
        if c_score[a] == max(c_score) and r_cost[b] == min(r_cost):
            result.append((a, b))
    return result


def witness(p, q):
    largest = max(p)
    smallest = min(q)
    peak = {i for i, x in enumerate(p) if x == largest}
    trough = {i for i, x in enumerate(q) if x == smallest}
    if not trough <= peak:
        return min(peak), min(trough - peak)
    if len(trough) == 1:
        a = next(iter(trough))
        return a, a
    return None


def run():
    total = 0
    obstruction_counts = {}
    for m in (2, 3, 4):
        bad = 0
        for p in product(range(3), repeat=m):
            for q in product(range(3), repeat=m):
                actual = direct_equilibria(p, q)
                criterion = theorem_obstructs(p, q)
                assert criterion == (not actual), (m, p, q, actual)
                proposed = witness(p, q)
                if criterion:
                    assert proposed is None
                    bad += 1
                else:
                    assert proposed in actual, (m, p, q, proposed, actual)
                total += 1
        obstruction_counts[m] = bad
    assert total == 81 + 729 + 6561
    assert obstruction_counts == {2: 9, 3: 63, 4: 501}
    # Exhaustive binary-valued counts for m=5 (1,024 instances).
    for p in product(range(2), repeat=5):
        for q in product(range(2), repeat=5):
            assert theorem_obstructs(p, q) == (not direct_equilibria(p, q))
    # First nonuniform obstruction when maximum degree matches strategy count.
    assert theorem_obstructs((0, 1, 1), (1, 0, 0))
    assert not direct_equilibria((0, 1, 1), (1, 0, 0))
    print('PASS: 7,371 ternary-count profiles and 1,024 binary-count profiles.')
    print('Nonexistence counts for m=2,3,4:', obstruction_counts)
    print('PASS: constructive witnesses and nonuniform three-strategy example.')


if __name__ == '__main__':
    run()
