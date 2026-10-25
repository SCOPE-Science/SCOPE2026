"""Finite checks for natural-basis graph spectra of rank-one binary evolution algebras.
Run: python verify.py. Uses only the Python standard library.
"""
from itertools import combinations


def parity(z):
    return z.bit_count() & 1


def orthogonal_bases(n):
    """Enumerate every ordered orthonormal basis, not a sample."""
    choices = [x for x in range(1, 1 << n) if parity(x)]

    def visit(cols):
        if len(cols) == n:
            yield tuple(cols)
            return
        for x in choices:
            if all(not parity(x & c) for c in cols):
                yield from visit(cols + [x])

    yield from visit([])


def graph_support(u, cols):
    return sum(parity(u & c) << i for i, c in enumerate(cols))


def predicted_spectrum(u, n):
    full = (1 << n) - 1
    if u == full:
        return {n}
    return {k for k in range(1, n) if k % 2 == parity(u)}


def switch(x, mask):
    return x ^ (mask if parity(x & mask) else 0)


def generated_orbit(u, n):
    generators = []
    for i in range(n):
        for j in range(i + 1, n):
            generators.append(('swap', i, j))
    for ids in combinations(range(n), 4):
        generators.append(('switch', sum(1 << i for i in ids)))
    visited = {u}
    queue = [u]
    for x in queue:
        for g in generators:
            if g[0] == 'swap':
                i, j = g[1:]
                y = x ^ (((x >> i ^ x >> j) & 1) * ((1 << i) | (1 << j)))
            else:
                mask = g[1]
                y = switch(x, mask)
                # The underlying four-coordinate transvection is an isometry.
                assert mask.bit_count() == 4
            assert parity(y) == parity(x)
            if x == (1 << n) - 1:
                assert y == x
            if y not in visited:
                visited.add(y)
                queue.append(y)
    return visited


def verify():
    for n in (3, 4):
        bases = tuple(orthogonal_bases(n))
        assert bases
        actual = {u: set() for u in range(1, 1 << n)}
        for cols in bases:
            assert len(set(cols)) == n
            assert all(parity(c) for c in cols)
            assert all(not parity(cols[i] & cols[j]) for i in range(n)
                       for j in range(i + 1, n))
            for u in actual:
                support = graph_support(u, cols)
                assert support
                actual[u].add(support.bit_count())
        for u, spectra in actual.items():
            assert spectra == predicted_spectrum(u, n), (n, u, spectra)
        print(f'EXHAUSTIVE_NATURAL_BASES_OK n={n}, count={len(bases)}, algebras={(1 << n)-1}')
    for n in range(3, 10):
        full = (1 << n) - 1
        for u in range(1, full + 1):
            orbit = generated_orbit(u, n)
            expected = {v for v in range(1, full + 1)
                        if v == full} if u == full else {
                        v for v in range(1, full)
                        if parity(v) == parity(u)}
            assert orbit == expected, (n, u, len(orbit), len(expected))
        print(f'ORTHOGONAL_GENERATOR_ORBITS_OK n={n}')
    print('VERIFY_OK')


if __name__ == '__main__':
    verify()
