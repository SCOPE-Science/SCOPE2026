#!/usr/bin/env python3
"""Independent direct-map verification of interval-translation commuting counts."""
from math import comb


def choose(n, k):
    return comb(n, k) if n >= k >= 0 else 0


def direct_maps(n):
    maps = [tuple([-1] * n)]
    shifts = [None]
    for length in range(1, n + 1):
        for src in range(0, n - length + 1):
            for dst in range(0, n - length + 1):
                f = [-1] * n
                for j in range(length):
                    f[src + j] = dst + j
                maps.append(tuple(f))
                shifts.append(dst - src)
    return maps, shifts


def compose(f, g):
    # First apply f and then g; -1 represents the undefined value.
    return tuple(-1 if j < 0 else g[j] for j in f)


def expected(n):
    count = 1 + n * (n + 1) * (2 * n + 1) // 6
    z = n * (n - 1) * (n + 1) * (n + 2) * (n*n + n - 1) // 30
    idem = choose(n + 1, 2)**2 - 2 * choose(n + 2, 4)
    mixed = 4 * choose(n + 3, 5)
    strict = 2 * choose(n + 1, 4)
    p = n * (n + 1) * (2*n**3 + 23*n*n - 3*n + 8) // 60
    total = (2*n**6 + 8*n**5 + 25*n**4 + 50*n**3 + 63*n*n + 32*n + 60) // 60
    assert p == idem + mixed + strict
    assert total == z + p + 2*count - 1
    return count, z, p, total, (idem, mixed, strict, 0)


def verify(n):
    maps, shifts = direct_maps(n)
    size, zz, pp, tt, categories = expected(n)
    assert len(maps) == size
    zero = maps[0]
    zero_mutual = 0
    nonzero = 0
    by_type = [0] * 4
    total = 0
    for i, f in enumerate(maps):
        for j, g in enumerate(maps):
            fg = compose(f, g)
            gf = compose(g, f)
            if fg != gf:
                continue
            total += 1
            if i == 0 or j == 0:
                continue
            if fg == zero:
                zero_mutual += 1
                continue
            nonzero += 1
            d, e = shifts[i], shifts[j]
            if d == e == 0:
                cat = 0
            elif d == 0 or e == 0:
                cat = 1
            elif d * e > 0:
                cat = 2
            else:
                cat = 3
            by_type[cat] += 1
    assert (zero_mutual, nonzero, total, tuple(by_type)) == (zz, pp, tt, categories), (
        n, zero_mutual, nonzero, total, by_type, expected(n))
    return n, size, zero_mutual, nonzero, total


if __name__ == '__main__':
    for n in range(1, 11):
        print('n,size,mutually_zero,commute_nonzero,total=', *verify(n))
    print('VERIFY_OK 10 exact direct-map enumerations; four nonzero-product shift classes')
