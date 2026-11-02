"""Independent finite evaluation of nested Sasaki implications on height-two orthomodular lattices."""
from itertools import product


def orthocomplement(m, x):
    if x == 0:
        return m + 1
    if x == m + 1:
        return 0
    return 1 + ((x - 1) ^ 1)


def meet(m, x, y):
    if x == 0 or y == 0:
        return 0
    if x == m + 1:
        return y
    if y == m + 1:
        return x
    return x if x == y else 0


def join(m, x, y):
    if x == m + 1 or y == m + 1:
        return m + 1
    if x == 0:
        return y
    if y == 0:
        return x
    return x if x == y else m + 1


def sasaki(m, x, y):
    return join(m, orthocomplement(m, x), meet(m, x, y))


def nested_weakening(m, values):
    a = values[0]
    outcome = a
    for b in reversed(values[1:]):
        outcome = sasaki(m, b, outcome)
    return sasaki(m, a, outcome)


def predicted_full(m, d):
    return m ** (d + 1) - m ** d - m * 2 ** (d - 1)


def predicted_atom(m, d):
    parity = (-1) ** d
    return (m - 1) ** (d + 1) + parity - m * (1 + parity) // 2


def direct_counts(m, d):
    universe = tuple(range(m + 2))
    atoms = tuple(range(1, m + 1))
    full = sum(
        nested_weakening(m, values) != m + 1
        for values in product(universe, repeat=d + 1)
    )
    pure = sum(
        nested_weakening(m, values) != m + 1
        for values in product(atoms, repeat=d + 1)
    )
    return full, pure


def transfer_counts(m, d, atom_only):
    permitted = list(range(1, m + 1)) if atom_only else list(range(m + 2))
    total = 0
    for a in range(1, m + 1):
        vector = [0] * (m + 2)
        vector[a] = 1
        for _ in range(d):
            nxt = [0] * (m + 2)
            for state, count in enumerate(vector):
                if count:
                    for b in permitted:
                        nxt[sasaki(m, b, state)] += count
            vector = nxt
        total += sum(count for x, count in enumerate(vector)
                     if sasaki(m, a, x) != m + 1)
    return total


def run():
    direct_instances = 0
    transfer_instances = 0
    for m in (2, 4, 6, 8):
        assert orthocomplement(m, orthocomplement(m, 1)) == 1
        for d in range(1, 5):
            expected = predicted_full(m, d), predicted_atom(m, d)
            if (m + 2) ** (d + 1) <= 200000:
                assert direct_counts(m, d) == expected, (m, d, 'direct')
                direct_instances += 1
            observed = transfer_counts(m, d, False), transfer_counts(m, d, True)
            assert observed == expected, (m, d, 'transfer', observed, expected)
            transfer_instances += 1
    for m in (2, 4, 6, 8, 10, 12):
        for d in (1, 2, 3, 5, 9, 20):
            assert transfer_counts(m, d, False) == predicted_full(m, d)
            assert transfer_counts(m, d, True) == predicted_atom(m, d)
            transfer_instances += 1
    print('ALL_CHECKS_OK', 'direct_instances=', direct_instances,
          'transfer_instances=', transfer_instances,
          'lattice_sizes=', '4,6,8,10,12,14')


if __name__ == '__main__':
    run()
