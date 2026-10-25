#!/usr/bin/env python3
"""Reproduce weight-three, three-deck collision classification (stdlib only)."""
from collections import defaultdict
from itertools import combinations
from math import comb


def deck3(w):
    # Dynamic programming over subsequence lengths: counts all ordered triples.
    dp = [[0] * (1 << k) for k in range(4)]
    dp[0][0] = 1
    for bit in w:
        for k in (3, 2, 1):
            for pat, multiplicity in enumerate(dp[k-1]):
                dp[k][2*pat + bit] += multiplicity
    return tuple(dp[3])


def word_from_gaps(g):
    return [0]*g[0]+[1]+[0]*g[1]+[1]+[0]*g[2]+[1]+[0]*g[3]


def partner(g):
    x0, x1, x2, x3 = g
    d, r = divmod(x1-x2, 3)
    if r or not d:
        return None
    y = (x0+d,x2,x1,x3-d)
    return y if min(y) >= 0 else None


def collision_pairs_formula(n):
    N = n-3
    return sum(N-4*d-2*y+1 for d in range(1,N//4+1)
               for y in range((N-4*d)//2+1))


def collision_pairs_rational(n):
    # Coefficient of z^(n-7) in (1-z)^-2 (1-z^2)^-1 (1-z^4)^-1.
    if n < 7:
        return 0
    m=n-7
    return sum(m-4*t-2*y+1 for t in range(m//4+1)
               for y in range((m-4*t)//2+1))


def exhaustive_deck_check():
    for n in range(3, 25):
        classes = defaultdict(list)
        for pos in combinations(range(n),3):
            gaps = (pos[0],pos[1]-pos[0]-1,pos[2]-pos[1]-1,n-pos[2]-1)
            # DP operates directly on the actual length-n binary word.
            classes[deck3(word_from_gaps(gaps))].append(gaps)
        assert sum(len(v) for v in classes.values()) == comb(n,3)
        assert all(len(v) <= 2 for v in classes.values()), n
        pairs = [v for v in classes.values() if len(v) == 2]
        assert len(pairs) == collision_pairs_formula(n), (n,len(pairs),collision_pairs_formula(n))
        assert len(classes) == comb(n,3)-collision_pairs_rational(n)
        for c in pairs:
            assert partner(c[0]) == c[1] and partner(c[1]) == c[0], (n,c)
        if n in (7,8,10,14,20,24):
            print(f'length={n} words={comb(n,3)} pairs={len(pairs)} decks={len(classes)}')
    print('EXHAUSTIVE_DECK_OK (n=3..24)')


def algebraic_count_check():
    for n in range(3,101):
        N=n-3
        # Independent direct count of all unordered gap pairs satisfying the claimed involution.
        direct=0
        for x0 in range(N+1):
            for x1 in range(N-x0+1):
                for x2 in range(N-x0-x1+1):
                    x3=N-x0-x1-x2
                    d=x1-x2
                    if d>0 and d%3 == 0 and x3>=d//3:
                        direct+=1
        assert direct == collision_pairs_formula(n) == collision_pairs_rational(n), n
    print('ALGEBRAIC_COUNT_OK (n=3..100)')


if __name__ == '__main__':
    exhaustive_deck_check()
    algebraic_count_check()
    print('VERIFY_OK')
