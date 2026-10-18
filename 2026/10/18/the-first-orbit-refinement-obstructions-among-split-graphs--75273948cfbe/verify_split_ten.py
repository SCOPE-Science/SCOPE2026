"""Independent replay for the four ten-vertex split-graph obstructions.

Usage: python3 verify_split_ten.py cutoff_census.txt
Uses only the Python standard library. The complete finite cutoff is checked by
verify_split_cutoff.cpp and independently through size nine by
verify_split_small_independent.cpp.
"""
from collections import Counter, defaultdict
from itertools import permutations, product
import re
import sys


def graph(k, masks):
    n = k + len(masks)
    A = [set() for _ in range(n)]
    for i in range(k):
        for j in range(i + 1, k):
            A[i].add(j)
            A[j].add(i)
    for j, m in enumerate(masks):
        for i in range(k):
            if m >> i & 1:
                A[i].add(k + j)
                A[k + j].add(i)
    return A


def colors(A):
    n = len(A)
    c = [0] * n
    rounds = 0
    while True:
        signatures = [(c[v], tuple(sorted(Counter(c[w] for w in A[v]).items()))) for v in range(n)]
        lookup = {key: ix for ix, key in enumerate(sorted(set(signatures)))}
        d = [lookup[key] for key in signatures]
        if all((c[i] == c[j]) == (d[i] == d[j]) for i in range(n) for j in range(i)):
            return d, rounds
        c = d
        rounds += 1


def full_orbits(A):
    n = len(A)
    deg = [len(s) for s in A]
    buckets = defaultdict(list)
    for v, d in enumerate(deg):
        buckets[d].append(v)
    groups = list(buckets.values())
    parent = list(range(n))

    def root(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    automorphisms = 0
    for images in product(*(permutations(g) for g in groups)):
        perm = list(range(n))
        for original_group, image_group in zip(groups, images):
            for u, v in zip(original_group, image_group):
                perm[u] = v
        if all((j in A[i]) == (perm[j] in A[perm[i]])
               for i in range(n) for j in range(i + 1, n)):
            automorphisms += 1
            for u in range(n):
                parent[root(u)] = root(perm[u])
    partition = defaultdict(list)
    for v in range(n):
        partition[root(v)].append(v)
    return sorted((sorted(vs) for vs in partition.values()), key=lambda x: x[0]), automorphisms


def canonical(k, masks):
    best = None
    for p in permutations(range(k)):
        transformed = sorted(sum(1 << p[i] for i in range(k) if mask >> i & 1) for mask in masks)
        key = tuple(transformed)
        if best is None or key < best:
            best = key
    return k, best


def main(path):
    failures = []
    counts = {}
    for line in open(path, encoding='utf-8'):
        if line.startswith('FAIL '):
            matched = re.fullmatch(r'FAIL k=(\d+) columns=([\d,]+) mismatch=\d+:\d+\n', line)
            assert matched is not None, line
            k = int(matched[1])
            masks = tuple(map(int, matched[2].split(',')))
            failures.append((k, masks))
        if line.startswith('COUNT '):
            match = re.fullmatch(r'COUNT n=(\d+) representations=(\d+) failures=(\d+)\n', line)
            assert match is not None
            counts[int(match[1])] = (int(match[2]), int(match[3]))
    assert len(failures) == 71
    assert counts[9] == (123983, 0)
    assert counts[10] == (1592513, 71)
    classes = defaultdict(list)
    for k, masks in failures:
        A = graph(k, masks)
        degrees = [len(s) for s in A]
        assert len(set(degrees[:k])) == len(set(degrees[k:])) == 1
        assert degrees[0] > degrees[k]
        classes[canonical(k, masks)].append((k, masks))
    assert len(classes) == 4
    print('Exact full-graph isomorphism classes:', len(classes))
    print('Enumerated failing incidence presentations:', len(failures))
    for (k, masks), representations in sorted(classes.items()):
        A = graph(k, masks)
        c, rounds = colors(A)
        stable = defaultdict(list)
        for v, col in enumerate(c):
            stable[col].append(v)
        stable_sizes = sorted(len(part) for part in stable.values())
        orbits, autcount = full_orbits(A)
        orbit_sizes = sorted(len(part) for part in orbits)
        assert stable_sizes != orbit_sizes
        assert rounds == 1
        assert len(stable) == 2
        print('Class k={} masks={} presentations={} stable={} orbit={} aut_order={}'.format(
            k, ','.join(map(str, masks)), len(representations), stable_sizes, orbit_sizes, autcount))
    print('INDEPENDENT_TEN_VERTEX_CLASSES_VERIFIED')


if __name__ == '__main__':
    assert len(sys.argv) == 2
    main(sys.argv[1])
