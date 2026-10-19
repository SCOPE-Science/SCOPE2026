#!/usr/bin/env python3
"""Reproducible finite checks of Cantor-word conjugacy counts.

The mathematical result for all scales is established separately by proof.
This program compares two generators, all factors of an explicit long prefix,
and an independent weight-gap based classification at the first eight scales.
"""
from collections import Counter

def cantor_morphism(level):
    w = b'1'
    for _ in range(level):
        w = b''.join(b'101' if x == 49 else b'000' for x in w)
    return w

def ternary_digit_word(length):
    out = bytearray(length)
    for n in range(length):
        q = n
        while q and q % 3 != 1:
            q //= 3
        out[n] = 48 if q else 49
    return bytes(out)

def least_rotation(w):
    n = len(w)
    v = w + w
    i, j, k = 0, 1, 0
    while i < n and j < n and k < n:
        a, b = v[i+k], v[j+k]
        if a == b:
            k += 1
        elif a > b:
            i += k + 1
            if i <= j:
                i = j + 1
            k = 0
        else:
            j += k + 1
            if j <= i:
                j = i + 1
            k = 0
    pos = min(i, j)
    return v[pos:pos+n]

def check(k):
    n = 3**k
    w = cantor_morphism(k+2)
    assert w == ternary_digit_word(len(w))
    fs = {w[i:i+n] for i in range(len(w)-n+1)}
    assert len(fs) == (2*n-1 if k else 2), (k, len(fs))
    cyc = {least_rotation(v) for v in fs}
    assert len(cyc) == 2**(k+1)-k, (k, len(cyc))
    central = cantor_morphism(k)
    pos = [i for i,c in enumerate(central) if c == 49]
    assert len(pos) == 2**k
    x, y = set(), set()
    symmetric = []
    for j, p in enumerate(pos, 1):
        a = central[:p+1]
        left = b'0'*(n-len(a)) + a
        right = a[::-1] + b'0'*(n-len(a))
        lc = least_rotation(left)
        rc = least_rotation(right)
        assert left in fs and right in fs
        x.add(lc); y.add(rc)
        if lc == rc:
            symmetric.append(j)
    assert len(x) == len(y) == 2**k
    assert x.intersection(y) == {least_rotation(b'0'*(n-pos[j-1]-1)+central[:pos[j-1]+1]) for j in symmetric}
    assert symmetric == [2**a for a in range(k+1)], (k,symmetric)
    assert cyc == x.union(y).union({b'0'*n})
    return k,n,len(fs),len(cyc),len(symmetric)

if __name__=='__main__':
    for k in range(8):
        print('k,n,factors,cyclic,symmetric=', *check(k))
    print('VERIFY_OK')
