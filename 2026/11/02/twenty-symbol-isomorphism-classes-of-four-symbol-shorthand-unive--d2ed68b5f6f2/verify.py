#!/usr/bin/env python3
"""Independent exhaustive arithmetic verification for the four-letter shorthand-cycle orbit profile.

Every permissible cycle uses each of the 24 distinct ordered triples once. The
anchor 012 appears once, so a rooted Euler trail uniquely represents its rotation
class. The DFS below enumerates all such trails; independently, the last-exit
arborescence method enumerates exactly the same set.
"""
from collections import Counter
from itertools import permutations, product
from pathlib import Path

ALPHABET = range(4)
VERTICES = tuple(permutations(ALPHABET, 2))
EDGES = tuple(permutations(ALPHABET, 3))
EDGE_ID = {edge: i for i, edge in enumerate(EDGES)}
OUTGOING = {v: tuple(e for e in EDGES if e[:2] == v) for v in VERTICES}
ROOT = (0, 1)
ANCHOR = (0, 1, 2)
GROUP = tuple(permutations(ALPHABET))


def cycles_by_dfs():
    full = (1 << len(EDGES)) - 1
    trail = [ANCHOR]
    result = set()

    def extend(vertex, mask):
        if mask == full:
            if vertex == ROOT:
                c = tuple(e[0] for e in trail)
                assert windows(c) == set(EDGES)
                assert c[:3] == ANCHOR
                result.add(c)
            return
        for edge in OUTGOING[vertex]:
            bit = 1 << EDGE_ID[edge]
            if not (mask & bit):
                trail.append(edge)
                extend(edge[1:], mask | bit)
                trail.pop()

    extend(ANCHOR[1:], 1 << EDGE_ID[ANCHOR])
    return result


def windows(c):
    return {tuple(c[(i + j) % len(c)] for j in range(3)) for i in range(len(c))}


def cycles_by_trees():
    """All 2**11 possible last-exit choices, with the other root exit anchored."""
    nonroot = tuple(v for v in VERTICES if v != ROOT)
    results = set()
    ntrees = 0
    for choices in product((0, 1), repeat=len(nonroot)):
        last = {v: OUTGOING[v][choice] for v, choice in zip(nonroot, choices)}
        # A functional digraph is an in-arborescence to ROOT iff all paths hit ROOT.
        if any(not reaches_root(v, last) for v in nonroot):
            continue
        ntrees += 1
        order = {v: tuple(e for e in OUTGOING[v] if e != last[v]) + (last[v],)
                 for v in nonroot}
        order[ROOT] = (ANCHOR, next(e for e in OUTGOING[ROOT] if e != ANCHOR))
        progress = {v: 0 for v in VERTICES}
        current = ROOT
        edges = []
        for _ in range(len(EDGES)):
            i = progress[current]
            assert i < 2
            edge = order[current][i]
            progress[current] += 1
            edges.append(edge)
            current = edge[1:]
        assert current == ROOT and len(set(edges)) == len(EDGES)
        word = tuple(e[0] for e in edges)
        assert word[:3] == ANCHOR and windows(word) == set(EDGES)
        results.add(word)
    return ntrees, results


def reaches_root(v, last):
    seen = set()
    while v != ROOT:
        if v in seen:
            return False
        seen.add(v)
        v = last[v][1:]
    return True


def normalize(c):
    # The triple ANCHOR occurs at exactly one cyclic position.
    hits = [i for i in range(len(c))
            if tuple(c[(i + j) % len(c)] for j in range(3)) == ANCHOR]
    assert len(hits) == 1
    i = hits[0]
    return tuple(c[(i + j) % len(c)] for j in range(len(c)))


def cycle_type(p):
    seen = set()
    lengths = []
    for x in ALPHABET:
        if x not in seen:
            y = x
            k = 0
            while y not in seen:
                seen.add(y)
                k += 1
                y = p[y]
            lengths.append(k)
    return tuple(sorted(lengths, reverse=True))


def transformed(c, p, reverse=False):
    return normalize(tuple(p[x] for x in (reversed(c) if reverse else c)))


def main():
    all_cycles = cycles_by_dfs()
    trees, tree_cycles = cycles_by_trees()
    assert trees == 384 and len(all_cycles) == 384 and all_cycles == tree_cycles

    fixes = {False: {}, True: {}}
    for reverse in (False, True):
        for p in GROUP:
            n = sum(transformed(c, p, reverse) == c for c in all_cycles)
            # Independent fixed-point check directly searches all cyclic shifts,
            # without the normalization routine used above.
            n_by_rotation = 0
            for c in all_cycles:
                raw = tuple(reversed(c)) if reverse else c
                image = bytes(p[x] for x in raw)
                circular_word = bytes(c) + bytes(c[:-1])
                n_by_rotation += image in circular_word
            assert n == n_by_rotation
            fixes[reverse].setdefault(cycle_type(p), set()).add(n)
    class_names = [(1, 1, 1, 1), (2, 1, 1), (2, 2), (3, 1), (4,)]
    assert [fixes[False][c] for c in class_names] == [
        {384}, {16}, {0}, {0}, {0}]
    assert [fixes[True][c] for c in class_names] == [
        {0}, {0}, {16}, {0}, {0}]

    label_orbits = set()
    both_orbits = set()
    for c in all_cycles:
        label = frozenset(transformed(c, p) for p in GROUP)
        double = frozenset(transformed(c, p, rev)
                           for p in GROUP for rev in (False, True))
        assert label <= all_cycles and double <= all_cycles
        label_orbits.add(label)
        both_orbits.add(double)
    assert Counter(len(o) for o in label_orbits) == {24: 12, 12: 8}
    assert Counter(len(o) for o in both_orbits) == {24: 6, 48: 5}
    assert sum(len(o) for o in label_orbits) == len(all_cycles)
    assert sum(len(o) for o in both_orbits) == len(all_cycles)
    assert (384 + 6*16) // 24 == len(label_orbits) == 20
    assert (384 + 6*16 + 3*16) // 48 == len(both_orbits) == 11
    assert sum(1 for o in label_orbits
               if any(transformed(next(iter(o)), p, True) in o for p in GROUP)) == 2
    # Independently reproduce every listed canonical class, stabilizer size, and
    # mirror-partner relation from the full set of words.
    canonical = lambda c: min(transformed(c, p) for p in GROUP)
    reps = sorted({canonical(c) for c in all_cycles})
    assert len(reps) == 20
    index = {rep: i + 1 for i, rep in enumerate(reps)}
    lines = ['class_index\trepresentative\tlabeled_orbit_size\treversal_partner_index']
    for i, rep in enumerate(reps, 1):
        size = len({transformed(rep, p) for p in GROUP})
        mirror = index[canonical(tuple(reversed(rep)))]
        lines.append(f'{i}\t{"".join(map(str, rep))}\t{size}\t{mirror}')
    expected = '\n'.join(lines) + '\n'
    observed = Path(__file__).with_name('classes.tsv').read_text(encoding='utf-8')
    assert observed == expected, 'class representative certificate differs'
    print('VERIFY_OK')
    print('rooted_tree_choices=2048 rooted_trees=384 unique_cycles=384')
    print('fixed_pure_by_cycle_type='+str({c: next(iter(fixes[False][c])) for c in class_names}))
    print('fixed_reflected_by_cycle_type='+str({c: next(iter(fixes[True][c])) for c in class_names}))
    print('alphabet_orbits=20 orbit_sizes='+str(dict(Counter(len(o) for o in label_orbits))))
    print('alphabet_and_reversal_orbits=11 orbit_sizes='+str(dict(Counter(len(o) for o in both_orbits))))


if __name__ == '__main__':
    main()
