#!/usr/bin/env python3
"""Independent exact checks for finite-language residual-ball/layer bounds.

No external dependencies. Input languages are finite sets of literal words.
"""
from collections import defaultdict, deque
from fractions import Fraction
import random


def invariants(words, alphabet, all_balls=True):
    assert words and all(isinstance(w, str) for w in words)
    D = max(map(len, words))
    partial = defaultdict(set)
    for word in words:
        for i in range(len(word) + 1):
            partial[word[:i]].add(word[i:])
    residuals = sorted({frozenset(v) for v in partial.values()}, key=lambda r:(len(r),tuple(sorted(r))))
    idx = {r:i for i,r in enumerate(residuals)}
    initial = idx[frozenset(words)]
    levels = [set() for _ in range(D+1)]
    for prefix, r in partial.items():
        levels[len(prefix)].add(idx[frozenset(r)])
    h = [len(x) for x in levels]
    U = max(h[i-1]+h[i]-1 for i in range(1,D+1))
    tr = [[] for _ in residuals]
    for i, r in enumerate(residuals):
        for a in alphabet:
            nr = frozenset(w[1:] for w in r if w.startswith(a))
            if nr:
                assert nr in idx
                tr[i].append(idx[nr])
    B = 0
    if all_balls:
        for p in range(len(residuals)):
            seen = {p}
            frontier = {p}
            ell = 0
            while frontier:
                nextf = {v for u in frontier for v in tr[u]} - seen
                if not nextf:
                    break
                ell += 1
                seen |= nextf
                frontier = nextf
                val = (len(seen)-1 + ell-1)//ell
                B = max(B,val)
        assert B<=U,(U,B,words)
        assert B<=max(len(alphabet),(2*U+1+2)//3),(U,B,words)
    return U,B,h,len(residuals),tr,initial


def test_family():
    trials=0
    for d in range(1,5):
        for T in (1,2,3,5,8,10):
            xs = [format(x, f'0{d}b') for x in range(1<<d)]
            words = {x+'0'*T+x for x in xs}
            U,B,h,m,tr,initial = invariants(words,'01')
            k = 1<<d
            assert U==2*k-1, (d,T,U)
            assert h == ([2**i for i in range(d)] + [k]*(T+1) + [2**(d-j) for j in range(1,d+1)]),(d,T,h)
            assert B >= (k*(T+1) + d+T-1)//(d+T),(d,T,B)
            print('family',d,T,'states',m,'U',U,'B',B)
            trials+=1
    return trials


def test_random():
    rng=random.Random(20261017)
    trials=0
    max_ub=0
    for q in (2,3):
        alphabet='012'[:q]
        for rep in range(500):
            n=rng.randint(2,9)
            count=rng.randint(1,60)
            words={''.join(rng.choices(alphabet,k=rng.randint(1,n))) for _ in range(count)}
            U,B,h,m,tr,init=invariants(words,alphabet)
            max_ub=max(max_ub,U)
            trials+=1
    print('random_languages',trials,'max_U',max_ub)
    return trials

if __name__=='__main__':
    f=test_family()
    r=test_random()
    print('PASS families',f,'random',r)
