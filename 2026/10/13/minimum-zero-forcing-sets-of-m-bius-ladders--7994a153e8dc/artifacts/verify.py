#!/usr/bin/env python3
from itertools import combinations

MAX_N = 12


def adjacency(n):
    N = 2 * n
    adj = [set() for _ in range(N)]
    for v in range(N):
        for w in ((v - 1) % N, (v + 1) % N, (v + n) % N):
            adj[v].add(w)
    return adj


def is_zero_forcing(n, initial):
    adj = adjacency(n)
    blue = set(initial)
    while True:
        move = None
        for v in sorted(blue):
            white_neighbors = adj[v] - blue
            if len(white_neighbors) == 1:
                move = next(iter(white_neighbors))
                break
        if move is None:
            return len(blue) == 2 * n
        blue.add(move)


def local_criterion(n, initial):
    N = 2 * n
    adj = adjacency(n)
    S = set(initial)
    for v in S:
        blue_neighbors = adj[v] & S
        if len(blue_neighbors) != 2:
            continue
        rest = S - ({v} | blue_neighbors)
        if len(rest) != 1:
            continue
        d = next(iter(rest))
        allowed = {
            (v + 2) % N,
            (v - 2) % N,
            (v + n - 1) % N,
            (v + n + 1) % N,
        }
        if d in allowed:
            return True
    return False


def dihedral_orbit(n, initial):
    N = 2 * n
    S = set(initial)
    ans = set()
    for shift in range(N):
        ans.add(tuple(sorted((x + shift) % N for x in S)))
        ans.add(tuple(sorted((-x + shift) % N for x in S)))
    return ans


def main():
    subset_checks = 0
    criterion_checks = 0
    orbit_checks = 0

    # Boundary case: M_6 is K_{3,3}; its minimum zero forcing sets are
    # exactly the complements of one vertex from each bipartition class.
    n = 3
    min_sets = []
    for S in combinations(range(2 * n), 4):
        subset_checks += 1
        if is_zero_forcing(n, S):
            min_sets.append(S)
    if len(min_sets) != 9:
        raise AssertionError(('n=3 count', len(min_sets)))

    for n in range(4, MAX_N + 1):
        all_four = list(combinations(range(2 * n), 4))
        zf = set()
        crit = set()
        for S in all_four:
            subset_checks += 1
            if is_zero_forcing(n, S):
                zf.add(S)
            criterion_checks += 1
            if local_criterion(n, S):
                crit.add(S)

        reps = [
            (0, 1, 2, 3),
            (0, 1, 2, n),
            (0, 1, 3, n + 1),
            (0, 1, n - 1, n),
            (0, 1, n, n + 1),
        ]
        orbits = [dihedral_orbit(n, r) for r in reps]
        orbit_checks += sum(len(o) for o in orbits)
        expected_sizes = [2 * n, 4 * n, 4 * n, 2 * n, n]
        if [len(o) for o in orbits] != expected_sizes:
            raise AssertionError(('orbit sizes', n, [len(o) for o in orbits]))
        for i in range(5):
            for j in range(i + 1, 5):
                if orbits[i] & orbits[j]:
                    raise AssertionError(('orbit overlap', n, i, j))
        classified = set().union(*orbits)
        if zf != crit or zf != classified:
            raise AssertionError(('classification', n, len(zf), len(crit), len(classified)))
        if len(zf) != 13 * n:
            raise AssertionError(('count', n, len(zf), 13 * n))

    print(
        'VERIFY_OK '
        f'n_boundary=3 boundary_count=9 n_range=4..{MAX_N} '
        f'subset_checks={subset_checks} criterion_checks={criterion_checks} '
        f'orbit_checks={orbit_checks} count_formula=13n max_order={2 * MAX_N}'
    )


if __name__ == '__main__':
    main()
