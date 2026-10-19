"""Direct finite cross-checks for the cyclic BWT sparse-weight theorem.

The infinite asymptotic assertion follows from the separate mathematical proof;
this script confirms the elementary rotation and gap assertions on finite ranges.
"""
from itertools import combinations
from math import comb


def bwt_direct(word):
    n = len(word)
    rotations = sorted((word[i:] + word[:i], i) for i in range(n))
    return ''.join(word[(i - 1) % n] for _, i in rotations)


def linear_runs(word):
    return 1 + sum(word[i] != word[i - 1] for i in range(1, len(word)))


def gaps_of_positions(pos, n):
    k = len(pos)
    return tuple((pos[(i + 1) % k] - pos[i] - 1) % n for i in range(k))


def clean(gaps):
    return min(gaps) >= 1 and all(
        abs(a - b) >= 2 for a, b in combinations(gaps, 2)
    )


def top_tie(gaps):
    return gaps.count(max(gaps)) >= 2


def check():
    total = 0
    for k in range(4, 7):
        for n in range(k + 1, 21):
            seen = 0
            for pos in combinations(range(n), k):
                word = ''.join('1' if i in pos else '0' for i in range(n))
                last = bwt_direct(word)
                runs = linear_runs(last)
                gaps = gaps_of_positions(pos, n)
                assert last[0] == '1' and last[-1] == '0'
                assert runs <= 2 * k and runs % 2 == 0
                if clean(gaps):
                    assert runs == 2 * k, (n, k, pos, gaps, last)
                if top_tie(gaps):
                    assert runs < 2 * k, (n, k, pos, gaps, last)
                seen += 1
            assert seen == comb(n, k)
            total += seen
    print('ALL_CHECKS_PASS', 'strings=', total, 'weights=4..6', 'lengths=k+1..20')

if __name__ == '__main__':
    check()
