#!/usr/bin/env python3
"""Exhaustive exact checker for two-coalition cutoff-cost deviation cycles."""
from fractions import Fraction
from itertools import combinations


def enemy_masks_from_bits(n, edge_bits):
    result = [0] * n
    for bit, (i, j) in enumerate(combinations(range(n), 2)):
        if edge_bits & (1 << bit):
            result[i] |= 1 << j
            result[j] |= 1 << i
    return tuple(result)


def canonical(mask, full):
    return mask if not mask & ((full + 1) >> 1) else full ^ mask


def exact_edges(n, enemies):
    """All profitable jumps between unordered, nonempty two-coalition states."""
    full = (1 << n) - 1
    out = {}
    for left in range(1, 1 << (n - 1)):
        right = full ^ left
        choices = []
        for i in range(n):
            bit = 1 << i
            source = left if left & bit else right
            destination = full ^ source
            if source.bit_count() <= 1:
                continue  # happy-in-isolation: cost zero cannot strictly improve
            before_numerator = (enemies[i] & source).bit_count()
            after_numerator = (enemies[i] & destination).bit_count()
            if before_numerator * destination.bit_count() > after_numerator * (source.bit_count() - 1):
                new_left = canonical(left ^ bit, full)
                assert 1 <= new_left < (1 << (n - 1))
                choices.append((new_left, i))
        out[left] = choices
    return out


def has_directed_cycle(adj):
    state = {vertex: 0 for vertex in adj}
    def visit(u):
        state[u] = 1
        for v, _ in adj[u]:
            if state[v] == 1:
                return True
            if state[v] == 0 and visit(v):
                return True
        state[u] = 2
        return False
    return any(visit(u) for u in adj if state[u] == 0)


def verify_lower_bound():
    graph_count = state_count = edge_count = 0
    for n in range(2, 6):
        num_edges = n * (n - 1) // 2
        for bits in range(1 << num_edges):
            enemies = enemy_masks_from_bits(n, bits)
            adj = exact_edges(n, enemies)
            assert not has_directed_cycle(adj), (n, bits)
            graph_count += 1
            state_count += len(adj)
            edge_count += sum(len(x) for x in adj.values())
    assert graph_count == 1098
    assert state_count == 15834
    return graph_count, state_count, edge_count


def verify_six_agent_cycle():
    values = (0, 9, 18, 26, 27, 28)
    threshold = 10
    n = len(values)
    enemy = [0] * n
    for i, j in combinations(range(n), 2):
        if abs(values[i] - values[j]) > threshold:
            enemy[i] |= 1 << j
            enemy[j] |= 1 << i
    # State masks represent the first coalition, with agents numbered 1,...,6.
    states = (30, 31, 27, 25, 17, 16, 20, 22, 30)
    movers = (0, 2, 1, 3, 0, 2, 1, 3)
    gain_pairs = []
    full = (1 << n) - 1
    for source_mask, target_mask, who in zip(states, states[1:], movers):
        assert target_mask == source_mask ^ (1 << who)
        old = source_mask if source_mask & (1 << who) else full ^ source_mask
        new = full ^ old
        assert old.bit_count() >= 2 and new.bit_count() >= 1
        old_cost = Fraction((enemy[who] & old).bit_count(), old.bit_count() - 1)
        new_cost = Fraction((enemy[who] & new).bit_count(), new.bit_count())
        assert new_cost < old_cost
        gain_pairs.append((str(old_cost), str(new_cost)))
    assert states[0] == states[-1]
    assert gain_pairs == [('1', '3/4'), ('1/4', '0'), ('2/3', '1/2'), ('1/2', '1/3')] * 2
    # Independently ensure that the complete state graph actually contains a cycle.
    assert has_directed_cycle(exact_edges(n, tuple(enemy)))
    return values, threshold, states, movers, gain_pairs


def main():
    graphs, states, edges = verify_lower_bound()
    values, threshold, cycle, movers, gains = verify_six_agent_cycle()
    print(f'LOWER_OK graphs={graphs} states={states} profitable_edges={edges}')
    print(f'WITNESS_OK values={values} cutoff={threshold} states={cycle} movers={tuple(i+1 for i in movers)}')
    print(f'GAIN_PAIRS={gains}')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
