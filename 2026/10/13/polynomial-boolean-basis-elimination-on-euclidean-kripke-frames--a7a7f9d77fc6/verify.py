"""Finite checks for the Euclidean successor-cluster lemma and context substitution.

Run with Python 3.9+: python verify.py. This checks finite cases only.
"""
from itertools import product


def euclidean(rows, n):
    for x in range(n):
        for y in range(n):
            if not (rows[x] >> y) & 1:
                continue
            for z in range(n):
                if (rows[x] >> z) & 1 and not (rows[y] >> z) & 1:
                    return False
    return True


def cluster_property(rows, n):
    for w in range(n):
        if rows[w] == 0:
            continue
        y = (rows[w] & -rows[w]).bit_length() - 1
        c = rows[y]
        if not ((rows[w] & ~c) == 0):
            return False
        for z in range(n):
            if (rows[w] >> z) & 1 and rows[z] != c:
                return False
            if (c >> z) & 1 and rows[z] != c:
                return False
    return True


def verify_substitution(rows, n, p):
    # For all roots, the S5 laws ◇□p=□p and □◇p=◇p may be
    # substituted *inside one root modality*, not necessarily at root.
    def box(w, a):
        return all(a(y) for y in range(n) if (rows[w] >> y) & 1)
    def dia(w, a):
        return any(a(y) for y in range(n) if (rows[w] >> y) & 1)
    atom = lambda x: bool((p >> x) & 1)
    for w in range(n):
        if dia(w, lambda y: dia(y, lambda z: box(z, atom))) != dia(w, lambda y: box(y, atom)):
            return False
        if box(w, lambda y: box(y, lambda z: dia(z, atom))) != box(w, lambda y: dia(y, atom)):
            return False
        if dia(w, lambda y: box(y, lambda z: dia(z, atom))) != dia(w, lambda y: dia(y, atom)):
            return False
        if box(w, lambda y: dia(y, lambda z: box(z, atom))) != box(w, lambda y: box(y, atom)):
            return False
    return True


def run():
    counts = []
    separating_example = None
    for n in range(1, 5):
        total = 0
        for matrix in range(1 << (n * n)):
            rows = tuple((matrix >> (w * n)) & ((1 << n) - 1) for w in range(n))
            if not euclidean(rows, n):
                continue
            total += 1
            assert cluster_property(rows, n), (n, rows)
            for p in range(1 << n):
                assert verify_substitution(rows, n, p), (n, rows, p)
            if separating_example is None:
                # K5 not necessarily transitive: xRy & yRz but not xRz.
                if any((rows[x] >> y) & 1 and (rows[y] >> z) & 1
                       and not (rows[x] >> z) & 1
                       for x, y, z in product(range(n), repeat=3)):
                    separating_example = (n, rows)
        counts.append((n, total))
    assert separating_example is not None
    print('EUCLIDEAN_COUNTS', counts)
    print('NONTRANSITIVE_EUCLIDEAN', separating_example)
    print('VERIFY_OK')


if __name__ == '__main__':
    run()
