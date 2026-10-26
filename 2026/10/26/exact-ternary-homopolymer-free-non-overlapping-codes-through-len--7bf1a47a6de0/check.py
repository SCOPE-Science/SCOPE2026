"""Exact finite verification of ternary homopolymer-free cross-bifix-free codes.

Run with python3 check.py. Requires only Python's standard library.
"""
import itertools

ALPHABET = '012'
EXPECTED = {
    2: (6, 2, 6, (6,)),
    3: (6, 2, 6, (6,)),
    4: (12, 2, 18, (6, 12)),
    5: (24, 4, 6, (6,)),
    6: (42, 5, 24, (12, 12)),
    7: (90, 8, 48, (6, 6, 12, 12, 12)),
    8: (162, 16, 6, (6,)),
    9: (342, 24, 12, (6, 6)),
}


def words(n):
    return [''.join(t) for t in itertools.product(ALPHABET, repeat=n)
            if all(t[j] != t[j+1] for j in range(n-1))]


def bad_overlap(u, v):
    return any(u[:k] == v[-k:] for k in range(1, len(u)))


def graph(n):
    candidates = [w for w in words(n) if not bad_overlap(w, w)]
    neighbors = [0] * len(candidates)
    for i, u in enumerate(candidates):
        for j in range(i+1, len(candidates)):
            v = candidates[j]
            if not bad_overlap(u, v) and not bad_overlap(v, u):
                neighbors[i] |= 1 << j
                neighbors[j] |= 1 << i
    return candidates, neighbors


def ordered_clique_search(neighbors):
    """An exhaustive ordered subset search; pruning uses only a size upper bound."""
    best = 0
    winners = set()
    visited = 0

    def visit(chosen, avail):
        nonlocal best, winners, visited
        visited += 1
        if not avail:
            length = len(chosen)
            if length > best:
                best, winners = length, {tuple(chosen)}
            elif length == best:
                winners.add(tuple(chosen))
            return
        if len(chosen) + avail.bit_count() < best:
            return
        while avail:
            bit = avail & -avail
            vertex = bit.bit_length() - 1
            avail -= bit
            visit(chosen + (vertex,), avail & neighbors[vertex])
            if len(chosen) + avail.bit_count() < best:
                return

    visit((), (1 << len(neighbors)) - 1)
    return best, winners, visited


def maximal_clique_search(neighbors):
    """Independent Bron-Kerbosch pivot enumeration of every maximal clique."""
    best = 0
    winners = set()
    maximal_count = 0

    def visit(chosen, possible, excluded):
        nonlocal best, winners, maximal_count
        if not possible and not excluded:
            maximal_count += 1
            length = len(chosen)
            if length > best:
                best, winners = length, {tuple(sorted(chosen))}
            elif length == best:
                winners.add(tuple(sorted(chosen)))
            return
        union = possible | excluded
        if union:
            pivot = max((v for v in range(len(neighbors)) if (union >> v) & 1),
                        key=lambda v: (possible & neighbors[v]).bit_count())
            candidates = possible & ~neighbors[pivot]
        else:
            candidates = possible
        while candidates:
            bit = candidates & -candidates
            candidates -= bit
            vertex = bit.bit_length() - 1
            visit(chosen + (vertex,), possible & neighbors[vertex],
                  excluded & neighbors[vertex])
            possible -= bit
            excluded |= bit

    visit((), (1 << len(neighbors)) - 1, 0)
    return best, winners, maximal_count


def orbit_profile(codes):
    """Use alphabet permutations and reversal; both preserve the constraint."""
    unseen = set(codes)
    all_codes = set(codes)
    profiles = []
    reps = []
    while unseen:
        one = next(iter(unseen))
        orbit = set()
        for perm in itertools.permutations(ALPHABET):
            table = str.maketrans(ALPHABET, ''.join(perm))
            transformed = frozenset(w.translate(table) for w in one)
            orbit.add(transformed)
            orbit.add(frozenset(w[::-1] for w in transformed))
        assert orbit <= all_codes
        profiles.append(len(orbit))
        reps.append(min(tuple(sorted(book)) for book in orbit))
        unseen -= orbit
    return tuple(sorted(profiles)), tuple(sorted(reps))


def verify_book(book, n):
    assert len(book) == len(set(book))
    assert all(len(w) == n and all(w[j] != w[j+1] for j in range(n-1))
               for w in book)
    assert all(not bad_overlap(u, v) for u in book for v in book)


def main():
    for n, expected in EXPECTED.items():
        candidates, neighbors = graph(n)
        best_a, win_a, visited = ordered_clique_search(neighbors)
        best_b, win_b, maximal_count = maximal_clique_search(neighbors)
        assert best_a == best_b and win_a == win_b
        win_codes = {frozenset(candidates[v] for v in code) for code in win_a}
        profile, reps = orbit_profile(win_codes)
        assert (len(candidates), best_a, len(win_codes), profile) == expected, (
            n, len(candidates), best_a, len(win_codes), profile)
        for book in win_codes:
            verify_book(book, n)
        if n == 9:
            assert maximal_count == 121728
            assert len(reps) == 2 and all(len(r) == 24 for r in reps)
            print('n9_representatives:')
            for r in reps:
                print(' '.join(r))
        print('n=%d candidates=%d optimum=%d maximizing=%d orbits=%s '
              'ordered_nodes=%d maximal_cliques=%d' %
              (n, len(candidates), best_a, len(win_codes), profile,
               visited, maximal_count))
    print('TERNARY_RUN_ONE_NONOVERLAP_PASS')


if __name__ == '__main__':
    main()
