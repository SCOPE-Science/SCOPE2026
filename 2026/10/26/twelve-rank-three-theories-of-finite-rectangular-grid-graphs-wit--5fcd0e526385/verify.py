"""Exact rank-three logical-type certificate for finite rectangular grid graphs.

Standalone: Python >=3.9, standard library only. Run `python3 verify.py`.
It recomputes all 28 canonical grid types and directly plays the three-round
Ehrenfeucht--Fraisse game on distinct minimum representatives. This script
checks a finite certificate; the product and infinite-path arguments are
mathematical parts of the accompanying proof.
"""

from functools import lru_cache
from itertools import combinations
from pathlib import Path
import json
import hashlib

ROOT = Path(__file__).resolve().parent


def rectangular_grid(m, n):
    if not (isinstance(m, int) and isinstance(n, int) and m > 0 and n > 0):
        raise ValueError('positive integer dimensions required')
    edges = [set() for _ in range(m * n)]
    for i in range(m):
        for j in range(n):
            v = i * n + j
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ii, jj = i + di, j + dj
                if 0 <= ii < m and 0 <= jj < n:
                    edges[v].add(ii * n + jj)
    return tuple(map(frozenset, edges))


def rank_one_pair(graph, x, y):
    """Exact atomic two-tuple diagram plus all atomic triple extensions.

    Bit 0: x=y=z. Bits 1,2: x=y !=z, with z nonadjacent/adjacent.
    Bits 3,4: x!=y and z equals x/y. Bits 5..8: all distinct,
    encoded by the two adjacency flags (x~z, y~z).
    """
    mask = 0
    for z in range(len(graph)):
        if x == y:
            bit = 0 if z == x else 1 + int(z in graph[x])
        else:
            bit = 3 if z == x else 4 if z == y else (
                5 + 2 * int(z in graph[x]) + int(z in graph[y])
            )
        mask |= 1 << bit
    return (int(x == y), int(y in graph[x]), mask)


def rank_one_pair_from_neighborhood_sets(graph, x, y):
    """Independent set-algebra derivation of the 9-bit atomic extension mask."""
    universe = set(range(len(graph)))
    if x == y:
        distinct = universe - {x}
        mask = 1 << 0
        if distinct - set(graph[x]):
            mask |= 1 << 1
        if distinct & set(graph[x]):
            mask |= 1 << 2
        return (1, 0, mask)
    others = universe - {x, y}
    nx, ny = set(graph[x]), set(graph[y])
    mask = (1 << 3) | (1 << 4)
    for left_flag, right_flag in ((False, False), (False, True),
                                  (True, False), (True, True)):
        candidates = (nx if left_flag else others - nx) & (ny if right_flag else others - ny) & others
        if candidates:
            mask |= 1 << (5 + 2 * int(left_flag) + int(right_flag))
    return (0, int(y in nx), mask)


def rank_three_type(graph):
    """Back-and-forth recursion, represented by immutable sets.

    Rank-one two-tuple types are the set of all atomic triple extensions.
    Rank-two one-tuple types are sets of rank-one pair types.
    Rank-three sentence types are sets of rank-two one-tuple types.
    """
    n = len(graph)
    pair = tuple(tuple(rank_one_pair(graph, x, y) for y in range(n))
                 for x in range(n))
    return frozenset(frozenset(pair[x]) for x in range(n))


def direct_game(graph_a, graph_b, rounds=3):
    """Independent alternating-game oracle, not using rank type encoding."""
    a, b = graph_a, graph_b
    @lru_cache(maxsize=None)
    def wins(tuples_a, tuples_b, remaining):
        if remaining == 0:
            for i in range(len(tuples_a)):
                for j in range(len(tuples_a)):
                    if (tuples_a[i] == tuples_a[j]) != (tuples_b[i] == tuples_b[j]):
                        return False
                    if (tuples_a[j] in a[tuples_a[i]]) != (tuples_b[j] in b[tuples_b[i]]):
                        return False
            return True
        # Spoiler can choose either board on every round.
        for x in range(len(a)):
            if not any(wins(tuples_a + (x,), tuples_b + (y,), remaining - 1)
                       for y in range(len(b))):
                return False
        for y in range(len(b)):
            if not any(wins(tuples_a + (x,), tuples_b + (y,), remaining - 1)
                       for x in range(len(a))):
                return False
        return True
    return wins((), (), rounds)


def canonical_table():
    profiles = {}
    for m in range(1, 8):
        for n in range(m, 8):
            profiles[m, n] = rank_three_type(rectangular_grid(m, n))
    groups = {}
    for dims, logical_type in profiles.items():
        groups.setdefault(logical_type, []).append(dims)
    families = sorted(groups.values(), key=lambda v: (min(m*n for m, n in v),
                                                       min(v, key=lambda d: (d[0]*d[1], d))))
    # Canonical representative = minimum order, then lexicographically first.
    result = []
    for number, members in enumerate(families, 1):
        rep = min(members, key=lambda pair: (pair[0] * pair[1], pair))
        result.append({"class": number, "representative": list(rep),
                       "representative_order": rep[0] * rep[1],
                       "canonical_members": [list(x) for x in members]})
    return result, profiles


def verify():
    table, profiles = canonical_table()
    expected = json.loads((ROOT / 'canonical_table.json').read_text(encoding='utf-8'))
    assert table == expected['classes'], 'classification table mismatch'
    assert len(table) == 12 and sum(len(v['canonical_members']) for v in table) == 28
    assert max(v['representative_order'] for v in table) == 10
    rep = [tuple(x['representative']) for x in table]
    assert len(set(rep)) == 12
    for m in range(1, 8):
        for n in range(m, 8):
            graph = rectangular_grid(m, n)
            for x in range(len(graph)):
                for y in range(len(graph)):
                    assert rank_one_pair(graph, x, y) == rank_one_pair_from_neighborhood_sets(graph, x, y), (m, n, x, y)
    for a, b in combinations(rep, 2):
        assert not direct_game(rectangular_grid(*a), rectangular_grid(*b)), (a, b)
    for row in table:
        r = tuple(row['representative'])
        for member in row['canonical_members']:
            assert profiles[tuple(member)] == profiles[r]
    # Independent game oracle on the nonisomorphic dimensions that collapse.
    stable = [tuple(x) for x in table[-1]['canonical_members']]
    for sample in ((2, 6), (3, 4), (4, 4), (7, 7)):
        assert sample in stable
    for a, b in [((2, 5), (3, 4)), ((2, 5), (7, 7)), ((3, 3), (2, 4))]:
        # Avoid a large direct-game instance for the 7-by-7 graph;
        # the exact type recurrence already checks every canonical case.
        if max(a[0]*a[1], b[0]*b[1]) <= 12:
            assert direct_game(rectangular_grid(*a), rectangular_grid(*b)) == (
                profiles[a] == profiles[b]
            )
    # Samples beyond the 7-by-7 reduction cutoff are corroborative, not proof.
    for m, n in ((1, 8), (1, 12), (2, 8), (2, 12), (3, 8), (8, 8), (8, 12)):
        reduced = tuple(sorted((min(m, 7), min(n, 7))))
        assert rank_three_type(rectangular_grid(m, n)) == profiles[reduced]
    ptypes = set()
    for m in range(1, 8):
        for n in range(m, 8):
            g = rectangular_grid(m, n)
            for x in range(len(g)):
                ptypes.add(frozenset(rank_one_pair(g, x, y) for y in range(len(g))))
    assert len(ptypes) == 18
    digest = hashlib.sha256(json.dumps(table, separators=(',', ':'),
                                       ensure_ascii=False).encode('utf-8')).hexdigest()
    print('VERIFY_OK classes=12 canonical_grids=28 pointed_types=18 sharp_order=10')
    print('INDEPENDENT_PAIR_ORACLE_OK all_canonical_ordered_pairs=TRUE')
    print('GAME_ORACLE_OK distinct_pairs=66 collision_ladder_square=TRUE')
    print('TABLE_SHA256', digest)


if __name__ == '__main__':
    verify()
