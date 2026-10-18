"""Finite corroboration of orbit-refinement for line graphs of double brooms.

Uses only the Python standard library. The all-parameter proof is in RESULT.md.
"""
from collections import Counter, defaultdict


def graph(a, b, ell):
    edges = [(i, i + 1) for i in range(ell)]
    edges += [(0, ell + 1 + j) for j in range(a)]
    edges += [(ell, ell + 1 + a + j) for j in range(b)]
    neighbors = [set() for _ in edges]
    for i, (u, v) in enumerate(edges):
        for j in range(i):
            x, y = edges[j]
            if u in (x, y) or v in (x, y):
                neighbors[i].add(j)
                neighbors[j].add(i)
    return neighbors


def refine(neighbors):
    colors = [0] * len(neighbors)
    while True:
        signatures = [(colors[i], tuple(sorted(colors[j] for j in neighbors[i])))
                      for i in range(len(neighbors))]
        dictionary = {s: j for j, s in enumerate(sorted(set(signatures)))}
        new = [dictionary[s] for s in signatures]
        if new == colors:
            return colors
        colors = new


def orbit_labels(a, b, ell):
    if a == b:
        return ([('spine', min(i, ell - 1 - i)) for i in range(ell)]
                + [('leaf', 0)] * (a + b))
    return ([('spine', i) for i in range(ell)]
            + [('left-leaf', 0)] * a + [('right-leaf', 0)] * b)


def partitions_equal(colors, labels):
    return all((colors[i] == colors[j]) == (labels[i] == labels[j])
               for i in range(len(colors)) for j in range(i))


def main():
    tested = 0
    exceptions = []
    for a in range(2, 15):
        for b in range(a, 15):
            for ell in range(1, 31):
                neighbors = graph(a, b, ell)
                colors = refine(neighbors)
                tags = orbit_labels(a, b, ell)
                if not partitions_equal(colors, tags):
                    exceptions.append((a, b, ell, sorted(Counter(colors).values()),
                                       sorted(Counter(tags).values())))
                tested += 1
    assert exceptions == [(2, 2, 4, [2, 6], [2, 2, 4])], exceptions
    print('parameter triples checked:', tested)
    print('exactly one exception (a,b,ell,colour-sizes,orbit-sizes):', exceptions[0])
    print('PASS')


if __name__ == '__main__':
    main()
