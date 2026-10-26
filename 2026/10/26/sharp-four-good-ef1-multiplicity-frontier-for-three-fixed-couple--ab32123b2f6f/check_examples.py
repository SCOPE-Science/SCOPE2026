"""Independent direct EF1 calculation for sharpness examples; stdlib only."""
from itertools import product


def valid_allocation(values, assignment):
    """Literal cardinal EF1 definition, with six agents grouped in three couples."""
    bundles = [[i for i, g in enumerate(assignment) if g == j] for j in range(3)]
    for group in range(3):
        for agent in values[group]:
            mine = sum(agent[item] for item in bundles[group])
            for other in range(3):
                if other == group:
                    continue
                others = [item for item in bundles[other]]
                if mine < sum(agent[item] for item in others) - max(
                    [agent[item] for item in others] + [0]
                ):
                    return False
    return True


four_values = [
    [(4, 3, 2, 1), (4, 1, 2, 3)],
    [(4, 3, 2, 1), (1, 2, 4, 3)],
    [(4, 1, 3, 2), (2, 4, 1, 3)],
]
four_fair = [
    tuple(a) for a in product(range(3), repeat=4)
    if sorted(a.count(i) for i in range(3)) == [1, 1, 2]
    and valid_allocation(four_values, a)
]
assert four_fair == [(0, 1, 1, 2), (0, 2, 1, 2)], four_fair
print("four_goods_exactly_two", four_fair)

five_values = [
    [(2, 2, 0, 0, 1), (0, 0, 2, 2, 1)],
    [(0, 2, 0, 2, 1), (2, 0, 2, 0, 1)],
    [(2, 0, 0, 2, 1), (0, 2, 2, 0, 1)],
]
five_fair = [a for a in product(range(3), repeat=5)
             if valid_allocation(five_values, a)]
assert not five_fair, five_fair
print("five_goods_no_EF1", len(five_fair))
