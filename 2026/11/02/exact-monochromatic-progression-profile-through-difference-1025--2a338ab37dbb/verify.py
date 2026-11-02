#!/usr/bin/env python3
"""Exact finite certificate for monochromatic progressions in 0011/1100 word.

Run: python3 verify.py in the same directory as AP_PROFILE.csv.
Only Python standard library is needed.
"""
import csv
from pathlib import Path

CAP = 1032
LIMIT = 1025

def t(n):
    """Fixed point bit: xor of high binary digits in base-four expansion."""
    assert n >= 0
    bit = 0
    while n:
        bit ^= (n % 4) // 2
        n //= 4
    return bit


def bit_word(k):
    T, B = 0, 1
    for _ in range(k):
        mask = (1 << B) - 1
        C = mask ^ T
        T = T | (T << B) | (C << (2 * B)) | (C << (3 * B))
        B *= 4
    return T, B


def exact_maximum(d):
    # For every tested length L <= CAP, B > (L-1)d gives at most one carry.
    B, k = 4, 1
    while B <= (CAP - 1) * d:
        B *= 4
        k += 1
    T, N = bit_word(k)
    assert N == B
    survivor = (1 << B) - 1
    previous = T
    best_length = 1
    witness_residue = 0
    for j in range(1, CAP):
        shift = j * d
        assert shift < B
        rotated = (T >> shift) | ((T & ((1 << shift) - 1)) << (B - shift))
        crossing = ((1 << d) - 1) << (B - shift)
        survivor &= (~(previous ^ rotated)) | crossing
        if not survivor:
            return best_length, witness_residue, B
        best_length = j + 1
        witness_residue = (survivor & -survivor).bit_length() - 1
        previous = rotated
    raise AssertionError('CAP was insufficient; no finite-exhaustion certificate')


def actual_start(r, B, d, L):
    # At most one carry, with low-digit color a and b on either side.
    c0 = t(r)
    boundary = next((j for j in range(L) if r + j*d >= B), L)
    if boundary == L:
        m = 0
    else:
        c1 = t((r + boundary * d) % B)
        m = int(c0 != c1)
    i = B*m + r
    assert all(t(i + j*d) == t(i) for j in range(L))
    return i


def main():
    rows = list(csv.DictReader(Path(__file__).with_name('AP_PROFILE.csv').open(newline='',encoding='utf-8')))
    assert len(rows) == LIMIT
    values = []
    for idx,row in enumerate(rows,1):
        d = int(row['difference'])
        a = int(row['maximum_length'])
        witness = int(row['witness_start'])
        assert idx == d
        computed, r, B = exact_maximum(d)
        assert computed == a, (d,computed,a)
        check_start = actual_start(r,B,d,a)
        assert witness == check_start,(d,witness,check_start)
        assert all(t(witness+j*d)==t(witness) for j in range(a))
        values.append(a)
    for cutoff,optimum,unique in [(65,66,65),(257,260,255),(1025,1026,1025)]:
        assert max(values[:cutoff]) == optimum
        assert [i+1 for i,x in enumerate(values[:cutoff]) if x==optimum]==[unique]
    print('VERIFY_OK: 1025 exact fixed-difference maxima; three unique bounded maximizers')

if __name__ == '__main__':
    main()
