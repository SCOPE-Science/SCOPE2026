#!/usr/bin/env python3
"""Finite exact two-abelian profile census for Rudin-Shapiro factors.

Only standard Python is required. All infinite-factor coverage is established by
an eight-pair substitution certificate and a supertile argument.
"""
import hashlib
import json
from pathlib import Path

PAIR_SET = {(0, 1), (0, 3), (1, 0), (1, 2),
            (2, 1), (2, 3), (3, 0), (3, 2)}

def sigma(a):
    bit, parity = divmod(a, 2)
    return (2 * bit, 2 * (bit ^ parity) + 1)

def substitute(word):
    return tuple(y for x in word for y in sigma(x))

def certify_pair_set():
    word = (0,)
    for level in range(1, 6):
        word = substitute(word)
        pairs = set(zip(word, word[1:]))
        if level == 4:
            assert pairs == PAIR_SET
    internal = {sigma(a) for a in range(4)}
    boundary = {(sigma(a)[1], sigma(b)[0]) for a, b in PAIR_SET}
    assert internal | boundary == PAIR_SET
    assert set(word) == set(range(4))
    # Independent check of the stated coding: rs(n) is the parity of 11 bits.
    for i, letter in enumerate(word):
        assert letter % 2 == i % 2
        assert letter // 2 == ((i & (i >> 1)).bit_count() % 2)

def profile_set_from_bits(bits, n):
    """Exactly the 2-abelian classes as (number of 1s, number of 01s, endpoints)."""
    ones = [0]
    rises = [0]
    for i, bit in enumerate(bits):
        ones.append(ones[-1] + bit)
        rises.append(rises[-1] + int(i != 0 and bits[i-1] == 0 and bit == 1))
    out = set()
    for start in range(len(bits)-n+1):
        out.add((ones[start+n]-ones[start],
                 rises[start+n]-rises[start+1],
                 bits[start], bits[start+n-1]))
    return out

def complete_profiles(m):
    n = 1 << m
    tiles = {a:(a,) for a in range(4)}
    for _ in range(m):
        tiles = {a:substitute(tiles[a]) for a in range(4)}
    assert all(len(tiles[a]) == n for a in range(4))
    profiles = set()
    for a,b in sorted(PAIR_SET):
        coded = tuple(x//2 for x in tiles[a]+tiles[b])
        profiles |= profile_set_from_bits(coded,n)
    return profiles

def digest(profiles):
    content = ''.join(','.join(map(str, row)) + '\n' for row in sorted(profiles))
    return hashlib.sha256(content.encode('utf-8')).hexdigest()

def independent_prefix_check(m, expected):
    n = 1 << m
    # 64n positions suffice in these checked cases; equality to the
    # separately proved full supertile census, not the prefix length,
    # justifies completeness.
    bits = tuple((i & (i >> 1)).bit_count() % 2 for i in range(64*n))
    assert profile_set_from_bits(bits, n) == expected
    # Validate the four-count reconstruction on selected windows.
    for i in range(0, 8*n, max(1,n//8)):
        w=bits[i:i+n]
        k,u,a,b = (sum(w), sum(w[j]==0 and w[j+1]==1 for j in range(n-1)),w[0],w[-1])
        n10 = sum(w[j]==1 and w[j+1]==0 for j in range(n-1))
        n11 = sum(w[j]==1 and w[j+1]==1 for j in range(n-1))
        n00 = sum(w[j]==0 and w[j+1]==0 for j in range(n-1))
        assert n10 == u+a-b and n11 == k-u-a and n00 == n-1-k-u+b

def main():
    certify_pair_set()
    cert=[]
    for m in range(4,17):
        profiles=complete_profiles(m)
        predicted=16*((1<<(m//2))-1) if m%2==0 else 16*(3*(1<<((m-3)//2))-1)
        assert len(profiles)==predicted,(m,len(profiles),predicted)
        if m<=10: independent_prefix_check(m, profiles)
        cert.append({'m':m,'n':1<<m,'classes':len(profiles),'profile_sha256':digest(profiles)})
    payload={'pair_set':[list(x) for x in sorted(PAIR_SET)],'results':cert}
    expected=json.loads((Path(__file__).resolve().parent/'certificates.json').read_text(encoding='utf-8'))
    assert payload==expected,'The packaged profile certificate does not match the recomputation'
    print(json.dumps(payload,indent=2))
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
