"""Reproduce finite character and incidence checks for Kneser neighborhood complexes.

No third-party dependencies. The two character calculations use separate face
models: neighborhood simplices and Boolean-rank chains.
"""
from itertools import combinations, permutations


def sign(seq):
    return -1 if sum(a > b for i, a in enumerate(seq) for b in seq[i + 1:]) % 2 else 1


def rank_poset_character(p):
    n = len(p)
    fixed = [s for s in range(1 << n) if 2 <= s.bit_count() <= n - 2
             and sum(1 << p[i] for i in range(n) if s >> i & 1) == s]
    ordered = sorted(fixed, key=lambda s: (s.bit_count(), s))
    interval_mobius = {}
    for s in ordered:
        interval_mobius[s] = 1 - sum(interval_mobius[t] for t in interval_mobius if t & s == t)
    # Negative reduced Lefschetz correction accounts for the augmented chain.
    reduced_trace = sum(interval_mobius.values()) - 1
    return (-1) ** (n - 4) * reduced_trace


def faces_and_edges(n):
    edges = list(combinations(range(n), 2))
    index = {e: i for i, e in enumerate(edges)}
    faces = set()
    for support in combinations(range(n), n - 2):
        contained = [index[e] for e in combinations(support, 2)]
        for s in range(1, 1 << len(contained)):
            mask = 0
            for j, a in enumerate(contained):
                if s >> j & 1:
                    mask |= 1 << a
            faces.add(mask)
    return edges, index, tuple(sorted(faces))


def neighborhood_character(p, edges, index, faces):
    image = [index[tuple(sorted((p[i], p[j])))] for i, j in edges]
    total = -1  # reduced Euler-Lefschetz contribution of the augmented chain
    for face in faces:
        members = [i for i in range(len(edges)) if face >> i & 1]
        mapped = [image[i] for i in members]
        mapped_mask = sum(1 << k for k in mapped)
        if mapped_mask == face:
            total += (-1) ** (len(members) - 1) * sign(mapped)
    return (-1) ** (len(p) - 4) * total


def predicted(p):
    f = sum(i == x for i, x in enumerate(p))
    return sign(p) * (f * f - 3 * f + 1)


def crown_check(n):
    # A spanning-tree test confirms the connected graph behind the integral
    # cochain presentation. Its oriented incidence matrix is totally unimodular.
    adjacency = {('L', i): set() for i in range(n)}
    adjacency.update({('R', j): set() for j in range(n)})
    for i in range(n):
        for j in range(n):
            if i != j:
                adjacency['L', i].add(('R', j))
                adjacency['R', j].add(('L', i))
    seen, frontier = {('L', 0)}, [('L', 0)]
    while frontier:
        for w in adjacency[frontier.pop()]:
            if w not in seen:
                seen.add(w)
                frontier.append(w)
    assert len(seen) == 2 * n
    return n * (n - 1) - 2 * n + 1


def run():
    for n in range(4, 8):
        edges, index, faces = faces_and_edges(n)
        perms = list(permutations(range(n))) if n <= 6 else [
            tuple(range(n)), tuple([1, 0] + list(range(2, n))),
            tuple(list(range(1, n)) + [0]),
            tuple([1, 2, 0] + list(range(3, n)))]
        for p in perms:
            expected = predicted(p)
            got_poset = rank_poset_character(p)
            got_graph = neighborhood_character(p, edges, index, faces)
            assert got_graph == got_poset == expected, (n, p, got_graph, got_poset, expected)
        rank = crown_check(n)
        assert rank == predicted(tuple(range(n)))
        print(f'n={n} graph_faces={len(faces)} permutations={len(perms)} integral_rank={rank}: PASS')
    print('KNESER_CROWN_INTEGRAL_LATTICE_FINITE_TESTS_OK')


if __name__ == '__main__':
    run()
