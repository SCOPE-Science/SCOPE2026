"""Finite exact checks of a cyclic two-letter transformation system.

These finite checks do not replace the proof for every positive parameter.
Run with: python3 verify.py
"""
from collections import deque
from itertools import combinations, product


def compose(f, g):
    """f after g, on {0,...,n-1}."""
    return tuple(f[g[i]] for i in range(len(f)))


def monoid(a, b):
    n = len(a)
    ident = tuple(range(n))
    seen = {ident}
    todo = deque([ident])
    while todo:
        f = todo.popleft()
        for g in (a, b):
            h = compose(g, f)
            if h not in seen:
                seen.add(h)
                todo.append(h)
    return seen


def expected_monoid(a, b):
    n = len(a)
    ident = tuple(range(n))
    result = set()
    powers = []
    p = ident
    for _ in range(n):
        powers.append(p)
        p = compose(b, p)
    assert p == ident
    for p in powers:
        result.add(p)
        for e in (0, 1):
            result.add(compose(p, compose(a, powers[e])))
    return result


def check_family(m):
    n = 2 * m
    a = tuple(i - i % 2 for i in range(n))
    b = tuple((i + 1) % n for i in range(n))
    s = monoid(a, b)
    form = expected_monoid(a, b)
    assert s == form, (m, "normal-form mismatch")
    assert len(s) == 3 * n, (m, "monoid size")
    assert {len(set(f)) for f in s} == {m, n}
    assert set(b) == set(range(n))
    for x in range(n):
        assert {f[x] for f in s} == set(range(n))
        for y in range(n):
            actual = any(f[x] == f[y] for f in s)
            wanted = (x == y or (x - y) % n in (1, n - 1))
            assert actual == wanted, (m, x, y)
            backward = any(f[z] == x == y for f in s for z in range(n))
            assert backward == (x == y), (m, x, y, "backward")
    return n * n + 5


def check_small_two_letter(n):
    transformations = list(product(range(n), repeat=n))
    pairs_tested = 0
    for i, a in enumerate(transformations):
        for b in transformations[i:]:
            s = monoid(a, b)
            if any({f[x] for f in s} != set(range(n)) for x in range(n)):
                continue
            p = {(x, y): any(f[x] == f[y] for f in s)
                 for x in range(n) for y in range(n)}
            assert all(not (p[x, y] and p[y, z]) or p[x, z]
                       for x in range(n) for y in range(n) for z in range(n))
            pairs_tested += 1
    return pairs_tested


if __name__ == "__main__":
    assertions = 0
    for m in range(2, 17):
        assertions += check_family(m)
    small = {n: check_small_two_letter(n) for n in (2, 3)}
    print("PASS: exact transformation-monoid and pair-relation tests")
    print("Even-cycle systems tested: m=2,...,16")
    print("Individual indexed pair/normal-form checks (lower bound):", assertions)
    print("Strongly connected two-letter automata checked at n=2,3:", small)
    print("Unbounded claims require the accompanying proof, not this finite run.")
