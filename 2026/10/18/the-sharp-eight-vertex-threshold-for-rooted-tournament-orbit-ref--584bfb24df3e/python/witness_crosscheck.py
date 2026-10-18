"""An independent dependency-free verification of the two explicit eight-vertex tournaments.

The bit order is (0,1),(0,2),...,(0,7),(1,2),...,(6,7).
A 1 bit means the lower-numbered vertex beats the higher-numbered vertex.
"""
from collections import Counter
from itertools import permutations


def tournament(n, word):
    arc = [[0] * n for _ in range(n)]
    bit = 0
    for a in range(n):
        for b in range(a + 1, n):
            arc[a][b] = (word >> bit) & 1
            arc[b][a] = 1 - arc[a][b]
            bit += 1
    return arc


def refined_classes(arc, root):
    n = len(arc)
    labels = [int(v == root) for v in range(n)]
    while True:
        signatures = []
        for v in range(n):
            out_by_color = tuple(sum(arc[v][u] for u in range(n)
                                     if labels[u] == color)
                                 for color in sorted(set(labels)))
            in_by_color = tuple(sum(arc[u][v] for u in range(n)
                                    if labels[u] == color)
                                for color in sorted(set(labels)))
            signatures.append((labels[v], out_by_color, in_by_color))
        lexicon = {key: idx for idx, key in enumerate(sorted(set(signatures)))}
        new_labels = [lexicon[key] for key in signatures]
        if all((labels[i] == labels[j]) == (new_labels[i] == new_labels[j])
               for i in range(n) for j in range(n)):
            return new_labels
        labels = new_labels


def automorphism_orbits(arc, root):
    n = len(arc)
    parent = list(range(n))

    def find(a):
        while a != parent[a]:
            a = parent[a]
        return a

    def union(a, b):
        parent[find(a)] = find(b)

    others = [v for v in range(n) if v != root]
    order = 0
    for mapped in permutations(others):
        perm = list(range(n))
        for v, w in zip(others, mapped):
            perm[v] = w
        if all(arc[i][j] == arc[perm[i]][perm[j]]
               for i in range(n) for j in range(n)):
            order += 1
            for i in range(n):
                union(i, perm[i])
    groups = {}
    for v in range(n):
        groups.setdefault(find(v), []).append(v)
    return sorted((tuple(vs) for vs in groups.values()), key=lambda x: (len(x), x)), order


def main():
    source, sink = 85042, 220421234
    for mask, expected_outdegree in [(source, 7), (sink, 0)]:
        arc = tournament(8, mask)
        assert sum(arc[7]) == expected_outdegree
        assert sorted(sum(row) for row in [a[:7] for a in arc[:7]]) == [3] * 7
        # Exactly one orientation word of the induced 7-vertex tournament.
        base = tournament(7, 22066)
        assert [row[:7] for row in arc[:7]] == base
        labels = refined_classes(arc, 7)
        cell_sizes = sorted(Counter(labels).values())
        orbits, order = automorphism_orbits(arc, 7)
        orbit_sizes = sorted(map(len, orbits))
        assert cell_sizes == [1, 7], cell_sizes
        assert orbit_sizes == [1, 1, 3, 3], orbit_sizes
        assert order == 3
        print(f'rooted_mask={mask} root_outdegree={expected_outdegree} '
              f'stable_color_sizes={cell_sizes} orbit_sizes={orbit_sizes} '
              f'rooted_automorphism_order={order} PASS')


if __name__ == '__main__':
    main()
