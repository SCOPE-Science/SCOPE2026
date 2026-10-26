#!/usr/bin/env python3
"""Exact finite polynomial identities for a two-colour binary-partition congruence.

All computations use integer arithmetic. The identities certify infinite
formal-power-series congruences; the finite coefficient checks are supplemental.
"""
from math import comb

MOD = 128
P = [1, 6, 7, 4, 5, 2, 3, 0]
RESIDUES = (36, 62)
EXPECTED_V = [112, 112, 16, 16, 96, 96, 32, 32, 48, 48, 80, 80, 0]

def mul(a, b, mod=MOD):
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                if bj:
                    out[i+j] = (out[i+j] + ai * bj) % mod
    return out

def build_v():
    v = [1]
    for j in range(7):
        step, count = 1 << j, 128 >> j
        w = [0] * (2 * (count - 1) * step + 1)
        for k in range(2 * count - 1):
            w[k*step] = k+1 if k < count else 2*count-1-k
        v = mul(v, w)
    assert len(v) == 1539
    return v

def check_thue_morse_square():
    # P(y)(1+y^8) = (1-y)^2 P(y^2), modulo 8.
    lhs = [0]*17
    rhs = [0]*17
    for i, c in enumerate(P):
        lhs[i] += c
        lhs[i+8] += c
        rhs[2*i] += c
        rhs[2*i+1] -= 2*c
        rhs[2*i+2] += c
    assert all((a-b) % 8 == 0 for a, b in zip(lhs, rhs))

def check_residues(v):
    for r in RESIDUES:
        vr = [v[128*k+r] if 128*k+r < len(v) else 0 for k in range(13)]
        assert vr == EXPECTED_V, (r, vr)
        # V_r(y)(1-y^8) = 112 P(y)(1-y)^13 (mod 128).
        lhs = [0]*21
        rhs = [0]*21
        for i, c in enumerate(vr):
            lhs[i] += c
            lhs[i+8] -= c
        for i, c in enumerate(P):
            for j in range(14):
                rhs[i+j] += 112*c*(-1)**j*comb(13, j)
        assert all((a-b) % MOD == 0 for a,b in zip(lhs, rhs))

def check_direct():
    limit = 128*80+62
    b = [0]*(limit+1)
    b[0] = 1
    for n in range(1, limit+1):
        b[n] = ((b[n//2] if n%2==0 else 0) + 2*b[n-1] -
                (b[n-2] if n>=2 else 0)) % MOD
    for r in RESIDUES:
        for k in range(81):
            assert b[128*k+r] == 112, (r,k,b[128*k+r])
    assert [r for r in range(128) if b[r] == 112] == [36, 62, 96]
    assert b[224] == 96

if __name__ == '__main__':
    check_thue_morse_square()
    v = build_v()
    check_residues(v)
    check_direct()
    print('PASS: Thue-Morse functional polynomial identity mod 8')
    print('PASS: both exact degree-20 polynomial certificates mod 128')
    print('PASS: direct recurrence on 162 instances and exact finite residue exclusion')
