"""Finite exact checks for the parallel binary carrying bound.

All arithmetic is integral. The theorem itself is proved in RESULT.md;
finite checks exercise its hypotheses and compare two independent updates.
"""
from itertools import product


def weight(c):
    return sum(v << k for k, v in enumerate(c))


def step(c):
    a = list(c) + [0]
    return [(v & 1) + ((a[k - 1] >> 1) if k else 0)
            for k, v in enumerate(a)]


def depth(c):
    c = list(c)
    t = 0
    target = weight(c)
    while any(v > 1 for v in c):
        c = step(c)
        t += 1
        assert weight(c) == target, "weighted mass changed"
        assert t <= target.bit_length() + 2
    return t


def convolution(a, b):
    out = [0] * (a.bit_length() + b.bit_length() - 1)
    for i in range(a.bit_length()):
        if (a >> i) & 1:
            for j in range(b.bit_length()):
                out[i + j] += ((b >> j) & 1)
    return out


def other_step(c):
    out = [0] * (len(c) + 1)
    for i, v in enumerate(c):
        out[i] += v % 2
        out[i + 1] += v // 2
    return out


def checks():
    sequence_count = 0
    for length in range(1, 6):
        for q in product(range(4), repeat=length):
            n = weight(q)
            if not n:
                continue
            candidates = [i for i, v in enumerate(q) if v >= 2]
            t = depth(q)
            if candidates:
                r = candidates[0]
                assert t >= 1
                assert t <= n.bit_length() - 1 - r, (q, t)
            else:
                assert t == 0
            assert step(q) == other_step(q)
            sequence_count += 1
    pairs = 0
    for a in range(1, 256):
        for b in range(1, 256):
            c = convolution(a, b)
            assert weight(c) == a * b
            t = depth(c)
            if t:
                r = next(i for i, v in enumerate(c) if v >= 2)
                assert r >= 1
                assert t <= (a * b).bit_length() - 2
                assert t <= a.bit_length() + b.bit_length() - 2
                assert t <= (a * b).bit_length() - 1 - r
            pairs += 1
    sharp = 0
    for k in range(3, 52, 2):
        b = ((1 << k) + 1) // 3
        c = convolution(3, b)
        assert c[:k] == [1, 2] + [1] * (k - 2)
        assert depth(c) == k - 1
        sharp += 1
    print(f"VERIFY_OK general_sequences={sequence_count} multiplier_pairs={pairs} sharp_families={sharp}")


if __name__ == "__main__":
    checks()
