"""Finite reconstruction of a crown deleted-product Stong core.

Run with Python 3: python verify.py
No external packages or input files are required.
"""
from itertools import product


def make_crown(n):
    assert n >= 2
    elements = [(level, i) for level in (0, 1) for i in range(n)]

    def leq_element(p, q):
        if p == q:
            return True
        return p[0] == 0 and q[0] == 1 and q[1] in (p[1], (p[1] + 1) % n)

    return elements, leq_element


def check(n):
    elements, less = make_crown(n)
    points = [(u, v) for u, v in product(elements, repeat=2) if u != v]
    pointset = set(points)

    def leq(p, q):
        return less(p[0], q[0]) and less(p[1], q[1])

    core = {p for p in points if not less(p[0], p[1]) and not less(p[1], p[0])}
    removed = pointset - core

    def retract(p):
        if p in core:
            return p
        x, y = p
        assert x[0] != y[0]
        if x[0] == 0:
            j = y[1]
            k = next(k for k in (j, (j - 1) % n) if k != x[1])
            return x, (0, k)
        j = x[1]
        k = next(k for k in (j, (j - 1) % n) if k != y[1])
        return (0, k), y

    assert len(points) == 2 * n * (2 * n - 1)
    assert len(removed) == 4 * n
    assert len(core) == 2 * n * (2 * n - 3)

    for p in points:
        rp = retract(p)
        assert rp in core and leq(rp, p)
        if p in core:
            assert rp == p
        else:
            preds = [q for q in points if q != p and leq(q, p)]
            assert preds and rp in preds
            assert all(leq(q, rp) for q in preds)  # down-beat witness

    for p in points:
        for q in points:
            if leq(p, q):
                assert leq(retract(p), retract(q))

    # Distinct deleted points must be pairwise incomparable. Thus deletions
    # may be performed in any order, each with its same beat witness.
    assert all(not leq(p, q) and not leq(q, p)
               for i, p in enumerate(sorted(removed))
               for q in sorted(removed)[i + 1:])

    # A finite T0 space is a Stong core iff it has no up or down beat point.
    for p in core:
        pred = [q for q in core if q != p and leq(q, p)]
        succ = [q for q in core if q != p and leq(p, q)]
        assert not pred or not any(all(leq(q, w) for q in pred) for w in pred)
        assert not succ or not any(all(leq(w, q) for q in succ) for w in succ)

    def rot_el(x):
        return x[0], (x[1] + 1) % n

    def refl_el(x):
        if x[0] == 0:
            return 0, (-x[1]) % n
        return 1, (1 - x[1]) % n

    for elmap in [rot_el, refl_el]:
        assert all(less(x, y) == less(elmap(x), elmap(y))
                   for x, y in product(elements, repeat=2))
        for p in points:
            gp = (elmap(p[0]), elmap(p[1]))
            assert gp in pointset
            assert retract(gp) == (elmap(retract(p)[0]), elmap(retract(p)[1]))
    for p in points:
        assert retract((p[1], p[0])) == tuple(reversed(retract(p)))

    def has_chain_three():
        return any(leq(p, q) and p != q and leq(q, r) and q != r
                   for p in core for q in core for r in core)

    # Faster equivalent existence test avoids a cubic scan.
    height_three = any(
        p != q and leq(p, q)
        and any(q != r and leq(q, r) for r in core)
        for p in core for q in core
    )
    assert height_three == (n >= 3)
    if n == 2:
        assert all(
            leq(p, q) == less(p[0], q[0]) for p, q in product(core, repeat=2)
        )
        assert len({p[0] for p in core}) == 4
    return len(points), len(removed), len(core), height_three


if __name__ == "__main__":
    for n in range(2, 13):
        total, deleted, core, height_three = check(n)
        print(f"n={n}: total={total}, down-beat={deleted}, core={core}, height3={int(height_three)}")
    print("VERIFY_OK")
