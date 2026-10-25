#!/usr/bin/env python3
"""Independent finite checks of a Dyck nesting-height / subsequence bound."""
from functools import lru_cache
from itertools import product


def arches(word):
    pending = None
    result = 0
    for c in word:
        if pending is None:
            pending = c
        elif c != pending:
            result += 1
            pending = None
    return result


def directly_universal(word, k):
    for target in product('01', repeat=k):
        pos = 0
        for c in word:
            if pos < k and c == target[pos]:
                pos += 1
        if pos < k:
            return False
    return True


@lru_cache(None)
def dyck(n):
    if n == 0:
        return ('',)
    return tuple('0'+u+'1'+v for m in range(n) for u in dyck(m) for v in dyck(n-1-m))


def height(w):
    balance = top = 0
    for c in w:
        balance += 1 if c == '0' else -1
        top = max(top, balance)
        assert balance >= 0
    assert balance == 0
    return top


def claimed(n, h):
    if h == 1:
        return n
    q, r = divmod(n, h)
    return max(1, 2*q - 1 + min(2, r))


def P(H, L, parity, h):
    if L == -1:
        return (-2 if H == 0 else -H) if parity == 0 else H-2*h+2
    if L == 0:
        return H-2 if parity == 0 else H-2*h+2
    return -H


def check_potentials(h):
    reachable = {(0,-1,0)}
    while True:
        expanded = set(reachable)
        for H,L,p in reachable:
            assert not (H == h and L != 0)
            assert not (H == h-1 and L == 1)
            for c,delta in ((0,1),(1,-1)):
                HH = H+delta
                if HH < 0 or HH > h:
                    continue
                reset = L != -1 and L != c
                LL = -1 if reset else c
                pp = p^reset
                increment = (3-2*h if p == 0 else -1) if reset else 1
                assert P(HH,LL,pp,h) >= P(H,L,p,h)+increment, (h,H,L,p,c)
                expanded.add((HH,LL,pp))
        if expanded == reachable:
            break
        reachable = expanded
    for H,L,p in reachable:
        if H == 0:
            assert P(H,L,p,h) <= 0


def check_dp(h, nmax):
    states = {(0,-1): 0}
    for j in range(1,2*nmax+1):
        nxt = {}
        for (H,L),val in states.items():
            for c,delta in ((0,1),(1,-1)):
                HH=H+delta
                if HH < 0 or HH > h:
                    continue
                reset = L != -1 and L != c
                key = (HH, -1 if reset else c)
                nxt[key] = min(nxt.get(key,10**9),val+reset)
        states = nxt
        if j%2 == 0:
            n=j//2
            actual = min(v for (H,_),v in states.items() if H==0)
            assert actual == claimed(n,h), (h,n,actual,claimed(n,h))


def main():
    for n in range(1,9):
        for w in dyck(n):
            k=arches(w)
            assert directly_universal(w,k)
            assert not directly_universal(w,k+1)
            for h in range(height(w),n+1):
                assert k >= claimed(n,h)
        for h in range(1,n+1):
            vals=[arches(w) for w in dyck(n) if height(w)<=h]
            assert min(vals)==claimed(n,h), (n,h,min(vals),claimed(n,h))
    for h in range(2,151):
        check_potentials(h)
        check_dp(h, min(6*h+3, 100))
    for h in range(2,51):
        for q in range(0,8):
            for r in range(h):
                n=q*h+r
                if n==0:continue
                witness=('0'*h+'1'*h)*q + ('0'*r+'1'*r if r else '')
                assert height(witness)<=h
                assert len(witness)==2*n
                assert arches(witness)==claimed(n,h), (h,n,arches(witness),claimed(n,h))
    print('DYCK_HEIGHT_UNIVERSALITY_PASS exact_Dyck_n_le_8 potential_h_2_150 dynamic_h_2_150 constructions_h_2_50')

if __name__=='__main__':
    main()
