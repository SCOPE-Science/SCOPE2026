#!/usr/bin/env python3
"""Independent finite local-factor certificate for locating-total domination of prism graphs.

Run: python3 verify_prism.py
"""
from itertools import combinations

BASE = (3, 1, 0, 3, 0, 3, 0, 0)
BLOCK = (3, 0, 3, 0, 0)
EXPECTED = {
    '00303', '00310', '03003', '03030', '03103',
    '10303', '30030', '30031', '30300', '31030',
}

def word(k):
    assert isinstance(k, int) and k >= 0
    return BASE + BLOCK * k


def factors(w):
    n = len(w)
    return {''.join(str(w[(i+j) % n]) for j in (-1, 0, 1, 2, 3))
            for i in range(n)}


def selected_from_local(window):
    # Five columns have relative indices -1, 0, 1, 2, 3.
    return {(j-1, s) for j, digit in enumerate(window)
            for s in (0, 1) if int(digit) & (1 << s)}


def nbr(i, s):
    return {(i-1, s), (i+1, s), (i, 1-s)}


def test_window(window):
    chosen = selected_from_local(window)
    tests = 0
    for side in (0, 1):
        origin = (0, side)
        footprint = nbr(*origin) & chosen
        # Total domination, including initially selected vertices.
        if not footprint:
            return False, ('undominated', origin), tests
        if origin in chosen:
            continue
        # In a prism with circumference at least 8, nonempty equal
        # footprints can arise only at these two relative offsets.
        for target in ((1, 1-side), (2, side)):
            if target in chosen:
                continue
            tests += 1
            if footprint == (nbr(*target) & chosen):
                return False, ('equal', origin, target), tests
    return True, None, tests


def graph_ltd(w):
    n = len(w)
    selected = {(i, side) for i, code in enumerate(w)
                for side in (0, 1) if code & (1 << side)}
    neighborhoods = {}
    for i in range(n):
        for side in (0, 1):
            vertex = (i, side)
            all_neighbors = {((i-1) % n, side),
                             ((i+1) % n, side), (i, 1-side)}
            footprint = all_neighbors & selected
            if not footprint:
                return False
            neighborhoods[vertex] = frozenset(footprint)
    outside = [v for v in neighborhoods if v not in selected]
    return len({neighborhoods[v] for v in outside}) == len(outside)


def run():
    windows = factors(word(0)) | factors(word(1)) | factors(word(2))
    assert windows == EXPECTED, ('factor table differs', windows)
    counts = {}
    for window in sorted(windows):
        passed, reason, checked = test_window(window)
        assert passed, (window, reason)
        counts[window] = checked
    # The infinite extension uses the following finite combinatorial fact:
    # every window of BASE BLOCK^k lies within one of BASE, BLOCK,
    # BASE/BLOCK, BLOCK/BASE, or BLOCK/BLOCK interfaces. The windows
    # of BASE, BASE+BLOCK and BASE+BLOCK+BLOCK cover all five types.
    for k in range(12):
        assert factors(word(k)) <= EXPECTED
        assert len(word(k)) == 8 + 5*k
        assert sum(int(d).bit_count() for d in word(k)) == 7+4*k
        assert graph_ltd(word(k)), ('direct_graph', k)
    # Directly reconstruct the original graph, not the local certificate,
    # for every smaller cardinality at the first counterexample n=8.
    n = 8
    for size in range(7):
        for comb in combinations(range(2*n), size):
            w = [0]*n
            for idx in comb:
                w[idx//2] |= 1 << (idx % 2)
            assert not graph_ltd(w), ('unexpected smaller configuration', comb)
    print('CERTIFICATE_OK')
    print('window_count=10')
    print('windows=' + ','.join(sorted(windows)))
    print('pair_tests_in_local_table=' + str(sum(counts.values())))
    print('direct_graph_witnesses_n=8,13,...,63')
    print('n8_exhaustive_smaller_cardinalities=0..6')

if __name__ == '__main__':
    run()
