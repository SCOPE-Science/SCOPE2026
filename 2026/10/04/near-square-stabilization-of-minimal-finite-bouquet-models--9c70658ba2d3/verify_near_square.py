#!/usr/bin/env python3
import itertools


def canon(p, q, edges):
    rows = [0] * p
    for i, j in edges:
        rows[i] |= 1 << j
    if p <= q:
        best = None
        for perm in itertools.permutations(range(p)):
            cols = []
            for j in range(q):
                v = 0
                for ni, oi in enumerate(perm):
                    if (rows[oi] >> j) & 1:
                        v |= 1 << ni
                cols.append(v)
            key = (p, q, tuple(sorted(cols)))
            if best is None or key < best:
                best = key
        return best
    cols = [0] * q
    for i, j in edges:
        cols[j] |= 1 << i
    best = None
    for perm in itertools.permutations(range(q)):
        rvec = []
        for i in range(p):
            v = 0
            for nj, oj in enumerate(perm):
                if (cols[oj] >> i) & 1:
                    v |= 1 << nj
            rvec.append(v)
        key = (p, q, tuple(sorted(rvec)))
        if best is None or key < best:
            best = key
    return best


def b(e):
    if e == 0:
        return 1
    seen = set()
    for p in range(1, e + 1):
        for q in range(1, e + 1):
            if p * q < e:
                continue
            cells = [(i, j) for i in range(p) for j in range(q)]
            for comb in itertools.combinations(cells, e):
                if len({i for i, _ in comb}) != p:
                    continue
                if len({j for _, j in comb}) != q:
                    continue
                seen.add(canon(p, q, comb))
    return len(seen)


def direct_count(k, d):
    n = k * k - d
    total = 0
    for p in range(1, 2 * k + 2):
        q = 2 * k + 2 - p
        if (p - 1) * (q - 1) < n:
            continue
        e = p * q - ((2 * k + 2) + n - 1)
        if e < 0:
            continue
        seen = set()
        cells = [(i, j) for i in range(p) for j in range(q)]
        for comb in itertools.combinations(cells, e):
            seen.add(canon(p, q, comb))
        total += len(seen)
    return total


bs = [b(e) for e in range(6)]
assert bs == [1, 1, 3, 6, 16, 34], bs
expected = [1, 3, 5, 12, 30, 68]
calc = []
for d in range(6):
    s = bs[d]
    r = 1
    while r * r <= d:
        s += 2 * bs[d - r * r]
        r += 1
    calc.append(s)
assert calc == expected, calc
samples = {(3, 0): 1, (3, 1): 3, (3, 2): 5, (4, 3): 12}
for args, want in samples.items():
    got = direct_count(*args)
    assert got == want, (args, got, want)
print('b_0..b_5 =', bs)
print('deficit counts d=0..5 =', calc)
for args, want in samples.items():
    print('direct', args, '=', want)
print('VERIFY_OK')
