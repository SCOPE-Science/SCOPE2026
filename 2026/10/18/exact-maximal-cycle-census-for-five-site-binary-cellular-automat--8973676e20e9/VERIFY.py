#!/usr/bin/env python3
"""Exact finite census for 5-cell equivariant maps, Python 3 standard library only."""
from collections import Counter

def rotate(x):
    return ((x << 1) & 31) | (x >> 4)

def necklace(x):
    p = x
    for _ in range(5):
        p = min(p, x)
        x = rotate(x)
    return p

NECK = [necklace(x) for x in range(32)]
REPS = sorted(set(NECK))
assert len(REPS) == 8 and sum(NECK.count(r) == 5 for r in REPS) == 6

# Precompute look-up indices for algorithm A.
IDX = [[sum(((x >> ((i + k + 1) % 5)) & 1) << k for k in range(4))
        for i in range(5)] for x in range(32)]

def direct_image(tt):
    im = []
    for x in range(32):
        y = 0
        for i in range(5):
            y += ((tt >> IDX[x][i]) & 1) << i
        im.append(y)
    return im

def second_image(tt, x):
    # Independent coordinate-string construction instead of index lookup.
    w = format(x, '05b')[::-1]
    out = []
    for i in range(5):
        stencil = [int(w[(i+j)%5]) for j in (1, 2, 3, 4)]
        address = stencil[0] + 2*stencil[1] + 4*stencil[2] + 8*stencil[3]
        out.append((tt >> address) & 1)
    return sum(bit << i for i, bit in enumerate(out))

def anf_degree(tt):
    t = [(tt >> i) & 1 for i in range(16)]
    for bit in (1, 2, 4, 8):
        for i in range(16):
            if i & bit:
                t[i] ^= t[i ^ bit]
    return max([i.bit_count() for i in range(16) if t[i]] or [0])

def cycle_signature(im):
    visited = 0
    lens = []
    for s in range(32):
        if (visited >> s) & 1:
            continue
        x = s
        k = 0
        while not (visited >> x) & 1:
            visited |= 1 << x
            x = im[x]
            k += 1
        assert x == s
        lens.append(k)
    assert visited == 0xffffffff
    return tuple(sorted(Counter(lens).items()))

def main():
    tally = Counter()
    degrees = Counter()
    special = Counter()
    type_counts = Counter()
    witnesses = {}
    checks = 0
    for tt in range(1 << 16):
        im = direct_image(tt)
        images_bijective = len(set(im)) == 32
        # Independent orbit-based test. Rotation acts with orbit sizes 1 and 5.
        const_images = [second_image(tt, r) for r in REPS if NECK.count(r) == 1]
        other_images = [second_image(tt, r) for r in REPS if NECK.count(r) == 5]
        bij_orbit = (len(set(const_images)) == 2 and
                     all(NECK[v] in (0,31) for v in const_images) and
                     len(set(NECK[v] for v in other_images)) == 6 and
                     all(NECK.count(NECK[v]) == 5 for v in other_images))
        assert images_bijective == bij_orbit, (tt, im)
        checks += 1
        if not images_bijective:
            continue
        deg = anf_degree(tt)
        degrees[deg] += 1
        cycles = cycle_signature(im)
        tally[cycles] += 1
        if any(length == 30 for length, _ in cycles):
            special[deg] += 1
            type_counts[cycles] += 1
            witnesses.setdefault((deg,cycles), tt)
            assert cycles in (((1,2),(30,1)), ((2,1),(30,1))), (tt,cycles)
            assert sum(mult for length,mult in cycles if length==30) == 1
        # Separate invariance check for every bijective map.
        for x in range(32):
            assert im[rotate(x)] == rotate(im[x]); checks += 1
    assert sum(tally.values()) == 472, tally
    assert degrees == Counter({1:16,2:64,3:392}), degrees
    assert len(tally) == 28, len(tally)
    assert sum(special.values()) == 96, special
    assert special == Counter({1:4,2:16,3:76}), special
    assert type_counts == Counter({((1,2),(30,1)):32, ((2,1),(30,1)):64}), type_counts
    # Independent witness replay on all states via second builder.
    for (_, _), tt in witnesses.items():
        image = [second_image(tt, x) for x in range(32)]
        assert len(set(image)) == 32
        assert max(l for l,_ in cycle_signature(image)) == 30
        checks += 32
    print('VERIFY_OK: 65536 functions; 472 bijections; 28 cycle types; 96 primitive-30 rules;',
          'degree profile 4/16/76; leftovers 32 fixed-pair and 64 swapped-pair;',
          'checks',checks)
    print('WITNESSES',witnesses)

if __name__ == '__main__':
    main()
