"""Independent direct sequential-burst check for q=2,3,4,5.
Python 3 standard library. No precomputed survivor-coordinate pairs are used.
"""
from collections import Counter
from itertools import product
from math import prod


def ball(word):
    states = {tuple(word)}
    for _ in range(2):
        states = {
            s[:i] + s[i+2:]
            for s in states
            for i in range(len(s)-1)
        }
    assert all(len(s)==2 for s in states)
    return states


def expected(q):
    coefficients = {3:210, 4:582, 5:363, 6:71, 7:4}
    return sum(v*prod(range(q-k+1,q+1)) for k,v in coefficients.items() if k<=q)//2


def test(q):
    mask_counts = Counter()
    for x in product(range(q), repeat=6):
        mask = sum(1<<(q*a+b) for a,b in ball(x))
        mask_counts[mask] += 1
    keys = list(mask_counts)
    maximum = 0
    top_pairs = 0
    for i, m in enumerate(keys):
        c = mask_counts[m]
        if c>1:
            overlap=m.bit_count()
            pair_count=c*(c-1)//2
            if overlap>maximum: maximum,top_pairs=overlap,pair_count
            elif overlap==maximum: top_pairs+=pair_count
        for n in keys[:i]:
            overlap=(m&n).bit_count()
            pair_count=c*mask_counts[n]
            if overlap>maximum: maximum,top_pairs=overlap,pair_count
            elif overlap==maximum: top_pairs+=pair_count
    assert maximum == (4 if q==2 else 5), (q,maximum)
    if q>=3: assert top_pairs == expected(q), (q,top_pairs,expected(q))
    print('DIRECT_OK', 'q',q,'maximum',maximum,'unordered_maximal_pairs',top_pairs,'masks',len(keys))


if __name__ == '__main__':
    for q in (2,3,4,5):test(q)
