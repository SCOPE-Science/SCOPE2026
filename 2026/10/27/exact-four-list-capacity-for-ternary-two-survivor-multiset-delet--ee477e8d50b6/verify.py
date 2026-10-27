#!/usr/bin/env python3
"""Independent finite sanity tests of an exact ternary multiset list-decoding theorem."""
from itertools import combinations
from math import comb


def words(n):
    return [(a, b, n-a-b) for a in range(n+1) for b in range(n-a+1)]


def observations():
    return [(2,0,0), (0,2,0), (0,0,2),
            (1,1,0), (1,0,1), (0,1,1)]


def trace(x):
    return tuple(i for i, y in enumerate(observations())
                 if all(x[j] >= y[j] for j in range(3)))


def candidate(n):
    if n < 4:
        raise ValueError('candidate is for n >= 4')
    pool = []
    for i in range(3):
        z = [0, 0, 0]; z[i] = n; pool.append(tuple(z))
    for i in range(3):
        for j in range(3):
            if i != j:
                z = [0, 0, 0]; z[i] = n-1; z[j] = 1
                pool.append(tuple(z))
    pool += [(n-2, 1, 1), (1, n-2, 1)]
    return pool


def occupancy(code):
    counts = [0] * 6
    for w in code:
        for k in trace(w):
            counts[k] += 1
    return counts


def verify_candidate(n):
    C = candidate(n)
    assert len(C) == len(set(C)) == 11
    assert all(sum(w) == n for w in C)
    occ = occupancy(C)
    assert occ == [4, 4, 3, 4, 4, 4], (n, occ)
    return tuple(occ)


def exhaustive_rule_out_twelve(n):
    # Complete search over ALL 12-element subfamilies of the length-n simplex.
    W = words(n)
    traces = [trace(w) for w in W]
    count = 0
    for sel in combinations(range(len(W)), 12):
        count += 1
        degrees = [0] * 6
        valid = True
        for ix in sel:
            for k in traces[ix]:
                degrees[k] += 1
                if degrees[k] > 4:
                    valid = False
                    break
            if not valid:
                break
        assert not valid, (n, [W[ix] for ix in sel])
    assert count == comb(len(W), 12)
    return count


def degree_profile(n):
    W = words(n)
    hist = {}
    for w in W:
        d = len(trace(w))
        hist[d] = hist.get(d, 0) + 1
    assert hist.get(1) == 3 and hist.get(2) == 6
    assert all(d >= 3 for d in hist if d not in (1, 2))
    # Each degree-3 source is supported on precisely two letters,
    # both with multiplicity >=2, hence produces two monochromatics.
    for w in W:
        if len(trace(w)) == 3:
            assert sum(int(v >= 2) for v in w) == 2
    return hist


def main():
    assert len(words(2)) == 6
    assert len(words(3)) == 10
    assert max(occupancy(words(3))) == 3
    for n in range(4, 129):
        verify_candidate(n)
    for n in range(4, 33):
        degree_profile(n)
    v4 = exhaustive_rule_out_twelve(4)
    v5 = exhaustive_rule_out_twelve(5)
    print('ALL CHECKS PASSED')
    print('all 127 constructions for 4<=n<=128 satisfy 4-list bound')
    print('degree-profile and degree-three monochromatic lemma verified for 4<=n<=32')
    print('exhausted size-12 subfamilies: n=4 count=%d, n=5 count=%d' % (v4, v5))
    print('exact profile at n=2,3,4,5: 6, 10, 11, 11')


if __name__ == '__main__':
    main()
