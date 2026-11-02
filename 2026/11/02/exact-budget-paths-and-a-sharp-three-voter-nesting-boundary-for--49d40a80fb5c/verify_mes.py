"""Exact-rational checks for budget nesting of uncompleted equal shares.

No floating-point arithmetic or heuristic stopping criteria are used.
Usage: python3 verify_mes.py
"""
from fractions import Fraction
from itertools import combinations_with_replacement, product


def affordable_price(balances, supporters):
    """Minimum uniform cap that raises one unit, or None if unaffordable."""
    caps = sorted(balances[i] for i in supporters)
    if not caps or sum(caps, Fraction(0)) < 1:
        return None
    paid = Fraction(0)
    for j, cap in enumerate(caps):
        price = (1 - paid) / (len(caps) - j)
        if price <= cap:
            return price
        paid += cap
    raise AssertionError("A fundable candidate has no price")


def mes(ballots, m, budget):
    """Uncompleted approval MES, unit costs, fixed candidate order 0,1,... ."""
    n = len(ballots)
    assert n > 0 and budget >= 0
    balances = [Fraction(budget, n)] * n
    remaining = set(range(m))
    chosen = []
    charges = []
    while remaining:
        options = []
        for c in sorted(remaining):
            supporters = [i for i, ballot in enumerate(ballots) if c in ballot]
            price = affordable_price(balances, supporters)
            if price is not None:
                options.append((price, c, supporters))
        if not options:
            break
        price, c, supporters = min(options, key=lambda rec: (rec[0], rec[1]))
        for i in supporters:
            balances[i] -= min(price, balances[i])
            assert balances[i] >= 0
        remaining.remove(c)
        chosen.append(c)
        charges.append((c, price))
    return frozenset(chosen), charges


def predicted_sunflower(ballots, budget):
    """Return exact all-budget normal form, or None if not a sunflower."""
    ballots = [frozenset(v) for v in ballots]
    types = sorted(set(ballots), key=lambda s: (len(s), tuple(sorted(s))))
    core = set.intersection(*(set(s) for s in types))
    petals = [set(s) - core for s in types]
    for i in range(len(petals)):
        for j in range(i + 1, len(petals)):
            if petals[i].intersection(petals[j]):
                return None
    u = len(core)
    taken = set(sorted(core)[:min(u, budget.numerator // budget.denominator)])
    if budget >= u:
        n = len(ballots)
        for typ, petal in zip(types, petals):
            ni = sum(v == typ for v in ballots)
            limit = ni * (budget - u) / n
            limit = limit.numerator // limit.denominator
            taken.update(sorted(petal)[:min(len(petal), limit)])
    return frozenset(taken)


def check():
    cases = 0
    # All pairs of ballot types on at most 4 projects; unequal multiplicities.
    for m in range(1, 5):
        masks = [frozenset(c for c in range(m) if bits & (1 << c))
                 for bits in range(1 << m)]
        for s, t in combinations_with_replacement(masks, 2):
            for a, b in product(range(1, 5), repeat=2):
                ballots = (s,) * a + (t,) * b
                preceding = frozenset()
                for step in range(0, 3 * (m + 2) + 1):
                    budget = Fraction(step, 3)
                    predicted = predicted_sunflower(ballots, budget)
                    actual, _ = mes(ballots, m, budget)
                    assert predicted == actual, (m, ballots, budget, predicted, actual)
                    assert preceding <= actual
                    preceding = actual
                    cases += 1
    # Exhaust all 5-project three-petal sunflower patterns, three population splits.
    m = 5
    for assignments in product(range(5), repeat=m):
        # Codes: 0 unapproved, 1 core, 2/3/4 belong to private petals.
        patterns = tuple(frozenset(c for c, t in enumerate(assignments)
                                   if t == 1 or t == i + 2) for i in range(3))
        for counts in ((1, 1, 1), (1, 2, 3), (3, 2, 1)):
            ballots = tuple(b for b, num in zip(patterns, counts) for _ in range(num))
            for step in range(0, 3 * (m + 2) + 1, 2):
                budget = Fraction(step, 3)
                actual, _ = mes(ballots, m, budget)
                predicted = predicted_sunflower(ballots, budget)
                assert actual == predicted, (assignments, counts, budget, actual, predicted)
                cases += 1
    # Three voters and four candidates, lexicographic ties, exact threshold witness.
    ballots = (
        frozenset((0, 1)),
        frozenset((0, 1, 3)),
        frozenset((2, 3)),
    )
    at_three, stages_three = mes(ballots, 4, Fraction(3))
    at_four, stages_four = mes(ballots, 4, Fraction(4))
    assert at_three == frozenset((0, 1, 2))
    assert at_four == frozenset((0, 1, 3))
    assert not at_three.issubset(at_four)
    assert stages_three == [(0, Fraction(1, 2)), (1, Fraction(1, 2)),
                            (2, Fraction(1))]
    assert stages_four == [(0, Fraction(1, 2)), (1, Fraction(1, 2)),
                           (3, Fraction(2, 3))]
    print(f"PASS: {cases} exact sunflower formula cases; "
          "three-voter nonnesting witness, budgets 3 and 4.")


if __name__ == "__main__":
    check()
