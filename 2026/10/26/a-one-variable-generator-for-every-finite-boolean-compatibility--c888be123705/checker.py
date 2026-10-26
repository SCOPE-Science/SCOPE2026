"""Finite diagnostic for singleton definability on Boolean compatibility frames.

This checks explicit constructive modal-algebra expressions against independent
set-intersection modal semantics. The general theorem is proved symbolically.
"""
from itertools import combinations


def check(n: int):
    worlds = list(range(1, 1 << n))
    all_worlds = set(worlds)
    # Each positive integer masks a nonempty Boolean-algebra element.
    p = {s for s in worlds if ((s & -s).bit_length() % 2) == 1}
    def diamond(f):
        return {s for s in worlds if any(s & t for t in f)}
    t = all_worlds.copy()
    hs = []
    for k in range(1, n + 1):
        target = {s for s in worlds if s & ((1 << (k - 1)) - 1) == 0}
        assert t == target, ('tail invariant', n, k)
        if k < n:
            opposite_parity = p if k % 2 == 0 else all_worlds - p
            q = t & opposite_parity
            union = 0
            for x in q:
                union |= x
            assert union == ((1 << n) - (1 << k)), ('support union', n, k)
            e = t - diamond(q)
        else:
            e = t.copy()
        assert e == {1 << (k - 1)}, ('defined atom', n, k, e)
        h = diamond(e)
        assert h == {s for s in worlds if s & (1 << (k - 1))}, ('coordinate', n, k)
        hs.append(h)
        t -= h
    assert t == set()
    for s in worlds:
        isolate = all_worlds.copy()
        for i, h in enumerate(hs):
            isolate &= h if s & (1 << i) else all_worlds - h
        assert isolate == {s}, ('full definability', n, s)
    return len(worlds), len(hs)


def refine_independently(n: int):
    worlds = list(range(1, 1 << n))
    palette = {s: int(((s & -s).bit_length() % 2) == 1) for s in worlds}
    neighbor = {s: tuple(t for t in worlds if s & t) for s in worlds}
    rounds = 0
    while True:
        signatures = {
            s: (palette[s], frozenset(palette[t] for t in neighbor[s]))
            for s in worlds
        }
        keys = {key: j for j, key in enumerate(sorted(set(signatures.values()), key=repr))}
        new_palette = {s: keys[signatures[s]] for s in worlds}
        if len(set(new_palette.values())) == len(worlds):
            return rounds + 1
        if len(set(new_palette.values())) == len(set(palette.values())):
            raise AssertionError(("partition did not separate worlds", n))
        palette = new_palette
        rounds += 1


def main():
    for n in range(1, 12):
        w, h = check(n)
        refining = refine_independently(n) if n <= 8 else 'not_run'
        print(f'n={n} worlds={w} coordinate_tests={h} world_isolates={w} partition_rounds={refining} OK')
    print('ALL_CHECKS_OK')

if __name__ == '__main__':
    main()
