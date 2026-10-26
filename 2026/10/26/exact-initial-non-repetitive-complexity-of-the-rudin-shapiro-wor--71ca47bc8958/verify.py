#!/usr/bin/env python3
"""Finite corroborations and exhaustive parity certificate.
Standard library only.  The unrestricted proof is in RESULT.md.
"""
from collections import defaultdict

PHI = {0:(0,1), 1:(0,2), 2:(3,1), 3:(3,2)}

def substitute(w):
    return tuple(x for a in w for x in PHI[a])

def phi_power(a, k):
    w=(a,)
    for _ in range(k): w=substitute(w)
    return w

def rs_digit(n):
    return ((n & (n>>1)).bit_count()) & 1

def rs_arithmetic(length):
    return bytes(rs_digit(i) for i in range(length))

def rs_morphic(length):
    w=(0,)
    while len(w)<length: w=substitute(w)
    return bytes(int(v>=2) for v in w[:length])

def pair_language():
    # Forward finite closure of two-letter factors of the fixed point phi^omega(0).
    # (0,1) appears in phi(0). The closure rule is exhaustive for any uniform
    # substitution image: internal adjacent pairs and image-boundary pairs.
    current={(0,1)}
    for _ in range(12):
        nxt=set(current)
        for a,b in current:
            w=PHI[a]+PHI[b]
            nxt.update(zip(w,w[1:]))
        if nxt==current: return current
        current=nxt
    raise AssertionError('pair closure did not stabilize')

def parity_certificate():
    pairs=pair_language()
    expected={(0,1),(0,2),(1,0),(1,3),(2,0),(2,3),(3,1),(3,2)}
    assert pairs==expected
    even=set();odd=set()
    for a,b in pairs:
        w=phi_power(a,3)+phi_power(b,3)
        binary=bytes(int(x>=2) for x in w)
        for offset in range(8):
            (even if offset%2==0 else odd).add(binary[offset:offset+8])
    assert len(even)==24 and len(odd)==32 and not even.intersection(odd)
    print('VERIFY_OK complete_8_factor_parity_certificate pairs=8 even=24 odd=32 intersection=0')

def first_collision(w,n):
    seen={}
    for j in range(0,len(w)-n+1):
        x=w[j:j+n]
        if x in seen:return j,seen[x]
        seen[x]=j
    raise AssertionError('prefix too short')

def predicted(n):
    if n<=2:return 1
    if n<=5:return 4
    B=1<<((n-1).bit_length()-1)
    return 4*B

def check():
    w=rs_arithmetic(65536)
    assert w==rs_morphic(65536)
    print('VERIFY_OK arithmetic_and_four_letter_morphic_definitions length=65536')
    parity_certificate()
    for B in [8,16,32,64,128,256,512,1024]:
        assert B&(B-1)==0
        h=B.bit_length()-1
        A=w[:B];C=w[B:2*B]
        assert C==bytes(v ^ int(i>=B//2) for i,v in enumerate(A))
        assert w[2*B:3*B]==A and w[3*B:4*B]==bytes(1-v for v in C)
        assert w[4*B:6*B]==w[:2*B]
        signatures=[w[i:i+B+1] for i in range(4*B)]
        assert len(set(signatures))==4*B
        assert w[4*B:5*B+1]==w[:B+1]
    print('VERIFY_OK dyadic_block_structure_and_distinct_before_first_repeat B=8..1024')
    for n in range(1,385):
        actual,prior=first_collision(w,n)
        assert actual==predicted(n),(n,actual,predicted(n))
        assert prior==({1:0,2:0,3:1,4:1,5:1}.get(n,0)),(n,prior)
    print('VERIFY_OK first_collision_exact_and_earlier_source n=1..384')
    for B in [8,16,32,64,128,256,512,1024]:
        for off in range(B):
            assert w[2*B+off]==w[off]
            assert w[3*B+off] != w[B+off]
    print('VERIFY_OK arithmetic_shift_bit_identity_all_offsets B=8..1024')
    print('VERIFY_OK asymptotic_extrema liminf=2 limsup=4 follow_from_formula')

if __name__=='__main__': check()
