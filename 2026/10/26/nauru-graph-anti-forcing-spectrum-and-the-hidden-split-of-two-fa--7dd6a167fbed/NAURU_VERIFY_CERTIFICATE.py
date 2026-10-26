#!/usr/bin/env python3
"""Check exhaustive finite Nauru anti-forcing certificate; standard library only.

Run: python NAURU_VERIFY_CERTIFICATE.py NAURU_CERTIFICATE.json
No numerical optimization, MILP, or outside data is used by this checker.
"""
import sys
import json
import itertools
from collections import Counter

N = 12
edges = sorted(set(tuple(sorted(e)) for e in (
    [(i, (i + 1) % N) for i in range(N)]
    + [(N + i, N + (i + 5) % N) for i in range(N)]
    + [(i, N + i) for i in range(N)]
)))
assert len(edges) == 36
edge_index = {e: i for i, e in enumerate(edges)}

# Independent perfect-matching enumeration as bijections between black and white
# vertices, with a three-choice restriction for each black vertex.
black = sorted([i for i in range(N) if i % 2 == 0]
               + [N + i for i in range(N) if i % 2 == 1])
white = sorted(set(range(2 * N)) - set(black))
assert len(black) == len(white) == 12
white_position = {v: j for j, v in enumerate(white)}
options = [[(j, edge_index[tuple(sorted((u, v)))])
            for j, v in enumerate(white)
            if tuple(sorted((u, v))) in edge_index]
           for u in black]
assert all(len(q) == 3 for q in options)


def list_matchings(row=0, used_white=0, chosen=()):
    if row == 12:
        yield frozenset(chosen)
        return
    for j, eid in options[row]:
        if not (used_white >> j) & 1:
            yield from list_matchings(row+1, used_white | (1 << j), chosen + (eid,))


def is_alternating_cycle(matching, outside_edges):
    s = set(outside_edges)
    if not s or s & matching:
        return False
    touched = set(v for e in s for v in edges[e])
    if len(touched) != 2 * len(s):
        return False
    matched = [e for e in matching if set(edges[e]) <= touched]
    if len(matched) != len(s):
        return False
    adjacency = {v: [] for v in touched}
    for e in s | set(matched):
        u, v = edges[e]
        adjacency[u].append(v)
        adjacency[v].append(u)
    if any(len(neighbors) != 2 for neighbors in adjacency.values()):
        return False
    reached = set()
    stack = [next(iter(touched))]
    while stack:
        u = stack.pop()
        if u not in reached:
            reached.add(u)
            stack.extend(adjacency[u])
    return reached == touched


def deleted_set_count(matching, matchings, k):
    remaining = [e for e in range(36) if e not in matching]
    alternatives = [other - matching for other in matchings if other != matching]
    count = 0
    for trial in itertools.combinations(remaining, k):
        s = set(trial)
        if all(s & other for other in alternatives):
            count += 1
    return count


def main(path):
    certificate = json.load(open(path, encoding='utf8'))
    assert certificate['graph'] == 'GP(12,5)'
    matchings = set(list_matchings())
    assert len(matchings) == certificate['perfect_matching_count'] == 120
    covered = set()
    profile = Counter()
    for orbit in certificate['orbit_representatives']:
        rep = frozenset(orbit['matching'])
        assert rep in matchings
        value = orbit['anti_forcing_number']
        deletion = set(orbit['upper_deletion_edges'])
        pack = [set(c) for c in orbit['lower_disjoint_cycles_outside_matching']]
        assert len(deletion) == len(pack) == value
        assert not (deletion & rep)
        # Exact anti-forcing upper certificate against every alternative matching.
        assert all(deletion & (other - rep) for other in matchings if other != rep)
        # Lower bound: distinct alternating cycles require disjoint deleted edges.
        assert all(is_alternating_cycle(rep, s) for s in pack)
        assert sum(map(len, pack)) == len(set().union(*pack))
        # Exhaustively count every minimum deletion set for orbit representative.
        number = deleted_set_count(rep, matchings, value)
        assert number == orbit['optimal_deletion_sets_per_matching']
        for obj in orbit['orbit_images']:
            target = frozenset(obj['matching'])
            perm = obj['vertex_permutation']
            assert sorted(perm) == list(range(24))
            transformed_edges = {
                edge_index[tuple(sorted((perm[u], perm[v])))]
                for u, v in edges
            }
            assert transformed_edges == set(range(36))
            translated = frozenset(edge_index[tuple(sorted((perm[edges[e][0]],
                                                            perm[edges[e][1]])))]
                                   for e in rep)
            assert translated == target
            assert target in matchings and target not in covered
            covered.add(target)
            profile[(tuple(orbit['type']), value, number)] += 1
    assert covered == matchings and len(certificate['orbit_representatives']) == 8
    assert Counter({k: sum(q for (t, a, n), q in profile.items() if a == k)
                    for k in (5, 6, 7, 8)}) == {5: 6, 6: 93, 7: 18, 8: 3}
    assert sum(n * q for (t, a, n), q in profile.items()) == 25092
    print(json.dumps({'method': 'explicit_cycle_packing_and_automorphism_orbit_certificate',
                      'perfect_matchings': 120,
                      'orbit_sizes': [len(o['orbit_images']) for o in certificate['orbit_representatives']],
                      'anti_forcing_spectrum': {5:6, 6:93, 7:18, 8:3},
                      'refined_profile': [(list(t), a, b, q) for (t, a, b), q in sorted(profile.items())],
                      'minimum_set_pairs': 25092}, sort_keys=True))

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'NAURU_CERTIFICATE.json')
