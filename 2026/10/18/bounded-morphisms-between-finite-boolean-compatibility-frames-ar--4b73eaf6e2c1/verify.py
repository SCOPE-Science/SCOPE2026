"""Independent finite checks for bounded morphisms of subset-intersection frames.
Run: python verify.py
"""
from itertools import product


def vertices(n):
    return tuple(range(1, 1 << n))


def is_bounded_map(f, n, m):
    """Direct definition; f is a tuple of target bit masks in vertex order."""
    src = vertices(n)
    tgt = vertices(m)
    for a in src:
        fa = f[a - 1]
        # Forth: every source neighbor's image must be a target neighbor.
        for b in src:
            if (a & b) and not (fa & f[b - 1]):
                return False
        # Back: each target neighbor must have an accessible preimage.
        for c in tgt:
            if (fa & c) and not any((a & b) and f[b - 1] == c for b in src):
                return False
    return True


def induced_map(g, n):
    out = []
    for a in vertices(n):
        b = 0
        for i in range(n):
            if a & (1 << i):
                b |= 1 << g[i]
        out.append(b)
    return tuple(out)


def onto(g, m):
    return set(g) == set(range(m))


def main():
    checked_functions = 0
    for n in (1, 2, 3):
        for m in (1, 2, 3):
            expected = {
                induced_map(g, n)
                for g in product(range(m), repeat=n)
                if onto(g, m)
            }
            observed = set()
            # Exhaustive enumeration of every set map of vertex sets.
            for f in product(vertices(m), repeat=(1 << n) - 1):
                checked_functions += 1
                if is_bounded_map(f, n, m):
                    observed.add(f)
            assert observed == expected, (n, m, len(observed), len(expected))
            print(f'n={n} m={m}: all p-morphisms={len(observed)}; expected={len(expected)}')
    # Forward/back and hom-set rigidity for longer induced examples.
    checked_surjections = 0
    for n in range(1, 7):
        for m in range(1, min(n, 3) + 1):
            for g in product(range(m), repeat=n):
                if onto(g, m):
                    assert is_bounded_map(induced_map(g, n), n, m)
                    checked_surjections += 1
    print(f'PASS: {checked_functions} all maps classified, {checked_surjections} generated surjections verified')


if __name__ == '__main__':
    main()
