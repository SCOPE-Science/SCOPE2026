#!/usr/bin/env python3
"""Exact finite verification for the triangular-prism Morse complex."""
from collections import Counter, deque
from itertools import permutations, product

EDGES = tuple(sorted(
    {tuple(sorted((i, (i + 1) % 3))) for i in range(3)}
    | {tuple(sorted((i + 3, (i + 1) % 3 + 3))) for i in range(3)}
    | {(i, i + 3) for i in range(3)}
))
ARCS = tuple(sorted((v, e) for e in EDGES for v in e))
PIVOT_ORDER = (1, 9, 2, 13, 14, 8, 16, 17, 15, 12, 4, 0, 3, 7, 10, 5, 6, 11)


def selected_indices(mask):
    return [i for i in range(len(ARCS)) if mask & (1 << i)]


def legal(mask):
    outgoing = {}
    used_edges = set()
    for index in selected_indices(mask):
        tail, edge = ARCS[index]
        if tail in outgoing or edge in used_edges:
            return False
        outgoing[tail] = edge[0] + edge[1] - tail
        used_edges.add(edge)
    for start in outgoing:
        visited = set()
        v = start
        while v in outgoing:
            if v in visited:
                return False
            visited.add(v)
            v = outgoing[v]
    return True


def generate_faces():
    assert len(EDGES) == 9 and len(ARCS) == 18
    all_faces = {mask for mask in range(1 << len(ARCS)) if legal(mask)}
    assert max(mask.bit_count() for mask in all_faces) == 5
    assert len(all_faces) == 1728
    return all_faces


def via_rooted_forests():
    # Independently enumerate undirected spanning edge forests and roots.
    result = set()
    for edge_mask in range(1 << len(EDGES)):
        parent = list(range(6))
        def root(x):
            while parent[x] != x:
                x = parent[x]
            return x
        chosen = []
        good = True
        for k, edge in enumerate(EDGES):
            if not (edge_mask & (1 << k)):
                continue
            u, v = edge
            ru, rv = root(u), root(v)
            if ru == rv:
                good = False
                break
            parent[ru] = rv
            chosen.append(edge)
        if not good:
            continue
        components = {}
        for v in range(6):
            components.setdefault(root(v), []).append(v)
        for roots in product(*[v for v in components.values()]):
            dest = {v: r for comp, r in zip(components.values(), roots) for v in comp}
            mask = 0
            for u, v in chosen:
                # Orient every tree edge towards the selected component root.
                r = dest[u]
                adjacency = {q: [] for q in range(6)}
                for a, b in chosen:
                    adjacency[a].append(b)
                    adjacency[b].append(a)
                distance = {r: 0}
                queue = deque([r])
                while queue:
                    q = queue.popleft()
                    for w in adjacency[q]:
                        if w not in distance:
                            distance[w] = distance[q] + 1
                            queue.append(w)
                tail = u if distance[u] > distance[v] else v
                mask |= 1 << ARCS.index((tail, (u, v)))
            result.add(mask)
    return result


def matching_and_critical(faces):
    remaining = set(faces) - {0}
    pairs = {}
    for idx in PIVOT_ORDER:
        bit = 1 << idx
        for lower in sorted(tuple(remaining)):
            if lower not in remaining or lower & bit:
                continue
            upper = lower | bit
            if upper in remaining:
                pairs[lower] = upper
                remaining.remove(lower)
                remaining.remove(upper)
    return pairs, remaining


def check_acyclic(faces, pairs):
    # Explicitly orient ALL nonempty-face incidences upward for matched
    # edges and downward otherwise. A topological ordering proves acyclicity.
    nodes = set(faces) - {0}
    indegree = {s: 0 for s in nodes}
    adjacency = {s: [] for s in nodes}
    incidences = 0
    for upper in nodes:
        for index in selected_indices(upper):
            lower = upper ^ (1 << index)
            if not lower:
                continue
            source, target = ((lower, upper) if pairs.get(lower) == upper
                              else (upper, lower))
            adjacency[source].append(target)
            indegree[target] += 1
            incidences += 1
    queue = deque(s for s in nodes if indegree[s] == 0)
    visited = 0
    while queue:
        source = queue.popleft()
        visited += 1
        for target in adjacency[source]:
            indegree[target] -= 1
            if indegree[target] == 0:
                queue.append(target)
    assert visited == len(nodes) == 1727
    assert incidences == 6606
    return incidences


def permutation_sign(image):
    return -1 if sum(image[i] > image[j]
                     for i in range(len(image))
                     for j in range(i + 1, len(image))) % 2 else 1


def character(faces):
    hist = Counter()
    for sigma in permutations(range(3)):
        for flip in (0, 1):
            def relabel(v):
                return sigma[v % 3] + 3 * ((v // 3) ^ flip)
            induced = tuple(ARCS.index((relabel(tail),
                         tuple(sorted(relabel(v) for v in edge))))
                         for tail, edge in ARCS)
            assert sorted(induced) == list(range(18))
            assert all(sum(1 << induced[i] for i in selected_indices(s)) in faces
                       for s in faces)
            L = 0
            for s in faces - {0}:
                indices = selected_indices(s)
                images = [induced[i] for i in indices]
                if set(images) == set(indices):
                    L += (-1 if len(indices) % 2 == 0 else 1) * permutation_sign(images)
            sigma_type = ('identity' if sigma == (0, 1, 2)
                          else '3-cycle' if all(sigma[i] != i for i in range(3))
                          else 'transposition')
            hist[(sigma_type, flip, L - 1)] += 1
    expected = {
        ('identity', 0, 64): 1, ('transposition', 0, 0): 3,
        ('3-cycle', 0, 1): 2, ('identity', 1, -4): 1,
        ('transposition', 1, -8): 3, ('3-cycle', 1, -1): 2,
    }
    assert hist == Counter(expected)
    sizes = (1, 3, 2)
    unsigned = (64, 0, 1)
    flipped = (-4, -8, -1)
    s3_characters = {'trivial': (1, 1, 1), 'sign': (1, -1, 1),
                     'standard': (2, 0, -1)}
    expected_mult = {('+', 'trivial'): 3, ('+', 'sign'): 7,
                     ('+', 'standard'): 10, ('-', 'trivial'): 8,
                     ('-', 'sign'): 4, ('-', 'standard'): 11}
    dimensions = {'trivial': 1, 'sign': 1, 'standard': 2}
    total_dim = 0
    for layer_sign in (1, -1):
        for name, vals in s3_characters.items():
            numerator = sum(sizes[i] * vals[i] *
                            (unsigned[i] + layer_sign * flipped[i])
                            for i in range(3))
            assert numerator % 12 == 0
            mult = numerator // 12
            assert mult == expected_mult[('+' if layer_sign == 1 else '-', name)]
            assert mult >= 0
            total_dim += mult * dimensions[name]
    assert total_dim == 64
    assert sum(sizes[i] * (unsigned[i] + flipped[i]) for i in range(3)) == 36
    return hist


def main():
    faces = generate_faces()
    # An independent construction as rooted spanning forests.
    assert faces == via_rooted_forests()
    counts = Counter(s.bit_count() for s in faces)
    assert [counts[k] for k in range(6)] == [1, 18, 126, 428, 705, 450]
    pairs, critical = matching_and_critical(faces)
    assert len(pairs) == 831
    assert Counter(s.bit_count() - 1 for s in critical) == {0: 1, 4: 64}
    incidences = check_acyclic(faces, pairs)
    hist = character(faces)
    print('FACES', [counts[k] for k in range(6)])
    print('MATCHED_PAIRS', len(pairs), 'CRITICAL',
          sorted(Counter(s.bit_count()-1 for s in critical).items()))
    print('HASSE_INCIDENCES', incidences)
    print('CHARACTER_CLASSES', sorted((str(key), count) for key, count in hist.items()))
    print('TRIANGULAR_PRISM_MORSE_64S4_FULL12_CHARACTER_OK')


if __name__ == '__main__':
    main()
