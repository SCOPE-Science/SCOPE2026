#!/usr/bin/env python3
"""Independent finite switching-orbit checks for marked bipartite type profiles."""
from itertools import product
from math import comb

GROUPS = ('AutStar', 'SwitchLeft', 'SwitchRight', 'SwitchBoth', 'All')


def closed_rank(group, a, b, x, y):
    A, B = a + x, b + y
    E = A * B - a * b
    if not A or not B:
        return 0
    if group == 'AutStar':
        return int(a * b == 0 and E > 0)
    if group == 'SwitchLeft':
        return x if b else A
    if group == 'SwitchRight':
        return y if a else B
    if group == 'SwitchBoth':
        return A + B - 1 - (a + b - 1 if a and b else 0)
    if group == 'All':
        return E
    raise ValueError(group)


def predicted_orbits(group, a, b, x, y):
    E = (a + x) * (b + y) - a * b
    return 1 << (E - closed_rank(group, a, b, x, y))


def direct_translation_masks(group, a, b, x, y):
    A, B = a + x, b + y
    cells = [(i, j) for i in range(A) for j in range(B)]
    base = [(i, j) for i, j in cells if i < a and j < b]
    new = [(i, j) for i, j in cells if not (i < a and j < b)]
    if group == 'All':
        return set(range(1 << len(new)))
    if group == 'AutStar':
        choices = [((), (), c) for c in (0, 1)]
    elif group == 'SwitchLeft':
        choices = [(s, (), 0) for s in product((0, 1), repeat=A)]
    elif group == 'SwitchRight':
        choices = [((), t, 0) for t in product((0, 1), repeat=B)]
    elif group == 'SwitchBoth':
        choices = [(s, t, 0) for s in product((0, 1), repeat=A)
                   for t in product((0, 1), repeat=B)]
    else:
        raise ValueError(group)
    masks = set()
    for s, t, c in choices:
        bit = lambda i, j: c ^ (s[i] if s else 0) ^ (t[j] if t else 0)
        if any(bit(i, j) for i, j in base):
            continue
        m = sum(bit(i, j) << h for h, (i, j) in enumerate(new))
        masks.add(m)
    return masks


def spectrum(group, a, b, k):
    return sum(comb(k, x) * predicted_orbits(group, a, b, x, k-x)
               for x in range(k+1))


def main():
    checks = 0
    for a, b, x, y in product(range(4), repeat=4):
        E = (a+x)*(b+y)-a*b
        if E > 10 or a+b+x+y > 7:
            continue
        for group in GROUPS:
            masks = direct_translation_masks(group, a, b, x, y)
            assert masks and len(masks) & (len(masks)-1) == 0
            actual = (1 << E)//len(masks)
            expect = predicted_orbits(group, a, b, x, y)
            assert actual == expect, (group,a,b,x,y,actual,expect)
            # Quotient really is a partition of the full space.
            if E <= 7:
                unseen = set(range(1 << E))
                orbits = 0
                while unseen:
                    p = next(iter(unseen))
                    orbit = {p ^ mask for mask in masks}
                    assert orbit <= unseen
                    unseen.difference_update(orbit)
                    orbits += 1
                assert orbits == expect
            checks += 1
    assert [spectrum(g, 1, 0, 3) for g in GROUPS] == [41,20,26,11,8]
    assert [spectrum(g, 1, 0, 2) for g in GROUPS] == [7,5,6,4,4]
    assert [spectrum(g, 1, 0, 1) for g in GROUPS] == [2]*5
    for k in range(1, 18):
        assert spectrum('SwitchLeft',0,0,k)==spectrum('SwitchRight',0,0,k)
        for a in range(5):
            assert spectrum('SwitchLeft',a,a,k)==spectrum('SwitchRight',a,a,k)
    for a,b in product(range(5),repeat=2):
        if a != b:
            assert any(spectrum('SwitchLeft',a,b,k)!=spectrum('SwitchRight',a,b,k) for k in (1,2))
    print('ALL_CHECKS_PASS')
    print('direct_transition_checks=',checks)
    print('singleton_base_k1=',[spectrum(g,1,0,1) for g in GROUPS])
    print('singleton_base_k2=',[spectrum(g,1,0,2) for g in GROUPS])
    print('singleton_base_k3=',[spectrum(g,1,0,3) for g in GROUPS])
    print('balanced_base_symmetry_through_k=17')

if __name__ == '__main__':
    main()
