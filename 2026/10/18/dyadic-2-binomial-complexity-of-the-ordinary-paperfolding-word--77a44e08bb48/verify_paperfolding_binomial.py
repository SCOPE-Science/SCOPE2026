#!/usr/bin/env python3
"""Reproduce dyadic scattered-two-binomial profiles for regular paperfolding."""
from collections import defaultdict


def fold_arithmetic(n):
    """Zero-based bit, from odd part of n+1 modulo four."""
    z = n + 1
    while z % 2 == 0:
        z //= 2
    return int(z % 4 == 3)


def fold_recursive(n):
    """Independent binary recursion (terminates for all n>=0)."""
    if n % 2 == 0:
        return (n // 2) % 2
    return fold_recursive(n // 2)


def profile(word):
    return (sum(word), sum(j * v for j, v in enumerate(word)))


def base_profiles():
    # Every adjacent pair (a,b) arises at both parities of i.
    witnesses = {}
    for i in range(32):
        witnesses.setdefault((i % 2, fold_arithmetic(i), fold_arithmetic(i+1)), i)
    assert len(witnesses) == 8, witnesses
    b = [set(), set()]
    for (e,a,c), i in witnesses.items():
        b[0].add(profile((e, a, 1-e, c)))
        b[1].add(profile((a, 1-e, c, e)))
    expected = [
        {(1,0),(1,2),(2,1),(2,3),(2,5),(3,4),(3,6)},
        {(1,1),(1,3),(2,1),(2,3),(2,5),(3,3),(3,5)},
    ]
    assert b == expected, (b, expected)
    return b


def double_profiles(P,L):
    assert L >= 4 and L % 4 == 0
    ans = [set(),set()]
    for e in (0,1):
        for w,s in P[e]:
            w1 = w + L//2
            # Start indices 2i and 2i+1 respectively.
            ans[0].add((w1, 2*s + w + L*L//2 - e*L))
            ans[1].add((w1, 2*s + L*L//2 + (2*e-1)*(L//2)))
    return ans


def exact_profile_check():
    P = base_profiles()
    for k in range(2,13):
        L = 1 << k
        counts = defaultdict(int)
        for e in (0,1):
            for w,s in P[e]:
                counts[(e,w)] += 1
        assert set(w for _,w in counts) == {L//2-1,L//2,L//2+1}
        for e in (0,1):
            assert counts[(e,L//2-1)] == L//2
            assert counts[(e,L//2+1)] == L//2
            center = sorted(s for w,s in P[e] if w == L//2)
            assert len(center) == k+1
            assert center == list(range(center[0],center[0] + (k+1)*(L//2),L//2))
        assert {s for w,s in P[0] if w==L//2} == {s for w,s in P[1] if w==L//2}
        for w in (L//2-1,L//2+1):
            assert not ({s for a,s in P[0] if a==w}&{s for a,s in P[1] if a==w})
        total = len(P[0]|P[1]); expected = 2*L+k+1
        assert total == expected, (k,total,expected)
        if k <= 10:
            print(f'k={k}: length={L}, classes={total}, parity profiles={len(P[0])},{len(P[1])}')
        if k < 12:
            P = double_profiles(P,L)


def independent_prefix_check():
    N = 1 << 16
    for i in range(N + 2048):
        assert fold_arithmetic(i) == fold_recursive(i)
    bits = bytearray(fold_arithmetic(i) for i in range(N+2048))
    P = base_profiles()
    for k in range(2,11):
        L = 1 << k
        w=sum(bits[:L]);s=sum(j*bits[j] for j in range(L))
        observed=[set(),set()]
        observed[0].add((w,s))
        for i in range(1,N):
            old=bits[i-1]; new=bits[i+L-1]
            s=s-w+old+(L-1)*new
            w=w-old+new
            observed[i%2].add((w,s))
        assert observed==P, (k,[(len(a),len(b)) for a,b in zip(observed,P)])
        P=double_profiles(P,L)
    # Explicit subsequence-word counts against the sufficient two moments.
    from itertools import product
    for L in range(2,18):
        for start in range(128):
            word = bits[start:start+L]
            moments=profile(word)
            singles=[word.count(a) for a in (0,1)]
            doubles=[]
            for a,b in product((0,1), repeat=2):
                doubles.append(sum(1 for i in range(L) for j in range(i+1,L)
                                   if word[i]==a and word[j]==b))
            w,s=moments
            assert singles==[L-w,w]
            assert doubles==[(L-w)*(L-w-1)//2,
                              s-w*(w-1)//2,
                              w*(L-w)-s+w*(w-1)//2,
                              w*(w-1)//2]
    print('VERIFY_OK: exact parity lifts, both generators, full direct-prefix class profiles and subsequence formulas')


if __name__=='__main__':
    exact_profile_check()
    independent_prefix_check()
