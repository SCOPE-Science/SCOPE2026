"""Direct checks of four explicit eight-point interval-order cover diagrams."""
from collections import Counter
from itertools import permutations

M1 = ((1, 0, 0, 0, 0, 0), (1, 0, 0, 0, 0), (1, 0, 1, 0),
      (2, 0, 0), (1, 0), (1,))
M2 = ((1, 0, 0, 0, 0, 0), (1, 0, 0, 0, 0), (1, 1, 0, 0),
      (1, 1, 0), (1, 0), (1,))
M3 = ((1, 0, 0, 0, 0, 0), (1, 0, 1, 0, 0), (2, 0, 0, 0),
      (1, 0, 0), (1, 0), (1,))
M4 = ((1, 0, 0, 0, 0, 0), (1, 1, 0, 0, 0), (1, 1, 0, 0),
      (1, 0, 0), (1, 0), (1,))


def strict_order(m):
    n = len(m)
    assert all(len(row) == n - i for i, row in enumerate(m))
    assert all(sum(row) for row in m)
    assert all(sum(m[i][j - i] for i in range(j + 1)) for j in range(n))
    cells = [(i, i + d) for i, row in enumerate(m)
             for d, c in enumerate(row) for _ in range(c)]
    assert len(cells) == 8
    return tuple(tuple(cells[i][1] < cells[j][0]
                       for j in range(8)) for i in range(8))


def cover(order):
    return tuple(tuple(order[i][j] and not any(
        order[i][k] and order[k][j] for k in range(8))
        for j in range(8)) for i in range(8))


def signature(edges, rounds):
    colors = [0] * 8
    for _ in range(rounds):
        newer = []
        for i in range(8):
            pred = tuple(sorted(Counter(colors[j] for j in range(8)
                                        if edges[j][i]).items()))
            succ = tuple(sorted(Counter(colors[j] for j in range(8)
                                        if edges[i][j]).items()))
            newer.append((colors[i], pred, succ))
        colors = newer
    return tuple(sorted(Counter(colors).items()))


def isomorphic(a, b):
    for p in permutations(range(8)):
        if all(a[i][j] == b[p[i]][p[j]] for i in range(8)
               for j in range(8)):
            return True
    return False


def main():
    orders = [strict_order(x) for x in (M1, M2, M3, M4)]
    covers = [cover(x) for x in orders]
    for index, (i, j) in enumerate(((0, 1), (2, 3)), 1):
        assert signature(covers[i], 2) == signature(covers[j], 2)
        assert signature(covers[i], 3) != signature(covers[j], 3)
        assert not isomorphic(orders[i], orders[j])
        print(f'pair_{index}: two_round_equal=True three_round_equal=False '
              f'order_isomorphic=False')
    for a, b in ((0, 2), (1, 3)):
        assert isomorphic(tuple(tuple(orders[a][j][i] for j in range(8))
                                for i in range(8)), orders[b])
    print('DUAL_WITNESSES_OK')


if __name__ == '__main__':
    main()
