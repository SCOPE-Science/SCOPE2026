"""Independent finite-instance checks for the complete-bipartite one-vacancy theorem.

Only Python's standard library is required. This checks instances, not the
unbounded theorem; the displayed combinatorial proof establishes that theorem.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import lcm


def potential(state, a, b):
    ca, cb = Counter(x for x in state[:a] if x), Counter(x for x in state[a:] if x)
    return sum(Fraction(n * (n - 1), 2 * (a - 1)) for n in ca.values()) + sum(
        Fraction(n * (n - 1), 2 * (b - 1)) for n in cb.values()
    )


def utility(state, position, a):
    label = state[position]
    assert label != 0
    neighbors = state[a:] if position < a else state[:a]
    occupied = [x for x in neighbors if x != 0]
    return (Fraction(sum(x != label for x in occupied), len(occupied))
            if occupied else Fraction(0))


def verify(a, b, k):
    n = a + b
    compared = improving = 0
    distinct_types = 0
    granularity = Fraction(1, lcm(a-1, b-1))
    bound = Fraction(n-2, 2)
    for zero_index in range(n):
        for labels in product(range(1, k+1), repeat=n-1):
            state = tuple(labels[:zero_index]) + (0,) + tuple(labels[zero_index:])
            if len(set(labels)) == k:
                distinct_types += 1
            p0 = potential(state, a, b)
            assert Fraction(0) <= p0 <= bound
            for origin in range(n):
                if origin == zero_index:
                    continue
                trial = list(state)
                trial[zero_index], trial[origin] = trial[origin], 0
                trial = tuple(trial)
                gain = utility(trial, zero_index, a) - utility(state, origin, a)
                change = potential(trial, a, b) - p0
                assert gain == change, (a,b,k,state,origin,gain,change)
                if (origin < a) == (zero_index < a):
                    assert change == 0
                if gain > 0:
                    assert gain >= granularity
                    improving += 1
                compared += 1
    return compared, improving, distinct_types


if __name__ == '__main__':
    count = gains = total_configs = 0
    for a,b,k in [(2,3,2),(2,3,3),(2,5,3),(3,4,3),(4,4,3),(4,5,3)]:
        moves, improving, fully_colored_states = verify(a,b,k)
        print(f'K_{{{a},{b}}}, {k} types: {moves} exact transitions; {improving} improvements; '
              f'{fully_colored_states} states using every type')
        count += moves
        gains += improving
        total_configs += fully_colored_states
    assert gains > 0
    assert total_configs > 0
    print(f'PASS: {count} exact transition identities, {gains} positive transitions')
