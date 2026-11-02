"""Exact small-period orbit census for loopless book graphs.

Uses only the Python standard library. No paper text or external data is embedded.
"""
from itertools import combinations, product
from math import comb


def words(q, k):
    return [tuple(int(t in cc) for t in range(q))
            for cc in combinations(range(q), k)]


def leaves(core_a, core_b):
    q = len(core_a)
    drive = [core_a[t] + core_b[t] for t in range(q)]
    result = []
    for initial in range(4):
        y = initial
        fire = []
        for input_ in drive:
            f = int(y >= 2)
            fire.append(f)
            y += input_ - 2*f
        if y == initial:
            result.append((initial, tuple(fire)))
    return result


def core_interval(core, other, leaf_fires, m):
    degree = m + 1
    height_change = 0
    low, high = 0, 2 * degree - 1
    for t in range(len(core)):
        if core[t]:
            low = max(low, degree - height_change)
        else:
            high = min(high, degree - 1 - height_change)
        height_change += other[t] + leaf_fires[t] - degree * core[t]
    assert height_change == 0
    return max(0, high - low + 1)


def word_class_counts(q, m):
    totals = {k: 0 for k in range(1, q)}
    good_pairs = {k: set() for k in range(1, q)}
    for k in range(1, q):
        for a in words(q, k):
            for b in words(q, k):
                leaf_options = leaves(a, b)
                assert len(leaf_options) == 2, (q, a, b, leaf_options)
                for j in range(m + 1):
                    s = [j * leaf_options[0][1][t] +
                         (m - j) * leaf_options[1][1][t] for t in range(q)]
                    multiplicity = (core_interval(a, b, s, m) *
                                    core_interval(b, a, s, m))
                    if multiplicity:
                        good_pairs[k].add((a, b))
                    totals[k] += comb(m, j) * multiplicity
    return totals, good_pairs


def direct_counts(m):
    degree = m + 1
    period3, period4 = 0, 0
    ranges = [range(2 * degree), range(2 * degree)] + [range(4)] * m
    for initial in product(*ranges):
        states = [initial]
        for _ in range(4):
            u, v, *z = states[-1]
            a, b = int(u >= degree), int(v >= degree)
            fs = [int(y >= 2) for y in z]
            num_fires = sum(fs)
            states.append((u + b + num_fires - degree * a,
                           v + a + num_fires - degree * b,
                           *(y + a + b - 2 * f for y, f in zip(z, fs))))
        if states[3] == initial and states[1] != initial:
            period3 += 1
        if states[4] == initial and states[2] != initial:
            period4 += 1
    return period3 // 3, period4 // 4, period3, period4


def main():
    # Exhaust all possible hub firing words, all peripheral phase types,
    # and all peripheral type populations for each listed m.
    for m in range(1, 26):
        c3, p3 = word_class_counts(3, m)
        c4, p4 = word_class_counts(4, m)
        expect3 = m * 2 ** (m + 1)
        expect4 = m * (m - 1) * 2 ** (m - 1)
        assert sum(c3.values()) == 3 * expect3, (m, c3)
        assert c4[1] + c4[3] == 4 * expect4, (m, c4)
        assert len(p3[1]) == 6 and len(p3[2]) == 6
        assert len(p4[1]) == len(p4[3]) == (4 if m >= 2 else 0)
        assert len(p4[2]) == 4
        assert all(a in ((1, 0, 1, 0), (0, 1, 0, 1)) and
                   b in ((1, 0, 1, 0), (0, 1, 0, 1))
                   for a, b in p4[2])
        if m <= 6:
            direct3, direct4, s3, s4 = direct_counts(m)
            assert (direct3, direct4) == (expect3, expect4), (m, direct3, direct4)
            print(f'm={m}: microscopic period-3 states={s3}, period-4 states={s4}; '
                  f'primitive orbits={direct3},{direct4}; verified')
    print('Symbolic-firing-word parametrization confirmed at m=1..25.')
    print('Book graph phase census: BOOK_PHASE_34_VERIFY_OK')

if __name__ == '__main__':
    main()
