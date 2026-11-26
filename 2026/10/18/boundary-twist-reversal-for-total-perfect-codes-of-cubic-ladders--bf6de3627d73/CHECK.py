"""Exact-cover corroboration for the individual total perfect code counts."""


def codes(families, universe):
    by_vertex = {v: [i for i, s in enumerate(families) if v in s] for v in universe}

    def search(uncovered):
        if not uncovered:
            yield frozenset()
            return
        v = min(uncovered, key=lambda q: sum(families[i] <= uncovered for i in by_vertex[q]))
        for i in by_vertex[v]:
            if families[i] <= uncovered:
                for tail in search(uncovered - families[i]):
                    yield tail | {i}

    return set(search(universe))


profiles = 0
for n in range(3, 16):
    universe = frozenset(range(2*n))
    for twisted in (False, True):
        # Use the Hamiltonian cycle and opposite chords for the twisted ladder.
        if twisted:
            adj = [{(i-1)%(2*n), (i+1)%(2*n), (i+n)%(2*n)} for i in range(2*n)]
        else:
            adj = [{i//n*n+(i-1)%n, i//n*n+(i+1)%n, (i+n)%(2*n)} for i in range(2*n)]
        actual = codes(adj, universe)
        expected = set()
        if n%3 == 0:
            words = [(0,0,3,0,0,3)]
            if n%6 == (3 if twisted else 0):
                words.append((0,1,1,0,2,2))
            for word in words:
                for phase in range(6):
                    expected.add(frozenset(i+r*n for i in range(n) for r in range(2)
                                           if word[(i+phase)%6] & (1<<r)))
        assert actual == expected
        assert len(actual) == (0 if n%3 else 9 if n%6 == (3 if twisted else 0) else 3)
        assert all(3*len(d) == 2*n for d in actual)
        profiles += 1
print(f'PASS: {profiles} individual-code profiles')
