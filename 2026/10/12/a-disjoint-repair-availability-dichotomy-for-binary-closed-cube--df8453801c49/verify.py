"""Finite checks of closed-neighborhood binary cube code repair availability.

Run with Python 3 (standard library only): python3 verify.py.
Finite checks do not replace the all-dimension algebraic arguments.
"""
from functools import lru_cache


def columns(r):
    d = r - 1
    N = 1 << d
    return [sum(1 << j for j in range(N) if j == i or
                (i ^ j).bit_count() == 1) for i in range(N)]


def matvec(cols, t):
    z = 0
    for i, col in enumerate(cols):
        if t >> i & 1:
            z ^= col
    return z


def checks(r):
    cs = columns(r)
    N = len(cs)
    return [(matvec(cs, t) | (t << N), t) for t in range(1, 1 << N)]


def maximum_disjoint_recovery(checkwords, target, length):
    targetbit = 1 << target
    choices = sorted(set(w ^ targetbit for w, _ in checkwords if w & targetbit),
                     key=lambda x: (x.bit_count(), x))
    # A recovery support that contains another is never needed in a maximal disjoint packing.
    minimal = []
    for h in choices:
        if not any((g & h) == g for g in minimal):
            minimal.append(h)
    @lru_cache(maxsize=None)
    def fit(free):
        return max((1 + fit(free ^ h) for h in minimal if (h & free) == h),
                   default=0)
    return fit(((1 << length) - 1) ^ targetbit), len(minimal)


def validate():
    for r in (2, 3, 4):
        cs = columns(r)
        n = len(cs)
        assert len(set(cs)) == n if r >= 3 else True
        assert all(c.bit_count() == r for c in cs)
        s_squared_should_be_identity = r % 2 == 1
        for j in range(n):
            sscol = matvec(cs, cs[j])
            assert sscol == ((1 << j) if s_squared_should_be_identity else 0)
        checks_r = checks(r)
        assert len(checks_r) == 2**n - 1
        # Distinct checks are distinct dual words, and any parity coordinate is attainable.
        assert len({w for w, _ in checks_r}) == len(checks_r)
        for target, expectation in ((0, 1), (n, (1 if r == 3 else r // 2 + 1))):
            avail, minimal_sets = maximum_disjoint_recovery(checks_r, target, 2*n)
            assert avail == expectation, (r, target, avail)
            print(f'r={r} coord={"x" if target < n else "y"}0 '
                  f'availability={avail} inclusion-minimal-repair-sets={minimal_sets}')
        local_expected = {2: (2, 1), 3: (3, 3), 4: (4, 3)}[r]
        for target, expected in ((0, local_expected[0]), (n, local_expected[1])):
            local = min(w.bit_count() - 1 for w, _ in checks_r if (w >> target) & 1)
            assert local == expected, (r, target, local, expected)
            print(f'r={r} coordinate={"x" if target < n else "y"}0 locality={local}')
        if r == 4:
            # Explicit disjoint repairs for y_0; the first is parity-only.
            t_values = (0xc3, 0x11, 0x09)
            word_masks = [matvec(cs, t) | (t << n) for t in t_values]
            assert all(w & (1 << n) for w in word_masks)
            helper_masks = [w ^ (1 << n) for w in word_masks]
            assert all((helper_masks[i] & helper_masks[j]) == 0
                       for i in range(3) for j in range(i + 1, 3))
            assert [matvec(cs, t) for t in t_values] == [0, 0x66, 0x99]
            # Independently enumerate every nonzero vector in image(S_3).
            image = {matvec(cs, t) for t in range(1 << n)}
            assert min(x.bit_count() for x in image if x) == 4
            assert len(image) == 16
    # Direct comparison with punctured word minimum distances for r=2,...,5.
    for r in (2, 3, 4, 5):
        cs = columns(r)
        n = len(cs)
        mind = min(t.bit_count() + matvec(cs, t).bit_count()
                   for t in range(1, 1 << n))
        assert mind == r + (r % 2), (r, mind)
        print(f'r={r} code_minimum_distance={mind}')
    print('VERIFY_OK')

if __name__ == '__main__':
    validate()
