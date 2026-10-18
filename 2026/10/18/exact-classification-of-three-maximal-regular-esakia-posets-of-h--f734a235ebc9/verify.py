"""Standalone exhaustive verification of regular finite rooted poset census.

Three maximal elements, height four (four vertices on a longest chain).
Only Python's standard library is needed.
"""
from itertools import permutations, combinations
from collections import Counter
from hashlib import sha256

MAX = (1, 2, 4)
SUPPORTS = (3, 5, 6, 7)
PERMS = tuple(permutations((0, 1, 2)))


def translate_code(v, permutation):
    return sum(1 << permutation[i] for i in range(3) if v & (1 << i))


def parents_for_supports(T):
    """Eligible two-or-more-element antichains including a middle element.

    Maximal points: (0,m) with mask m in MAX; middle points: (1,t) in T.
    A middle point of support t lies strictly below maximal point (0,m)
    precisely when t & m is nonzero.
    """
    vertices = [(0, m) for m in MAX] + [(1, t) for t in T]
    eligible = []
    for size in range(2, len(vertices) + 1):
        for combo in combinations(vertices, size):
            if not any(level == 1 for level, _ in combo):
                continue
            if any(a[0] != b[0] and ((a[1] & b[1]) != 0)
                   for a, b in combinations(combo, 2)):
                continue
            eligible.append(tuple(combo))
    return tuple(eligible)


def minimal_initial(T):
    return tuple([(1, t) for t in T] +
                 [(0, m) for m in MAX if not any(t & m for t in T)])


def canonical(T, U):
    options = []
    for p in PERMS:
        tt = tuple(sorted(translate_code(t, p) for t in T))
        uu = tuple(sorted(tuple(sorted((lev, translate_code(mask, p))
                                      for lev, mask in child))
                          for child in U))
        options.append((tt, uu))
    return min(options)


def validate_poset(T, U):
    """Reconstruct Hasse order and recompute cover sets and heights."""
    nodes = [(0, m) for m in MAX] + [(1, t) for t in T] + \
            [(2, index) for index in range(len(U))] + [(3, 0)]
    immediate = {}
    for m in MAX:
        immediate[(0, m)] = ()
    for t in T:
        immediate[(1, t)] = tuple((0, m) for m in MAX if t & m)
    for index, child in enumerate(U):
        immediate[(2, index)] = child
    lower_minimal = set((2, i) for i in range(len(U)))
    for v in nodes[:-1]:
        if v[0] == 1:
            if not any(v in c for c in U):
                lower_minimal.add(v)
        elif v[0] == 0:
            if not any(v in c for c in U) and not any(v in immediate[(1, t)] for t in T):
                lower_minimal.add(v)
    immediate[(3, 0)] = tuple(lower_minimal)
    assert len(immediate[(3, 0)]) >= 2
    closure = {}
    depth = {}
    for v in nodes:
        closure[v] = {v}.union(*(closure[w] for w in immediate[v]))
        depth[v] = (1 + max(depth[w] for w in immediate[v])) if immediate[v] else 0
    assert depth[(3, 0)] == 3
    assert len([v for v in nodes if not immediate[v]]) == 3
    assert closure[(3, 0)] == set(nodes)
    successors = {}
    for v in nodes:
        if not immediate[v]:
            continue
        upward = closure[v] - {v}
        successors[v] = frozenset(w for w in upward if not any(
            w in closure[z] and z != w for z in upward))
        assert successors[v] == frozenset(immediate[v])
        assert len(successors[v]) >= 2
    assert len(set(successors.values())) == len(successors)


def main():
    type_counts = Counter()
    signatures = set()
    pointed = 0
    per_T = {}
    for bits in range(1 << len(SUPPORTS)):
        T = tuple(s for i, s in enumerate(SUPPORTS) if bits & (1 << i))
        A = parents_for_supports(T)
        if not A:
            continue
        forbidden = tuple(minimal_initial(T))
        assert len(forbidden) >= 2 and set(forbidden) in map(set, A)
        excluded_index = next(i for i, parents in enumerate(A) if set(parents) == set(forbidden))
        n_here = 0
        for subset in range(1, 1 << len(A)):
            if subset == (1 << excluded_index):
                continue
            U = tuple(A[i] for i in range(len(A)) if subset & (1 << i))
            validate_poset(T, U)
            signatures.add(canonical(T, U))
            type_counts[len(T) + len(U) + 4] += 1
            pointed += 1
            n_here += 1
        assert n_here == 2 ** len(A) - 2
        per_T[T] = (len(A), n_here)
    assert pointed == 16718, pointed
    assert len(signatures) == 3344, len(signatures)
    # Independent Burnside orbit count (fixed configurations by conjugacy type).
    fixed = {}
    for p in PERMS:
        count = 0
        for T, (num, _) in per_T.items():
            if tuple(sorted(translate_code(t, p) for t in T)) != T:
                continue
            A = parents_for_supports(T)
            unvisited = set(A)
            cycles = 0
            while unvisited:
                child = next(iter(unvisited))
                seq = set()
                while child not in seq:
                    seq.add(child)
                    child = tuple(sorted((lev, translate_code(mask, p)) for lev, mask in child))
                assert seq <= unvisited
                unvisited -= seq
                cycles += 1
            count += 2 ** cycles - 2
        fixed[p] = count
    assert fixed[(0, 1, 2)] == 16718
    assert sorted(fixed.values()) == [68, 68, 1070, 1070, 1070, 16718]
    assert sum(fixed.values()) // 6 == len(signatures)
    print('MAXIMA=3 HEIGHT=4 POINTED=', pointed, 'UNMARKED=', len(signatures))
    print('BURNSIDE_FIXED=', sorted(fixed.values()))
    print('SIZE_RANGE=', min(type_counts), max(type_counts))
    print('SIZE_COUNTS_POINTED=', sorted(type_counts.items()))
    print('VERIFIED')


if __name__ == '__main__':
    main()
