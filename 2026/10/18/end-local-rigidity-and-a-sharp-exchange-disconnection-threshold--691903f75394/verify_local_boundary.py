"""Certify the three-column seed test with a white guard at column 4."""
from itertools import combinations, product

GRID = set(product(range(5), range(3)))
FIRST = {v for v in GRID if v[0] < 3}
NEIGHBORS = {
    (c, r): GRID.intersection(((c-1, r), (c+1, r), (c, r-1), (c, r+1)))
    for c, r in GRID
}


def test(seed):
    blue = set(seed)
    rounds = 0
    while not FIRST <= blue:
        assert all(c < 4 for c, r in blue)
        targets = set()
        for u in blue:
            missing = NEIGHBORS[u] - blue
            if len(missing) == 1:
                targets.update(missing)
        if not targets:
            return None
        assert all(c < 4 for c, r in targets), (seed, blue, targets)
        blue.update(targets)
        rounds += 1
    assert blue == FIRST, (seed, blue)
    return rounds


def main():
    expect = {
        (0, 1, 2): 2, (0, 1, 4): 3, (0, 1, 6): 5,
        (0, 2, 3): 3, (0, 2, 5): 3, (0, 3, 4): 4,
        (0, 3, 6): 4, (1, 2, 4): 3, (1, 2, 8): 5,
        (2, 4, 5): 4, (2, 5, 8): 4, (3, 4, 6): 5, (4, 5, 8): 5,
    }
    observed = {}
    rejected = 0
    for ids in combinations(range(9), 3):
        rounds = test(tuple(divmod(i, 3) for i in ids))
        if rounds is None:
            rejected += 1
        else:
            observed[ids] = rounds
    assert observed == expect and rejected == 71, (observed, rejected)
    print('local boundary: 13 full prefixes, 71 closed sets, no early force into column 4')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
