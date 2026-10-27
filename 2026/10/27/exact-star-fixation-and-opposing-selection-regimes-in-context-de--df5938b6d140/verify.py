"""Exact finite-state consistency checks for a state-dependent star-voter model.

Uses only the Python standard library. These finite computations are checks,
not a substitute for the all-size mathematical proof.
"""
from fractions import Fraction as F


def fixation(m, a, b, hub, leaves):
    q = b / a
    R = (1 + q / m) / (1 + 1 / (q * m))
    powers = [R**j for j in range(m)]
    Z = 1 + q / m * sum(powers)
    if hub == 0:
        return sum(R**j for j in range(1, leaves + 1)) / (q * m * Z)
    return (1 + q / m * sum(powers[:leaves])) / Z


def exact_check(m, a, b):
    n = m + 1
    assert a > 0 and b > 0 and a <= 1 and b <= 1
    r = F(b, a) if isinstance(a, int) else b / a
    R = (1 + r / m) / (1 + 1 / (r * m))
    Z = 1 + r / m * sum(R**j for j in range(m))
    trials = 0
    for mask in range(1 << n):
        hub = mask & 1
        leaves = (mask >> 1).bit_count()
        current = fixation(m, a, b, hub, leaves)
        delta = F(0)
        for leaf in range(1, n):
            leaf_color = (mask >> leaf) & 1
            if hub == leaf_color:
                continue
            accept_hub = a if hub == 0 else b
            accept_leaf = a if leaf_color == 0 else b
            hub_after = fixation(m, a, b, leaf_color, leaves)
            new_leaves = leaves + (1 if hub else -1)
            leaf_after = fixation(m, a, b, hub, new_leaves)
            delta += accept_hub * (hub_after - current) / (n * m)
            delta += accept_leaf * (leaf_after - current) / n
            trials += 2
        assert delta == 0, (m, a, b, mask, delta)
        if mask == 0:
            assert current == 0
        if mask == (1 << n) - 1:
            assert current == 1
    assert fixation(m, a, b, 1, 0) == 1 / Z
    assert fixation(m, a, b, 0, 1) == R / (r * m * Z)
    star_uniform = (fixation(m, a, b, 1, 0) + m * fixation(m, a, b, 0, 1)) / n
    assert star_uniform == (1 + R / r) / (n * Z)
    if a == b:
        assert star_uniform == F(1, n)
    return trials, 1 << n


if __name__ == '__main__':
    tests = [(F(1, 2), F(1, 2)),
             (F(2, 3), F(1, 4)),
             (F(1, 5), F(3, 5)),
             (F(1), F(1, 10)),
             (F(1, 10), F(1))]
    checked = 0
    transition_comparisons = 0
    for m in range(2, 9):
        for a, b in tests:
            comparisons, states = exact_check(m, a, b)
            transition_comparisons += comparisons
            checked += states
    print(f"PASS: {len(tests) * 7} rational parameter-star cases, "
          f"{checked} labeled configurations and "
          f"{transition_comparisons} exact transition-drift terms.")
