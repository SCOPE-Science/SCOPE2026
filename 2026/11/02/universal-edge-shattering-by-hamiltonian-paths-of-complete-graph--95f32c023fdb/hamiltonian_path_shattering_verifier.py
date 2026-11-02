"""Finite checks for shattering by undirected Hamiltonian paths of complete graphs.

Run: python3 hamiltonian_path_shattering_verifier.py
Uses only Python's standard library. These tests corroborate, but do not replace,
the unrestricted constructive proof.
"""
from itertools import permutations, combinations
from collections import Counter


def edge_universe(n):
    return list(combinations(range(n), 2))


def all_hamiltonian_masks(n, edges):
    if n <= 1:
        return {0}
    index = {e: i for i, e in enumerate(edges)}
    ans = set()
    for p in permutations(range(n)):
        ans.add(sum(1 << index[tuple(sorted((p[i], p[i + 1])))]
                    for i in range(n - 1)))
    return ans


def submasks(mask):
    current = mask
    while True:
        yield current
        if current == 0:
            break
        current = (current - 1) & mask


def is_linear_forest(mask, edges, n):
    parent = list(range(n))
    degree = [0] * n
    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for i, (a, b) in enumerate(edges):
        if not mask & (1 << i):
            continue
        degree[a] += 1
        degree[b] += 1
        if degree[a] > 2 or degree[b] > 2:
            return False
        aroot, broot = find(a), find(b)
        if aroot == broot:
            return False
        parent[aroot] = broot
    return True


def shatters(mask, hamiltonian_masks):
    observed = {P & mask for P in hamiltonian_masks}
    return len(observed) == 1 << mask.bit_count()


def main():
    counts = []
    for n in range(1, 8):
        edges = edge_universe(n)
        hs = all_hamiltonian_masks(n, edges)
        linear_forests = {s for h in hs for s in submasks(h)}
        # Every linear forest extends to a Hamiltonian path; the equality here
        # also checks its enumeration independently against n<=7 masks.
        if n <= 3:
            candidates = set(range(1 << len(edges)))
        else:
            candidates = linear_forests
        actual = {s for s in candidates if shatters(s, hs)}
        expected = ({0} if n <= 2 else
                    {s for s in linear_forests if s.bit_count() <= 1}
                    if n == 3 else linear_forests)
        assert actual == expected, (n, 'shattering mismatch',
                                    sorted(actual ^ expected)[:3])
        if n <= 6:
            # Test all edge supports, including cycles and degree-three stars.
            all_actual = {s for s in range(1 << len(edges))
                          if shatters(s, hs)}
            assert all_actual == expected, (n, 'non-forest counterexample')
            assert {s for s in range(1 << len(edges))
                    if is_linear_forest(s, edges, n)} == linear_forests
        histogram = Counter(s.bit_count() for s in actual)
        vc = max(histogram)
        assert vc == (0 if n <= 2 else 1 if n == 3 else n - 1)
        if n >= 4:
            assert histogram[n - 1] * 2 == __import__('math').factorial(n)
        counts.append((n, len(hs), len(actual), vc, dict(sorted(histogram.items()))))
    for n, hyp, shattered, vc, hist in counts:
        print(f'n={n} paths={hyp} shattered_supports={shattered} '
              f'VCdim={vc} profile={hist}')
    print('ALL_HAMILTONIAN_PATH_SHATTERING_CHECKS_PASS')


if __name__ == '__main__':
    main()
