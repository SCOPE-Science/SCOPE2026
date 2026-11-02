#!/usr/bin/env python3
"""Exact finite checks for length-at-most-three binary composition read profiles."""
from collections import Counter, defaultdict
from itertools import combinations, product
from math import comb


def signature(bits):
    n = len(bits)
    return tuple(
        sum(sum(bits[i:i+width]) == grade for i in range(n-width+1))
        for width in (2, 3) for grade in range(1, width+1)
    )


def cap_word(gaps):
    return tuple(int(bit) for bit in '1'.join('0'*g for g in gaps))


def modeled_fibers(n, w):
    image = Counter()
    for h in product(range(3), repeat=w+1):
        t = h.count(2)
        remain = n-w-sum(h)
        if t == 0:
            copies = int(remain == 0)
        else:
            copies = comb(remain+t-1, t-1) if remain >= 0 else 0
        if copies:
            image[signature(cap_word(h))] += copies
    return image


def direct_fibers(n, w):
    image = Counter()
    for chosen in combinations(range(n), w):
        bits = [0]*n
        for i in chosen:
            bits[i] = 1
        image[signature(bits)] += 1
    return image



def indicator_signature_three(h):
    a0,b0,c0,d0 = h
    p = int(b0 == 0) + int(c0 == 0)
    q = int(b0 == 1) + int(c0 == 1)
    u = int(b0 == 0 and c0 == 0)
    boundary_pairs = int(a0 == 0 and b0 == 0) + int(c0 == 0 and d0 == 0)
    endpoint_ones = int(a0 == 0) + int(d0 == 0)
    triple_deficit = (2*int(a0 == 0) + int(a0 == 1 or (a0 == 0 and b0 == 0))
                      + 2*int(d0 == 0) + int(d0 == 1 or (c0 == 0 and d0 == 0)))
    c32 = 2*p + q - 2*u - boundary_pairs
    return (6-endpoint_ones-2*p, p, 9-triple_deficit-2*c32-3*u, c32, u)


def check():
    cases = 0
    for n in range(3, 19):
        for w in range(0, min(n, 6)+1):
            expected = direct_fibers(n, w)
            observed = modeled_fibers(n, w) if w else Counter({(0, 0, 0, 0, 0): 1})
            assert observed == expected, (n, w, observed, expected)
            assert sum(observed.values()) == comb(n,w)
            cases += 1
    print('FIBER_CROSSCHECK_PASS', cases, 'all (n,w) for 3<=n<=18, 0<=w<=min(n,6)')
    tab = [1, 2, 6, 9, 16, 21, 26, 28]
    for n, expected in zip(range(3, 11), tab):
        assert len(modeled_fibers(n,3)) == expected
    for n in range(11, 31):
        assert len(modeled_fibers(n,3)) == 29
    print('WEIGHT_THREE_ALL_LENGTH_PROFILE_PASS', tab, 'then 29 for lengths 11..30')
    for w in range(1, 9):
        before = modeled_fibers(3*w+1,w)
        stable = modeled_fibers(3*w+2,w)
        after = modeled_fibers(3*w+5,w)
        assert len(stable) == len(after)
        assert len(before) < len(stable)
        print('THRESHOLD', w, len(before), len(stable))
    # The 3-marker finite normal-form certificate has 65 feasible capped tuples.
    cap_map=defaultdict(list)
    for h in product(range(3), repeat=4):
        if 2 in h:
            cap_map[signature(cap_word(h))].append(h)
    assert sum(len(v) for v in cap_map.values()) == 65
    assert len(cap_map) == 29
    for h in product(range(3),repeat=4):
        assert indicator_signature_three(h)==signature(cap_word(h)), h
    classes=sorted(cap_map.items())
    for sig, members in classes:
        h=min(members, key=lambda x:(sum(x),x))
        word = cap_word(h)
        assert signature(word)==sig
        assert 3+sum(h)<=11
        # Stretch the first gap of length >=2 to total length 11.
        ext=list(h)
        ext[next(i for i,x in enumerate(h) if x==2)] += 8-sum(h)
        assert len(cap_word(ext)) == 11
        assert signature(cap_word(ext))==sig
    print('CAP_SIGNATURE_CERTIFICATE_PASS 65 tuples in 29 classes with length-11 witnesses')
    # Example of two sources with the same length-three composition deck
    # but different length-two profiles.
    a=tuple(map(int, '11000000100'))
    b=tuple(map(int, '10100000010'))
    assert signature(a)[2:]==signature(b)[2:]
    assert signature(a)[:2]!=signature(b)[:2]
    print('ADDED_SHORT_READ_INFORMATION_PASS')
    print('VERIFY_OK')


if __name__=='__main__':
    check()
