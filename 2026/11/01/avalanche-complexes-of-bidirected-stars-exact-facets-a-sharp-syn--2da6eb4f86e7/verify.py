#!/usr/bin/env python3
"""Independent finite checks of a parallel-firing avalanche-complex theorem.

Uses only Python's standard library. No external packages or data.
"""
from itertools import combinations_with_replacement


def faces_from_firing_sets(sets):
    faces = set()
    for mask in sets:
        sub = mask
        while sub:
            faces.add(sub)
            sub = (sub - 1) & mask
    return faces


def components(faces, n):
    vertices = {i for i in range(n+1) if (1 << i) in faces}
    parent = {i: i for i in vertices}

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    for i in vertices:
        for j in vertices:
            if i < j and ((1 << i) | (1 << j)) in faces:
                parent[find(i)] = find(j)
    return len({find(i) for i in vertices})


def dynamics(n, h, leaves):
    """Return the complete sequence of distinct-state firing sets.

    Hub is vertex 0; leaves are 1..n; firing means chips >= outdegree.
    States are handled until stabilisation or the first repeated state.
    """
    state = (h,) + tuple(leaves)
    seen = set()
    sets = []
    while state not in seen:
        seen.add(state)
        bits = (1 if state[0] >= n else 0)
        for i in range(n):
            if state[i+1] >= 1:
                bits |= 1 << (i+1)
        if not bits:
            break
        sets.append(bits)
        center_fires = bits & 1
        active = bin(bits >> 1).count("1")
        new_h = state[0] - n*center_fires + active
        new_leaves = tuple(state[i+1] - ((bits >> (i+1)) & 1) + center_fires
                           for i in range(n))
        state = (new_h,) + new_leaves
        if len(seen) > 4000:
            raise RuntimeError('Unexpectedly long state sequence')
    return sets


def predicted_facets(n, h, leaves):
    total = h + sum(leaves)
    all_leaves = sum(1 << i for i in range(1, n+1))
    if total < n:
        support = sum(1 << (i+1) for i, a in enumerate(leaves) if a > 0)
        return ([support] if support else []), False, None
    if total >= 2*n:
        return [all_leaves | 1], False, None
    t = 0
    while h + sum(min(t, a) for a in leaves) < n:
        t += 1
    remaining = sum(1 << (i+1) for i, a in enumerate(leaves) if a > t)
    if remaining:
        return [all_leaves, remaining | 1], False, None
    birth = t if max(leaves) > 0 else 1
    return [all_leaves, 1], True, birth


def execute():
    cases = 0
    steps = 0
    count_two = 0
    for n, cap in [(1, 8), (2, 8), (3, 7), (4, 6), (5, 6), (6, 5), (7, 4)]:
        for leaves in combinations_with_replacement(range(cap+1), n):
            for h in range(2*n + cap + 1):
                observed = dynamics(n, h, leaves)
                expected_facets, two, birth = predicted_facets(n, h, leaves)
                full = faces_from_firing_sets(observed)
                model = faces_from_firing_sets(expected_facets)
                assert full == model, ('facet mismatch', n, h, leaves, expected_facets, observed)
                total = h + sum(leaves)
                m = sum(a == max(leaves) for a in leaves)
                assert two == (n <= total < 2*n and total - m < n), ('threshold', n, h, leaves)
                if two:
                    count_two += 1
                prefix = set()
                for t, firing in enumerate(observed):
                    prefix.update(faces_from_firing_sets([firing]))
                    comp = components(prefix, n)
                    expected_comp = 2 if two and t >= birth else (1 if prefix else 0)
                    assert comp == expected_comp, ('persistence', n, h, leaves, t, comp, expected_comp)
                    steps += 1
                cases += 1
    print(f'VERIFY_OK cases={cases} firing_steps={steps} two_component_cases={count_two}')


if __name__ == '__main__':
    execute()
