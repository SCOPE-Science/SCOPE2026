from itertools import product
from math import comb


def pairs_nat(n):
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def posets_natural(n):
    pairs = pairs_nat(n)
    for mask in range(1 << len(pairs)):
        E = {pairs[k] for k in range(len(pairs)) if (mask >> k) & 1}
        ok = True
        for a, b in tuple(E):
            for bb, c in tuple(E):
                if b == bb and (a, c) not in E:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            yield E


def is_antichain(mask, n, E):
    xs = [i for i in range(n) if (mask >> i) & 1]
    return all((a, b) not in E and (b, a) not in E
               for i, a in enumerate(xs) for b in xs[i + 1:])


def antichains(n, E):
    return [m for m in range(1 << n) if is_antichain(m, n, E)]


def status_count(n, E):
    total = 0
    # -1 means a<x, 0 incomparable, +1 means x<a.
    for s in product((-1, 0, 1), repeat=n):
        L = {i for i, t in enumerate(s) if t == -1}
        U = {i for i, t in enumerate(s) if t == 1}
        # L is an ideal.
        if any(b in L and a not in L for a, b in E):
            continue
        # U is a filter.
        if any(a in U and b not in U for a, b in E):
            continue
        # Cross condition.
        if any((l, u) not in E for l in L for u in U):
            continue
        total += 1
    return total


def separated_pair_data(n, E):
    ants = antichains(n, E)
    J = len(ants)
    total = 0
    q = 0
    for X in ants:
        xs = [i for i in range(n) if (X >> i) & 1]
        for Y in ants:
            ys = [j for j in range(n) if (Y >> j) & 1]
            if all((x, y) in E for x in xs for y in ys):
                total += 1
                if X and Y:
                    q += 1
    return total, J, q


def pair_stats(n, E):
    cmp_ = 0
    inc = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (i, j) in E or (j, i) in E:
                cmp_ += 1
            else:
                inc += 1
    return inc, cmp_


checked = 0
for n in range(7):
    vals = []
    argmin = []
    argmax = []
    full_chain = {(i, j) for i in range(n) for j in range(i + 1, n)}
    antichain = set()
    for E in posets_natural(n):
        checked += 1
        c1 = status_count(n, E)
        c2, J, q = separated_pair_data(n, E)
        assert c1 == c2, (n, E, c1, c2)
        assert c1 == 2 * J - 1 + q, (n, E, c1, J, q)
        assert q <= (1 << n) - J, (n, E, q, J)
        inc, cmp_ = pair_stats(n, E)
        lo = comb(n + 2, 2) + inc
        hi = (1 << (n + 1)) - 1 - cmp_
        assert lo <= c1 <= hi, (n, E, lo, c1, hi)
        vals.append((c1, E))
    mn = min(v for v, _ in vals)
    mx = max(v for v, _ in vals)
    mins = [E for v, E in vals if v == mn]
    maxs = [E for v, E in vals if v == mx]
    assert mn == comb(n + 2, 2)
    assert mx == (1 << (n + 1)) - 1
    assert mins == [full_chain], (n, len(mins), mins[:3])
    assert maxs == [antichain], (n, len(maxs), maxs[:3])
    print(f'n={n} posets={len(vals)} min={mn} max={mx}')

# Independent closed-form spot checks beyond the exhaustive range.
for n in range(8):
    chain = {(i, j) for i in range(n) for j in range(i + 1, n)}
    anti = set()
    assert status_count(n, chain) == comb(n + 2, 2)
    assert status_count(n, anti) == (1 << (n + 1)) - 1

print('checked_posets=', checked)
print('VERIFY_OK')
