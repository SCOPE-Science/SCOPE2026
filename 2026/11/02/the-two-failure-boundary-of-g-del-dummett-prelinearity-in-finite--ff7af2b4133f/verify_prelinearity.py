"""Exact standalone finite checks for the two-counterexample prelinearity theorem.

Enumerates all posets compatible with an increasing vertex enumeration. Every
finite poset admits a linear extension, so every isomorphism type occurs.
"""
from itertools import combinations
from fractions import Fraction


def posets(n):
    pairs = list(combinations(range(n), 2))
    seen = set()
    for mask in range(1 << len(pairs)):
        lower = [1 << i for i in range(n)]
        for j, (u, v) in enumerate(pairs):
            if mask >> j & 1:
                lower[v] |= 1 << u
        for v in range(n):
            for u in range(v):
                if lower[v] >> u & 1:
                    lower[v] |= lower[u]
        key = tuple(lower)
        if key not in seen:
            seen.add(key)
            yield key


def ideals(lower):
    n = len(lower)
    return [s for s in range(1 << n)
            if all(not (s >> v & 1) or (s & lower[v]) == lower[v]
                   for v in range(n))]


def failures(lower, downsets):
    n = len(lower)
    top = (1 << n) - 1
    def imply(a, b):
        return sum(1 << p for p in range(n)
                   if (lower[p] & a & ~b) == 0)
    return [(a, b) for a in downsets for b in downsets
            if imply(a, b) | imply(b, a) != top]


def is_minimal_failure_form(lower):
    n = len(lower)
    allset = (1 << n) - 1
    for u in range(n):
        for v in range(u + 1, n):
            if (lower[u] >> v & 1) or (lower[v] >> u & 1):
                continue
            L = (lower[u] & lower[v])
            U = allset & ~(L | (1 << u) | (1 << v))
            if not U:
                continue
            if lower[u] != L | (1 << u) or lower[v] != L | (1 << v):
                continue
            if any((lower[w] & (L | (1 << u) | (1 << v))) != (L | (1 << u) | (1 << v)) for w in range(n) if U >> w & 1):
                continue
            if any((lower[w] & L) != lower[w] for w in range(n) if L >> w & 1):
                continue
            if any(not ((lower[x] >> y & 1) or (lower[y] >> x & 1))
                   for x in range(n) for y in range(x+1,n) if L >> x & 1 and L >> y & 1):
                continue
            if any(not ((lower[x] >> y & 1) or (lower[y] >> x & 1))
                   for w in range(n) if U >> w & 1
                   for x in range(n) for y in range(x+1,n)
                   if U >> x & 1 and U >> y & 1 and lower[w] >> x & 1 and lower[w] >> y & 1):
                continue
            return True
    return False


def check():
    for n in range(1, 7):
        total = good = 0
        max_ideals = 0
        best = None
        for lower in posets(n):
            total += 1
            ds = ideals(lower)
            bad = failures(lower, ds)
            assert len(bad) % 2 == 0
            got = len(bad) == 2
            assert got == is_minimal_failure_form(lower), (n, lower, len(bad))
            if got:
                good += 1
                if len(ds) > max_ideals:
                    max_ideals = len(ds)
                    best = lower
        if n >= 3:
            assert max_ideals == 3 + 2 ** (n - 2), (n, max_ideals)
        else:
            assert good == 0
        print(f'CHECKED n={n} natural_posets={total} minimal_failure_posets={good} maximum_algebra_order={max_ideals}')
    for m in range(1, 8):
        n = m + 2
        lower = [(1 << i) for i in range(2)] + [3 | (1 << (i + 2)) for i in range(m)]
        ds = ideals(lower)
        assert len(ds) == 3 + (1 << m)
        assert len(failures(lower, ds)) == 2
        assert is_minimal_failure_form(lower)
    print('EXPLICIT_UNBOUNDED_FAMILY_PASS m=1..7')
    print('ALL_TWO_COUNTEREXAMPLE_PRELINEARITY_CHECKS_PASS')

if __name__ == '__main__':
    check()
