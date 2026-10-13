#!/usr/bin/env python3
"""Exact small-frame tests for iteration of the non-contingency modality."""
from itertools import product


def noncontingency(successors, values):
    return sum(1 << i for i, neighbors in enumerate(successors)
               if not (neighbors & values) or (neighbors & values) == neighbors)


def is_transitive(successors):
    return all(not (successors[j] & ~successors[i])
               for i in range(len(successors))
               for j in range(len(successors)) if successors[i] & (1 << j))


def is_reflexive(successors):
    return all(successors[i] & (1 << i) for i in range(len(successors)))


def stabilization(n):
    return 1 if n == 1 else (2 if n == 2 else n - 1)


def strict_order(n):
    return tuple(sum(1 << j for j in range(i + 1, n)) for i in range(n))


def test_exhaustive(max_worlds=4):
    counts = {}
    total_valuations = 0
    for n in range(1, max_worlds + 1):
        transitive = 0
        reflexive_transitive = 0
        checks = 0
        for relation in product(range(1 << n), repeat=n):
            if not is_transitive(relation):
                continue
            transitive += 1
            reflexive = is_reflexive(relation)
            reflexive_transitive += int(reflexive)
            for valuation in range(1 << n):
                values = valuation
                iterates = [values]
                for _ in range(max(n + 2, 5)):
                    values = noncontingency(relation, values)
                    iterates.append(values)
                k = stabilization(n)
                assert iterates[k] == iterates[k + 1], (n, relation, valuation, iterates)
                if reflexive:
                    assert iterates[2] == iterates[3], (n, relation, valuation, iterates)
                for t in range(1, len(iterates) - 1):
                    if iterates[t] == iterates[t + 1]:
                        assert all(z == iterates[t] for z in iterates[t + 1:]), (n, relation, valuation)
                        break
                checks += 1
        counts[n] = (transitive, reflexive_transitive, checks)
        total_valuations += checks
    assert [counts[n][0] for n in range(1, 5)] == [2, 13, 171, 3994]
    assert [counts[n][1] for n in range(1, 5)] == [1, 4, 29, 355]
    assert total_valuations == 65328
    print('TRANSITIVE_FRAME_COUNTS', ','.join(f'{n}:{counts[n][0]}' for n in counts))
    print('REFLEXIVE_TRANSITIVE_COUNTS', ','.join(f'{n}:{counts[n][1]}' for n in counts))
    print('VALUATION_TESTS', total_valuations)


def test_sharpness(max_worlds=60):
    # Nonconstant choices at last two worlds force the first iterate
    # to equal exactly the two-world final segment of a strict order.
    for n in range(3, max_worlds + 1):
        frame = strict_order(n)
        valuation = 1 << (n - 1)
        current = valuation
        for k in range(1, n):
            current = noncontingency(frame, current)
            expected = sum(1 << j for j in range(max(0, n - 1 - k), n))
            assert current == expected, (n, k, current, expected)
        assert noncontingency(frame, current) == current
    # At two worlds, a complete accessibility relation with a split
    # valuation fails to stabilize at the first application.
    frame = (3, 3)
    first = noncontingency(frame, 1)
    second = noncontingency(frame, first)
    assert first == 0 and second == 3 and noncontingency(frame, second) == second
    print('SHARP_STRICT_ORDERS_TESTED', f'3..{max_worlds}')
    print('SHARP_TWO_WORLD_WITNESS', frame, first, second)


if __name__ == '__main__':
    test_exhaustive()
    test_sharpness()
    print('VERIFY_OK')
