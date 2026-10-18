"""Independent graph-level verification of two-anchor refinement on Johnson graphs."""
from collections import defaultdict
from itertools import combinations


def canonical_partition(labels):
    cells = defaultdict(set)
    for i, label in enumerate(labels):
        cells[label].add(i)
    return frozenset(frozenset(cell) for cell in cells.values())


def rank_colors(keys):
    index = {key: i for i, key in enumerate(sorted(set(keys)))}
    return [index[key] for key in keys]


def run(n, k, b):
    vertices = list(combinations(range(n), k))
    loc = {v: i for i, v in enumerate(vertices)}
    A = set(range(k))
    B = set(range(k-b)) | set(range(k, k+b))
    assert len(B) == k
    idx_a = loc[tuple(sorted(A))]
    idx_b = loc[tuple(sorted(B))]
    nbrs = []
    for v in vertices:
        s = set(v)
        nbrs.append([loc[tuple(sorted((s-{i})|{j}))]
                     for i in v for j in range(n) if j not in s])
    color = rank_colors([0 if i == idx_a else 1 if i == idx_b else 2
                         for i in range(len(vertices))])
    iterations = 0
    while True:
        nxt = rank_colors([(color[i], tuple(sorted(color[j] for j in nbrs[i])))
                           for i in range(len(vertices))])
        if nxt == color:
            break
        color = nxt
        iterations += 1
        assert iterations <= min(k, n-k) + 1
    zones = [A & B, A - B, B - A, set(range(n)) - (A | B)]
    count_by_zone = [tuple(len(set(v) & z) for z in zones) for v in vertices]
    def true_key(x):
        if n != 2*k:
            return x
        a = k - b
        flipped = (a-x[3], b-x[2], b-x[1], a-x[0])
        return min(x, flipped)
    expected = canonical_partition([true_key(x) for x in count_by_zone])
    actual = canonical_partition(color)
    assert actual == expected, (n, k, b, len(actual), len(expected))
    return len(vertices), len(actual), iterations


def main():
    tested, vertices_seen = 0, 0
    highlights = {}
    for n in range(6, 13):
        for k in range(3, n//2+1):
            for b in range(1, k+1):
                v, cells, rounds = run(n, k, b)
                tested += 1
                vertices_seen += v
                if (n, k, b) in {(6,3,1),(8,4,2),(9,4,2),(12,6,3)}:
                    highlights[(n,k,b)] = (cells, rounds)
    print('direct_graph_instances', tested)
    print('total_graph_vertices_over_instances', vertices_seen)
    for key in sorted(highlights):
        print('example', *key, 'cells', *highlights[key])
    print('PASS: every direct stable partition matches the claimed orbit grouping')

if __name__ == '__main__':
    main()
