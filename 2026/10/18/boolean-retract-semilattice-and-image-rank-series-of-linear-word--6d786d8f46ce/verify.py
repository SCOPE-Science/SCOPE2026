"""Independent finite checks for interval-semiring retract classification.
Run: python verify.py; uses only Python standard library.
"""
from itertools import product
from collections import Counter


def elements(m):
    return [None] + [(i, j) for i in range(1, m+1) for j in range(i, m+1)]


def multiply(a, b):
    if a is not None and b is not None and a[1] + 1 == b[0]:
        return (a[0], b[1])
    return None


def additive(a, b):
    return a if a == b else None


def brute(m):
    E = elements(m)
    nz = E[1:]
    counts = Counter()
    retracts = set()
    for images_of_letters in product(E, repeat=m):
        f = {None: None}
        for i in range(1, m+1):
            value = images_of_letters[i-1]
            for j in range(i, m+1):
                if j > i:
                    value = multiply(value, images_of_letters[j-1])
                f[(i, j)] = value
        # Check the ORIGINAL operations on every ordered pair, not a shortcut.
        if any(f[additive(x, y)] != additive(f[x], f[y])
               or f[multiply(x, y)] != multiply(f[x], f[y])
               for x in E for y in E):
            continue
        counts[sum(f[x] is not None for x in nz)] += 1
        if all(f[f[x]] == f[x] for x in E):
            retracts.add(tuple(f[x] for x in E))
    return counts, retracts


def predicted(m):
    E = elements(m)
    profiles = Counter()
    maps = set()
    for bits in product([0, 1], repeat=m):
        f = tuple(None if x is None or not all(bits[k-1] for k in range(x[0], x[1]+1)) else x
                  for x in E)
        maps.add(f)
        profiles[sum(x is not None for x in f)] += 1
    return profiles, maps


def recurrence_coeff(m):
    # Enumerate binary words via their maximal 1-run lengths.
    a = [None] * (m+1)
    a[0] = Counter({0: 1})
    for n in range(1, m+1):
        c = a[n-1].copy()
        for ell in range(1, n+1):
            v = (ell*(ell+1))//2
            prev = a[n-ell-1] if n-ell-1 >= 0 else Counter({0: 1})
            for r, count in prev.items():
                c[r+v] += count
        a[n] = c
    return a[m]


def run():
    for m in range(1, 5):
        c, ret = brute(m)
        p, maps = predicted(m)
        assert ret == maps, ('retract mismatch', m)
        assert Counter({sum(x is not None for x in f): 0 for f in ret}) is not None
        assert Counter(sum(x is not None for x in f) for f in ret) == p
        assert p == recurrence_coeff(m)
        assert len(ret) == 2**m
        print('m=',m, 'all_endomorphisms=',sum(c.values()),
              'idempotents=',len(ret), 'retract_image_rank_counts=',dict(sorted(p.items())))
    expected = {0:1,1:4,2:3,3:3,4:2,6:2,10:1}
    assert predicted(4)[0] == expected
    print('VERIFY_OK: exact all-pair additive/multiplicative homomorphism tests passed')

if __name__ == '__main__':
    run()
