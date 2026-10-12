"""Finite sanity tests for modal valuation on equivalence classes of size at most two.

Run with Python 3: python verify.py. Finite checks are not formal proofs in RCA_0.
"""
from functools import lru_cache
from itertools import product


def pair_partitions(n):
    if not n:
        yield ()
    else:
        for tail in pair_partitions(n - 1):
            yield ((n - 1,),) + tail
        for j in range(n - 1):
            for tail in pair_partitions(n - 1):
                if (j,) in tail:
                    yield tuple(tuple(sorted((j, n - 1))) if block == (j,) else block for block in tail)


def relation(n, blocks):
    r = [[False] * n for _ in range(n)]
    for block in blocks:
        for x in block:
            for y in block:
                r[x][y] = True
    return r


def apply_formula(f, w, truth, r, mate=None):
    if f[0] == "var":
        return truth[w]
    if f[0] == "bot":
        return False
    if f[0] == "imp":
        return (not apply_formula(f[1], w, truth, r, mate)) or apply_formula(f[2], w, truth, r, mate)
    if f[0] == "box":
        if mate is None:
            return all(not r[w][v] or apply_formula(f[1], v, truth, r) for v in range(len(r)))
        return apply_formula(f[1], w, truth, r, mate) and apply_formula(f[1], mate[w], truth, r, mate)
    raise ValueError(f)


P = ("var",)
B = ("bot",)
I = lambda a, b: ("imp", a, b)
BOX = lambda a: ("box", a)
FORMULAS = [P, B, I(P, B), I(P, P), BOX(P), BOX(B), BOX(I(P, B)), BOX(BOX(P)),
            I(BOX(P), P), BOX(I(BOX(P), P)), I(BOX(BOX(P)), BOX(P))]


def check_small_frames():
    checks, frames, assignments = 0, 0, 0
    for n in range(1, 7):
        for blocks in pair_partitions(n):
            frames += 1
            assert sorted(x for block in blocks for x in block) == list(range(n))
            assert all(1 <= len(block) <= 2 for block in blocks)
            r = relation(n, blocks)
            assert all(r[w][w] for w in range(n))
            assert all(r[x][y] == r[y][x] for x in range(n) for y in range(n))
            assert all(not (r[x][y] and r[y][z]) or r[x][z]
                       for x in range(n) for y in range(n) for z in range(n))
            mate = [next((v for v in range(n) if v != w and r[w][v]), w) for w in range(n)]
            for bits in product((False, True), repeat=n):
                assignments += 1
                for f in FORMULAS:
                    for w in range(n):
                        a = apply_formula(f, w, bits, r)
                        b = apply_formula(f, w, bits, r, mate)
                        assert a == b, (n, blocks, bits, f, w)
                        checks += 1
    return frames, assignments, checks


def check_injective_ranges():
    checked = 0
    samples = [(), (2,), (3, 0), (5, 2, 0, 6), (1, 4, 7, 2, 9)]
    for f in samples:
        lim = max(max(f, default=-1) + 2, len(f) + 2)
        n = 2 * lim + 2 * len(f)
        r = [[x == y for y in range(n)] for x in range(n)]
        even_of = lambda j: 2*j
        odd_of = lambda j: 2*lim + 2*j + 1
        for s, v in enumerate(f):
            x, y = even_of(v), odd_of(s)
            r[x][y] = r[y][x] = True
        for j in range(lim):
            w = even_of(j)
            truth = tuple((x < 2 * lim and x % 2 == 0) for x in range(n))
            v = apply_formula(BOX(P), w, truth, r)
            assert v == (j not in f)
            checked += 1
    return checked


if __name__ == "__main__":
    a, b, c = check_small_frames()
    d = check_injective_ranges()
    print(f"VERIFY_OK frames={a} valuations={b} formula_world_comparisons={c} range_checks={d}")
