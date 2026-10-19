#!/usr/bin/env python3
"""Exact finite-field checks for the cubic moment-curve Gabor projector rank.
No external packages. Brute-force arithmetic checks; not an infinite proof.
"""
from itertools import product


def check(p):
    assert p >= 5 and all(p % d for d in range(2, int(p**0.5) + 1))
    curve = [(t, t*t % p, t*t*t % p) for t in range(p)]
    lag_pairs = {}
    for x in curve:
        for y in curve:
            delta = tuple((a-b) % p for a,b in zip(x,y))
            lag_pairs.setdefault(delta, []).append(x)
    assert len(lag_pairs) == 1 + p*(p-1)
    assert len(lag_pairs[(0,0,0)]) == p
    for d, pts in lag_pairs.items():
        if d != (0,0,0):
            assert d[0] != 0 and len(pts) == 1
            t = (d[1] - d[0]*d[0])*pow(2*d[0], -1, p) % p
            assert pts[0] == curve[t + d[0] if t+d[0]<p else (t+d[0])%p]
            assert d[2] == ((t+d[0])**3 - t**3) % p
    zero_freq = []
    for aa, bb, cc in product(range(p),repeat=3):
        cnt = [0]*p
        for t in range(p):
            cnt[(aa*t + bb*t*t + cc*t*t*t) % p] += 1
        if cnt == [1]*p: zero_freq.append((aa,bb,cc))
    formula = {(aa, 0, 0) for aa in range(1,p)}
    if p % 3 == 2:
        for cc in range(1,p):
            for bb in range(p):
                formula.add((bb*bb*pow(3*cc,-1,p) % p,bb,cc))
    assert set(zero_freq) == formula, (p,set(zero_freq)^formula)
    # Independent check of collision classification in the depressed cubic.
    for u in range(p):
        injective = len({(t**3+u*t)%p for t in range(p)}) == p
        assert injective == (u==0 and p%3==2)
    rank = len(lag_pairs)*p**3 - len(zero_freq)
    predicted = p**3*(p*(p-1)+1) - (p*p-1 if p%3==2 else p-1)
    assert rank == predicted
    nullity = p**6-rank
    assert 0<rank<p**6
    return f'p={p} |C-C|={len(lag_pairs)} origin_zeros={len(zero_freq)} rank={rank} nullity={nullity}'

if __name__ == '__main__':
    for p in [5,7,11,13,17,19,23,29]: print(check(p))
    print('PASS: exact combinatorial and permutation checks over eight primes.')
