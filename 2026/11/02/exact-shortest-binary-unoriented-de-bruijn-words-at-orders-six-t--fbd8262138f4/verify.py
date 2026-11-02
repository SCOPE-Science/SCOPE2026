#!/usr/bin/env python3
"""Exact-integer verifier of unoriented binary word covering witnesses and dual bounds.
Usage: python3 verify.py certificates.json
No third-party packages required.
"""
import json
import sys
from collections import Counter, defaultdict, deque
from itertools import product


def words(n):
    return [''.join(x) for x in product('01', repeat=n)]


def rev_class(s):
    return min(s, s[::-1])


def signed_graph(n):
    vertices = sorted({rev_class(w) for w in words(n - 1)})
    edges = sorted({rev_class(w) for w in words(n)})
    adj = {v: [] for v in vertices}
    deg = Counter()
    type_counts = {v: [0, 0] for v in vertices}
    for w in edges:
        x, y = w[:-1], w[1:]
        a, b = rev_class(x), rev_class(y)
        # Incidence type 0: outgoing from lexicographic representative.
        # Incidence type 1: incoming to lexicographic representative.
        ta, tb = (0 if x == a else 1), (1 if y == b else 0)
        adj[a].append((b, ta, tb))
        adj[b].append((a, tb, ta))
        deg[a] += 1
        deg[b] += 1
        type_counts[a][ta] += 1
        type_counts[b][tb] += 1
    odd = sorted(v for v in vertices if deg[v] & 1)
    demand = {}
    for v in vertices:
        if v == v[::-1]:
            demand[v] = None
        else:
            diff = type_counts[v][0] - type_counts[v][1]
            if v in odd:
                assert abs(diff) == 1, (n, v, diff)
                demand[v] = 0 if diff < 0 else 1
            else:
                assert diff == 0, (n, v, diff)
    return edges, adj, odd, demand


def signed_distance(source, target, adj, demand):
    starts = [(source, t) for t in ((0, 1) if demand[source] is None else (demand[source],))]
    q = deque(starts)
    distance = dict.fromkeys(starts, 0)
    while q:
        v, required = q.popleft()
        for u, at_v, at_u in adj[v]:
            if v != v[::-1] and at_v != required:
                continue
            next_state = (u, 1 - at_u)
            if next_state not in distance:
                distance[next_state] = distance[(v, required)] + 1
                q.append(next_state)
    # The last edge must arrive with the minority (missing) type at the target.
    end_states = [(target, t) for t in ((0, 1) if demand[target] is None else (1 - demand[target],))]
    found = [distance[state] for state in end_states if state in distance]
    assert found, (source, target)
    return min(found)


def check_record(n, rec):
    edges, adj, odd, demand = signed_graph(n)
    assert rec['odd_vertices'] == odd
    word = rec['binary_word']
    assert isinstance(word, str) and all(c in '01' for c in word)
    assert len(word) == rec['length']
    assert len(edges) == rec['orbit_count']
    assert rec['extra'] == len(word) - n + 1 - len(edges)
    windows = [word[i:i+n] for i in range(len(word) - n + 1)]
    observed = {rev_class(w) for w in windows}
    assert observed == set(edges), (n, len(observed), len(edges))

    z = rec['dual_twice']
    assert len(z) == len(odd) + 2 and all(isinstance(q, int) for q in z)
    # Dual of the perfect-matching relaxation on odd terminals plus two
    # freely matched path-endpoint tokens. All costs are exact integers.
    for i, u in enumerate(odd):
        for j in range(i + 1, len(odd)):
            v = odd[j]
            d = min(signed_distance(u, v, adj, demand),
                    signed_distance(v, u, adj, demand))
            assert z[i] + z[j] <= 2 * d, (n, u, v, d, z[i], z[j])
        assert z[i] + z[-2] <= 0
        assert z[i] + z[-1] <= 0
    assert z[-2] + z[-1] <= 0
    assert sum(z) == 2 * rec['extra'], (n, sum(z), rec['extra'])
    print('ORDER', n, 'SHORTEST_LENGTH', len(word), 'REFLECTION_CLASSES', len(edges),
          'REPEATED_WINDOWS', rec['extra'], 'SIGNED_ODD_VERTICES', len(odd), 'PASS')


def main():
    with open(sys.argv[1], encoding='utf-8') as stream:
        data = json.load(stream)
    assert data['schema_version'] == 1
    assert set(data['records']) == {'6', '7', '8', '9'}
    for n in (6, 7, 8, 9):
        check_record(n, data['records'][str(n)])
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
