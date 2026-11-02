"""Independent finite checks for the prism minimum-zero-forcing classification.

Run: python verify.py
The exhaustive search is supplemental: the accompanying structural proof is
needed for the assertion at all n.
"""
from itertools import combinations


def vert(n, row, column):
    return row * n + column % n


def neighbours(n):
    return [frozenset((vert(n, row, j - 1),
                       vert(n, row, j + 1), vert(n, 1-row, j)))
            for row in (0, 1) for j in range(n)]


def forces_all(adj, seed):
    """Simultaneous colour changes, independent of a chosen force sequence."""
    black = set(seed)
    while True:
        newly = set()
        for u in black:
            remaining = adj[u] - black
            if len(remaining) == 1:
                newly.update(remaining)
        if not newly:
            return len(black) == len(adj)
        black.update(newly)


def sequential_forces_all(adj, seed):
    """A separately implemented greedy, one-force-at-a-time procedure."""
    black = set(seed)
    while True:
        changed = False
        for u in range(len(adj)):
            if u not in black:
                continue
            missing = [v for v in adj[u] if v not in black]
            if len(missing) == 1:
                black.add(missing[0])
                changed = True
                break
        if not changed:
            return len(black) == len(adj)


def predicted(n):
    d = {k: set() for k in 'ABCDE'}
    for row in (0, 1):
        for i in range(n):
            d['A'].add(frozenset(vert(n, row, i+j) for j in range(4)))
            for e in (-1, 1):
                d['B'].add(frozenset((vert(n, row, i),
                                      vert(n, row, i+e),
                                      vert(n, row, i+2*e),
                                      vert(n, 1-row, i))))
                d['C'].add(frozenset((vert(n, row, i),
                                      vert(n, row, i+e),
                                      vert(n, row, i+3*e),
                                      vert(n, 1-row, i+e))))
    for i in range(n):
        for e in (-1, 1):
            d['D'].add(frozenset((vert(n, 0, i), vert(n, 0, i+e),
                                  vert(n, 1, i), vert(n, 1, i-e))))
        d['E'].add(frozenset((vert(n, 0, i), vert(n, 0, i+1),
                              vert(n, 1, i), vert(n, 1, i+1))))
    return d


def orbit(n, seed):
    return {frozenset(vert(n, (u//n)^sw, a+b*(u % n)) for u in seed)
            for sw in (0, 1) for a in range(n) for b in (-1, 1)}


if __name__ == '__main__':
    n3 = 0
    n4 = 0
    all_four = 0
    for n in range(5, 17):
        adj = neighbours(n)
        d = predicted(n)
        predicted_sizes = dict(zip('ABCDE', (2*n, 4*n, 4*n, 2*n, n)))
        known = set()
        for k, members in d.items():
            assert len(members) == predicted_sizes[k], (n, k, 'size')
            assert not known.intersection(members), (n, k, 'overlap')
            known.update(members)
            assert orbit(n, next(iter(members))) == members, (n, k, 'orbit')
            assert all(forces_all(adj, s) for s in members), (n, k, 'not forcing')
        assert len(known) == 13*n
        if n <= 13:
            actual_three = {frozenset(s) for s in combinations(range(2*n), 3)
                            if forces_all(adj, s)}
            assert not actual_three, (n, 'three-seed counterexample')
            n3 += 1
            actual_four = set()
            for s in combinations(range(2*n), 4):
                a = forces_all(adj, s)
                b = sequential_forces_all(adj, s)
                assert a == b, (n, s, 'forcing disagreement')
                if a:
                    actual_four.add(frozenset(s))
                all_four += 1
            assert known == actual_four, (n, 'classification mismatch')
            n4 += 1
        # The finite check also tests the local first-force boundary.
        if n <= 16:
            allowed = {vert(n, 0, 2), vert(n, 0, -2),
                       vert(n, 1, -1), vert(n, 1, 1)}
            for core, newly in (({vert(n, 0, -1), vert(n, 0, 0), vert(n, 0, 1)},
                                 vert(n, 1, 0)),
                                ({vert(n, 0, 0), vert(n, 0, 1), vert(n, 1, 0)},
                                 vert(n, 0, -1))):
                for x in set(range(2*n)) - core - {newly} - allowed:
                    black = core | {newly, x}
                    assert all(len(adj[u] - black) != 1 for u in black), (n, x, 'local boundary')
    print('VERIFY_OK complete_n=5..13 constructive_n=5..16 '
          f'exhaustive_three_sizes={n3} exhaustive_four_sizes={n4} '
          f'four_subsets_checked={all_four} families_per_n=5 exact_count=13n')
