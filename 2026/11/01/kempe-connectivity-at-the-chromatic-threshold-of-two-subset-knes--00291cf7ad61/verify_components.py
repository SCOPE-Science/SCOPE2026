"""Explicit labelled-coloring state graph from elementary edge-partition parameters.

For n=4,5,6 this program constructs every parameter state, independently
checks properness, enumerates every legal single-site recoloring directly,
and recomputes graph components and diameters by breadth-first search.
Run: python3 verify_components.py
"""
from collections import Counter, deque
from itertools import combinations, permutations
from math import comb, factorial


def analyze(n):
    edge_list = tuple(combinations(range(n), 2))
    index = {e: i for i, e in enumerate(edge_list)}
    k = n - 2
    all_states = {}
    for Q in combinations(range(n), 3):
        S = tuple(x for x in range(n) if x not in Q)
        E = tuple(combinations(S, 2))
        for labeling in permutations(range(k)):
            triangle_label = labeling[0]
            center_labels = dict(zip(S, labeling[1:]))
            for mask in range(1 << len(E)):
                v = [None] * len(edge_list)
                for e in combinations(Q, 2):
                    v[index[e]] = triangle_label
                for s in S:
                    for q in Q:
                        v[index[tuple(sorted((s, q)))]] = center_labels[s]
                for bit, (s, t) in enumerate(E):
                    v[index[(s, t)]] = center_labels[t if (mask >> bit) & 1 else s]
                v = tuple(v)
                assert all(x is not None for x in v)
                assert v not in all_states, (n, v)
                all_states[v] = (Q, triangle_label, tuple(sorted(center_labels.items())), mask)

    d = comb(n - 3, 2)
    assert len(all_states) == factorial(k) * comb(n, 3) * (1 << d)
    adj = {}
    for v, token in all_states.items():
        assert all(v[i] != v[j] for i, e in enumerate(edge_list) for j, f in enumerate(edge_list)
                   if i < j and not (set(e) & set(f))), (n, v)
        neighborhood = set()
        for i, e in enumerate(edge_list):
            for c in range(k):
                if c == v[i]:
                    continue
                if all(v[j] != c or set(e) & set(f)
                       for j, f in enumerate(edge_list) if j != i):
                    w = v[:i] + (c,) + v[i + 1:]
                    assert w in all_states, (n, e, c)
                    other = all_states[w]
                    assert token[:3] == other[:3] and (token[3] ^ other[3]).bit_count() == 1
                    neighborhood.add(w)
        assert len(neighborhood) == d
        adj[v] = neighborhood

    unseen = set(all_states)
    component_sizes = Counter()
    diameters = Counter()
    while unseen:
        root = next(iter(unseen))
        q = deque([root]); unseen.remove(root)
        distances = {root: 0}
        while q:
            v = q.popleft()
            for w in adj[v]:
                if w not in distances:
                    distances[w] = distances[v] + 1
                    unseen.remove(w)
                    q.append(w)
        assert set(distances.values()) == set(range(d+1))
        assert max(distances.values()) == d
        component_sizes[len(distances)] += 1
        diameters[d] += 1
    assert component_sizes == {1 << d: factorial(k) * comb(n, 3)}
    print(f'GRAPH_PASS n={n} vertices={len(all_states)} edges={len(all_states)*d//2} '
          f'components={sum(component_sizes.values())} cube_dimension={d} component_sizes={dict(component_sizes)}')


for n in (4, 5, 6):
    analyze(n)
print('ALL_GRAPH_PASS')
