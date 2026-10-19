#!/usr/bin/env python3
"""Independently check the explicit cyclic and sentinel BWT formula for Zimin words.

Usage: python3 verify.py; uses only the Python standard library.
The exhaustive and finite computations corroborate, but do not prove, the
all-level mathematical statement.
"""

def zimin(n):
    return [(i & -i).bit_length() for i in range(1, 1 << n)]


def predicted_cyclic(n):
    if n == 1:
        return [1]
    output = list(range(2, n+1)) + [1]
    for value in range(n-1, 1, -1):
        output += [value] * ((1 << (n-value)) - 1)
    output += [1] * ((1 << (n-1)) - 1)
    return output


def predicted_sentinel(n):
    output = list(range(1, n+1)) + [0]
    for value in range(n-1, 0, -1):
        output += [value] * ((1 << (n-value)) - 1)
    return output


def naive_cyclic_bwt(w):
    length = len(w)
    order = sorted(range(length), key=lambda i: w[i:] + w[:i])
    return [w[(i-1) % length] for i in order]


def naive_sentinel_bwt(w):
    s = w + [0]
    order = sorted(range(len(s)), key=lambda i: s[i:])
    return [s[(i-1) % len(s)] for i in order]


def cyclic_doubling_sa(w):
    length = len(w)
    rank = w[:]
    ordering = list(range(length))
    step = 1
    while step < length:
        ordering.sort(key=lambda i: (rank[i], rank[(i+step) % length]))
        new_rank = [0]*length
        last = None
        group = -1
        for i in ordering:
            pair = (rank[i], rank[(i+step) % length])
            if pair != last:
                group += 1
                last = pair
            new_rank[i] = group
        rank = new_rank
        step <<= 1
    return ordering


def linear_doubling_sa(w):
    length = len(w)
    rank = w[:]
    ordering = list(range(length))
    step = 1
    while step < length:
        ordering.sort(key=lambda i: (rank[i], rank[i+step] if i+step < length else -1))
        new_rank = [0]*length
        last = None
        group = -1
        for i in ordering:
            pair = (rank[i], rank[i+step] if i+step < length else -1)
            if pair != last:
                group += 1
                last = pair
            new_rank[i] = group
        rank = new_rank
        step <<= 1
    return ordering


def run_count(seq):
    return 1 + sum(a != b for a,b in zip(seq, seq[1:]))


def verify():
    direct_cyclic = direct_sentinel = larger = order_checks = 0
    # Directly sort complete rotations and suffixes at small levels.
    for n in range(1,10):
        w=zimin(n)
        pc=predicted_cyclic(n)
        ps=predicted_sentinel(n)
        assert len(pc)==len(w)
        assert len(ps)==len(w)+1
        assert naive_cyclic_bwt(w) == pc, ('naive cyclic',n)
        direct_cyclic += 1
        assert naive_sentinel_bwt(w) == ps, ('naive sentinel',n)
        direct_sentinel += 1
    # Independent suffix-array and circular-rotation order algorithms.
    for n in range(1,17):
        w=zimin(n)
        cyclic_order=cyclic_doubling_sa(w)
        actual=[w[(i-1)%len(w)] for i in cyclic_order]
        assert actual==predicted_cyclic(n), ('doubling cyclic',n)
        s=w+[0]
        linear_order=linear_doubling_sa(s)
        b=[s[(i-1)%len(s)] for i in linear_order]
        assert b==predicted_sentinel(n), ('doubling suffix',n)
        assert run_count(actual)==(2*n-1 if n>=3 else 2 if n==2 else 1), ('runs',n)
        # The lexicographically sorted odd rotations are ordered by
        # the suffix-array ranks of the preceding Zimin level.
        if n>=2:
            odd_starts=[i for i in cyclic_order if i%2==0]
            parent=zimin(n-1)+[0]
            suffix_order=linear_doubling_sa(parent)
            assert odd_starts == [2*i for i in suffix_order],('projection',n)
            order_checks+=1
        larger+=1
    print(f'VERIFY_OK zimin_BWT direct_cyclic={direct_cyclic} direct_sentinel={direct_sentinel} '
          f'independent_doubling_levels={larger} odd_rotation_suffix_order_levels={order_checks} '
          f'max_level=16 max_word_length={(1<<16)-1} max_cyclic_runs=31')

if __name__=='__main__':
    verify()
