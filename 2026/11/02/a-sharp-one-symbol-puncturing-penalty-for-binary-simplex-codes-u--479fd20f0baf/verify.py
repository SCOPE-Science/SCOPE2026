#!/usr/bin/env python3
"""Self-contained finite verification of a punctured-simplex 2-opt construction."""
from collections import Counter
from itertools import permutations

PRIMITIVE = {3: 0b1011, 4: 0b10011, 5: 0b100101,
             6: 0b1000011, 7: 0b10001001, 8: 0b100011101}

def mul_x(value, m, polynomial):
    value <<= 1
    if value & (1 << m):
        value ^= polynomial
    return value

def construct(m, polynomial):
    q = 1 << m
    powers = [1]
    for _ in range(q-2):
        powers.append(mul_x(powers[-1], m, polynomial))
    assert len(set(powers)) == q-1 and powers[-1] != 1
    g, g_inv = powers[1], powers[-1]
    t, s = g_inv ^ 1, g ^ 1
    raw = powers[1:]
    i = raw.index(t)
    assert raw[(i+1)%len(raw)] == s
    perm = raw[:i+1] + list(reversed(raw[i+1:]))
    assert len(perm) == q-2 and set(perm)==set(range(2,q))
    diffs = Counter(perm[j] ^ perm[(j+1)%len(perm)] for j in range(len(perm)))
    missing = {t, s, t ^ s}
    assert len(missing) == 3
    assert diffs[1] == 3 and all(diffs[x] == (0 if x in missing else (3 if x == 1 else 1)) for x in range(1,q))
    weights = Counter()
    for a in range(1,q):
        codeword = [(a & x).bit_count() & 1 for x in perm]
        w = sum(codeword[j] | codeword[(j+1)%len(perm)] for j in range(q-2))
        weights[w] += 1
    k=q//4
    assert weights == Counter({3*k-1:3*k, 3*k:k-1}), (m,weights)
    return perm, weights

def check_upper_bound(m):
    q=1<<m
    n=q-2
    k=q//4
    # Each edge comprises independent nonzero columns. Exactly (2^(m-2)-1)
    # nonzero functionals vanish on both. Summing over all nonzero messages
    # gives the ordering-independent total zero-zero count.
    total=n*(k-1)
    assert total > (q-1)*(k-2)
    # Thus some nonzero message has >= k-1 zero-zero edges:
    # maximum pair distance <= n-(k-1) = 3k-1.
    assert n-(k-1) == 3*k-1


def small_exhaustion():
    # All 6! labeled cyclic orders with u=1 omitted at m=3,
    # including rotations. Check the maximum pair distance independently.
    best=0; hist=Counter()
    for v in permutations(range(2,8)):
        ws=[]
        for a in range(1,8):
            bit=[(a & x).bit_count() & 1 for x in v]
            ws.append(sum(bit[j] | bit[(j+1)%6] for j in range(6)))
        val=min(ws)
        hist[val]+=1; best=max(best,val)
    assert best == 5
    return hist

if __name__ == '__main__':
    for m, p in PRIMITIVE.items():
        check_upper_bound(m)
        perm, weights=construct(m,p)
        print(m, len(perm), sorted(weights.items()))
    print('m3 exhaustive min-distance histogram:',sorted(small_exhaustion().items()))
    print('VERIFY_OK')
