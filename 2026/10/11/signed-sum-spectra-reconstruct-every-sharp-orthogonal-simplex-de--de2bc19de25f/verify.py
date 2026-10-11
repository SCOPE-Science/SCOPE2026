from collections import Counter
from fractions import Fraction
from math import comb

def block_measure(k):
    c = Counter()
    for t in range(k // 2 + 1):
        c[Fraction(4*t*(t+1), k)] += 2 * comb(k+1, k//2-t)
    assert sum(c.values()) == 2**(k+1)
    return c

def conv(a, b):
    c = Counter()
    for x, ax in a.items():
        for y, by in b.items():
            c[x+y] += ax*by
    return c

def partitions_even(total_max, parts, lo=2):
    if parts == 0:
        yield ()
        return
    for k in range(lo, total_max+1, 2):
        for rest in partitions_even(total_max-k, parts-1, k):
            yield (k,) + rest

def spectrum(d, ks):
    r = d - sum(ks)
    assert r >= 0
    c = Counter({Fraction(0): 2**r})
    for k in ks:
        c = conv(c, block_measure(k))
    return c

configs = 0
for d in range(1, 17):
    for m in range(0, d//2 + 1):
        n = d + m
        seen = {}
        if m == 0:
            cases = [()]
        else:
            cases = [ks for ks in partitions_even(d, m) if sum(ks) <= d]
        for ks in cases:
            configs += 1
            c = spectrum(d, ks)
            key = tuple(sorted(c.items()))
            if key in seen and seen[key] != ks:
                raise AssertionError(("collision", d, n, seen[key], ks))
            seen[key] = ks
            if ks:
                K = max(ks)
                q = sum(k == K for k in ks)
                pos = sorted(x for x in c if x > 0)
                first = pos[0]
                assert first == Fraction(8, K), (d, ks, first, K)
                ratio = Fraction(c[first], c[Fraction(0)])
                assert ratio == Fraction(q*K, K+4), (d, ks, ratio, q, K)

print(f"VERIFY_OK configurations={configs} max_dimension=16 collisions=0")
