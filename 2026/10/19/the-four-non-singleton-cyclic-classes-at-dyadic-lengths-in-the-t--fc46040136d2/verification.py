#!/usr/bin/env python3
"""Complete-factor finite checks for a dyadic Thue-Morse cyclic-orbit profile."""
from collections import Counter, defaultdict

TRANS = str.maketrans({'0': '01', '1': '10'})

def morph(w):
    return ''.join('01' if ch == '0' else '10' for ch in w)

def iterate(w, r):
    for _ in range(r):
        w = morph(w)
    return w

def all_factors(n):
    # Exhaustive cover: any n-window intersects at most two 2^r-aligned
    # blocks if 2^r >= n; all four underlying adjacent-letter pairs occur.
    r = max(1, (n - 1).bit_length())
    return {blk[i:i+n]
            for a in '01' for b in '01'
            for blk in (iterate(a+b, r),)
            for i in range(len(blk) - n + 1)}

def least_rotation(s):
    n = len(s)
    ss = s+s
    i, j, k = 0, 1, 0
    while i < n and j < n and k < n:
        if ss[i+k] == ss[j+k]:
            k += 1
        elif ss[i+k] > ss[j+k]:
            i += k+1
            if i <= j: i = j+1
            k = 0
        else:
            j += k+1
            if j <= i: j = i+1
            k = 0
    h = min(i, j)
    return ss[h:h+n]

def rotations(s):
    return {s[i:]+s[:i] for i in range(len(s))}

def run():
    w = iterate('0', 17)
    for n in range(1, 18):
        f = all_factors(n)
        sample = {w[i:i+n] for i in range(len(w)-n+1)}
        assert f == sample, ('factor_cover', n)
        for s in f:
            assert least_rotation(s) == min(rotations(s)), ('booth', n, s)
    assert all_factors(3) == {'001','010','011','100','101','110'}
    assert len(all_factors(4)) == 10
    assert len(all_factors(5)) == 12

    for k in range(2, 10):
        n = 1 << k
        f = all_factors(n)
        fp = all_factors(n+1)
        groups = defaultdict(set)
        for s in f:
            groups[least_rotation(s)].add(s)
        histogram = Counter(map(len, groups.values()))
        assert histogram == Counter({1:2*n-8, 2:3, n:1}), ('histogram', k, histogram)
        t = iterate('0', k)
        assert len(rotations(t)) == n
        assert groups[least_rotation(t)] == rotations(t), ('full_class', k)
        one_step = {s for s in f if s+s[0] in fp}
        assert one_step == rotations(t), ('extendible', k)
        assert sum(s[0] != s[-1] for s in fp) == 2*n, ('D_count', k)
        for seed in ('0010', '0101', '1011'):
            representative = iterate(seed, k-2)
            assert representative in f
            assert len(groups[least_rotation(representative)]) == 2
        if n <= 128:
            prefix_f = {w[i:i+n] for i in range(len(w)-n+1)}
            assert f == prefix_f, ('independent_prefix', k)
        print('N', n, 'factors', len(f), 'singletons', histogram.get(1,0),
              'doubletons', histogram[2], 'full_orbits', histogram[n])
    print('VERIFY_OK')

if __name__ == '__main__':
    run()
