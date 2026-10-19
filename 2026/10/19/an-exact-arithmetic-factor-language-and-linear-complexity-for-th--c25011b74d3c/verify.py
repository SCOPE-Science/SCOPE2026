#!/usr/bin/env python3
"""Reproduce the arithmetic-window language of the powers-of-two indicator."""
from collections import Counter

def odd_part(x):
    assert x > 0
    return x >> ((x & -x).bit_length() - 1)

def is_power_of_two(n):
    return n > 0 and n & (n - 1) == 0

def direct(k, start, step):
    assert start >= 0 and step >= 1
    return sum((1 << i) for i in range(k) if is_power_of_two(start + i * step))

def order_two(h):
    assert h > 0 and h % 2
    q, t = 2 % h, 1
    while q != 1 % h:
        q = (q * 2) % h
        t += 1
    return t

def language(k, check_witness=False):
    assert k >= 1
    output = {0}
    # Every singleton is attained in a sufficiently large gap.
    U = (2 * k).bit_length() + 2
    for a in range(k):
        mask = 1 << a
        output.add(mask)
        if check_witness:
            assert direct(k, (1 << U) - a, 1) == mask
    # For each b, choose t divisible by ord_{odd(b)}(2), large enough
    # to forbid all additional power-of-two entries.
    for b in range(1, k):
        mask = 1 | (1 << b)
        output.add(mask)
        if check_witness:
            e, h = b.bit_length() - odd_part(b).bit_length(), odd_part(b)
            r = order_two(h)
            t = r * (1 + ((2 * k.bit_length()) // r))
            q = (1 << t) - 1
            assert q % h == 0
            assert direct(k, 1 << e, q // h) == mask, (k, b, t)
    # Two selected powers at positions a and b force this pair of
    # normalized integers and can be characterized by a Mersenne divisor.
    T = k.bit_length() - 1
    for t in range(1, T + 1):
        q = (1 << t) - 1
        for a in range(k - 1):
            for b in range(a + 1, k):
                h = b - a
                if a * q > h or q % odd_part(h):
                    continue
                H = odd_part(h)
                mask = 0
                for i in range(k):
                    num = h + (i - a) * q
                    if num > 0 and odd_part(num) == H:
                        mask |= 1 << i
                output.add(mask)
                if check_witness:
                    n, d = (h - a * q) // H, q // H
                    assert d >= 1 and n >= 0
                    assert direct(k, n, d) == mask, (k, a, b, t, mask)
    return output

def main():
    # All candidates have independently checked concrete AP witnesses.
    for k in range(1, 41):
        x = language(k, True)
        assert len(x) <= 30 * k
        assert len(x) >= 2 * k
        if k <= 17:
            for n in range(0, 512):
                for d in range(1, 47):
                    assert direct(k, n, d) in x, (k, n, d)
        if k in (1, 2, 3, 4, 5, 8, 16, 24, 32, 40):
            print(f'AP_POWER_2 k={k} complexity={len(x)} masks_by_weight={dict(sorted(Counter(m.bit_count() for m in x).items()))}')
    # Random-like deterministic AP checks with much larger starts/steps.
    for k in (19, 24, 31, 40):
        L = language(k)
        for j in range(1, 12000):
            n = (j * 982451653) % (1 << 50)
            d = (j * 65537) % (1 << 25) + 1
            assert direct(k, n, d) in L
    print('VERIFY_OK witnesses_all_lengths_1_to_40 direct_small_AP_1_to_17 large_AP_samples_19_24_31_40')
if __name__ == '__main__':
    main()
