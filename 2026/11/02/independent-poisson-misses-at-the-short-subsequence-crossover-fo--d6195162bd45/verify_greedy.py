"""Exact checks of greedy subsequence-avoidance counts and pair intersections.
All inputs and outputs are public mathematical quantities; no external packages.
"""
from collections import defaultdict
from itertools import product, combinations
from math import comb


def greedy_count(word, patterns):
    positions = [0] * len(patterns)
    for bit in word:
        for j, pattern in enumerate(patterns):
            if positions[j] < len(pattern) and bit == pattern[positions[j]]:
                positions[j] += 1
    return sum(pos < len(pat) for pos, pat in zip(positions, patterns))


def dynamic_count_avoiding(patterns, n):
    length = len(patterns[0]); assert all(len(x)==length for x in patterns)
    initial = (0,) * len(patterns)
    dp = {initial: 1}
    for _ in range(n):
        new = defaultdict(int)
        for state, count in dp.items():
            for bit in (0,1):
                after = tuple(p + (p < length and bit == patterns[j][p]) for j,p in enumerate(state))
                if all(i < length for i in after):
                    new[after] += count
        dp = new
    return sum(dp.values())


if __name__ == '__main__':
    for r in range(1, 5):
        pats = list(product(range(2), repeat=r))
        for n in range(r, 13):
            exact = sum(comb(n,j) for j in range(r))
            for pat in pats:
                result = dynamic_count_avoiding([pat], n)
                assert result == exact, (r,n,pat,result,exact)
                if n <= 8:
                    brute = sum(greedy_count(bits,[pat]) == 1 for bits in product((0,1), repeat=n))
                    assert brute == exact
            for p,q in combinations(pats, 2):
                pair = dynamic_count_avoiding([p,q],n)
                if n<=8:
                    brute = sum(greedy_count(bits,[p,q]) == 2 for bits in product((0,1),repeat=n))
                    assert pair == brute, (p,q,n)
                if r >= 2:
                    # Crude explicit polynomial majorant implied by the proof.
                    assert pair <= 2**(2*r+3) * (n+1)**(r-2), (r,n,p,q,pair)
                else:
                    assert pair == 0
        print(f'r={r}: exact one-pattern formula; all unordered pattern pairs checked through n=12; brute cross-check through n=8; polynomial bound verified')
    for r in (2,3,4):
        pats = list(product(range(2), repeat=r))
        for n in (12,16,20):
            counts = [dynamic_count_avoiding([p,q], n) for p,q in combinations(pats,2)]
            max_pair = max(counts)
            print(f'r={r}, n={n}, maximum_pair_avoid_count={max_pair}, ratio_to_n_power={max_pair/(n+1)**(r-2):.5f}')
    print('PASS')
