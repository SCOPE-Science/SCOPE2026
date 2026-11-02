"""Standalone finite tests for the factual-contraction transformation theorem.
Run with Python >= 3.9; no third-party dependencies.
"""
from collections import deque
from itertools import permutations


def row_update(x, a):
    return x | a if (x & a) == 0 else x


def generator(n, a, serial=False):
    start = 1 if serial else 0
    return tuple(row_update(x, a) for x in range(start, 1 << n))


def apply(f, x, serial=False):
    return f[x - int(serial)]


def multiply(f, g, serial=False):
    return tuple(apply(g, y, serial) for y in f)


def identity(n, serial=False):
    return tuple(range(int(serial), 1 << n))


def monoid(n, serial=False, excluded=()):
    identity_map = identity(n, serial)
    alphabet = [generator(n, a, serial) for a in range(1, 1 << n) if a not in excluded]
    seen = {identity_map}
    queue = deque([identity_map])
    while queue:
        f = queue.popleft()
        for g in alphabet:
            h = multiply(f, g, serial)
            if h not in seen:
                seen.add(h)
                queue.append(h)
    return seen


def free_lrb_test(k, serial=False):
    # One common hub 0, k private labels 1..k; serial probes use extra marker k+1.
    n = k + 1 + int(serial)
    alphabet = [generator(n, 1 | (1 << (i + 1)), serial) for i in range(k)]
    outcomes = {}
    for size in range(k + 1):
        for word in permutations(range(k), size):
            f = identity(n, serial)
            for a in word:
                f = multiply(f, alphabet[a], serial)
            assert f not in outcomes, ('free injectivity failure', k, serial, word, outcomes.get(f))
            outcomes[f] = word
    expected = sum(__import__('math').factorial(k) // __import__('math').factorial(k - j) for j in range(k + 1))
    assert len(outcomes) == expected
    return expected


def main():
    tested = []
    for serial in (False, True):
        for n in (1, 2, 3):
            mon = monoid(n, serial)
            for f in mon:
                assert multiply(f, f, serial) == f
                for g in mon:
                    assert multiply(multiply(f, g, serial), f, serial) == multiply(f, g, serial)
            assert generator(n, 0, serial) == identity(n, serial)
            rank = 0
            for a in range(1, 1 << n):
                g = generator(n, a, serial)
                if g == identity(n, serial):
                    assert serial and a == (1 << n) - 1
                    continue
                assert g not in monoid(n, serial, excluded=(a,)), (n, serial, a)
                rank += 1
            assert rank == ((1 << n) - 2 if serial else (1 << n) - 1)
            tested.append((n, 'serial' if serial else 'all', len(mon), rank))
    assert [m[2] for m in tested if m[1] == 'all'] == [2, 7, 97]
    for k in range(1, 6):
        assert free_lrb_test(k, False) == free_lrb_test(k, True)
    # Verify the row and frame definitions coincide on every 3-world row.
    n = 3
    W = (1 << n) - 1
    for P in range(1 << n):
        A = W ^ P
        for X in range(1 << n):
            semantically = (X | A) if (X & A) == 0 else X
            assert row_update(X, A) == semantically
    print('MONOID_COUNTS', tested)
    print('FREE_LRB_COUNTS', [(k, free_lrb_test(k)) for k in range(1, 6)])
    print('ALL_CHECKS_OK')


if __name__ == '__main__':
    main()
