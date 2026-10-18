"""Exhaustive two-round cover-relation refinement for finite interval orders.

Requires only Python 3.10+. Rows of a Fishburn matrix are stored as its
upper-triangular tails, and each admissible matrix is generated exactly once.
"""
from collections import Counter, defaultdict


def compositions(total, length):
    if length == 1:
        yield (total,)
    else:
        for first in range(total + 1):
            for tail in compositions(total - first, length - 1):
                yield (first,) + tail


def matrices(weight):
    for dim in range(1, weight + 1):
        def extend(row, left, tails, occupied):
            if row == dim:
                if left == 0 and all(occupied):
                    yield tails
                return
            for count in range(1, left - (dim - row - 1) + 1):
                for vec in compositions(count, dim - row):
                    filled = list(occupied)
                    for col, value in enumerate(vec, row):
                        if value:
                            filled[col] = True
                    if not all(filled[:row + 1]):
                        continue
                    yield from extend(row + 1, left - count,
                                      tails + (vec,), tuple(filled))
        for tails in extend(0, weight, (), (False,) * dim):
            yield tails


def cover(tails):
    intervals = []
    for a, row in enumerate(tails):
        for offset, multiplicity in enumerate(row):
            intervals.extend([(a, a + offset)] * multiplicity)
    n = len(intervals)
    smaller = [[intervals[i][1] < intervals[j][0]
                for j in range(n)] for i in range(n)]
    return tuple(tuple(smaller[i][j] and not any(
        smaller[i][k] and smaller[k][j] for k in range(n))
        for j in range(n)) for i in range(n))


def fingerprint(edge, rounds):
    n = len(edge)
    colors = [0] * n
    for _ in range(rounds):
        nxt = []
        for v in range(n):
            above = Counter(colors[w] for w in range(n) if edge[v][w])
            below = Counter(colors[w] for w in range(n) if edge[w][v])
            nxt.append((colors[v], tuple(sorted(below.items())),
                        tuple(sorted(above.items()))))
        colors = nxt
    return tuple(sorted(Counter(colors).items()))


def dual(tails):
    dim = len(tails)
    full = [[0] * dim for _ in range(dim)]
    for a, row in enumerate(tails):
        for delta, value in enumerate(row):
            full[a][a + delta] = value
    return tuple(tuple(full[dim - 1 - j][dim - 1 - i]
                       for j in range(i, dim)) for i in range(dim))


def main():
    counts = []
    first_collision_layer = []
    for n in range(1, 9):
        groups = defaultdict(list)
        total = 0
        for tails in matrices(n):
            total += 1
            groups[fingerprint(cover(tails), 2)].append(tails)
        collisions = [entry for entry in groups.values() if len(entry) > 1]
        counts.append(total)
        print(f'n={n} types={total} round2_classes={len(groups)} '
              f'colliding_classes={len(collisions)} '
              f'colliding_unordered_pairs={sum(len(g)*(len(g)-1)//2 for g in collisions)}')
        if n <= 7:
            assert not collisions
        else:
            assert len(collisions) == 2 and sorted(map(len, collisions)) == [2, 2]
            first_collision_layer = collisions
            print('exceptional_pairs=', repr(collisions))
            assert all(fingerprint(cover(a), 3) != fingerprint(cover(b), 3)
                       for a, b in collisions)
            assert {frozenset((dual(a), dual(b))) for a, b in collisions} == {
                frozenset(pair) for pair in collisions}
            print('round3_classes=', len({fingerprint(cover(t), 3) for t in matrices(8)}))
    assert counts == [1, 2, 5, 15, 53, 217, 1014, 5335]
    assert first_collision_layer
    print('FISHBURN_EXHAUSTIVE_OK')


if __name__ == '__main__':
    main()
