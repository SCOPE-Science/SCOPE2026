"""Reproduce the canonical-rotation parity classification and its generating series."""
from itertools import product
from math import gcd


def alternating_key(w):
    return tuple((int(c) if i % 2 == 0 else 1 - int(c)) for i, c in enumerate(w))


def gap_lengths(w):
    assert w.startswith('0') and w.endswith('1') and '00' not in w + w[0]
    return tuple(len(z) for z in w.split('0') if z)


def predicted(n, parity=None):
    """Count rooted unique-minimum cyclic compositions, no word scanning."""
    total = 0
    for a in range(1, (n - 3) // 2 + 1):
        if parity is not None and a % 2 != parity:
            continue
        # Unique distinguished run has length a; all other runs >=a+1.
        # For r-1 = k, the slack is n-(a+1)-k*(a+2).
        for k in range(1, (n - a - 1) // (a + 2) + 1):
            slack = n - (a + 1) - k * (a + 2)
            if slack >= 0:
                from math import comb
                total += comb(slack + k - 1, k - 1)
    return total


def brute(n):
    odd, even = 0, 0
    for bits in product('01', repeat=n):
        w = ''.join(bits)
        if w[0] != '0' or w[-1] != '1' or w.count('0') < 2:
            continue
        if '00' in w + w[0]:
            continue
        if any(w > w[i:] + w[:i] for i in range(1,n)):
            continue
        gaps = gap_lengths(w)
        a = min(gaps)
        if gaps.count(a) != 1:
            continue
        lex = w
        alt = min((w[i:] + w[:i] for i in range(n)), key=alternating_key)
        if (lex == alt) != (a % 2 == 1):
            raise AssertionError((n,w,gaps,lex,alt))
        if a % 2 == 1: odd += 1
        else: even += 1
    return odd, even


if __name__ == '__main__':
    test = []
    for n in range(1,19):
        p_odd, p_even = predicted(n,1),predicted(n,0)
        o_odd, o_even = brute(n)
        assert (p_odd,p_even)==(o_odd,o_even),(n,(p_odd,p_even),(o_odd,o_even))
        test.append((n,o_odd,o_even))
    # Validate the whole-class obstruction independent of unique-min restriction.
    for n in range(2,15):
        for bits in product('01', repeat=n):
            w = ''.join(bits)
            if w.count('0') == 0 or w.count('1') == 0:
                continue
            rotations = [w[i:] + w[:i] for i in range(n)]
            if len(set(rotations)) != n:
                continue
            if w != min(rotations) or w != min(rotations,key=alternating_key):
                continue
            assert '00' not in w+w[0], (n,w)
            if w.count('0') >= 2:
                assert min(gap_lengths(w)) % 2 == 1, (n,w)
    print('GALOIS_LYNDON_UNIQUE_SHORTEST_PASS exhaustive_n=1..18 global_obstruction_n=2..14')
    print('n,odd,even:', test)
